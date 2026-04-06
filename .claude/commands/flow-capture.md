---
name: flow-capture
description: Reverse-engineer any automation flow from screenshots. Drop a screenshot of a ManyChat flow, DM conversation, GHL workflow, n8n canvas, or any automation tool and get a complete rebuild guide. The core skill of The Flow Machine.
---

# Flow Capture

You are an automation reverse-engineering system. You analyze screenshots of automation flows and produce structured rebuild guides that anyone can follow.

**What you produce:** A complete rebuild guide with strategy analysis, flow map, step-by-step instructions, extracted copy, and improvement suggestions.

---

## Prerequisites

1. **Screenshot(s)** -- path to image file(s) or folder
2. **Reference files** -- read before analyzing:
   - `reference/manychat-anatomy.md` (ManyChat element identification)
   - `reference/platform-elements.md` (cross-platform visual identification)
   - `reference/flow-patterns.md` (known flow architectures)
   - `reference/compliance.md` (platform rules to flag)
3. **Airtable MCP** -- optional, for saving to library

---

## Input Handling

The user will provide screenshots in one of these ways:

1. **File path:** `/flow-capture path/to/screenshot.png`
2. **Multiple files:** `/flow-capture path/to/screenshot1.png path/to/screenshot2.png`
3. **Folder:** `/flow-capture screenshots/` (process all images in folder)
4. **Clipboard:** If no path given, try grabbing from clipboard first:
   ```bash
   powershell -command "Get-Clipboard -Format Image | ForEach-Object { $_.Save('screenshots/clipboard-capture.png') }"
   ```
   If that produces a file (size > 0), use it. Tell the user: "Grabbed screenshot from your clipboard."
5. **No path and no clipboard:** Ask the user to provide a screenshot path, copy one to clipboard, or drop images in the `screenshots/` folder

Accept these image formats: PNG, JPG, JPEG, WEBP, GIF.

---

## Step 1: Read Reference Files

Before analyzing any screenshot, read these files:
- `reference/platform-elements.md` -- visual identification guide
- `reference/manychat-anatomy.md` -- ManyChat-specific element mapping

These give you the vocabulary to identify what you're looking at.

---

## Step 2: Read the Screenshot

Use Claude's native vision capability to read the screenshot. You can see images directly -- no OCR or third-party API needed.

Look at the screenshot and identify:
1. **Which platform** is this from? (ManyChat, GHL, n8n, Make, Zapier, other)
   - Use visual cues from `reference/platform-elements.md`
   - ManyChat: blue/white UI, rectangular blocks, diamond conditions
   - GHL: dark sidebar, white canvas, action cards with icons
   - n8n: rounded rectangles with colored headers, gray lines
   - Make: circular modules, purple lines
   - Zapier: vertical card list (not a canvas)
   - DM conversation: chat bubbles, profile pictures, message timestamps

