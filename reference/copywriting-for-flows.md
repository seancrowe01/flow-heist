# Copywriting for DM Automation Flows

Message patterns, templates, and tone guidance for every stage of a DM flow.

---

## Character Limits

| Platform | Limit |
|---|---|
| Instagram DM | 1,000 characters |
| Facebook Messenger | 2,000 characters |
| WhatsApp | 4,096 characters |
| ManyChat button label | 20 characters |
| ManyChat quick reply | 20 characters |

Keep messages well under the limit. Shorter is almost always better in DMs.

---

## Opening Messages

### The Warm Welcome
Personalized, friendly, gets to the point fast.

> Hey {{first_name}}! Thanks for reaching out. I've got that guide ready for you -- let me grab it.

> {{first_name}}, welcome! Glad you're here. Let me get you set up with exactly what you need.

> Hey {{first_name}}! I saw your comment -- sending over the free resource now.

### The Context Setter
Reminds them why they are receiving this message.

> Hey {{first_name}}, you commented "GUIDE" on our post about lead generation. Here's what I promised.

> {{first_name}}, you signed up for the free training on our website. Here's your access link.

> Hey! You replied to our story asking about pricing. Let me walk you through it.

### The Curiosity Hook
Teases value before delivering it.

> {{first_name}}, before I send the guide -- quick question. What's the biggest challenge you're dealing with right now?

> Hey {{first_name}}! I've got your resource ready. But first, I want to make sure I send you the right version. Are you just getting started or already running ads?

> {{first_name}}, I have something for you. But I want to make sure it actually helps. What best describes you?

---

## Qualification Questions

### Open vs Closed Questions
- **Open questions** get richer answers but are harder to route automatically. Use when a human will read the response or when you want to tag based on keywords.
- **Closed questions** (buttons/quick replies) are better for automation. The user taps, the flow continues.

Use closed questions for routing. Use one open question max per flow for personalization.

### The 2-Option Rule
Give exactly 2 choices. Three or more creates decision fatigue and drops completion rates.

> What best describes you?
>
> [Just getting started] [Already running ads]

> Which would help you more right now?
>
> [Get more leads] [Close more sales]

> Are you a...
>
> [Coach / Consultant] [Agency Owner]

### Question Sequencing
1. Easy, low-commitment question first (role, industry)
2. Slightly more specific (current situation, challenge)
3. Personal info last (email, phone -- only if needed)

Never ask for email or phone in the first message. Earn it.

### Handling Unexpected Answers
When someone types something your flow does not recognize:

> Thanks for sharing that! I want to make sure I point you in the right direction. Could you tap one of the options below?

> Appreciate the detail! To get you the right resource, just tap one of these.

> Got it. Let me narrow it down for you -- which of these fits best?

Always re-present the buttons after the fallback message.

---

## Button Labels

### Rules
- Start with an action verb: Get, Download, Book, Start, Show, Send
- Max 20 characters (ManyChat hard limit)
- One emoji maximum, at the start or end, never in the middle
- Make one button the obvious choice (the one you want them to tap)

### Good Button Labels
| Instead of | Use |
|---|---|
| Click here | Get the Guide |
| Yes | Yes, send it! |
| Learn more | Show Me How |
| Submit | Book My Call |
| Option 1 | I'm a Coach |
| Next | Let's Go |

### The Obvious Choice Pattern
Make one option clearly more appealing. The "wrong" choice should feel like missing out.

