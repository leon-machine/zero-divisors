#!/usr/bin/env python3
"""Call any Transport Lab MCP tool from the shell.

  python3 colony/labcli.py <tool> '<json args>'
  python3 colony/labcli.py <tool> @args.json      (args from a file)
  python3 colony/labcli.py tools                  (list tools)

Examples:
  labcli.py get_open_problem '{"id": "op.kerr-ring"}'
  labcli.py get_claim '{"id": "angle.hop-across-cut"}'
  labcli.py get_proof '{"id": "angle.hop-across-cut"}'
  labcli.py search_claims '{"query": "Cauchy horizon", "limit": 8}'
  labcli.py find_text '{"pattern": "Q(x)"}'
  labcli.py validate_draft @draft.json     (draft.json = {"entity_md": "...", "proofs": {...}, "check_py": "..."})
  labcli.py propose_claim @draft.json
"""
import json
import os
import sys

LAB = os.environ.get("TP_LAB") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, LAB)
os.chdir(LAB)
from tp.mcp_server import Lab, TOOLS  # noqa: E402


def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print(__doc__)
        return
    name = sys.argv[1]
    if name == "tools":
        for t in TOOLS:
            print(f"{t[0]}: {t[1]}\n   args: {list(t[2].keys())}")
        return
    if name not in {t[0] for t in TOOLS}:
        sys.exit(f"unknown tool {name}")
    raw = sys.argv[2] if len(sys.argv) > 2 else "{}"
    if raw.startswith("@"):
        raw = open(raw[1:]).read()
    args = json.loads(raw)
    lab = Lab("store")
    res = getattr(lab, name)(**args)
    print(json.dumps(res, indent=1, default=str, ensure_ascii=False))


if __name__ == "__main__":
    main()