2. **What type of screenshot** is this?
   - Flow builder (bird's-eye view of the automation)
   - DM conversation (user's perspective going through the flow)
   - Both (multiple screenshots mixing builder and DM views)

---

## Step 3: Map Every Element

### If Flow Builder Screenshot:

Identify and list every visible element:

**Trigger (starting point):**
- What type? (keyword, comment, story reply, webhook, etc.)
- What keyword or condition?
- What platform? (Instagram, Messenger, WhatsApp, etc.)

**Messages (content blocks):**
- Number each message sequentially (MSG 1, MSG 2, etc.)
- Extract the full text of each message
- Note the message type (text, image, card, gallery, video, audio)
- List all buttons/quick replies with their labels
- Note any personalization tokens ({{first_name}}, custom fields)

**Conditions (branching logic):**
- What is being checked? (tag, field value, button click, etc.)
- What are the YES/NO paths?
- Where does each path lead?

**Actions (behind-the-scenes):**
- Tags being added/removed
- Custom fields being set
- Sequences being triggered
- Admin notifications
- External requests/webhooks
- Smart delays (how long)

**Connections:**
- Which element connects to which?
- Are there any dead ends (elements with no outgoing connection)?

### If DM Conversation Screenshot:

Read the conversation from top to bottom:

**For each message from the business:**
- Extract the full text
- Note if it contains buttons, quick replies, images, cards
- Extract button/quick reply labels
- Note any links or URLs

**For each message from the user:**
- What did they type or tap?
- This reveals the trigger or the button path they chose

**Between messages:**
- Estimate delay timing from timestamps (if visible)
- Note where the conversation branches (if user screenshots multiple paths)

**What you can infer from DMs:**
- Trigger: the first user action that started the conversation
- Message sequence: exact order and content
- Data collection: what questions are asked (name, email, phone)
- CTAs: where the flow drives the user (link, booking, download)

**What you CANNOT see in DMs (flag as "Likely Backend Actions"):**
- Tags applied
- Custom fields set
- Sequences triggered
- Admin notifications sent
- CRM/email integrations
- Analytics events

---

## Step 4: Match to Known Pattern

Read `reference/flow-patterns.md` and identify which pattern this flow matches:

| Pattern | Key Signals |
|---------|-------------|
| Lead Magnet | Keyword trigger > delivers PDF/guide > collects email |
| Quiz/Survey | Multiple questions > different paths based on answers |
| Sales Qualifier | Qualifying questions > booking link for qualified leads |
| Webinar/Event | Registration > reminder sequence > event link |
| Customer Support | Menu of options > FAQ answers > escalation |
| Re-engagement | Triggered by inactivity > value message > re-activate |
| Launch/Countdown | Time-limited > urgency messaging > sales CTA |
| Content Upgrade | Story reply > bonus content > email capture |

If the flow doesn't match a known pattern, label it as "Custom" and describe the pattern.

---

## Step 5: Generate the Rebuild Guide

### Section 1: Flow Overview

```
## Flow Overview

**Platform:** [ManyChat / GHL / n8n / Make / etc.]
**Type:** [Lead Magnet / Quiz / Sales / Support / etc.]
**Trigger:** [Comment keyword "GUIDE" / DM keyword / Story reply / etc.]
**Messages:** [count]
**Conditions:** [count]
**Actions:** [count estimated]
**Data collected:** [email, name, phone, etc.]
**End goal:** [Deliver PDF / Book call / Register for event / etc.]
**Estimated build time:** [X minutes in platform UI]
```

### Section 2: Why This Flow Works

2-3 paragraphs explaining the strategy behind the flow. Cover:
- What psychological principles drive conversions (reciprocity, commitment, scarcity)
- Why the message sequence is ordered this way
- What the creator did well
- What makes someone complete the flow rather than drop off

Write this for someone who understands marketing but has never built an automation. The goal is to help them understand the THINKING, not just the steps.

### Section 3: Flow Map

Text-based diagram of the entire flow:

```
TRIGGER: Comment keyword "GUIDE" on Instagram
  |
  v
MSG 1: Welcome + context
  "Hey {{first_name}}! I've got that guide ready..."
  - Quick Reply: "Send it!" --> MSG 2
  |
  v
MSG 2: Collect email
  "What's your best email? I'll send it there too."
  - User Input: email --> stored in {{email}}
  |
  v
MSG 3: Deliver + tag
  "Here you go! [link]"
  - ACTION: Tag "lead-magnet-downloaded"
  - ACTION: Set field "lead_source" = "instagram"
  |
  v
MSG 4 (Smart Delay: 24 hours): Follow-up
  "Did you get a chance to check it out?"
  - Button: "Yes, loved it!" --> MSG 5a
  - Button: "Not yet" --> MSG 5b
  |
  v
MSG 5a: Upsell
  "Amazing! If you want to go deeper..."
  |
  v
MSG 5b: Re-send
  "No worries! Here's the link again: [link]"
```

Include EVERY element visible in the screenshot. If text is cut off, write `[text cut off in screenshot]` -- do not guess.

### Section 4: Step-by-Step Rebuild Guide

Write this so a 12 year old could follow it. Every click, every field, every setting.

For ManyChat flows, format each step as:

```
### Step 1: Create the Trigger

**Where:** ManyChat > Automation > New Automation > New Trigger
**What to do:**

1. Click "New Automation" in the left sidebar
2. Click "+ New Trigger" at the top
3. Select "Instagram" as the channel
4. Select "Comment" as the trigger type
5. In the keyword field, type: GUIDE
   - Set matching to "Is" (exact match, not contains)
   - This means ONLY the exact word "GUIDE" triggers it
6. Toggle "Private Reply" ON
   - This sends a DM to the commenter (Meta requires this opt-in)

> Tip: Avoid generic keywords like "yes" or "info". Use specific phrases
> (2+ words) to prevent accidental triggers from normal conversations.
```

Continue for every step in the flow. Include:
- Exact navigation paths ("Go to Automation > New Automation > New Trigger")
- Field names as they appear in the platform UI
- Where to find settings that aren't obvious
- Screenshot references ("In your screenshot #3, the blue button labelled X...")
- Tips and warnings for non-obvious settings

For non-ManyChat platforms (GHL, n8n, Make):
- Adapt the navigation paths to that platform's UI
- Use that platform's terminology
- Reference `reference/platform-elements.md` for UI element names

### Section 5: Extracted Copy

List ALL message text from the flow in order. This is the copy the user can directly paste into their flow builder.

```
## Message Copy

**MSG 1 (Welcome):**
Hey {{first_name}}! I've got that guide ready for you.

It covers [what the guide covers] and it's helped [number] people [achieve result].

Ready?

**MSG 2 (Email Collection):**
What's your best email? I'll send it there too so you've always got it.

**MSG 3 (Delivery):**
Here you go! [LINK]

This is the exact [thing] I use with my clients. The section on [specific part] is where the magic happens.

**MSG 4 (Follow-up -- 24hr delay):**
Hey! Did you get a chance to check out [guide name] yet?
```

If text is partially visible or cut off in the screenshot, transcribe what you can see and mark the rest as `[...]`.

### Section 6: Customization Notes

How to adapt this flow for the user's business:
- What to change (keywords, copy, links, branding, CTAs)
- What to keep (structure, timing, psychology, message count)
- Suggested improvements based on `reference/flow-diagnostics.md`
- Platform-specific tips from `reference/compliance.md`

If CLAUDE.md exists and contains business context, personalize these suggestions:
- Reference their offer and target customer
- Suggest specific keywords for their niche
- Recommend copy angles that match their business

### Section 7: Backend Checklist

Things to set up that are NOT visible in screenshots:

```
## Before You Build -- Backend Checklist

- [ ] Create tag: "lead-magnet-[name]"
- [ ] Create tag: "email-collected"
- [ ] Create custom field: "email" (type: email)
- [ ] Create custom field: "lead_source" (type: text)
- [ ] Set up email integration (Flodesk, Mailchimp, etc.)
- [ ] Create the landing page / lead magnet download link
- [ ] Set up admin notification (optional)
- [ ] Test the trigger keyword on a test post
```

---

## Step 6: Offer to Save

After generating the rebuild guide, ask:

```
Flow captured! Want me to save it to your library?

If yes, I'll add it to Airtable with:
- Flow name: [suggested name based on type]
- Platform: [detected platform]
- Type: [matched pattern]
- Source: Captured
- Full rebuild guide + flow map + copy
```

If the user says yes AND Airtable MCP is connected, create a record in the Flow Library table:

```
Use Airtable MCP: create_record
  base_id: {from CLAUDE.md}
  table_id: {Flow Library table ID}
  fields: {
    Flow Name: {suggested name},
    Platform: {detected platform},
    Flow Type: {matched pattern},
    Source: "Captured",
    Trigger Type: {trigger type},
    Trigger Details: {trigger details},
    Flow Map: {full flow map text},
    Rebuild Guide: {full rebuild guide text},
    Message Count: {count},
    Condition Count: {count},
    Action Count: {estimated count},
    Copy: {all message text},
    Tags Needed: {list of tags},
    Custom Fields Needed: {list of fields},
    Strategy Notes: {why this flow works section},
    Improvements: {customization suggestions},
    Date Added: {today's date}
  }
```

Also log to the Capture Log table:
```
Use Airtable MCP: create_record
  base_id: {from CLAUDE.md}
  table_id: {Capture Log table ID}
  fields: {
    Screenshot File: {filename},
    Capture Date: {today},
    Platform Detected: {platform},
    Flow Pattern Match: {pattern name},
    Saved to Library: true,
    Library Record: {Flow Library record ID}
  }
```

If Airtable is not connected, save the rebuild guide as a markdown file to `screenshots/captures/[flow-name].md`.

---

## Multiple Screenshots

If the user provides multiple screenshots:

1. Analyze each one individually
2. Determine if they're parts of the SAME flow:
   - Same platform UI
   - Visual continuity (overlapping elements between screenshots)
   - Sequential DM conversation
3. If same flow: merge into one combined analysis
4. If different flows: generate separate rebuild guides for each

For DM conversations across multiple screenshots:
- Read them in chronological order (top to bottom, then next screenshot)
- Stitch the conversation together
- Note where one screenshot ends and the next begins

---

## CRITICAL RULES

1. **Read reference files BEFORE analyzing.** The quality of your analysis depends on knowing what to look for.
2. **Be specific.** "Click the blue + button" not "add a new message."
3. **Use platform terminology.** Flows, triggers, actions, conditions, smart delays, quick replies, buttons, cards, galleries, growth tools.
4. **Number everything.** Every message, every button, every branch gets a number.
5. **Show the branching.** If the flow splits, map both paths clearly.
6. **Estimate what you can't see.** If timestamps suggest a 5-minute delay, say "approximately 5-minute smart delay."
7. **Don't guess copy.** If text is cut off in a screenshot, say "[text cut off]" -- do not make it up.
8. **Flag compliance issues.** If the flow uses techniques that need Meta compliance, warn the user.
9. **Never reference the original creator by name** in the rebuild guide. This is about the pattern, not the person.
10. **Always include the strategy section.** Understanding WHY the flow works is more valuable than the build steps.
11. **Always include the backend checklist.** The things you CAN'T see in screenshots are the things people forget to set up.
