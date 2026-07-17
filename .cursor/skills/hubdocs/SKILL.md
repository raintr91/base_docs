---
name: hubdocs
description: /hubdocs — optional local index for arc42/C4 Markdown relationships.
disable-model-invocation: true
extractBundle: architecture-core
---

# /hubdocs — local adapter

Markdown in this repository owns architecture and product truth. Hubdocs is an
optional read/index aid; it does not own or generate the documentation.

Usage and setup guidance: [`platform/toolchain/HUBDOCS.md`](../../../platform/toolchain/HUBDOCS.md).

## Local relationships and routing

- `LND-*` / `CTX-*` → `/context`
- `CTR-*` → `/containers`
- `CMP-*` → `/component`
- `FLOW-*` → `/journey`
- `DEP-*` → `/deployment`
- `ADR-*` → `/decision`

When the MCP is already connected, prefer `hubdocs_route`, ID lookup,
dependency/dependent queries, journey/orphan checks, and link validation before
loading broad Markdown trees.

If Hubdocs is unavailable, use repository search and the architecture skills.
Do not install, wire, or treat Hubdocs as required from this adapter.
