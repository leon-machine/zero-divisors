# The Physics Graph's public, read-only MCP endpoint (tp/mcp_http.py). docs/HOSTING.md says how
# to run and deploy it. Build from the repository root, ideally at a release tag:
#   docker build -t physics-graph-mcp .
#   docker run -p 8080:8080 physics-graph-mcp        # then http://localhost:8080/mcp
FROM python:3.11-slim

WORKDIR /lab
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY tp/ tp/
COPY lib/ lib/
COPY store/ store/
COPY documents/ documents/
COPY recipes/ recipes/

# the derived state the reading tools use: evidence per result (build/graph.json) and the
# graph's layout for neighbourhood (build/layout.json). Layers 1-3 only: no code from the store
# runs while the image is built.
RUN python -m tp build --store store --no-mutants --layers 1-3 \
 && python -m tp.layout > /dev/null

ENV HOST=0.0.0.0 PORT=8080 PYTHONUNBUFFERED=1
EXPOSE 8080
USER nobody
CMD ["python", "-m", "tp.mcp_http", "--store", "store"]
