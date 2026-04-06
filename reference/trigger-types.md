# Trigger Types Reference

Universal reference for automation triggers across ManyChat, GoHighLevel, n8n, and Make.com.

---

## ManyChat

| Trigger | What Activates It | Visual Appearance | Common Use Cases | Setup Path |
|---------|-------------------|-------------------|------------------|------------|
| **Keyword** | User sends a specific word or phrase in DMs | Blue rounded node, chat bubble icon, shows the keyword text | Lead magnet delivery ("Send PDF"), support routing, menu navigation | Automation > New Automation > Keyword |
| **Comment Automation** | User comments a keyword on a specific post | Purple node, Instagram/FB post icon, shows keyword + post preview | Comment-to-DM funnels, giveaways, engagement hooks | Automation > New Automation > Instagram Comment / FB Comment |
| **Story Reply** | User replies to your Instagram Story | Pink/gradient node, story ring icon | Conversational openers, poll follow-ups, flash sale DMs | Automation > New Automation > Instagram Story Reply |
| **Story Mention** | User mentions your account in their Story | Pink/gradient node, @ icon | Thank-you automations, UGC collection, relationship building | Automation > New Automation > Instagram Story Mention |
| **Ads JSON** | Meta ad click with JSON payload | Blue node, megaphone/ad icon | Ad-to-DM funnels, lead qualification from paid traffic | Automation > New Automation > Ads JSON |
| **Ref URL** | User clicks a ManyChat ref link | Blue node, link icon, shows ref parameter | External traffic routing (bio link, email, website), UTM-style tracking | Automation > New Automation > Ref URL |
| **Welcome Message** | First-time user messages your page | Green node, wave/hand icon | Onboarding sequence, main menu, opt-in prompt | Automation > New Automation > Welcome Message |
| **Default Reply** | User sends a message that matches no other trigger | Grey node, question mark icon | Fallback handler, live agent handoff, "I didn't understand" reply | Automation > New Automation > Default Reply |
| **Rule Trigger** | Condition-based (tag applied, field changed, date reached) | Orange node, gear/cog icon, shows rule condition | Drip sequences, birthday messages, renewal reminders | Automation > New Automation > Rule |
| **External Trigger** | API call from another system hits ManyChat endpoint | Grey node, webhook/lightning icon | CRM integration, purchase confirmation, n8n/Zapier handoff | Automation > New Automation > External Trigger |

### ManyChat Notes

- Comment Automation is the highest-converting trigger for organic content. Pair with a post CTA like "Comment GUIDE to get it."
- Welcome Message fires only once per subscriber. Use Default Reply for ongoing fallback.
- Ads JSON requires the Meta ad to be configured with "Send to Messenger/Instagram" destination and a JSON payload in the ad setup.
- External Trigger gives you a unique URL. POST to it with the subscriber ID to fire the flow.

---

## GoHighLevel (GHL)

| Trigger | What Activates It | Visual Appearance | Common Use Cases | Setup Path |
|---------|-------------------|-------------------|------------------|------------|
| **Form Submit** | User submits a GHL form or survey | Green circle node, form/document icon | Lead capture, intake forms, application funnels | Automation > New Workflow > Add Trigger > Form Submitted |
| **Webhook** | External system sends HTTP POST to GHL endpoint | Blue circle node, lightning bolt icon | Stripe payment events, Calendly bookings, custom integrations | Automation > New Workflow > Add Trigger > Inbound Webhook |
| **Tag Applied** | A contact gets a specific tag added | Yellow circle node, tag/label icon | Segment-based nurture, post-purchase upsell, lead scoring actions | Automation > New Workflow > Add Trigger > Tag Added |
| **Pipeline Stage Change** | Contact moves to a new pipeline stage | Purple circle node, kanban/columns icon | Sales follow-up sequences, onboarding steps, status notifications | Automation > New Workflow > Add Trigger > Pipeline Stage Changed |
| **Appointment Booked** | Contact books via GHL calendar | Green circle node, calendar icon | Confirmation SMS, reminder sequence, show-rate automation | Automation > New Workflow > Add Trigger > Appointment Status |
| **Invoice Paid** | Contact pays a GHL invoice | Green circle node, dollar/currency icon | Receipt delivery, onboarding trigger, access provisioning | Automation > New Workflow > Add Trigger > Invoice > Paid |
| **Opportunity Status Changed** | Opportunity moves to won/lost/abandoned | Purple circle node, trophy or pipeline icon | Win celebration email, lost lead re-engagement, reporting | Automation > New Workflow > Add Trigger > Opportunity Status Changed |
| **Inbound Call** | Contact calls a GHL tracking number | Blue circle node, phone icon | Missed call text-back, call routing, lead tagging | Automation > New Workflow > Add Trigger > Call Status |
| **Email Opened** | Contact opens a GHL email | Orange circle node, envelope icon | Engagement scoring, follow-up timing, re-send to non-openers | Automation > New Workflow > Add Trigger > Email Events > Opened |

### GHL Notes

- All triggers appear as colored circles at the top of the workflow canvas. The color indicates the trigger category.
- Pipeline Stage Change is one of the most powerful triggers for agency workflows. Combine with "If/Else" to branch by stage name.
- Webhook trigger auto-generates a unique URL. Copy it from the trigger settings panel.
- Appointment Booked can filter by calendar, status (booked, confirmed, showed, no-showed, cancelled).

---

## n8n

