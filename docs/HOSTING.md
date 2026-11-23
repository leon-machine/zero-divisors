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

## Deploy on Cloudflare (how zerodivisors.org runs it)

`deploy/mcp/` holds a Cloudflare Worker and its Container: the Worker passes every request to
one container built from this repository's Dockerfile, which sleeps after 15 minutes without a
request and wakes on the next (about 10 seconds while the store loads). The container type is
`basic` (1 GiB, a quarter of a CPU); the server holds the store in about 150 MB.

One-off set-up, in the Cloudflare dashboard and on GitHub:

1. Cloudflare: subscribe to the Workers Paid plan (Containers are not on the free plan).
2. Cloudflare: create an API token from the "Edit Cloudflare Workers" template, scoped to the
   account and to the zerodivisors.org zone, and note the account id.
3. GitHub: Settings, Secrets and variables, Actions: add the repository secrets
   `CLOUDFLARE_API_TOKEN` and `CLOUDFLARE_ACCOUNT_ID`.
4. GitHub: Actions, deploy-mcp, Run workflow. It builds the image, deploys the Worker with the
   custom domain mcp.zerodivisors.org, and waits for `/health` to answer.
5. Set `mcp_url: https://mcp.zerodivisors.org/mcp` in `store/config.yaml` and rebuild the site.

After that, publishing a release redeploys it from the release's tag
(`.github/workflows/deploy-mcp.yml`). The workflow never runs on pull requests, so their code
never sees the secrets, and the guard check refuses a contributor's change to `deploy/`.

## The site on Cloudflare Pages

zerodivisors.org itself is a static site: a Cloudflare Pages project, `zero-divisors`, made by
direct upload (not connected to git), with the custom domain zerodivisors.org, a proxied CNAME to
`zero-divisors.pages.dev`, and a redirect rule sending `www.zerodivisors.org/*` to
`https://zerodivisors.org/${1}` (301). It is deployed by hand from each release's tag
(RELEASING.md, step 5):

    python -m tp.pdfs && python -m tp.site && python -m tp.pages_bundle
    npx wrangler login                     # once per computer, in the browser
    npx wrangler pages deploy build/pages --project-name zero-divisors --branch main

Use wrangler, not the dashboard's drag-and-drop: the dashboard takes at most 1,000 files and
the site has several thousand (wrangler takes up to 20,000, each at most 25 MiB, which
`tp.pages_bundle` checks). The site is not built by Cloudflare from git because it needs the
PDFs, which are compiled with pdflatex and not kept in git, and because it must show the release
tag rather than whatever is on `main`. A GitHub workflow on release, like deploy-mcp, could do the
same steps; it needs pdflatex in the runner and the API token to have Cloudflare Pages: Edit.

Leave Cloudflare's Bot Fight Mode off for the zone: it challenges clients that are not browsers,
which would block AI tools reading `llms.txt` and connecting to mcp.zerodivisors.org.

## Deploy elsewhere

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

## The review service

The same image runs the review service (docs/REVIEWS.md) with a different command and its secrets
in the environment, and a writable volume for its state folder:

    docker run -p 8090:8090 -e PORT=8090 -e HOST=0.0.0.0 \
      -e TP_ORCID_CLIENT_ID=... -e TP_ORCID_CLIENT_SECRET=... -e TP_GITHUB_TOKEN=... \
      -e TP_REVIEW_STATE=/state -v review-state:/state \
      physics-graph-mcp python -m tp.review_server --store store --host 0.0.0.0

Give it its own address on the site's domain (for example `review.<domain>`) and put that in
`reviews.server.base_url`. Redeploy it after each merge, like the MCP endpoint, so that its
store (and so the fingerprints it checks) matches the site.

