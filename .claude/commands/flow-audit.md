---
name: flow-audit
description: Run a 10-point diagnostic checklist on any automation flow. Finds dead ends, compliance risks, missing tags, copy issues, and more. Works on screenshots, library flows, or live ManyChat flows.
---

# Flow Audit

You are a flow diagnostic system. You analyze automation flows against a 10-point checklist and produce a scorecard with prioritized fixes.

**What you produce:** A PASS/FAIL scorecard for 10 diagnostic checks, an overall health score (GREEN/YELLOW/RED), and specific fix instructions for every failure.

---

## Prerequisites

1. **A flow to audit** -- screenshot, library record, or ManyChat MCP
2. **Reference files:**
   - `reference/flow-diagnostics.md` (the 10-point checklist)
   - `reference/conversion-benchmarks.md` (expected metrics)
   - `reference/compliance.md` (platform rules)

---

## Input Handling

Three ways to get the flow data:

**Option A: Screenshot**
- User provides a screenshot path
- Run the `/flow-capture` analysis pipeline (Steps 1-4) to extract flow structure
- Then run the audit on the extracted data

**Option B: Library**
- User names a flow from the library: "audit Lead Magnet - PDF Delivery"
- Load from Airtable and audit the Flow Map and Copy fields

**Option C: ManyChat MCP (if connected)**
- User says "audit my flows"
- List all flows using ManyChat MCP (`flow_list`)
- User picks one
- Note: MCP can list flows but not read flow internals -- this works best combined with a screenshot

---

## Step 1: Read Reference Files

Read before auditing:
- `reference/flow-diagnostics.md` -- the full diagnostic matrix
- `reference/conversion-benchmarks.md` -- expected performance metrics
- `reference/compliance.md` -- platform rules

---

## Step 2: Get Flow Data

Depending on input type:
- Screenshot: analyze with vision, extract flow map
- Library: load Flow Map, Copy, Tags Needed, Custom Fields Needed from Airtable
- ManyChat MCP: get flow name and metadata, combine with screenshot if available

You need at minimum:
- Message content (what is being sent)
- Flow structure (what connects to what)
- Trigger type
- Platform

---

## Step 3: Run the 10-Point Checklist

### Check 1: Dead Ends
**What to look for:** Paths that lead nowhere -- no next message, no CTA, no redirect.
- **PASS:** Every path ends with a clear next step or intentional endpoint (e.g., "Thanks, talk soon!")
- **FAIL:** Found path(s) that end abruptly with no closure
- **Fix:** Add a closing message or redirect at each dead end
- **Priority:** Critical

### Check 2: Delay Timing
**What to look for:** Messages firing too fast (<1 second gaps) or delays pushing beyond the 24-hour messaging window.
- **PASS:** All delays are appropriate -- immediate for interactive, 1-24hr for follow-ups
- **FAIL:** Messages fire instantly in sequence (feels robotic) or delays exceed 24hr window
- **Fix:** Add 1-3 second typing delays between messages; keep follow-ups within 24hr
- **Priority:** Critical

### Check 3: Segmentation
**What to look for:** Does everyone get the exact same experience regardless of their answers?
- **PASS:** Flow branches based on user input (button choice, answer, tag)
- **FAIL:** Linear flow with no branching -- everyone gets identical messages
- **Fix:** Add at least one condition that personalizes the path based on user response
- **Priority:** Important

### Check 4: Fallback Handling
**What to look for:** What happens when user types something unexpected or doesn't respond?
- **PASS:** Default reply handles unexpected input; timeout re-engages after silence
- **FAIL:** Unexpected input causes flow to break or produces no response
- **Fix:** Add a fallback message: "Sorry, I didn't catch that. Try tapping one of the buttons above."
- **Priority:** Critical

### Check 5: Re-engagement
**What to look for:** If a user stops mid-flow, does the flow follow up?
- **PASS:** Smart delay triggers a "still there?" message after X hours of silence
- **FAIL:** Abandoned users are never contacted again
- **Fix:** Add a 24hr follow-up: "Hey {{first_name}}, just checking in -- did you still want [thing]?"
- **Priority:** Important

### Check 6: Button Overload
**What to look for:** More than 3 buttons or quick replies on any single message.
- **PASS:** All messages have 3 or fewer choices
- **FAIL:** Messages with 4+ options causing choice paralysis
- **Fix:** Reduce to 2-3 options. If you need more categories, use a two-step menu (pick category > pick option)
- **Priority:** Important

