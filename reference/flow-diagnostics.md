# Flow Diagnostics: 10-Point Audit Checklist

Run this checklist on every flow before it goes live and during monthly audits. Each check has a clear PASS/FAIL and a specific fix.

---

## The 10 Checks

### 1. Dead Ends

Paths that lead nowhere. The user hits a message with no next step, no button, no CTA.

| | Details |
|---|--------|
| **What to look for** | Any message node with zero outgoing connections. Any button that links to nothing. Any conditional branch with an empty path. |
| **PASS** | Every path ends with either a clear CTA (button, link, quick reply), a handoff to a human, or an explicit closing message ("You're all set!"). |
| **FAIL** | User receives a message and then... nothing. No response options, no next step, no closure. Flow just stops. |
| **Fix** | Trace every branch to its end. Add a closing message, a CTA, or a loop back to the main menu. If a branch is incomplete, either build it or remove the option that leads to it. |
| **Priority** | Critical |

---

### 2. Delay Timing

Messages firing too fast (feels robotic) or too slow (user loses interest or hits the 24-hour window).

| | Details |
|---|--------|
| **What to look for** | Time delays between messages. Multiple messages sent in rapid succession with no pause. Delays longer than a few hours in a lead capture flow. Any delay that risks crossing the 24-hour messaging window. |
| **PASS** | 1-3 second delay between consecutive messages. Typing indicator enabled. No delays longer than 1 hour in active lead capture flows. Re-engagement messages sent well before the 24-hour window closes. |
| **FAIL** | Three messages arrive simultaneously (feels like spam). Or a 12-hour delay sits between "What's your email?" and the delivery message. Or a follow-up fires at hour 25, violating platform rules. |
| **Fix** | Add 1-3 second delays between messages. Enable typing indicators. For long delays, add a "smart delay" that checks if the user has already responded. Move any message that might cross the 24-hour window to within 23 hours. |
| **Priority** | Critical |

---

### 3. Segmentation

Everyone gets the same path regardless of their answers. The flow collects data but never uses it.

| | Details |
|---|--------|
| **What to look for** | Conditional logic (if/else branches) based on user responses. Different paths for different user types. Personalized messages using collected data. |
| **PASS** | At least one branch point where the flow adapts based on user input. Qualifier questions route users to different outcomes (e.g., "Ready to buy" vs "Just browsing" get different next steps). Custom fields are set and used downstream. |
| **FAIL** | User answers 5 qualifying questions and then everyone gets the exact same sales pitch. Collected data sits in custom fields but is never referenced in any message or condition. |
| **Fix** | Map the user journey. Identify where answers should change the path. Add condition nodes after key questions. At minimum: separate paths for qualified vs unqualified leads. |
| **Priority** | Important |

---

### 4. Fallback Handling

What happens when the user says something unexpected, sends an emoji, or types gibberish instead of clicking a button.

| | Details |
|---|--------|
| **What to look for** | Default reply or fallback message at every free-text input step. Handling for unexpected responses. Graceful recovery that gets the user back on track. |
| **PASS** | Every input step has a fallback: "I didn't catch that. Could you try again?" or "Just tap one of the buttons above." After 2-3 failed attempts, handoff to a human or offer to restart. |
| **FAIL** | User types "maybe" when the flow expects an email address. Flow breaks, goes silent, or loops infinitely. No validation on inputs. |
| **Fix** | Add a Default Reply at every text input step. Use input validation (email regex, phone format). After 2 failed attempts, offer a button-based alternative or route to live chat. |
| **Priority** | Critical |

---

### 5. Re-engagement

What happens when a user starts a flow and goes silent mid-way. No follow-up means lost leads.

| | Details |
|---|--------|
| **What to look for** | Smart delay + check for response. Follow-up message for users who stop responding. Re-engagement sequence with a new hook or reminder. |
| **PASS** | If no response within 1-3 hours, a follow-up fires: "Still want that guide? Just tap below." If still no response at 23 hours, one final nudge before the window closes. Tags applied so you can retarget later. |
| **FAIL** | User drops off at step 3. Nothing happens. They are gone forever. No follow-up, no tag, no retargeting. |
| **Fix** | Add a Smart Delay (1-3 hours) after each critical step. If the user hasn't responded, send a short re-engagement message with a button. Before the 24-hour window closes, send a final message. Tag all abandoned users for ad retargeting. |
| **Priority** | Critical |

---

### 6. Button Overload

More than 3 options on a single message causing choice paralysis. Users freeze and don't click anything.

