# MCP Server Configs

These JSON files are templates for connecting external services to Claude Code.

## Required

- **airtable.json** -- Flow library storage. Free tier works.

## Optional

- **manychat.json** -- Live flow data (list flows, check tags/fields, verify setup). Cannot create or edit flows (API limitation).
- **slack.json** -- Team notifications when flows are captured or audits run.

## How configs work

The `/flow-setup` wizard merges these into your project's `.claude.json` automatically. You do not need to copy them manually.

If you prefer manual setup, copy the relevant JSON into your `.claude.json` file and replace the `${VAR}` placeholders with your actual API keys.
