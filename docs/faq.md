# FAQ

## General

**Q: Do I need a ManyChat account?**
No. The core feature (screenshot analysis) works with just Claude Code and Airtable. ManyChat MCP is optional -- it lets you check if tags/fields exist before building, but the rebuild guides work without it.

**Q: Does this actually build the flow for me?**
No. ManyChat's API does not support flow creation. The Flow Machine generates a step-by-step rebuild guide that you follow in the ManyChat UI. Think of it as a detailed recipe, not a robot chef.

**Q: What platforms are supported?**
ManyChat has full support (templates, audits, anatomy reference). GHL, n8n, Make, and Zapier work for screenshot analysis and rebuild guides. Claude can read any automation screenshot.

**Q: How accurate is the screenshot analysis?**
Claude's vision is strong with automation screenshots because the UIs are consistent and predictable. Flow builder screenshots give 90%+ accuracy. DM conversation screenshots give the message content perfectly but can't see backend actions (tags, fields, webhooks).

**Q: Is this legal?**
You're analyzing publicly visible screenshots and generating instructions. You're not scraping private data, bypassing authentication, or copying code. The same way you can look at a restaurant's menu and cook the dish at home.

---

## Setup

**Q: What API keys do I need?**
Just an Airtable API key (free tier). ManyChat and Slack are optional.

**Q: Can I use an existing Airtable base?**
Yes. The setup wizard asks if you want a new base or existing. It creates 3 new tables in whichever base you choose.

**Q: What if Airtable table creation fails?**
See `docs/airtable-setup.md` for manual setup instructions.

---

## Usage

**Q: Can I capture flows from courses/paid content?**
You can screenshot anything you can see on your screen. The Flow Machine doesn't access paid content -- it analyzes screenshots you provide. Use your judgement about sharing copyrighted material.

**Q: How many screenshots do I need for one flow?**
One screenshot of a flow builder view often captures the whole flow. For DM conversations, you might need 3-5 screenshots to capture all the messages and paths. The batch skill handles multiple screenshots.

**Q: Can I export my library?**
Yes. `/flow-export` generates clean markdown documents. You can also export the full Airtable table as CSV.

---

## Pairing

**Q: How does this work with the Ads Machine?**
Ads Machine researches what ads to run. Flow Machine builds the automation that captures leads from those ads. Ads Machine drives traffic, Flow Machine converts it.

**Q: How does this work with the Agency Command Centre?**
ACC tracks client performance. Flow Machine builds the client's automation flows. ACC tells you if the funnel is leaking, Flow Machine helps you fix it.