| Trigger | What Activates It | Visual Appearance | Common Use Cases | Setup Path |
|---------|-------------------|-------------------|------------------|------------|
| **Webhook** | External HTTP request hits the n8n endpoint | Purple node, globe/webhook icon, labeled "Webhook" | Receiving data from GHL, ManyChat, Stripe, any external system | Add Node > On webhook call |
| **Schedule / Cron** | Time-based (every X minutes, daily at 9am, etc.) | Purple node, clock icon, labeled "Schedule Trigger" | Daily reports, recurring data syncs, morning briefings | Add Node > On a schedule |
| **Gmail Trigger** | New email arrives matching filter | Red node, Gmail envelope icon | Email triage, auto-forwarding, lead capture from email | Add Node > On Gmail message received |
| **Slack Trigger** | Message posted in channel, reaction added, etc. | Purple node, Slack hash icon | Team notifications, command bots, approval flows | Add Node > On Slack event |
| **Airtable Trigger** | Record created or updated in Airtable | Blue/teal node, Airtable grid icon | CRM sync, content pipeline updates, task management | Add Node > On Airtable event |
| **Manual Trigger** | User clicks "Test Workflow" or "Execute" in n8n | Grey node, play button icon, labeled "When clicking Test workflow" | Testing, one-off tasks, on-demand reports | Add Node > Manually (default on new workflow) |
| **Error Trigger** | Another workflow fails | Red node, warning triangle icon | Error alerting, retry logic, Slack error notifications | Add Node > On workflow error |
| **Google Sheets Trigger** | Row added or updated in Google Sheets | Green node, Sheets icon | Form response processing, inventory updates | Add Node > On Google Sheets row event |
| **Telegram Trigger** | Message received in Telegram bot | Blue node, Telegram paper plane icon | Bot commands, group monitoring, notification replies | Add Node > On Telegram message |
| **HTTP Request (polling)** | Periodically checks an API endpoint for changes | Orange node, globe icon | Monitoring APIs without webhooks, RSS-style polling | Schedule Trigger > HTTP Request node chain |

### n8n Notes

- Trigger nodes always sit at the far left of the canvas. They have a single output connector (no input).
- Webhook trigger generates two URLs: test (for building) and production (for live use). Always use the production URL in external systems.
- Schedule Trigger uses cron syntax. Common patterns: `0 9 * * 1-5` (weekdays at 9am), `*/15 * * * *` (every 15 min).
- Error Trigger must be in a separate workflow from the one it monitors.

---

## Make.com (formerly Integromat)

| Trigger | What Activates It | Visual Appearance | Common Use Cases | Setup Path |
|---------|-------------------|-------------------|------------------|------------|
| **Watch Triggers** | Polls an app for new/updated records at intervals | Circular module, app-colored, clock badge, labeled "Watch [Records]" | New Airtable records, new Google Drive files, new CRM contacts | New Scenario > Choose App > Watch [item type] |
| **Instant Triggers** | Real-time event via app webhook | Circular module, app-colored, lightning badge, labeled "Watch [Events]" | Stripe payment received, Typeform submitted, Slack message | New Scenario > Choose App > Instant trigger variant |
| **Custom Webhook** | External system sends data to a Make webhook URL | Purple circle, globe icon, labeled "Custom webhook" | Receiving data from any system, GHL events, custom apps | New Scenario > Webhooks > Custom webhook |
| **Scheduled** | Scenario runs on a fixed schedule | No trigger module needed; schedule set in scenario settings | Daily data syncs, weekly reports, batch processing | Scenario Settings > Scheduling (bottom toolbar) |
| **Email (Mailhook)** | Email received at a Make-generated address | Purple circle, envelope icon | Email parsing, attachment processing, forwarding logic | New Scenario > Webhooks > Mailhook |
| **Google Sheets Watch** | New row added to a Google Sheet | Green circle, Sheets icon, labeled "Watch Rows" | Form responses, inventory, lead lists | New Scenario > Google Sheets > Watch Rows |

### Make.com Notes

- Watch triggers have a polling interval set in the scenario scheduling (minimum 1 minute on paid plans, 15 minutes on free).
- Instant triggers are always preferred over Watch triggers when the app supports them. They use zero operations while waiting.
- Modules appear as colored circles connected left-to-right. The first module (trigger) has a clock or lightning badge.
- Custom Webhook auto-generates a URL. Click "Copy address to clipboard" in the module settings.
- Scheduled scenarios with no trigger module start with the first action module. The schedule is set globally for the scenario.

---

## Cross-Platform Trigger Comparison

| Capability | ManyChat | GHL | n8n | Make.com |
|-----------|----------|-----|-----|----------|
| Webhook receive | External Trigger | Inbound Webhook | Webhook | Custom Webhook |
| Time-based | Rule (date) | Workflow schedule | Schedule Trigger | Scenario scheduling |
| Form/survey submit | N/A | Form Submit | Via webhook | Via app module |
| Tag/segment change | Rule Trigger | Tag Applied | Via webhook/API | Watch trigger |
| Payment event | N/A | Invoice Paid | Stripe Trigger | Stripe Instant |
| Social comment | Comment Automation | N/A | Via webhook | Instagram Watch |
| DM received | Keyword / Default Reply | N/A | Via ManyChat webhook | Via ManyChat webhook |
| Error handling | N/A | N/A | Error Trigger | Error handler route |

---

## When to Use Which Trigger

| Scenario | Best Trigger | Platform |
|----------|-------------|----------|
| Comment "GUIDE" to get a lead magnet | Comment Automation | ManyChat |
| New lead fills out a form, start nurture | Form Submit | GHL |
| Daily morning report at 9am | Schedule Trigger | n8n |
| Stripe payment triggers onboarding | Webhook (Stripe event) | n8n or Make.com |
| Lead goes silent for 48 hours | Rule Trigger (date-based) | ManyChat or GHL |
| Ad click opens a DM conversation | Ads JSON | ManyChat |
| Pipeline deal moves to "Won" | Opportunity Status Changed | GHL |
| New Airtable record syncs to CRM | Airtable Trigger | n8n or Make.com |
