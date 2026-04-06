# The Flow Machine -- System Blueprint

## The Loop

```
                    ┌─────────────────────┐
                    │   SCREENSHOT IN      │
                    │   (any platform)     │
                    └──────────┬──────────┘
                               │
                    ┌──────────▼──────────┐
                    │   /flow-capture      │
                    │   Claude vision      │
                    │   reads every        │
                    │   element            │
                    └──────────┬──────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
    ┌─────────▼────────┐ ┌────▼────────┐ ┌────▼─────────┐
    │  Rebuild Guide   │ │  Flow Map   │ │  Extracted   │
    │  (step by step)  │ │  (diagram)  │ │  Copy        │
    └─────────┬────────┘ └────┬────────┘ └────┬─────────┘
              │                │                │
              └────────────────┼────────────────┘
                               │
                    ┌──────────▼──────────┐
                    │   /flow-library      │
                    │   Save, tag,         │
                    │   categorize          │
                    └──────────┬──────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
    ┌─────────▼────────┐ ┌────▼────────┐ ┌────▼─────────┐
    │  /flow-adapt     │ │  /flow-audit│ │  /flow-export│
    │  Customize for   │ │  10-point   │ │  Share as    │
    │  your business   │ │  diagnostic │ │  document    │
    └──────────────────┘ └─────────────┘ └──────────────┘
```

## Data Flow

```
Screenshots (input)
    │
    ▼
Claude Vision (analysis)
    │
    ▼
Rebuild Guide (output)
    │
    ▼
Airtable (storage)
    │
    ├──► Flow Library (all flows)
    ├──► Flow Audits (health history)
    └──► Capture Log (processing history)
```

## Architecture

- **Skills** (`.claude/commands/`) -- 8 Claude Code commands
- **Reference** (`reference/`) -- 8 universal framework documents
- **Storage** -- Airtable (3 tables)
- **MCPs** -- Airtable (required), ManyChat (optional), Slack (optional)
- **Input** -- Screenshot files (any format)
- **Output** -- Rebuild guides, flow maps, extracted copy
