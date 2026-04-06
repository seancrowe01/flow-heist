# n8n Automation

## Weekly Flow Digest

**File:** `flow-digest-workflow.json`

Runs every Monday at 9am. Reads your Flow Library from Airtable, counts activity from the past 7 days, and posts a summary to Slack.

### What it reports

- New flows captured this week
- Flows adapted this week
- Audits run this week
- Total library size
- Platform breakdown

### Setup (5 minutes)

1. Import `flow-digest-workflow.json` into your n8n instance
2. Add your Airtable Personal Access Token as a credential
3. Replace the Base ID and Table ID placeholders with your values from CLAUDE.md
4. Add your Slack webhook URL (optional -- you can remove the Slack node)
5. Toggle the workflow ON

### Without n8n

You don't need n8n. The Flow Machine is user-driven -- you run `/flow-capture` when you have a screenshot. The n8n workflow is just a weekly accountability nudge.
