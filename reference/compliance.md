# DM Automation Compliance Guide

Rules, limits, and best practices for automated messaging on Meta platforms and WhatsApp.

---

## Meta / Instagram DM Rules

### The 24-Hour Messaging Window

Once a user messages you (or interacts in a qualifying way), you have a 24-hour window to send them messages freely. After 24 hours with no new user interaction, you cannot message them unless you use an approved method.

**What opens/resets the window:**
- User sends a DM to your page or Instagram account
- User replies to your automated message
- User comments on your post (if comment automation is set up)
- User replies to your story
- User taps a button in your automated flow
- User clicks a "Send Message" CTA on your ad

**What does NOT reset the window:**
- You sending a message (only user actions reset it)
- User viewing your story without replying
- User liking your post
- User visiting your profile

### Business-Initiated Messages (Outside the Window)

To message someone after the 24-hour window closes, you need one of these:

**One-Time Notification (OTN):**
- User must explicitly opt in by tapping a "Notify Me" button you present
- Each opt-in is single-use -- once you send the notification, the token is consumed
- You must specify a topic when requesting: Upcoming Event, Product Update, Appointment Reminder, Community Alert, Account Change
- You cannot stockpile OTNs to blast users later
- Each OTN opens a new 24-hour window when sent

**Message Tags (Messenger only, not Instagram):**
- Confirmed Event Update: reminders for events the user registered for
- Post-Purchase Update: order confirmations, shipping, receipts
- Account Update: changes to account status, payment issues
- Tags are NOT for promotional content -- Meta audits this

### Comment Automation Rules

- Keywords must be specific (not single common words like "yes" or "info")
- The automated DM must relate to the post content
- User must comment the keyword voluntarily -- you cannot trick them
- Private reply must include opt-in language ("I'm sending this because you commented X on our post")
- Do not auto-reply to every comment -- only keyword matches
- Limit one DM per user per post (do not spam on repeat comments)

### What Gets Your Automation Disabled

- High spam report rate (users tapping "Report" or "Block" on your messages)
- Sending promotional content via Message Tags
- Messaging users outside the 24-hour window without OTN or tags
- Sending too many messages too quickly (velocity limits)
- Banned content: cryptocurrency promotions, adult content, weapons, counterfeit goods, multi-level marketing schemes, unauthorized health claims
- Misleading opt-in flows (user did not clearly consent)
- Scraping user data from conversations for external use

---

## WhatsApp Business Rules

### Message Types

**Template Messages (outbound, outside 24hr window):**
- Must be pre-approved by Meta before sending
- Used for: appointment reminders, shipping updates, payment confirmations
- Templates have fixed text with variable placeholders
- Approval takes 1-24 hours (sometimes longer)
- Rejected templates can be edited and resubmitted

**Session Messages (inside 24hr window):**
- Free-form messaging after user sends you a message
- 24-hour window works the same as Instagram/Messenger
- No pre-approval needed for session messages

### Template Categories
- Marketing: promotions, offers, product announcements (highest cost per message)
- Utility: order updates, account alerts, appointment changes (medium cost)
- Authentication: OTPs, login codes, verification (lowest cost)
- Service: customer-initiated conversations (free within window)

### Opt-In Requirements
- Users must explicitly opt in to receive WhatsApp messages from your business
- Opt-in must be collected separately from other consents
- You must clearly state what types of messages they will receive
- Opt-in can be collected via: website form, during checkout, QR code, click-to-WhatsApp ad
- You cannot add users to WhatsApp from purchased contact lists

### Template Approval Process
1. Write template with placeholders: "Hi {{1}}, your appointment is on {{2}} at {{3}}."
2. Select category (Marketing, Utility, Authentication)
3. Submit for review
4. Wait for approval (do not send until approved)
5. If rejected: review reason, edit, resubmit
6. Common rejection reasons: too promotional for Utility category, unclear opt-out, missing business name

---

## General Best Practices

### Identification
- Include your business name in the first message of any flow
- Do not pretend to be a person when it is a bot
- If using AI-generated replies, disclose it when asked

### Opt-Out
- Every automated sequence must include an opt-out option
- Common patterns: "Reply STOP to unsubscribe" or a button labeled "Unsubscribe"
- Honor opt-outs immediately -- do not send "are you sure?" follow-ups
- Keep an exclusion list and check it before sending

### Frequency Caps
- Lead magnet delivery: 1-3 messages in the first flow, then stop
- Follow-up sequences: maximum 1 message per day
- Re-engagement: maximum 1 attempt per 30 days
- Total messages per user per week: aim for under 5 across all flows
- If open/reply rates drop below 20%, you are messaging too often

### Inactive Subscribers
- Stop messaging users who have not opened or replied in 30 days
- Run a re-engagement flow once, then remove non-responders
- Sending to inactive subscribers tanks your deliverability and increases spam reports

### GDPR Considerations
- If you serve EU users, you need a lawful basis for processing their data
- Legitimate interest can cover DM automation if the user initiated contact
- Include a data collection notice in your first message or link to privacy policy
- Honor right to deletion -- if a user asks you to delete their data, do it within 30 days
- Keep records of consent (when they opted in, what they consented to)
- Data collected in DM flows (name, email, phone) is personal data under GDPR

### CAN-SPAM and DM Marketing
- CAN-SPAM primarily covers email, but the principles apply to DM marketing
- Do not use deceptive subject lines or misleading content
- Include your business identity and contact information
- Provide a clear way to opt out
- Process opt-out requests within 10 business days

---

## Consequences of Violations

### Level 1: Account Restriction (Temporary)
- Duration: 24-72 hours
- Cause: minor spike in spam reports, sending slightly outside guidelines
- Effect: cannot send automated messages, manual messaging still works
- Recovery: wait it out, fix the offending flow, reduce message volume

### Level 2: Automation Disabled (Specific Flow)
- Duration: until you fix and resubmit
- Cause: a specific flow flagged for policy violation
- Effect: that flow stops running, other flows may still work
- Recovery: edit the flow to comply, resubmit for review

### Level 3: Page Restricted (Messaging Blocked)
- Duration: 7-30 days or until appeal
- Cause: repeated violations, high spam report rate, banned content
- Effect: cannot send any messages (manual or automated) from the page
- Recovery: appeal through Meta Business Support, fix all flagged issues

### Level 4: Account Banned (Permanent)
- Duration: permanent
- Cause: severe or repeated violations, fraud, illegal content
- Effect: page and/or ad account permanently disabled
- Recovery: extremely difficult -- appeal possible but rarely successful
- Prevention: follow every rule above, monitor spam rates weekly

---

## Compliance Checklist

Before launching any DM automation flow:

- [ ] First message identifies your business by name
- [ ] Opt-out option included in every sequence
- [ ] Messages only sent within the 24-hour window (or via OTN/tags)
- [ ] Comment trigger keywords are specific, not generic
- [ ] No banned content (crypto, adult, health claims, MLM)
- [ ] Frequency caps set (no more than 1 message/day in follow-ups)
- [ ] Inactive subscribers excluded after 30 days
- [ ] GDPR notice included or linked for EU users
- [ ] WhatsApp templates submitted and approved before sending
- [ ] Spam report rate monitored weekly (target: under 1%)
