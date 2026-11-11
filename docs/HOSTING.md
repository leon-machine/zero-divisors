# Hosting the public MCP endpoint

The stdio server (`python -m tp.mcp_server`) needs a clone, Python and a client that runs local
servers. Most people use an AI in a browser or on a phone, and those clients can add a *remote* MCP
server by its address. `tp/mcp_http.py` is that server: the same tools over HTTP, read-only.

## What it serves

- `POST /mcp`: MCP's Streamable HTTP transport, one JSON response per request. No sessions and
  no event streams, so it is stateless and can run as several instances.
- `GET /`: a short page saying how to connect; `GET /health`: `ok`.
- Read-only always: the reading tools and the prompts. `validate_draft` (which copies the whole
  store on every call), `generate_doc`, `regenerate_doc` and the proposal tools are not offered.
  Contributors run the stdio server on their own clone.

## Run it locally

    pip install -r requirements.txt
    python -m tp build --store store --no-mutants --layers 1-3
    python -m tp.layout
    python -m tp.mcp_http --store store --port 8080       # http://127.0.0.1:8080/mcp

Or with Docker, from the repository root:

    docker build -t physics-graph-mcp .
    docker run -p 8080:8080 physics-graph-mcp

The image loads the store at start (a few seconds) and then holds it in memory (a few hundred MB).

## Deploy

Any host that runs a container and gives it an HTTPS address will do. Choose one that scales to
zero or has a free allowance, since the server is idle most of the time, and one whose own limits
cap requests per client (the server sets none). Then:

1. Build the image from the release tag, so the endpoint shows what was archived:
   `git checkout vX.Y.Z && docker build -t physics-graph-mcp .`
2. Deploy it with port 8080 exposed and the host's HTTPS address in front.
3. Give it a stable address on the site's domain, for example `mcp.<domain>`, so the address on
   the Explore with AI page never changes when the host does.
4. Check it: `curl https://mcp.<domain>/health` says `ok`, and adding `https://mcp.<domain>/mcp`
   as a custom connector in claude.ai lists the tools.
5. Set `mcp_url` in `store/config.yaml` to that address and rebuild the site
   (`python -m tp.site`): the Explore with AI page and llms.txt then lead with it.

Redeploy at each release (RELEASING.md, step 5).

## What a visitor does

The site's Explore with AI page (`#contribute/connect`) gives the steps per app once `mcp_url` is
set: Claude (a custom connector, no sign-in), ChatGPT (developer mode, an app with no
authentication), Claude Code (`claude mcp add --transport http physics-graph <address>`) and
other apps that take a remote server by its address. Every tool the endpoint offers is marked
read-only, so clients that ask before write actions do not ask before each call. The page
ends with a check: ask the AI to call `conventions` and say what the graph is.