> [Get the Free Guide] [No thanks, I'm good]

> [Book a Free Call] [Maybe later]

> [Send Me the Training] [Skip for now]

---

## Delivery Messages

### Lead Magnet Delivery
Link first, context second, next step third.

> Here's your guide: [link]
>
> It covers the exact 3-step system we use to generate leads on autopilot. Takes about 5 minutes to read.
>
> Once you've gone through it, reply "DONE" and I'll send you the bonus checklist.

> Your free training is ready: [link]
>
> This is the same framework our clients use to book 15+ calls per month. Worth watching all the way through.
>
> Let me know what you think!

### Booking Confirmation
Include what, when, and what to expect.

> You're all booked! Here are the details:
>
> Date: {{appointment_date}}
> Time: {{appointment_time}}
> Link: {{meeting_link}}
>
> It's a casual 15-minute chat. No pitch, no pressure. Come with your questions and I'll give you honest feedback on your setup.

### Content Delivery
Lead with value, ask second.

> Here's the video breakdown you asked for: [link]
>
> The section on hook formulas starts at 3:20 -- that's the part most people screenshot.
>
> Found it useful? I've got a more detailed version I can send over.

---

## Follow-Up Messages

### The Check-In (24 hours after delivery)
> Hey {{first_name}}, just checking in -- did you get a chance to look at the guide I sent yesterday?

> {{first_name}}, quick check-in. Any questions about the resource I sent over?

> Hey! Did the guide make sense? Happy to clarify anything.

### The Social Proof Nudge
> {{first_name}}, just wanted to share -- we had 200+ people download that guide this week and the feedback has been incredible. Did you get a chance to go through it?

> Quick note -- a few people who downloaded the same guide ended up booking a call and landing their first 3 clients within 60 days. If you want to chat about how that could work for you, I'm here.

### The Next Step
> {{first_name}}, now that you've got the guide, the natural next step is a quick call where we map out how to apply it to your business specifically. Want me to send you a link to book?
>
> [Book a Free Call] [Not right now]

> Glad you found it helpful! Most people who grab this guide want to know how to implement it fast. I do free 15-minute strategy calls if you want one.

### The Re-Engagement (30+ days inactive)
> Hey {{first_name}}, it's been a while! We just released a new resource that I think you'd find useful. Want me to send it over?
>
> [Yes please!] [Unsubscribe]

> {{first_name}}, we've updated our system since you last checked in. The results have been pretty wild. Want a quick look?
>
> [Show me] [No thanks]

Always include an unsubscribe option in re-engagement messages.

---

## Error and Fallback Messages

### Unrecognized Input
> Hmm, I didn't quite catch that. Could you tap one of the buttons below so I can point you in the right direction?

> Thanks for the message! I'm set up to respond to a few specific options. Tap one of these and I'll take it from there.

### Timeout (User Went Silent)
Send once, 24 hours after last interaction. Do not send more than one timeout message.

> Hey {{first_name}}, no rush at all. Your resource is still here whenever you're ready. Just reply "READY" and I'll send it right over.

> Still interested in the guide? Tap below and I'll send it now.
>
> [Send it] [Not interested]

### Graceful Degradation (Something Broke)
> Hey {{first_name}}, looks like something didn't work on my end. Let me sort it out. In the meantime, you can grab the resource directly here: [backup link]

> Apologies, I hit a small hiccup. Here's a direct link to what you were looking for: [backup link]. If you need anything else, just reply here.

Always have a backup static link for every lead magnet delivery flow.

---

## Personalization Tokens

### Standard Tokens
- `{{first_name}}` -- use in the first message of every flow, and sparingly after
- `{{last_name}}` -- only in formal or professional flows (booking confirmations, invoices)
- `{{email}}` -- only reference back to confirm ("I'll send it to {{email}}, sound good?")

### Custom Field References
When you collect data earlier in the flow, reference it later.

> You mentioned you're a {{business_type}} -- here's the version of the guide built for your industry.

> Since you said your biggest challenge is {{main_challenge}}, I'd focus on page 3 of the guide first.

### Conditional Content
Show different messages based on tags or field values.

- Tagged "coach" -> send coaching-specific examples
- Tagged "agency" -> send agency-specific case studies
- Field "budget" = "under 1k" -> send DIY resource
- Field "budget" = "5k+" -> send done-for-you offer

Set these up as condition blocks in your flow builder, not as text logic in the message.

---

## Tone Calibration

### Lead Magnet Flows
Friendly, generous, zero pressure. You are giving something away for free. Act like it.

> Here you go! No strings attached. If you find it useful, I'd love to hear what stood out.

Do not pitch in the delivery message. Wait at least 24 hours.

### Sales Flows
Direct, confident, clear on what happens next. No hedging, no "just wondering if maybe."

> Here's what I'd recommend: book a 15-minute call and I'll show you exactly how this works for your business. No prep needed.

One CTA per message. Do not give three options when you want them to book a call.

### Support Flows
Empathetic, efficient, focused on solving the problem.

> Sorry to hear that -- let me fix it. Can you tell me what happened so I can sort it out quickly?

Acknowledge the issue, then move to resolution. Do not over-apologize.

### Re-Engagement Flows
Casual, no guilt, easy way out. The user owes you nothing.

> Hey! No worries if you've been busy. We've got something new that might be worth a look. Interested?

Never say "I noticed you haven't opened my messages" or "you've been ignoring me." Treat every re-engagement like a fresh start.
