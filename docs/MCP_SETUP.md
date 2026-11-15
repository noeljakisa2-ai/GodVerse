# GodVerse MCP

This service exposes the GodVerse project through the Model Context Protocol
using Streamable HTTP.

## Hosted deployment

The repository includes a Render Blueprint at `render.yaml`. To create the
hosted service, sign in to Render, choose **New → Blueprint**, and select
`noeljakisa2-ai/GodVerse`. Choose the free instance if offered.

After deployment, the MCP endpoint is:

`https://godverse-mcp.onrender.com/mcp`

The URL above is the expected Render service address, not a confirmed live URL.
Render may assign a different hostname; use the URL shown on the service page
and append `/mcp`.

## Tools

- `godverse_status`
- `godverse_project_info`
- `godverse_capabilities`

## Current boundary

This initial MCP is read-only project metadata. It is not yet connected to a
live GodVerse browser session, world state, or simulation controls. Do not
describe it as controlling the game/world until that integration is implemented
and tested.

## Local run

```bash
pip install -r requirements-mcp.txt
python mcp_server.py
```

The local endpoint is `http://localhost:10000/mcp`.