| | Details |
|---|--------|
| **What to look for** | Count the buttons and quick replies on every message. Look for "menu" messages with 4+ options. Check if all buttons are actually needed. |
| **PASS** | Maximum 3 buttons per message. Primary CTA is visually obvious (first position). Each button leads somewhere meaningfully different. |
| **FAIL** | A message has 5 buttons: "Learn More", "See Pricing", "Book a Call", "Watch Video", "Ask a Question". User taps nothing because they can't decide. |
| **Fix** | Cut to 3 buttons maximum. If you need more options, split into two sequential messages ("What are you most interested in?" then show relevant sub-options). Use the first button position for the action you want most. |
| **Priority** | Important |

---

### 7. Tag Coverage

Leads pass through the flow but never get tagged. This means no segmented retargeting, no audience building, no reporting.

| | Details |
|---|--------|
| **What to look for** | Tags applied at key moments: flow entry, qualification answers, lead magnet delivered, booking made, flow completed, flow abandoned. Custom fields populated with collected data. |
| **PASS** | Every flow applies at minimum: an entry tag (e.g., "lead-magnet-guide-name"), a completion tag, and a qualification tag (e.g., "qualified-hot" or "not-ready"). Data collected is stored in custom fields. |
| **FAIL** | 500 people go through a lead magnet flow. You have no way to tell who completed it, who dropped off, or who is qualified. Your subscriber list is an unsegmented blob. |
| **Fix** | Add tag actions at: flow entry, each major branch point, completion, and abandonment. Name tags consistently (e.g., "flow-[name]-entered", "flow-[name]-completed"). Store all collected data in custom fields for future use. |
| **Priority** | Important |

---

### 8. Compliance

Messages sent outside the 24-hour window, missing opt-in confirmation, or promotional content in restricted message types.

| | Details |
|---|--------|
| **What to look for** | Any message that could fire more than 24 hours after the user's last interaction. Opt-in confirmation at flow start. Promotional content in non-promotional message types (WhatsApp template categories). One-Time Notification (OTN) token collection. |
| **PASS** | All automated messages fire within 23 hours of last user interaction (1-hour safety buffer). Opt-in collected and stored. OTN tokens requested for future promotional sends. WhatsApp templates categorized correctly. |
| **FAIL** | A "limited time offer" message fires 3 days after the user last interacted. No opt-in recorded. Promotional WhatsApp messages sent as "utility" templates (risks account ban). |
| **Fix** | Audit every delay in the flow. If any message could cross 24 hours, either move it earlier or gate it behind an OTN token. Add an opt-in step at flow entry. For WhatsApp, submit templates under the correct category. |
| **Priority** | Critical |

---

### 9. Copy Quality

Wall of text messages, no personalization, weak CTAs, robotic tone.

| | Details |
|---|--------|
| **What to look for** | Message length (count the lines). Use of the subscriber's first name. Conversational tone vs corporate tone. CTA clarity and urgency. Emoji usage (some is good, a wall of emojis is bad). |
| **PASS** | Messages are 1-3 lines max. First name used where natural. Tone matches the brand (casual, warm, direct). Every message with a CTA has a clear, specific action ("Tap below to grab it" not "Click here for more information"). |
| **FAIL** | A single message is 8 lines of dense text. No personalization. CTA says "Submit" instead of something human. Messages read like a legal document or a marketing email crammed into a chat bubble. |
| **Fix** | Break long messages into 2-3 short ones with delays between them. Add `{{first_name}}` where it fits naturally. Rewrite CTAs as conversational commands ("Grab your copy" not "Download now"). Read every message out loud. If it doesn't sound like a real person texting, rewrite it. |
| **Priority** | Important |

---

### 10. Measurement

No way to track how the flow performs. No conversion tracking, no completion tracking, no revenue attribution.

| | Details |
|---|--------|
| **What to look for** | UTM parameters on all external links. Conversion events or goals defined. Step-by-step completion tracking (tags or custom fields at each step). Revenue attribution for booking or purchase flows. |
| **PASS** | Every link has UTMs. You can pull a report showing: how many entered, how many completed each step, where drop-offs happen, and (for sales flows) revenue generated. Dashboard or spreadsheet tracks flow performance weekly. |
| **FAIL** | You know 1,000 people entered the flow. You have no idea how many finished, where they dropped off, or whether anyone bought. Links have no UTMs so Google Analytics shows all DM traffic as "direct." |
| **Fix** | Add UTM parameters to every external link (`utm_source=manychat&utm_medium=dm&utm_campaign=flow-name`). Add step-tracking tags at each major node. Build a simple dashboard (Airtable or Google Sheets) that pulls tag counts weekly. For booking/sales flows, connect the payment or booking event back to the flow entry. |
| **Priority** | Critical |

