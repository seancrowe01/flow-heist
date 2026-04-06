# Flow Machine -- 8 Proven DM Flow Architectures

Reference document for building automated DM flows across ManyChat, GoHighLevel, and other automation platforms. Each pattern is battle-tested and includes enough detail to rebuild from scratch.

---

## Table of Contents

1. [Lead Magnet Delivery](#1-lead-magnet-delivery)
2. [Quiz/Survey Funnel](#2-quizsurvey-funnel)
3. [Sales Qualifier](#3-sales-qualifier)
4. [Webinar/Event Registration](#4-webinarevent-registration)
5. [Customer Support Router](#5-customer-support-router)
6. [Re-engagement/Win-back](#6-re-engagementwin-back)
7. [Launch/Countdown Sequence](#7-launchcountdown-sequence)
8. [Content Upgrade / Story Reply](#8-content-upgrade--story-reply)

---

## 1. Lead Magnet Delivery

### What It Does

Turns a social media comment or keyword into a lead. Someone comments a keyword on a post or sends a DM, gets a welcome message, hands over their email, receives a PDF or guide, and enters a short nurture sequence.

### When to Use It

- You have a free resource (PDF, checklist, template, swipe file) to give away
- You want to grow your email list from social content
- You are running a "comment X to get Y" style post or reel

### Typical Trigger

Instagram comment keyword, Facebook comment keyword, or DM keyword.

### Flow Diagram

```
TRIGGER: Comment keyword "GUIDE" on post/reel
  |
  v
ACTION: Check if subscriber exists
  - New subscriber  --> MSG 1
  - Existing subscriber --> MSG 1 (skip email if already collected)
  |
  v
MSG 1: "Hey {{first_name}}! Glad you want this -- I put a lot into it.
        Want me to send it over?"
  - Quick Reply: "Yes please!" --> MSG 2
  - Quick Reply: "What's in it?" --> MSG 1b
  |
  v
MSG 1b: "It covers [brief 2-3 bullet summary of what the guide includes].
         Ready for it?"
  - Quick Reply: "Send it!" --> MSG 2
  |
  v
MSG 2: "Sweet. What's your best email? I'll send a copy there too
        so you don't lose it."
  - User Input: email --> stored in {{email}}
  - Validation: email format check
  - Action: If invalid --> "Hmm, that doesn't look right. Try again?"
  |
  v
MSG 3: "You're all set! Here's your guide:
        [Button: Download Guide --> PDF link]

        I'll send a copy to {{email}} as well."
  - Action: Tag subscriber "lead-magnet-[guide-name]"
  - Action: Set custom field "lead_source" = "instagram_dm"
  - Action: Set custom field "lead_magnet" = "[guide-name]"
  - Action: Send email with PDF attachment via integration
  |
  v
MSG 4 (24hr delay): "Hey {{first_name}} -- did you get a chance to
                      check out the guide?"
  - Quick Reply: "Yes, loved it!" --> MSG 5a
  - Quick Reply: "Not yet" --> MSG 5b
  |
  v
MSG 5a: "That's great to hear! The section on [key topic] is where
         most people get the biggest win.

         If you want help putting it into action, I do a free
         [call/audit/review] -- want the link?"
  - Quick Reply: "Yes, book me in" --> MSG 6 (booking link)
  - Quick Reply: "I'm good for now" --> END (tag "nurture-warm")
  |
  v
MSG 5b: "No stress -- it's not going anywhere. Here's the link
         again whenever you're ready:
         [Button: Download Guide --> PDF link]"
  - Action: Set reminder to follow up in 48hrs --> MSG 5c
  |
  v
MSG 5c (48hr delay): "Just checking in -- any questions about the
                       guide? Happy to help."
  - User replies --> route to live chat or auto-reply
  - No reply within 24hr --> END (tag "nurture-cold")
  |
  v
MSG 6: "Here you go:
        [Button: Book Your Free Call --> calendar link]

        Pick whatever time works. Talk soon!"
  - Action: Tag "booked-call" or "sent-booking-link"
  - END
```

### Message Count

5-7 messages (core flow is 4, plus 2-3 nurture follow-ups).

### Expected Completion Rate

40-60% from trigger to email collected. 15-25% click through to the nurture CTA.

### Key Psychology

**Reciprocity and micro-commitments.** The subscriber asked for the thing (comment trigger), so they already want it. Each step is a tiny yes -- "want me to send it?" then "what's your email?" -- that builds momentum. By the time you ask for a call booking, they have already said yes three times.

### Common Variations

- **No email collection:** Skip MSG 2 and deliver the asset directly. Faster, but you lose the email. Best for pure follower growth plays.
- **Double opt-in:** After collecting email, send a confirmation email before delivering the asset. Higher quality list, lower completion.
- **Multi-asset:** After delivery, offer a second related resource ("Want the advanced version too?"). Increases engagement and tags interests.
- **Paid upsell:** After delivery, offer a low-ticket product ($7-$47) instead of a free call. Works well for digital products.

### Platform Notes (ManyChat)

- Use the Comments Growth Tool to auto-trigger on specific keywords. Set it to "message contains" not "exact match" to catch variations.
- Enable the "Reply to comment" option so the bot also leaves a public reply ("Just sent it to your DMs!") -- this signals to other viewers that the flow is active and drives more comments.
- Store emails using a Custom Field (type: email) so ManyChat validates the format automatically.
- Use the ManyChat-Mailchimp/ConvertKit/Flodesk integration to sync the email immediately. Do not rely on a delayed batch sync.
- Set a Smart Delay of 1-2 seconds between messages so they feel conversational, not robotic.

---

## 2. Quiz/Survey Funnel

### What It Does

Engages the subscriber with 3-5 interactive questions, segments them by their answers using tags and custom fields, then delivers a personalized recommendation or CTA based on their segment.

### When to Use It

- You serve multiple audience types and want to tailor the next step
- You want higher engagement than a simple lead magnet
- You are running a "find out which X you are" or "get your custom plan" style post
- You want to pre-qualify without feeling like a sales call

### Typical Trigger

DM keyword ("QUIZ", "TEST", "PLAN") or comment keyword on a post/reel.

### Flow Diagram

```
TRIGGER: DM keyword "QUIZ"
  |
  v
MSG 1: "Hey {{first_name}}! Let's find out [what the quiz promises].
        It's 4 quick questions -- takes about 30 seconds.
        Ready?"
  - Quick Reply: "Let's go!" --> MSG 2
  - Quick Reply: "What will I learn?" --> MSG 1b
  |
  v
MSG 1b: "You'll get [specific outcome, e.g., a personalized plan /
         your score / which type you are]. Based on thousands of
         [clients/users/results]."
  - Quick Reply: "I'm in" --> MSG 2
  |
  v
MSG 2 (Question 1 -- Situation):
  "First up -- which best describes you right now?"
  - Quick Reply: "Just starting out" --> Tag "stage-beginner",
                                         set {{quiz_stage}} = "beginner"
  - Quick Reply: "Growing but stuck" --> Tag "stage-intermediate",
                                         set {{quiz_stage}} = "intermediate"
  - Quick Reply: "Scaling past 10k/mo" --> Tag "stage-advanced",
                                           set {{quiz_stage}} = "advanced"
  |
  v
MSG 3 (Question 2 -- Problem):
  "What's the biggest thing holding you back?"
  - Quick Reply: "Not enough leads" --> Tag "problem-leads",
                                        set {{quiz_problem}} = "leads"
  - Quick Reply: "Can't convert" --> Tag "problem-conversion",
                                     set {{quiz_problem}} = "conversion"
  - Quick Reply: "No time" --> Tag "problem-time",
                               set {{quiz_problem}} = "time"
  |
  v
MSG 4 (Question 3 -- Goal):
  "What would make the biggest difference in the next 90 days?"
  - Quick Reply: "More clients" --> Tag "goal-clients",
                                    set {{quiz_goal}} = "clients"
  - Quick Reply: "More revenue" --> Tag "goal-revenue",
                                    set {{quiz_goal}} = "revenue"
  - Quick Reply: "More freedom" --> Tag "goal-freedom",
                                    set {{quiz_goal}} = "freedom"
  |
  v
MSG 5 (Question 4 -- Budget/Commitment):
  "Last one -- if you found something that worked, how fast
   would you want to move?"
  - Quick Reply: "Right now" --> Tag "urgency-high",
                                 set {{quiz_urgency}} = "high"
  - Quick Reply: "Next 30 days" --> Tag "urgency-medium",
                                    set {{quiz_urgency}} = "medium"
  - Quick Reply: "Just exploring" --> Tag "urgency-low",
                                      set {{quiz_urgency}} = "low"
  |
  v
ACTION: Evaluate segment using Conditions
  - IF {{quiz_urgency}} = "high" AND {{quiz_stage}} != "beginner"
    --> SEGMENT A (hot lead)
  - IF {{quiz_urgency}} = "medium" OR {{quiz_stage}} = "intermediate"
    --> SEGMENT B (warm lead)
  - ELSE
    --> SEGMENT C (nurture)
  |
  +-- SEGMENT A ----------------------------------+
  |                                               |
  v                                               |
  MSG 6a: "Here's what I'd recommend based on     |
           your answers:                           |
                                                   |
           You're at the {{quiz_stage}} stage,     |
           your main blocker is {{quiz_problem}},  |
           and you want to move fast.              |
                                                   |
           Honestly -- a quick call would be the   |
           fastest way to map this out.            |
           [Button: Book a Free Call --> link]"     |
  - Action: Tag "segment-hot"                      |
  - END                                            |
  |                                                |
  +-- SEGMENT B ----------------------------------+
  |                                               |
  v                                               |
  MSG 6b: "Based on your answers, here's the best |
           next step:                              |
                                                   |
           I've got a free [resource] that covers  |
           exactly how to fix {{quiz_problem}}     |
           at the {{quiz_stage}} stage.            |
                                                   |
           Want me to send it?"                    |
  - Quick Reply: "Yes!" --> deliver resource,      |
                            tag "segment-warm"     |
  - Quick Reply: "I'd rather chat" --> booking     |
                                       link        |
  - END                                            |
  |                                                |
  +-- SEGMENT C ----------------------------------+
  |                                               |
  v                                               |
  MSG 6c: "No rush at all. Here's a quick         |
           [video/post/guide] that'll help you     |
           get started:                            |
           [Button: Watch/Read --> content link]   |
                                                   |
           I'll check in with you in a few days."  |
  - Action: Tag "segment-nurture"                  |
  - Action: Start nurture sequence (48hr delay)    |
  - END                                            |
```

### Message Count

6-8 messages (1 intro + 4 questions + 1-2 result messages).

### Expected Completion Rate

30-50% complete all questions. Of those, 20-35% click the final CTA.

### Key Psychology

**Self-discovery and the IKEA effect.** People value what they participate in creating. Each answer feels like the subscriber is building their own custom result. By the time the recommendation arrives, it feels earned and personal -- not like a generic pitch. The segmentation also means the CTA actually matches their situation, which dramatically increases conversion.

### Common Variations

- **Scored quiz:** Assign point values to each answer (beginner = 1, advanced = 3). Sum the score and deliver a result like "Your Score: 8/12 -- here's what that means." Makes it feel more official.
- **Personality type:** Instead of a recommendation, assign a "type" ("You're The Builder" / "You're The Hustler"). People love identity labels and will share them.
- **Email gate:** Collect email before revealing results. "Almost done -- where should I send your results?" Higher email capture, slightly lower completion.
- **Progressive profiling:** If the subscriber has taken a quiz before, skip questions you already know and ask new ones. Uses existing custom fields.

### Platform Notes (ManyChat)

- Use Quick Replies (not buttons) for quiz answers -- they disappear after selection, keeping the chat clean.
- Store each answer in a separate Custom Field. This lets you build advanced Conditions later without relying on tags alone.
- Use the Condition block after the last question to branch to segments. Keep it simple -- no more than 3-4 segments or the flow becomes unmanageable.
- Add a "typing" delay of 1-2 seconds before each question to simulate real conversation pacing.
- If someone abandons mid-quiz, use the "Hasn't reached this step in X hours" condition to send a nudge: "Hey, you were halfway through -- want to finish?"

---

## 3. Sales Qualifier

### What It Does

Asks 2-3 targeted qualifying questions to separate serious prospects from tire-kickers. Qualified leads get a booking link. Unqualified leads get pointed to free content or a lower-ticket offer.

### When to Use It

- You sell high-ticket services or coaching and your time is limited
- You are getting too many unqualified calls
- You want to pre-screen before someone lands on your calendar
- You are running "DM me X" posts that attract mixed intent

### Typical Trigger

DM keyword ("CALL", "APPLY", "READY") or reply to a story.

### Flow Diagram

```
TRIGGER: DM keyword "APPLY"
  |
  v
MSG 1: "Hey {{first_name}}! Thanks for reaching out.

        Before I send you the booking link, I want to make
        sure I can actually help -- mind if I ask a couple
        quick questions?"
  - Quick Reply: "Go for it" --> MSG 2
  - Quick Reply: "Just send the link" --> MSG 2 (skip intro)
  |
  v
MSG 2 (Question 1 -- Fit Check):
  "What do you do? Like, what's your business or what
   are you looking to grow?"
  - User Input: free text --> stored in {{business_type}}
  - Action: No validation needed, any answer moves forward
  |
  v
MSG 3 (Question 2 -- Revenue/Budget Signal):
  "Nice. And roughly where are you at revenue-wise right now?"
  - Quick Reply: "Under $3k/mo" --> set {{revenue}} = "low"
  - Quick Reply: "$3k-$10k/mo" --> set {{revenue}} = "mid"
  - Quick Reply: "$10k+/mo" --> set {{revenue}} = "high"
  |
  v
MSG 4 (Question 3 -- Urgency):
  "Last one -- how soon are you looking to get this
   sorted?"
  - Quick Reply: "ASAP" --> set {{urgency}} = "now"
  - Quick Reply: "Next month or so" --> set {{urgency}} = "soon"
  - Quick Reply: "Just researching" --> set {{urgency}} = "later"
  |
  v
ACTION: Qualification check
  - IF {{revenue}} = "high" OR ({{revenue}} = "mid" AND {{urgency}} = "now")
    --> QUALIFIED
  - IF {{revenue}} = "mid" AND {{urgency}} != "later"
    --> SEMI-QUALIFIED
  - ELSE
    --> NOT YET READY
  |
  +-- QUALIFIED ----------------------------------+
  |                                               |
  v                                               |
  MSG 5a: "Love it. Sounds like we'd be a great   |
           fit.                                    |
                                                   |
           Here's my calendar -- grab whatever     |
           time works:                             |
           [Button: Book Your Call --> link]        |
                                                   |
           It's a quick 15-min chat. No pitch,     |
           just figuring out if I can help."        |
  - Action: Tag "qualified-lead"                   |
  - Action: Set custom field "lead_score" = "hot"  |
  - Action: Notify via email/Slack (new qualified  |
            lead: {{first_name}}, {{business_type}}|
            {{revenue}})                           |
  - END                                            |
  |                                                |
  +-- SEMI-QUALIFIED -----------------------------+
  |                                               |
  v                                               |
  MSG 5b: "Here's what I'd suggest -- I put        |
           together a free [training/guide] that   |
           covers the exact process I use.         |
                                                   |
           Check it out first, and if it clicks,   |
           we can hop on a call after.             |
           [Button: Watch Free Training --> link]   |
                                                   |
           Sound good?"                            |
  - Action: Tag "warm-lead"                        |
  - Action: Set custom field "lead_score" = "warm" |
  - Action: Start nurture sequence (48hr delay)    |
  - END                                            |
  |                                                |
  +-- NOT YET READY ------------------------------+
  |                                               |
  v                                               |
  MSG 5c: "Totally get it -- no rush.              |
                                                   |
           Here's some free stuff that'll help     |
           you get started:                        |
           [Button: Free Guide --> link]            |
           [Button: Follow for tips --> profile]    |
                                                   |
           When you're ready to go, just DM me     |
           'READY' and we'll pick up from here."   |
  - Action: Tag "nurture-lead"                     |
  - Action: Set custom field "lead_score" = "cold" |
  - END                                            |
```

### Message Count

5-6 messages total.

### Expected Completion Rate

25-40% complete all questions. Of qualified leads, 50-70% book a call.

### Key Psychology

**Exclusivity and screening.** By asking questions before giving the booking link, you flip the dynamic -- instead of chasing prospects, they are proving they are a fit for you. This positions you as the authority. Even the "not yet ready" path feels respectful, not dismissive, so they stay warm for later.

### Common Variations

- **Application form:** Instead of quick replies, send a link to a Typeform or GHL form. More data, but more friction and lower completion.
- **Video qualifier:** Send a short video message (voice note or Loom) instead of text for MSG 1. Builds trust faster.
- **Two-tier booking:** Qualified leads get the premium calendar (30-min strategy call). Semi-qualified get a shorter discovery call (15-min). Protects your time.
- **Auto-CRM sync:** Push qualified lead data directly to GHL or your CRM via webhook so your sales pipeline updates instantly.

### Platform Notes (ManyChat)

- Use "User Input" for the business type question (free text). Store it in a Text custom field.
- For revenue and urgency questions, Quick Replies keep it clean and prevent ambiguous answers.
- Set up an External Request (webhook) to push qualified leads to GHL, Slack, or email immediately. Speed to lead matters.
- Use the "Notify Admin" action to send yourself a DM or email the moment someone qualifies. Respond within 5 minutes if possible.
- If someone answers "Just send the link" at the start, still ask at least one qualifying question. Frame it as "just want to make sure I point you to the right thing."

---

## 4. Webinar/Event Registration

### What It Does

Converts a social comment or DM into an event registration, collects the email, confirms the signup, then runs an automated reminder sequence to maximize attendance and reduce no-shows.

### When to Use It

- You are hosting a live webinar, workshop, challenge, or event
- You want to drive registrations directly from social content
- You need a reminder sequence to fight the "I forgot" no-show problem
- You are running ads or posts with a "comment X to register" CTA

### Typical Trigger

Comment keyword ("REGISTER", "WEBINAR", "LIVE") or DM keyword.

### Flow Diagram

```
TRIGGER: Comment keyword "REGISTER" on promo post
  |
  v
MSG 1: "Hey {{first_name}}! You're in the right place.

        Here's what we're covering:
        [Event name]
        [Date + Time + Timezone]
        [1-2 sentence description of what they'll learn]

        Want me to save your spot?"
  - Quick Reply: "Yes, sign me up!" --> MSG 2
  - Quick Reply: "Tell me more" --> MSG 1b
  |
  v
MSG 1b: "Here's the full rundown:
         - [Benefit 1]
         - [Benefit 2]
         - [Benefit 3]
         Plus everyone who shows up live gets [bonus].

         Want in?"
  - Quick Reply: "I'm in!" --> MSG 2
  |
  v
MSG 2: "What's your best email? I'll send the calendar
        invite and all the details there."
  - User Input: email --> stored in {{email}}
  - Validation: email format check
  |
  v
MSG 3: "You're registered! Here's what to expect:

        [Event name]
        [Date + Time + Timezone]
        [Button: Add to Calendar --> .ics link or Google Cal link]
        [Button: Join Link --> zoom/meet link]

        I'll send you a reminder before we go live so you
        don't miss it."
  - Action: Tag "registered-[event-name]"
  - Action: Set custom field "event_registered" = "[event-name]"
  - Action: Send confirmation email with calendar invite
  - Action: Subscribe to reminder sequence
  |
  v
REMINDER 1 (72hr before event):
  "Hey {{first_name}} -- just a heads up, [event name]
   is in 3 days!

   Here's what to have ready: [prep item, e.g., a notebook,
   your ad account open, etc.]

   [Button: Add to Calendar --> link]"
  |
  v
REMINDER 2 (24hr before event):
  "Tomorrow's the day! [Event name] kicks off at [time].

   Quick reminder -- people who show up live get [bonus].

   [Button: Set a Phone Reminder --> link or instruction]"
  |
  v
REMINDER 3 (1hr before event):
  "We're going live in 1 hour!

   [Button: Join Now --> zoom/meet link]

   See you in there."
  |
  v
REMINDER 4 (at event start):
  "We're LIVE right now! Jump in:

   [Button: Join Now --> zoom/meet link]"
  - Action: Tag "reminded-[event-name]"
  |
  v
POST-EVENT (1hr after event ends):
  - IF subscriber clicked join link --> MSG POST-A
  - IF subscriber did NOT click join link --> MSG POST-B
  |
  v
MSG POST-A: "Thanks for showing up live!

             Here's the [replay/slides/bonus] I promised:
             [Button: Get the Replay --> link]

             What was your biggest takeaway?"
  - User Input: free text (engagement + testimonial capture)
  - Action: Tag "attended-[event-name]"
  |
  v
MSG POST-B: "Hey {{first_name}} -- looks like you missed
             the live session. No worries, here's the replay:
             [Button: Watch Replay --> link]

             It's only up for 48 hours though."
  - Action: Tag "no-show-[event-name]"
  - Action: Set 48hr expiry reminder
  |
  v
REPLAY EXPIRY (48hr after event):
  "Last chance -- the replay for [event name] comes down
   tonight.

   [Button: Watch Now --> link]

   After this I won't be able to share it."
  - Action: Remove replay access after 24hr
  - END
```

### Message Count

8-11 messages (3 registration + 4 reminders + 1-3 post-event).

### Expected Completion Rate

35-55% from trigger to registered. 40-60% of registered actually attend (with full reminder sequence). Without reminders, attendance drops to 15-25%.

### Key Psychology

**Commitment escalation and loss aversion.** Each reminder reinforces the decision they already made ("you registered, don't waste it"). The live-only bonus creates FOMO. The 48-hour replay window creates urgency for no-shows. People who add it to their calendar are 3x more likely to attend.

### Common Variations

- **Challenge format:** Instead of a single event, run a 3-5 day challenge. Each day has its own registration confirmation and reminder. Higher commitment, higher conversion.
- **Bring-a-friend:** After registration, ask "Know anyone who'd benefit? Share this with them and you both get [bonus]." Adds viral loop.
- **VIP upgrade:** Offer a paid VIP experience ($27-$97) with bonus Q&A, recording, or workbook. Captures some revenue pre-event.
- **SMS backup:** Collect phone number as well as email. Send the 1hr and "live now" reminders via SMS for higher open rates.

### Platform Notes (ManyChat)

- Use the Comments Growth Tool with "Reply to Comment" enabled. The public reply ("Just sent you the details!") creates social proof and drives more comments.
- Set up reminders using the Smart Delay block. Build each reminder as a separate step in the same flow, not as separate flows.
- Use the "Date/Time" condition to make sure reminders only fire if the event hasn't passed yet (in case someone registers late).
- For the post-event split (attended vs. no-show), use a tag applied by a webhook from Zoom/Meet when someone joins, or track the "Join Now" button click in ManyChat.
- Connect to Google Calendar via Zapier/Make to auto-send calendar invites. ManyChat does not do this natively.

---

## 5. Customer Support Router

### What It Does

Intercepts inbound DMs with a category menu, answers common questions automatically, and only escalates to a human when the bot cannot resolve the issue. Reduces support volume and response time.

### When to Use It

- You are getting repetitive DMs about the same 5-10 questions
- You want to offer instant responses outside business hours
- You need to triage support tickets before they hit your inbox
- You have a team and want to route issues to the right person

### Typical Trigger

Default Reply (any DM that does not match another flow), or keyword "HELP" / "SUPPORT".

### Flow Diagram

```
TRIGGER: Default Reply (any unmatched inbound DM)
         OR keyword "HELP"
  |
  v
MSG 1: "Hey {{first_name}}! Thanks for reaching out.

        What can I help you with today?"
  - Quick Reply: "Pricing / Plans" --> BRANCH A
  - Quick Reply: "Technical Issue" --> BRANCH B
  - Quick Reply: "Billing / Refund" --> BRANCH C
  - Quick Reply: "Something Else" --> BRANCH D
  |
  +-- BRANCH A: Pricing / Plans ------------------+
  |                                               |
  v                                               |
  MSG A1: "Here's a quick overview:               |
                                                   |
           [Plan 1] -- [price] -- [1-line desc]    |
           [Plan 2] -- [price] -- [1-line desc]    |
           [Plan 3] -- [price] -- [1-line desc]    |
                                                   |
           Want more details on any of these?"     |
  - Quick Reply: "[Plan 1]" --> MSG A2-1 (details) |
  - Quick Reply: "[Plan 2]" --> MSG A2-2 (details) |
  - Quick Reply: "Talk to someone" --> ESCALATE    |
  |                                               |
  MSG A2-1: "[Detailed breakdown of Plan 1]       |
             [Button: Sign Up --> link]            |
             [Button: Compare Plans --> link]"     |
  - Quick Reply: "I have more questions"           |
       --> ESCALATE                                |
  - Quick Reply: "That's all, thanks" --> END-GOOD |
  |                                                |
  +-- BRANCH B: Technical Issue ------------------+
  |                                               |
  v                                               |
  MSG B1: "Sorry to hear that. Let me help.       |
                                                   |
           What's the issue?"                      |
  - Quick Reply: "Login problems" --> MSG B2-1     |
  - Quick Reply: "Feature not working" --> MSG B2-2|
  - Quick Reply: "App crash / error" --> MSG B2-3  |
  |                                               |
  MSG B2-1: "Try these steps:                     |
             1. Clear your browser cache           |
             2. Use the 'Forgot Password' link     |
             3. Try a different browser             |
                                                   |
             Did that fix it?"                     |
  - Quick Reply: "Yes, fixed!" --> END-GOOD        |
  - Quick Reply: "Still broken" --> ESCALATE       |
  |                                               |
  MSG B2-2: "Which feature is giving you trouble?" |
  - User Input: free text --> stored in            |
    {{support_issue}}                              |
  - Action: Auto-reply with relevant FAQ link      |
    if keyword match found                         |
  - Action: If no match --> ESCALATE               |
  |                                               |
  MSG B2-3: "Can you share a screenshot of the     |
             error? Just send it here as an image." |
  - User Input: image --> stored                   |
  - Action: Forward to support channel --> ESCALATE|
  |                                                |
  +-- BRANCH C: Billing / Refund -----------------+
  |                                               |
  v                                               |
  MSG C1: "I'll get this sorted. What's going on?" |
  - Quick Reply: "Charged incorrectly" --> MSG C2  |
  - Quick Reply: "Want to cancel" --> MSG C3       |
  - Quick Reply: "Need a refund" --> MSG C4        |
  |                                               |
  MSG C2: "Can you share your order number or the  |
           email you signed up with? I'll look     |
           into it."                               |
  - User Input: text --> stored in                 |
    {{billing_query}}                              |
  - Action: --> ESCALATE with context              |
  |                                               |
  MSG C3: "Sorry to hear that. Before you go --    |
           can I ask what's not working for you?   |
           Sometimes there's a quick fix."         |
  - User Input: text --> stored in {{cancel_reason}}|
  - Action: Tag "churn-risk"                       |
  - Action: --> ESCALATE (priority)                |
  |                                               |
  MSG C4: "Got it. I'll pass this to the team      |
           right away. What's the order number or  |
           email on the account?"                  |
  - User Input: text --> stored in {{refund_query}}|
  - Action: --> ESCALATE with context              |
  |                                                |
  +-- BRANCH D: Something Else -------------------+
  |                                               |
  v                                               |
  MSG D1: "No problem. Just type your question     |
           and I'll do my best to help, or I'll    |
           connect you with someone who can."      |
  - User Input: free text --> stored in            |
    {{open_query}}                                 |
  - Action: Keyword scan for FAQ matches           |
  - IF match --> auto-reply with FAQ answer        |
  - IF no match --> ESCALATE                       |
  |                                                |
  +-- ESCALATE -----------------------------------+
  |                                               |
  v                                               |
  MSG ESC: "Let me connect you with a real person. |
            Someone will get back to you within    |
            [timeframe, e.g., 2 hours / next       |
            business day].                         |
                                                   |
            In the meantime, is there anything     |
            else I can help with?"                 |
  - Action: Tag "needs-human-support"              |
  - Action: Set custom field "support_category"    |
            = [branch letter]                      |
  - Action: Send notification to support team      |
            (Slack/email) with full conversation   |
            context                                |
  - Action: Assign to live chat agent (if using    |
            ManyChat Live Chat or GHL              |
            Conversations)                         |
  - END                                            |
  |                                                |
  +-- END-GOOD ----------------------------------+
  |                                               |
  v                                               |
  MSG END: "Glad I could help! If anything else    |
            comes up, just DM 'HELP' anytime."     |
  - Action: Tag "support-resolved-auto"            |
  - END                                            |
```

### Message Count

3-6 messages (depending on branch depth before resolution or escalation).

### Expected Resolution Rate

40-60% resolved without a human. Remaining 40-60% escalated with full context, reducing agent handle time by 30-50%.

### Key Psychology

**Perceived responsiveness and control.** Instant replies -- even from a bot -- dramatically reduce frustration. The category menu gives the subscriber control over the experience. And by collecting context (issue description, screenshots, order numbers) before escalating, the human agent can resolve faster, which makes the whole brand feel more competent.

### Common Variations

- **AI-powered:** Replace the static FAQ branches with an AI chatbot (using OpenAI or Claude) that handles freeform questions. Use the menu as a fallback.
- **Business hours split:** During business hours, offer "Talk to someone now" as a Quick Reply. Outside hours, show estimated response time.
- **Satisfaction survey:** After resolution (auto or human), send a quick "How'd we do? 1-5" rating. Track CSAT per branch.
- **Return customer detection:** Check if the subscriber has a "customer" tag. If yes, skip the menu and go straight to priority escalation.

### Platform Notes (ManyChat)

- Set this as the Default Reply in Settings > Automation so it catches any DM that does not match a keyword trigger.
- Use the "Assign to" action to route escalated conversations to specific team members in ManyChat Live Chat.
- Keep the Quick Reply categories to 4-5 max. More than that and people freeze.
- For the "Something Else" branch, use ManyChat's keyword detection to scan the free text input and auto-route before escalating.
- Add a "Back to Menu" Quick Reply at the end of each branch so subscribers can ask about something else without starting over.
- In GHL, use the Conversations inbox with round-robin assignment for escalated tickets. Tag the conversation with the category for reporting.

---

## 6. Re-engagement/Win-back

### What It Does

Targets subscribers who have gone quiet (no interaction in 7+ days), sends a value-first re-engagement message, and either reactivates them or removes them from active messaging to keep your list healthy.

### When to Use It

- Your open/response rates are dropping because of inactive subscribers
- You want to clean your list without losing recoverable leads
- You are about to run a launch and want to warm up dormant contacts first
- ManyChat is charging you for subscribers you are not using

### Typical Trigger

Subscriber condition: "Last interaction > 7 days ago" (automated rule or broadcast segment).

### Flow Diagram

```
TRIGGER: Automated Rule -- subscriber has not interacted
         in 7+ days
         OR
         Broadcast to segment "inactive-7-days"
  |
  v
MSG 1 (Value-first, no ask):
  "Hey {{first_name}} -- been a minute!

   I just dropped something new that I think you'll
   find useful:
   [1-2 sentence description of a genuinely valuable
    piece of content, tip, or resource]

   [Button: Check it out --> content link]"
  - Action: Tag "reengagement-attempt-1"
  |
  v
WAIT: 48 hours. Check for interaction.
  - IF subscriber clicked button or replied --> REACTIVATED
  - IF no interaction --> MSG 2
  |
  +-- REACTIVATED --------------------------------+
  |                                               |
  v                                               |
  MSG R1: "Good to have you back!                  |
                                                   |
           By the way -- is there anything         |
           specific you're working on right now?   |
           I might have something that helps."     |
  - Quick Reply: "[Topic A]" --> Tag + route to    |
                  relevant content/flow            |
  - Quick Reply: "[Topic B]" --> Tag + route       |
  - Quick Reply: "Just browsing" --> Tag "active", |
                  END                              |
  - Action: Remove "inactive" tag                  |
  - Action: Tag "reengaged"                        |
  - END                                            |
  |                                                |
  +-- NO INTERACTION (MSG 2) ---------------------+
  |                                               |
  v                                               |
  MSG 2 (Direct question):                         |
  "Quick question -- are you still interested in   |
   [topic/niche]?                                  |
                                                   |
   No hard feelings either way. Just want to make  |
   sure I'm only sending you stuff you actually    |
   want."                                          |
  - Quick Reply: "Yes, keep me in!" --> REACTIVATED|
  - Quick Reply: "Nah, I'm good" --> UNSUBSCRIBE   |
  |                                               |
  WAIT: 72 hours. Check for interaction.           |
  - IF replied "Yes" --> REACTIVATED               |
  - IF replied "Nah" --> UNSUBSCRIBE               |
  - IF no interaction --> MSG 3                    |
  |                                               |
  v                                               |
  MSG 3 (Final attempt):                           |
  "Last one from me -- I'm cleaning up my list     |
   and I don't want to spam anyone who's moved on. |
                                                   |
   Tap below if you still want to hear from me.    |
   Otherwise I'll stop messaging you."             |
  - Quick Reply: "Keep me!" --> REACTIVATED        |
  |                                               |
  WAIT: 48 hours.                                  |
  - IF replied --> REACTIVATED                     |
  - IF no interaction --> REMOVE                   |
  |                                                |
  +-- UNSUBSCRIBE / REMOVE -----------------------+
  |                                               |
  v                                               |
  ACTION: Tag "unsubscribed-reengagement"          |
  ACTION: Unsubscribe from bot (or move to         |
          "dormant" segment -- do NOT delete)       |
  ACTION: Remove from active sequences             |
  - Optional: MSG FINAL: "Got it -- no more         |
    messages from me. If you ever want back in,    |
    just DM 'START' anytime."                      |
  - END                                            |
```

### Message Count

3-4 messages over 5-7 days.

### Expected Re-activation Rate

10-20% of inactive subscribers re-engage. Another 5-10% actively unsubscribe (which is a good outcome -- clean list). 70-80% simply do not respond and get moved to dormant.

### Key Psychology

**Loss aversion and respect.** The first message leads with value, not guilt. The second message gives them an easy out, which paradoxically makes them more likely to stay (people do not like losing access to things). The final "I'm going to stop messaging you" triggers loss aversion -- "wait, maybe I do want this." Those who still do not respond were never going to convert anyway.

### Common Variations

- **Win-back offer:** Instead of free content in MSG 1, offer a discount or exclusive deal. Works better for e-commerce than service businesses.
- **Survey re-engagement:** Ask "What would be most helpful right now?" with 3-4 Quick Replies. Uses the re-engagement as a re-segmentation opportunity.
- **Graduated timeline:** Instead of 7 days, run three tiers: 7-day (light nudge), 14-day (value offer), 30-day (final warning). More gentle, but more messages.
- **Seasonal cleanup:** Run the win-back flow quarterly instead of continuously. Batch approach is simpler to manage.

### Platform Notes (ManyChat)

- Use ManyChat's "Subscriber Filter" in Automations to target people where "Last Interaction" is older than 7 days.
- Important: ManyChat charges per subscriber. Regularly removing inactive subscribers saves money. Move them to "unsubscribed" rather than deleting -- you keep the data.
- Respect the 24-hour messaging window. If someone has not interacted in 7+ days, you CANNOT message them on Instagram unless they re-engage. Use this flow as a broadcast to those still within the window, or use the "Message Tag" feature (limited use cases).
- On Facebook Messenger, you can use the "Non-Promotional Subscription" permission to message outside the 24-hour window for certain content types. Do not abuse this.
- In GHL, use a workflow trigger "Contact has no activity in X days" and send via SMS or email instead of DM if the messaging window has expired.

---

## 7. Launch/Countdown Sequence

### What It Does

Builds a waitlist for a time-limited offer, then runs a countdown sequence with escalating urgency that drives purchases before the deadline. Each message adds more scarcity and social proof.

### When to Use It

- You are launching a new product, course, or offer with a hard deadline
- You are running an early-bird or limited-time discount
- You want to create urgency around an evergreen offer (manufactured launch)
- You have a warm audience that needs a push to buy

### Typical Trigger

Broadcast to existing subscribers, comment keyword ("WAITLIST", "EARLY"), or DM keyword.

### Flow Diagram

```
TRIGGER: Comment keyword "WAITLIST" on launch teaser post
         OR broadcast to warm segment
  |
  v
MSG 1 (Waitlist Signup):
  "Hey {{first_name}}! You're one of the first to
   hear about this.

   [Product name] is launching on [date].

   Here's what it is in one sentence:
   [Clear, benefit-driven description]

   Want me to put you on the early access list?
   You'll get first dibs + a launch discount."
  - Quick Reply: "Yes, I'm in!" --> MSG 2
  - Quick Reply: "Tell me more" --> MSG 1b
  |
  v
MSG 1b: "Here's the full breakdown:
         - [Benefit/feature 1]
         - [Benefit/feature 2]
         - [Benefit/feature 3]
         - Launch price: [price] (goes up to [full price])
         - Only available until [deadline]

         Want early access?"
  - Quick Reply: "Sign me up" --> MSG 2
  |
  v
MSG 2: "You're on the list! I'll DM you the moment
        it goes live.

        What's your email so I can send the details
        there too?"
  - User Input: email --> stored in {{email}}
  - Action: Tag "waitlist-[product-name]"
  - Action: Set custom field "waitlist_date" = now()
  - Action: Add to email waitlist sequence
  |
  v
MSG 3 (Confirmation):
  "Locked in. You'll hear from me on [launch date].

   In the meantime, here's a sneak peek:
   [Button: Preview --> teaser content link]

   Talk soon!"
  - END (wait for launch)
  |
  ========== LAUNCH DAY ==========
  |
  v
MSG 4 (Launch -- Day 0):
  "It's live! {{first_name}}, you have early access.

   [Product name] is officially available at the
   launch price of [price].

   [Button: Get It Now --> sales page link]

   This price is only good until [deadline date].
   After that it goes to [full price]."
  - Action: Tag "launch-notified"
  |
  v
MSG 5 (3 days before deadline):
  "Hey {{first_name}} -- just wanted to make sure
   you saw this.

   [Product name] is closing in 3 days.

   [Social proof: X people have already grabbed it /
    here's what [name] said about it: '[testimonial]']

   [Button: Grab Your Spot --> sales page link]"
  - Action: Check if already purchased -->
    IF yes, skip remaining messages + tag "customer"
  |
  v
MSG 6 (1 day before deadline):
  "24 hours left.

   After tomorrow, [product name] either goes away
   or the price jumps to [full price].

   If you've been on the fence, this is the nudge.

   [Button: Last Chance --> sales page link]

   Any questions before you decide? Just reply here."
  - User Input: optional reply --> route to live chat
  |
  v
MSG 7 (Day of deadline -- morning):
  "Today's the day. [Product name] closes tonight
   at [time].

   Everything you get:
   - [Bullet 1]
   - [Bullet 2]
   - [Bullet 3]
   - [Bonus if applicable]

   [Button: Get It Before It's Gone --> sales page]"
  |
  v
MSG 8 (Day of deadline -- final hours):
  "Final call -- [Product name] closes in [X] hours.

   I won't be sending this again.

   [Button: Last Chance --> sales page link]"
  - Action: Tag "launch-final-notice"
  |
  v
MSG 9 (Post-deadline -- next day):
  - IF purchased --> MSG 9a
  - IF not purchased --> MSG 9b
  |
  v
MSG 9a: "Welcome in, {{first_name}}! Here's how to
         get started:
         [Button: Access [Product] --> login/access link]

         Any questions, just reply here."
  - Action: Tag "customer-[product-name]"
  - Action: Remove from launch sequence
  - END
  |
  v
MSG 9b: "Hey {{first_name}} -- the launch is over
         and the doors are closed.

         If you want to be first to know when it
         opens again, just reply 'NEXT' and I'll
         add you to the priority list."
  - Quick Reply: "NEXT" --> Tag "priority-next-launch"
  - No reply --> END
  - Action: Remove "waitlist" tag
  - END
```

### Message Count

8-10 messages over 7-14 days (2-3 pre-launch, 1 launch, 4-5 countdown, 1 post-deadline).

### Expected Conversion Rate

5-15% of waitlist subscribers purchase. 60-70% of purchases happen in the last 48 hours. First-day purchases account for 20-30% of total.

### Key Psychology

**Manufactured urgency and escalating scarcity.** The countdown creates a decision deadline. Each message raises the stakes: "3 days" feels like plenty of time, "24 hours" feels real, "final hours" triggers action. Social proof in the middle messages normalizes buying. The post-deadline "doors are closed" message creates FOMO for anyone who hesitated, making them more likely to buy next time.

### Common Variations

- **Evergreen launch:** Use subscriber-specific dates instead of fixed dates. Each person's countdown starts when they join the waitlist. Requires dynamic date fields.
- **Bonus stacking:** Add a new bonus at each countdown stage ("If you grab it in the next 24 hours, you also get [bonus]"). Rewards early action.
- **Payment plan:** Offer a payment plan option in the final 24 hours for price-sensitive buyers. "Still on the fence? Split it into 3 payments of [amount]."
- **Founder's price:** First X buyers get the lowest price. Once those spots fill, the price goes up. Real scarcity, not manufactured.

### Platform Notes (ManyChat)

- Use Broadcasts for the launch and countdown messages. Schedule them in advance so nothing gets missed.
- Track purchases using a webhook from your payment processor (Stripe, PayPal, Gumroad). When a purchase comes in, tag the subscriber as "customer" and use a Condition to skip remaining countdown messages.
- The 24-hour messaging window is critical here. If someone joined the waitlist 8 days ago and has not interacted since, you CANNOT DM them on Instagram. Solve this by including a Quick Reply in each message to keep the window open.
- For Facebook Messenger, use Sponsored Messages (paid) to reach subscribers outside the 24-hour window during launches.
- Always include a Quick Reply or button in countdown messages so the subscriber "interacts" and resets the 24-hour window for the next message.
- In GHL, run the same sequence via SMS and email in parallel for maximum reach. DM for engagement, email for details, SMS for urgency.

---

## 8. Content Upgrade / Story Reply

### What It Does

Turns an Instagram story reply (or story mention) into a lead capture flow. Acknowledges the reply, delivers bonus content related to the story, collects an email, and enters a short nurture sequence.

### When to Use It

- You share tips, insights, or behind-the-scenes content on stories
- You want to turn casual story engagement into actual leads
- You are running a "reply to this story to get X" call to action
- You want a lower-friction entry point than a comment trigger (story replies feel more private and personal)

### Typical Trigger

Story reply (any reply to a specific story), story mention, or keyword in a DM that was prompted by a story.

### Flow Diagram

```
TRIGGER: Story reply containing keyword
         OR any reply to a specific story
         (ManyChat Story Reply trigger)
  |
  v
MSG 1 (Acknowledge + hook):
  "Hey {{first_name}}! Love that you replied to that.

   I've actually got a [bonus resource type, e.g.,
   full breakdown / cheat sheet / extended version]
   that goes way deeper on this.

   Want me to send it?"
  - Quick Reply: "Yes please!" --> MSG 2
  - Quick Reply: "What's in it?" --> MSG 1b
  |
  v
MSG 1b: "It covers:
         - [Detail 1]
         - [Detail 2]
         - [Detail 3]

         Basically everything I couldn't fit in
         a 15-second story. Want it?"
  - Quick Reply: "Send it!" --> MSG 2
  |
  v
MSG 2: "Awesome. Drop your email and I'll send it
        there too -- easier to save."
  - User Input: email --> stored in {{email}}
  - Validation: email format check
  |
  v
MSG 3: "Here you go!
        [Button: Get the [Resource] --> link]

        Sent a copy to {{email}} as well."
  - Action: Tag "content-upgrade-[topic]"
  - Action: Set custom field "lead_source" = "story_reply"
  - Action: Set custom field "content_upgrade" = "[topic]"
  - Action: Send email with resource
  |
  v
MSG 4 (12hr delay -- lighter than 24hr for stories):
  "By the way -- if you liked that, you'll probably
   love [related content piece].

   [Button: Watch/Read --> link]"
  - Action: Tag "engaged-story-lead"
  |
  v
MSG 5 (48hr delay):
  "Hey {{first_name}} -- quick question.

   What's the one thing you're trying to figure out
   right now when it comes to [niche topic]?

   Just curious -- I'm planning some new content and
   your answer helps a lot."
  - User Input: free text --> stored in
    {{content_feedback}}
  - Action: Tag with topic keyword from response
    (manual review or keyword match)
  |
  v
MSG 6 (based on response):
  - IF response mentions [problem A]:
    "That's super common. I actually covered this in
     [specific content]. Check it out:
     [Button: Watch --> link]"
  - IF response mentions [problem B]:
    "I hear that a lot. Here's something that might
     help: [Button: Read --> link]"
  - DEFAULT:
    "Thanks for sharing that. I'm going to put
     something together on this soon. I'll DM you
     when it's ready."
  - Action: Tag "story-nurture-complete"
  - END
```

### Message Count

5-6 messages over 2-3 days.

### Expected Completion Rate

50-70% from story reply to email collected. This is the highest-converting flow pattern because the subscriber initiated the conversation.

### Key Psychology

**Social reciprocity and conversational momentum.** Story replies are the most personal interaction on Instagram -- it feels like a 1-on-1 conversation, not a public comment. The subscriber already made the first move by replying, so there is strong momentum. The "I've got something extra" offer feels like a reward for engaging, not a sales pitch. And asking for their content feedback in MSG 5 makes them feel heard, which deepens the relationship.

### Common Variations

- **Voice note reply:** Instead of text in MSG 1, send a short voice note. Feels incredibly personal and builds trust fast. Higher engagement but harder to automate at scale.
- **Story poll follow-up:** Run a story poll, then DM everyone who voted with a follow-up related to their answer. ManyChat can trigger on poll responses.
- **Multi-story sequence:** Post a 3-story sequence (hook, teach, CTA) where the CTA story prompts the reply. Pre-warms them before the flow starts.
- **Instagram Close Friends:** Deliver the content upgrade to Close Friends list as exclusive stories. Collect email for "full access." Adds exclusivity layer.
- **Reel-to-story bridge:** Post a reel, add a story saying "Reply for the thing I mentioned in my reel," and run this flow. Combines reach (reel) with conversion (story DM).

### Platform Notes (ManyChat)

- Use the "Instagram Story Reply" trigger in ManyChat. It fires when someone replies to ANY of your stories, so use a Condition block to check the reply content or use the "Specific Story" trigger if available.
- Story reply triggers only work on Instagram, not Facebook. For Facebook, use the comment keyword trigger on a post instead.
- The 24-hour messaging window starts when they reply to your story. You have 24 hours for promotional content. Keep MSG 1-3 within the first few hours.
- Smart Delays of 10-15 minutes between MSG 1 and MSG 3 feel more natural than instant responses for story flows. People expect a slight delay from stories.
- Story replies have the highest engagement rate of any trigger type. Use them as the top of funnel and feed qualified leads into the Sales Qualifier (Pattern 3) or Quiz (Pattern 2) flows.
- If someone replies to multiple stories, use a Condition to check if they already received this flow. Avoid sending duplicate content upgrades.

---

## Quick Reference Table

| # | Pattern | Trigger | Messages | Completion Rate | Best For |
|---|---------|---------|----------|-----------------|----------|
| 1 | Lead Magnet Delivery | Comment/DM keyword | 5-7 | 40-60% | List building |
| 2 | Quiz/Survey Funnel | DM keyword | 6-8 | 30-50% | Segmentation |
| 3 | Sales Qualifier | DM keyword | 5-6 | 25-40% | High-ticket sales |
| 4 | Webinar/Event Registration | Comment/DM keyword | 8-11 | 35-55% | Event attendance |
| 5 | Customer Support Router | Default reply | 3-6 | 40-60% resolved | Support volume |
| 6 | Re-engagement/Win-back | Automated rule | 3-4 | 10-20% reactivated | List hygiene |
| 7 | Launch/Countdown | Broadcast/keyword | 8-10 | 5-15% purchase | Product launches |
| 8 | Content Upgrade / Story Reply | Story reply | 5-6 | 50-70% | Warm lead capture |

---

## Combining Patterns

These flows are building blocks. The most effective automations chain them together:

- **Story Reply (8) into Lead Magnet (1):** Story reply captures attention, lead magnet captures email.
- **Lead Magnet (1) into Quiz (2):** After delivering the guide, ask 2-3 segmentation questions to personalize the next offer.
- **Quiz (2) into Sales Qualifier (3):** Hot quiz respondents get routed straight to qualification questions.
- **Webinar (4) into Launch (7):** Event attendees become the warmest segment for your next launch.
- **Any flow into Re-engagement (6):** Every subscriber who goes cold eventually enters the win-back sequence.
- **Support Router (5) into Sales Qualifier (3):** Pricing questions in support get routed to the qualifier instead of a static FAQ.

---

## Universal Rules

1. **Always lead with value before asking for anything.** The first message should give, not take.
2. **Keep Quick Reply options to 2-4 per message.** More than that causes decision paralysis.
3. **Use the subscriber's first name in every message.** Personalization is not optional.
4. **Set Smart Delays between messages (1-3 seconds).** Instant replies feel robotic.
5. **Tag everything.** Every action, every segment, every path. You cannot optimize what you cannot measure.
6. **Respect the 24-hour window on Instagram.** If someone has not interacted in 24 hours, you cannot message them. Plan accordingly.
7. **Always give an exit.** Every flow should have a graceful way out. Trapping people in loops destroys trust.
8. **Test the flow yourself before going live.** Send yourself through it. Read every message out loud. If it sounds like a robot, rewrite it.
9. **One CTA per message.** Do not ask them to watch a video AND book a call AND download a guide in the same message.
10. **Track completion rates per step.** The drop-off point tells you exactly where the flow is broken.