### Check 7: Tag Coverage
**What to look for:** Are leads being tagged at key conversion points?
- **PASS:** Tags applied at trigger, email collection, download, booking, completion
- **FAIL:** No tags -- leads enter and exit with no way to segment them later
- **Fix:** Add tags at minimum: trigger engagement, data collected, CTA completed
- **Priority:** Critical

### Check 8: Compliance
**What to look for:** Platform rule violations.
- **PASS:** All messages within 24hr window, proper opt-in, no banned content types
- **FAIL:** Promotional messages after 24hr window, no opt-in mechanism, restricted content
- **Fix:** Keep automations within 24hr of user action; use OTN for later messages; add opt-out
- **Priority:** Critical

### Check 9: Copy Quality
**What to look for:** Wall of text, no personalization, weak CTAs.
- **PASS:** Messages are under 3 lines, use {{first_name}}, have clear action-oriented CTAs
- **FAIL:** Long paragraphs, generic copy, vague CTAs like "click here"
- **Fix:** Break long messages into multiple shorter ones; add personalization; use specific CTA labels
- **Priority:** Important

### Check 10: Measurement
**What to look for:** Can you track who completed the flow and converted?
- **PASS:** Tags or custom fields mark flow completion and key conversions
- **FAIL:** No tracking -- you cannot tell who finished the flow or took the desired action
- **Fix:** Add a "completed-[flow-name]" tag at the end; set a custom field with completion date
- **Priority:** Critical

---

## Step 4: Calculate Score

Count PASS results:
- **GREEN (9-10):** Flow is solid. Ship it.
- **YELLOW (6-8):** Usable but has leaks. Fix the failures before scaling.
- **RED (0-5):** Major issues. Fix critical failures before going live.

---

## Step 5: Generate Scorecard

```
=== FLOW AUDIT: {Flow Name} ===

Platform: {Platform}
Type: {Flow Type}
Trigger: {Trigger Details}
Messages: {Count}

Overall: {GREEN/YELLOW/RED emoji} {SCORE} ({X}/10 passed)

✅ PASS  Dead Ends
✅ PASS  Delay Timing
❌ FAIL  Segmentation -- everyone gets the same path
✅ PASS  Fallback Handling
❌ FAIL  Re-engagement -- no follow-up for abandoned users
✅ PASS  Button Count
❌ FAIL  Tag Coverage -- no tags at conversion points
✅ PASS  Compliance
✅ PASS  Copy Quality
✅ PASS  Measurement

PRIORITY FIXES:
1. [Critical] Add tags at key points (download, email collected, completion)
   Where: After MSG 3 (delivery) and MSG 5 (CTA click)
   Tags: "downloaded-{asset}", "email-collected", "flow-completed"

2. [Important] Add re-engagement message
   Where: After MSG 2 (email collection), add 24hr smart delay
   Copy: "Hey {{first_name}}, still want that [asset]? Tap below and I'll send it over."

3. [Important] Add condition branch after MSG 4
   Where: Split based on whether they clicked the CTA
   Why: Qualified leads get follow-up, others get value content
```

---

## Step 6: Save Audit to Airtable

If Airtable is connected:

```
Use Airtable MCP: create_record
  base_id: {from CLAUDE.md}
  table_id: {Flow Audits table ID}
  fields: {
    Flow Name: {name},
    Audit Date: {today},
    Platform: {platform},
    Overall Score: {GREEN/YELLOW/RED},
    Dead Ends: {PASS/FAIL},
    Delay Timing: {PASS/FAIL},
    Segmentation: {PASS/FAIL},
    Fallback Handling: {PASS/FAIL},
    Re-engagement: {PASS/FAIL},
    Button Count: {PASS/FAIL},
    Tag Coverage: {PASS/FAIL},
    Compliance: {PASS/FAIL},
    Copy Quality: {PASS/FAIL},
    Measurement: {PASS/FAIL},
    Issues Found: {count of FAIL},
    Fixes: {prioritized fix list},
    Notes: {any additional observations}
  }
```

---

## Step 7: Offer Next Steps

```
Want me to fix these issues?

- /flow-adapt -- I'll rebuild this flow with all fixes applied
- /flow-templates -- Start fresh with a proven template instead
- Run this audit again later to track improvement
```

---

## CRITICAL RULES

1. Read reference files BEFORE auditing. Don't wing it.
2. Every FAIL must include a specific fix with exact instructions.
3. Prioritize fixes: Critical first, then Important.
4. Never rate a flow GREEN if it has compliance issues (Check 8).
5. If auditing from a screenshot, acknowledge what you CAN'T see (backend actions, tags, fields).
6. The audit is non-judgmental. Don't criticize the flow -- diagnose and prescribe.
7. If the same flow has been audited before, mention the previous score and whether it improved.
