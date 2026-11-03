# Registers the Transport Lab MCP server with the Claude desktop app.
# Run:  powershell -ExecutionPolicy Bypass -File register_mcp.ps1
# Safe to re-run: it backs up the config and only sets the "transport-lab" entry.
$ErrorActionPreference = "Continue"   # native stderr is not an error; failures throw below
$lab   = $PSScriptRoot
$store = Join-Path $lab "store"
if (-not (Test-Path $store)) { throw "No store folder at $store" }

# 1. Find a real Python (not the Microsoft Store stub)
$py = $null
$probe = "import sys; print(sys.executable)"
foreach ($cand in @("py", "python", "python3")) {
    try {
        if ($cand -eq "py") { $exe = & py -3 -c $probe 2>$null } else { $exe = & $cand -c $probe 2>$null }
        if ($LASTEXITCODE -eq 0 -and $exe -and ($exe -notmatch "WindowsApps")) { $py = $exe.Trim(); break }
    } catch {}
}
if (-not $py) { throw "No Python found. Install it from python.org and re-run." }
Write-Host "Python: $py"

# 2. Make sure the packages the server imports are there
#    (pip name, import name, required?)  scikit-learn powers the meaning-based
#    half of search_claims; without it search falls back to word matching.
$pkgs = @(@("pyyaml","yaml",$true), @("jsonschema","jsonschema",$true), @("scikit-learn","sklearn",$false))
foreach ($p in $pkgs) {
  $has = "import importlib.util, sys; sys.exit(0 if importlib.util.find_spec('$($p[1])') else 1)"
  & $py -c $has
  if ($LASTEXITCODE -ne 0) {
    Write-Host "Installing $($p[0])..."
    & $py -m pip install --user $p[0]
    & $py -c $has
    if ($LASTEXITCODE -ne 0) {
      if ($p[2]) { throw "Could not install $($p[0])." }
      Write-Host "Warning: $($p[0]) did not install; search will use word matching only."
    }
  }
}

# 3. Smoke test the server
$env:PYTHONPATH = $lab; $env:PYTHONUTF8 = "1"
$msgs = @(
 '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"test","version":"0"}}}',
 '{"jsonrpc":"2.0","id":2,"method":"tools/list"}'
)
$out = $msgs | & $py -m tp.mcp_server --store $store 2>&1 | Out-String
if (-not ($out -match '"list_subjects"')) { Write-Host $out; throw "Server smoke test failed (output above)." }
Write-Host "Server smoke test OK"

# 4. Find the desktop app's config (standard install, and Store/MSIX install)
$dirs = @(Join-Path $env:APPDATA "Claude")
Get-ChildItem (Join-Path $env:LOCALAPPDATA "Packages") -Directory -Filter "Claude_*" -ErrorAction SilentlyContinue |
  ForEach-Object { $dirs += (Join-Path $_.FullName "LocalCache\Roaming\Claude") }
$targets = @($dirs | Where-Object { Test-Path $_ })
if ($targets.Count -eq 0) { New-Item -ItemType Directory -Force -ErrorAction Stop $dirs[0] | Out-Null; $targets = @($dirs[0]) }

$entry = [pscustomobject]@{
  command = $py
  args    = @("-m", "tp.mcp_server", "--store", $store)
  env     = [pscustomobject]@{ PYTHONPATH = $lab; PYTHONUTF8 = "1" }
}

foreach ($d in $targets) {
  $cfg = Join-Path $d "claude_desktop_config.json"
  $obj = [pscustomobject]@{}
  if (Test-Path $cfg) {
    Copy-Item -ErrorAction Stop $cfg "$cfg.bak-$(Get-Date -Format yyyyMMdd-HHmmss)"
    $raw = Get-Content $cfg -Raw -ErrorAction Stop
    if ($raw -and $raw.Trim()) { $obj = $raw | ConvertFrom-Json -ErrorAction Stop }
  }
  if (-not ($obj.PSObject.Properties.Name -contains "mcpServers")) {
    $obj | Add-Member -NotePropertyName mcpServers -NotePropertyValue ([pscustomobject]@{})
  }
  $obj.mcpServers | Add-Member -NotePropertyName "transport-lab" -NotePropertyValue $entry -Force
  $json = $obj | ConvertTo-Json -Depth 32
  [IO.File]::WriteAllText($cfg, $json, (New-Object Text.UTF8Encoding($false)))
  Write-Host "Updated $cfg"
}
Write-Host ""
Write-Host "Done. Quit Claude fully (right-click the tray icon > Quit), then reopen it."
