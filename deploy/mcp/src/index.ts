// The Worker in front of the MCP server's container (wrangler.jsonc). The server is stateless
// and read-only, so one instance serves everyone; it sleeps after 15 minutes without a request
// (billing stops while it sleeps) and the next request wakes it, which takes about 10 seconds
// while the store loads.
import { Container, getContainer } from "@cloudflare/containers";

export class GraphServer extends Container {
  defaultPort = 8080;      // tp.mcp_http listens here (the Dockerfile's PORT)
  sleepAfter = "15m";
}

export default {
  async fetch(request: Request, env: { GRAPH: DurableObjectNamespace<GraphServer> }): Promise<Response> {
    return getContainer(env.GRAPH, "graph").fetch(request);
  },
};