---

## Audit Summary Template

| # | Check | Status | Notes |
|---|-------|--------|-------|
| 1 | Dead Ends | PASS / FAIL | |
| 2 | Delay Timing | PASS / FAIL | |
| 3 | Segmentation | PASS / FAIL | |
| 4 | Fallback Handling | PASS / FAIL | |
| 5 | Re-engagement | PASS / FAIL | |
| 6 | Button Overload | PASS / FAIL | |
| 7 | Tag Coverage | PASS / FAIL | |
| 8 | Compliance | PASS / FAIL | |
| 9 | Copy Quality | PASS / FAIL | |
| 10 | Measurement | PASS / FAIL | |

**Score: ___ / 10 PASS**

- 10/10: Ship it.
- 7-9: Fix the failures before going live.
- 4-6: Significant rework needed. Do not launch.
- Under 4: Rebuild from scratch using a proven template.

---

## Common Anti-Patterns

### The "Wall of Text"

Messages over 3 lines kill response rates. Users see a block of text in a chat bubble and instinctively skip it.

- **What it looks like:** A single message with 5-10 lines explaining the offer, the benefits, the process, and the CTA all in one paragraph.
- **Why it fails:** DMs are not emails. People scan, they don't read. A wall of text in a chat bubble feels overwhelming.
- **The fix:** Break it into 2-3 short messages (1-2 lines each) with 1-2 second delays between them. Lead with the hook, follow with the value, close with the CTA. Each message should be one thought.

---

### The "Button Menu"

Five or more buttons on a single message. Nobody clicks because they can't decide.

- **What it looks like:** "What are you interested in?" followed by 6 buttons covering every possible topic.
- **Why it fails:** Choice paralysis. Research shows that 3 options is the sweet spot. Beyond that, decision fatigue kicks in and the default action is "do nothing."
- **The fix:** Maximum 3 buttons. If you need to cover more options, use a two-step approach: first message narrows the category (2-3 broad options), second message shows specific choices within that category.

---

### The "Ghost Flow"

User starts a flow, stops responding, and never hears from you again. No re-engagement, no follow-up, no retargeting tag.

- **What it looks like:** Flow has 6 steps. User completes step 2 and goes silent. The flow just waits forever. No follow-up fires. No tag is applied. The lead is lost.
- **Why it fails:** 40-60% of users will pause or abandon mid-flow. If you have no re-engagement, you're losing the majority of your potential conversions.
- **The fix:** Add a Smart Delay after every critical step. If no response in 1-3 hours, send a casual nudge ("Still there? Tap below whenever you're ready."). Before the 24-hour window closes, send a final message. Tag abandoned users for ad retargeting.

---

### The "Compliance Bomb"

Sending promotional messages after the 24-hour messaging window has closed. This violates platform rules and can get your account banned.

- **What it looks like:** User interacted 3 days ago. An automated "Flash sale -- 50% off today only!" message fires. Platform flags it. Account restricted.
- **Why it fails:** Instagram, Messenger, and WhatsApp all enforce a 24-hour window for free-form messaging. Outside that window, you can only send approved templates (WhatsApp) or use One-Time Notification tokens (Messenger).
- **The fix:** Never schedule promotional messages with delays longer than 23 hours. Collect OTN tokens during active conversations for future sends. For WhatsApp, pre-approve templates for time-sensitive promotions. Build a re-engagement ad audience instead of violating messaging rules.

---

### The "Data Black Hole"

The flow collects emails, phone numbers, quiz answers, and preferences. None of it is ever used. It sits in custom fields that nobody looks at.

- **What it looks like:** A qualification flow asks 5 questions, saves answers to custom fields, then sends everyone the same generic follow-up regardless of what they said.
- **Why it fails:** Users gave you their data expecting a personalized experience. When they get a generic response, trust drops. And you've wasted the most valuable asset in your funnel: first-party data.
- **The fix:** Every piece of data you collect must trigger at least one action. Email collected? Add to the correct email segment. Quiz answer? Route to the matching path. Phone number? Tag for SMS follow-up. If you're not going to use a data point, don't ask for it.

---

## Priority Summary

| Priority | Checks | Rule |
|----------|--------|------|
| **Critical** | Dead Ends, Delay Timing, Fallback Handling, Re-engagement, Compliance, Measurement | Must pass before launch. These break the flow or break the rules. |
| **Important** | Segmentation, Button Overload, Tag Coverage, Copy Quality | Should pass before launch. These reduce performance significantly. |

Fix Critical items first. A flow with perfect copy but dead ends and no compliance is worse than a simple flow that works end to end.
