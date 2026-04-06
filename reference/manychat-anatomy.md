# ManyChat Flow Builder -- Visual Anatomy Reference

> This file is the Rosetta Stone for reading ManyChat screenshots.
> Use it to identify every UI element by sight and map it to exact rebuild instructions.

---

## How the Flow Builder Canvas Works

The Flow Builder is a visual drag-and-drop canvas. Flows read left to right. Every flow starts with one or more **Starting Steps** (triggers) on the left, connected by blue lines to **Content Steps** and **Action Steps** on the right. Each step is a rounded-corner card on the canvas.

**Universal visual rules:**

| Element | Visual Cue |
|---------|-----------|
| Starting Step (trigger) | Blue header bar, lightning bolt icon |
| Content Step | White card, content-type icon in top-left corner |
| Action Step | Grey or colored small pill/chip inside a step |
| Connection line | Blue curved line between steps |
| Selected step | Blue border highlight |
| Error/warning | Red or orange dot on the step corner |
| Draft (unpublished) | Yellow "Draft" badge in top bar |
| Published | Green "Published" badge in top bar |

---

## 1. Triggers (Starting Steps)

Starting Steps appear as blue-header cards on the far left of the canvas. They define what causes a subscriber to enter the flow. Each has a lightning bolt icon and a label describing the trigger type.

---

### 1.1 Keyword Trigger

| Field | Detail |
|-------|--------|
| **UI name** | Keyword |
| **Visual** | Blue card header reading "Keyword". Below it a white body listing the keyword(s) in grey pill tags. Channel icon (Instagram DM or Messenger) shown top-right. |
| **What it does** | Fires the flow when a subscriber sends a DM containing one of the listed keywords. Supports exact match, contains, begins with. |
| **How to create** | Flow Builder > click "Add Starting Step" (or the blue "+" on the left rail) > choose **Keyword**. Select channel (Instagram or Messenger). Type each keyword and press Enter. Choose match type from dropdown. |
| **Key settings** | Match type (Is, Contains, Begins with, Regex). Multiple keywords per trigger. Case insensitive by default. "Only if no other keyword matched" toggle. Channel selector (Instagram, Messenger, or both). |

---

### 1.2 Comment Trigger (Instagram Comment Automation)

| Field | Detail |
|-------|--------|
| **UI name** | Instagram Comment Automation / Comments |
| **Visual** | Blue header card with Instagram icon and "Comments" label. Body shows linked post thumbnail or "All Posts" tag. May show keyword filter pills. |
| **What it does** | Fires when someone comments on a specific Instagram post (or any post). Can filter by keyword in the comment. Triggers both a public comment reply and/or a private DM reply. |
| **How to create** | Flow Builder > Add Starting Step > **Instagram Comment Automation**. Select a specific post or "All Posts". Optionally add keyword filters. Configure the comment reply message and/or the DM (private reply) message. |
| **Key settings** | Post selector (specific post URL or all posts). Keyword filter (comment must contain). "Reply to comment" toggle (public reply text). "Send message in DM" toggle (private reply flow). Exclude comments containing certain words. Only trigger once per user per post. |

---

### 1.3 Story Reply Trigger

| Field | Detail |
|-------|--------|
| **UI name** | Instagram Story Reply |
| **Visual** | Blue header card with Instagram story icon (circle with gradient border) and "Story Reply" text. |
| **What it does** | Fires when someone replies to your Instagram Story via DM. |
| **How to create** | Flow Builder > Add Starting Step > **Instagram Story Reply**. |
| **Key settings** | Keyword filter (optional -- only trigger if reply contains keyword). Works on any active story. Cannot target a specific story. |

---

### 1.4 Story Mention Trigger

| Field | Detail |
|-------|--------|
| **UI name** | Instagram Story Mention |
| **Visual** | Blue header card with "@" icon and "Story Mention" text. |
| **What it does** | Fires when someone mentions your Instagram account in their Story. |
| **How to create** | Flow Builder > Add Starting Step > **Instagram Story Mention**. |
| **Key settings** | No keyword filter available. Triggers for any mention. Good for thank-you or engagement automations. |

---

### 1.5 Instagram Ads JSON Trigger

| Field | Detail |
|-------|--------|
| **UI name** | Instagram Ads (JSON) |
| **Visual** | Blue header card with a megaphone/ads icon and "Ig Ads JSON" or "Instagram Ads" label. Body may show the JSON payload reference. |
| **What it does** | Fires when a user clicks a "Send Message" CTA on an Instagram ad configured with a JSON payload. The JSON tells ManyChat which flow to trigger. |
| **How to create** | Flow Builder > Add Starting Step > **Instagram Ads JSON**. Copy the generated JSON payload. In Meta Ads Manager, paste the JSON into the Messenger/Instagram destination field of your ad. |
| **Key settings** | Auto-generated JSON payload (copy to clipboard button). The JSON contains a flow reference ID. Works with Click-to-Instagram-Direct ads. |

---

### 1.6 Messenger Ref URL Trigger

| Field | Detail |
|-------|--------|
| **UI name** | Ref URL |
| **Visual** | Blue header card with link icon and "Ref URL" label. Body shows the generated m.me URL with ref parameter. |
| **What it does** | Fires when someone clicks a unique m.me link (Messenger deep link) that contains a ref parameter pointing to this flow. |
| **How to create** | Flow Builder > Add Starting Step > **Ref URL**. A unique URL is auto-generated. Copy and share it. |
| **Key settings** | Auto-generated ref URL. Custom ref parameter (optional). Works only on Messenger (not Instagram). |

---

### 1.7 Customer Chat Plugin Trigger

| Field | Detail |
|-------|--------|
| **UI name** | Customer Chat Plugin |
| **Visual** | Blue header card with chat bubble icon and "Customer Chat" label. |
| **What it does** | Fires when someone opens the Messenger chat widget embedded on your website. |
| **How to create** | Flow Builder > Add Starting Step > **Customer Chat Plugin**. Configure the widget in Settings > Growth Tools > Customer Chat. |
| **Key settings** | Greeting text. Logged-in vs logged-out greeting. Color theme. Widget position. Domain whitelist. |

---

### 1.8 Welcome Message Trigger

| Field | Detail |
|-------|--------|
| **UI name** | Welcome Message |
| **Visual** | Blue header card with a waving hand icon and "Welcome Message" label. Only one per bot. |
| **What it does** | Fires the very first time a user opens a conversation with your bot (Messenger or Instagram). This is the entry point for new subscribers. |
| **How to create** | Settings > General (or Automation > Welcome Message). There is only one Welcome Message per channel. Click "Edit" to open it in Flow Builder. |
| **Key settings** | Single instance per channel. Cannot be duplicated. Typically contains a greeting and quick reply buttons to route the user. |

---

### 1.9 Default Reply Trigger

| Field | Detail |
|-------|--------|
| **UI name** | Default Reply |
| **Visual** | Blue header card with a question mark icon and "Default Reply" label. Only one per bot. |
| **What it does** | Fires when a subscriber sends a message that does not match any keyword or active automation. Acts as a fallback. |
| **How to create** | Settings > General (or Automation > Default Reply). Single instance per channel. Click "Edit" to open in Flow Builder. |
| **Key settings** | Delay before firing (e.g., "If no other rule matches within 2 seconds"). Typically offers quick replies or hands off to live chat. Single instance per channel. |

---

### 1.10 Rule Trigger (Condition-Based)

| Field | Detail |
|-------|--------|
| **UI name** | Rule |
| **Visual** | Blue header card with a filter/funnel icon and "Rule" label. Body shows the condition summary (e.g., "Tag is X" or "Custom Field equals Y"). |
| **What it does** | Fires based on subscriber data conditions (tag added, field changed, date reached, etc.). Rules are evaluated when subscriber data changes. |
| **How to create** | Automation > Rules > New Rule. Define the trigger event (tag added, field changed, subscribed to bot, date field matches, etc.) and the action (start a flow, send a message, etc.). Rules also appear as Starting Steps when linked to a flow. |
| **Key settings** | Trigger event type. Condition filters (AND/OR logic). Action to perform. One-time vs recurring. |

---

### 1.11 External Trigger (API / Webhook)

| Field | Detail |
|-------|--------|
| **UI name** | External Trigger |
| **Visual** | Blue header card with a webhook/arrow icon and "External Trigger" label. Body shows the unique webhook URL. |
| **What it does** | Fires when an external system sends an HTTP POST to the trigger's unique URL. Used for n8n, Zapier, or custom integrations. |
| **How to create** | Flow Builder > Add Starting Step > **External Trigger**. Copy the generated webhook URL. Send a POST request with the subscriber's ID or custom data. |
| **Key settings** | Auto-generated webhook URL. Accepts subscriber_id or user_ref in the payload. Can pass custom field values in the POST body. Test button to simulate a trigger. |

---

## 2. Content Blocks

Content blocks are the white cards on the canvas that display messages to the subscriber. They appear as rounded rectangles with a content-type icon in the top-left corner and a preview of the content in the body.

---

### 2.1 Text Block

| Field | Detail |
|-------|--------|
| **UI name** | Text |
| **Visual** | White card with a text/speech bubble icon. Body shows the message text preview. Personalization tokens appear as blue highlighted pills (e.g., `{{first_name}}` shows as a blue tag reading "First Name"). |
| **What it does** | Sends a plain text message to the subscriber. Supports personalization tokens, emojis, and links. |
| **How to create** | In a Content Step, click "Add Content" (or the "+" inside a step) > **Text**. Type your message. Click the `{ }` button to insert personalization tokens. |
| **Key settings** | Message text (up to 2000 characters for Messenger, 1000 for Instagram). Personalization tokens: `{{first_name}}`, `{{last_name}}`, `{{full_name}}`, `{{email}}`, `{{phone}}`, any custom field. Fallback text (shown if token is empty). Typing delay (simulated typing indicator). |

**Personalization token visual:** Inside the text editor, tokens appear as blue rounded pills with the field name. In the canvas preview, they show as `{{field_name}}` in blue.

---

### 2.2 Image Block

| Field | Detail |
|-------|--------|
| **UI name** | Image |
| **Visual** | White card with an image/photo icon. Body shows a thumbnail preview of the uploaded image. |
| **What it does** | Sends an image to the subscriber. |
| **How to create** | In a Content Step, click "+" > **Image**. Upload an image or paste a URL. |
| **Key settings** | Image file (JPEG, PNG, GIF). Max size 8 MB. Image URL (must be publicly accessible). No caption in Messenger (use a Text block before/after). Instagram allows alt text. |

---

### 2.3 Card (Single Card)

| Field | Detail |
|-------|--------|
| **UI name** | Card |
| **Visual** | White card showing an image preview at the top, title text in bold below, subtitle text in grey, and one or more buttons at the bottom (blue rounded rectangles with button labels). |
| **What it does** | Sends a rich card with an image, title, subtitle, and up to 3 buttons. |
| **How to create** | In a Content Step, click "+" > **Card**. Fill in image, title, subtitle, and add buttons. |
| **Key settings** | Image (optional). Title (80 char max). Subtitle (80 char max). Action URL (tapping the card opens this link). Up to 3 buttons per card. Button types: URL, Flow, Call, Buy (Messenger only). |

---

### 2.4 Gallery (Horizontal Scrolling Cards)

| Field | Detail |
|-------|--------|
| **UI name** | Gallery |
| **Visual** | White card showing multiple card previews side by side with a horizontal scroll indicator (left/right arrows or dots). Each card has its own image, title, subtitle, and buttons. |
| **What it does** | Sends a horizontally scrollable carousel of cards (up to 10). The subscriber swipes left/right to browse. |
| **How to create** | In a Content Step, click "+" > **Gallery**. Add cards (each with image, title, subtitle, buttons). Click "Add Card" to add more. Drag to reorder. |
| **Key settings** | Up to 10 cards. Each card: image, title, subtitle, up to 3 buttons. Image aspect ratio: 1.91:1 recommended. Square image mode toggle. |

---

### 2.5 List (Vertical List Items)

| Field | Detail |
|-------|--------|
| **UI name** | List |
| **Visual** | White card showing stacked list items vertically. Each item has a small thumbnail on the right, title, and subtitle. A global button may appear at the bottom. |
| **What it does** | Sends a vertical list of items (2-4). Each item can link to a URL or trigger an action. Messenger only (not available on Instagram). |
| **How to create** | In a Content Step, click "+" > **List**. Add list items with title, subtitle, image, and URL. |
| **Key settings** | 2-4 list items. Top item can be "large" (expanded with bigger image). Each item: title, subtitle, image, URL. One global button at the bottom. Messenger only. |

---

### 2.6 Audio Block

| Field | Detail |
|-------|--------|
| **UI name** | Audio |
| **Visual** | White card with a speaker/audio wave icon and a play button preview. |
| **What it does** | Sends an audio file or voice message to the subscriber. |
| **How to create** | In a Content Step, click "+" > **Audio**. Upload an MP3 or paste a URL. |
| **Key settings** | Audio file (MP3, WAV, OGG). Max size 25 MB. URL must be publicly accessible and direct-link (not a streaming page). |

---

### 2.7 Video Block

| Field | Detail |
|-------|--------|
| **UI name** | Video |
| **Visual** | White card with a video camera icon and a video thumbnail preview with a play button overlay. |
| **What it does** | Sends a video to the subscriber as a native playable message. |
| **How to create** | In a Content Step, click "+" > **Video**. Upload an MP4 or paste a URL. |
| **Key settings** | Video file (MP4 recommended). Max size 25 MB. URL must be publicly accessible and direct-link. Thumbnail auto-generated. No inline caption (use a Text block). |

---

### 2.8 File Block

| Field | Detail |
|-------|--------|
| **UI name** | File |
| **Visual** | White card with a document/paperclip icon and the filename displayed. |
| **What it does** | Sends a downloadable file (PDF, document, etc.) to the subscriber. |
| **How to create** | In a Content Step, click "+" > **File**. Upload the file or paste a URL. |
| **Key settings** | Any file type (PDF, DOCX, XLSX, etc.). Max size 25 MB. URL must be publicly accessible. Subscriber taps to download. |

---

## 3. Input Blocks

Input blocks collect information from subscribers. They appear inside Content Steps and have distinctive interactive previews.

---

### 3.1 Quick Reply

| Field | Detail |
|-------|--------|
| **UI name** | Quick Reply |
| **Visual** | Appears as a row of rounded pill-shaped buttons below a message, rendered in outline style (not filled). Each pill shows the reply label. On the canvas, quick replies appear as small rounded tags at the bottom of a Content Step. Blue connection lines extend from each quick reply to the next step. |
| **What it does** | Shows ephemeral tappable buttons below the last message. They disappear after the subscriber taps one (or sends any message). Used for guided choices. |
| **How to create** | In a Content Step, click "Quick Reply" at the bottom of the step (below all content blocks). Type the label. Click the quick reply to configure what happens when tapped. |
| **Key settings** | Label text (up to 20 characters). Action on tap: go to step, open URL, call phone. Connect each quick reply to a different next step via blue lines. Max 13 quick replies per message (Messenger), 10 for Instagram. Can attach an image/emoji to each pill. |

**Key visual difference from Buttons:** Quick Replies are rounded pills in a horizontal row beneath the message. Buttons are rectangular and attached to a Card. Quick Replies disappear after use; Buttons do not.

---

### 3.2 Button

| Field | Detail |
|-------|--------|
| **UI name** | Button |
| **Visual** | Rectangular blue or white button with text label, attached to the bottom of a Card or Text block. On the canvas, buttons appear as labeled rectangles inside the card preview. Connection lines extend from each button. |
| **What it does** | Persistent tappable button attached to a Card or Text (Messenger only for Text buttons). Does not disappear after tapping. |
| **How to create** | Inside a Card block, click "Add Button". Choose button type and label. |
| **Key settings** | Button types: **URL** (opens a link), **Flow** (triggers a step/flow), **Call** (opens phone dialer), **Buy** (Stripe/PayPal payment -- Messenger only). Label text (up to 20 characters). Up to 3 buttons per card. Webview height for URL buttons: Full, Tall, Compact. |

---

### 3.3 User Input (Free Text Collection)

| Field | Detail |
|-------|--------|
| **UI name** | User Input |
| **Visual** | White card with a form/input icon and a question preview. Shows the target custom field name in a blue tag. The card has a distinctive input field preview with the field name below it. Often has a "Skip" option shown as a small link. |
| **What it does** | Asks the subscriber an open-ended question and saves their reply to a Custom Field. The bot waits for a reply before continuing. |
| **How to create** | In a Content Step, click "+" > **User Input**. Type your question. Select the Custom Field to save the answer to (or create a new one). |
| **Key settings** | Question text. Target custom field (text, number, date, etc.). Validation type: Text, Number, Email, Phone, URL, Date, Date/Time. "Reply type" setting. Validation error message (shown if input fails validation). Skip button text (optional). Timeout (how long to wait before moving on). Retry message (on invalid input). |

---

### 3.4 Email / Phone Input (Validated Collection)

| Field | Detail |
|-------|--------|
| **UI name** | Request Email / Request Phone |
| **Visual** | White card with an envelope icon (email) or phone icon (phone). Shows a pre-built input prompt. Has a distinctive "Quick Reply" style button at the bottom labeled with the subscriber's detected email/phone (pre-filled from Facebook profile if available). |
| **What it does** | Specialized input that requests the subscriber's email or phone number with built-in validation. On Messenger, it can pre-fill from the subscriber's Facebook profile. |
| **How to create** | In a Content Step, click "+" > **User Input** > set Reply Type to **Email** or **Phone Number**. Alternatively, some templates offer a dedicated "Request Email" / "Request Phone" block. |
| **Key settings** | Pre-fill from profile (Messenger only -- shows a quick reply with their profile email/phone). Validation (must be valid email format or phone format). Saves to the built-in Email or Phone system field. Custom validation error message. Skip option. |

---

## 4. Action Blocks

Action blocks perform operations without sending visible messages. They appear as small colored pills, chips, or compact cards within a step. Many action blocks are added inside an "Action" step (grey header).

On the canvas, an **Action Step** has a grey or light blue header labeled "Actions" and contains a vertical stack of action pills.

---

### 4.1 Tag (Add / Remove)

| Field | Detail |
|-------|--------|
| **UI name** | Add Tag / Remove Tag |
| **Visual** | Small pill/chip with a tag icon (label shape). Green "+" for add, red "-" for remove. Shows the tag name. |
| **What it does** | Adds or removes a tag from the subscriber. Tags are used for segmentation, targeting, and conditional logic. |
| **How to create** | In an Action Step, click "+" > **Add Tag** or **Remove Tag**. Select an existing tag or type a new one to create it. |
| **Key settings** | Tag name. Add or Remove toggle. Tags are global (shared across all flows). |

---

### 4.2 Set Custom Field

| Field | Detail |
|-------|--------|
| **UI name** | Set Custom Field |
| **Visual** | Small pill/chip with a pencil/field icon. Shows the field name and the value being set (e.g., "lead_source = instagram"). |
| **What it does** | Sets a subscriber-level custom field to a specific value. Used for storing data, tracking state, and personalization. |
| **How to create** | In an Action Step, click "+" > **Set Custom Field Value**. Choose the field from the dropdown (or create new). Enter the value (static text, token, or expression). |
| **Key settings** | Field name. Value (static, dynamic token, clear/empty). Field types: Text, Number, Date, DateTime, Boolean, URL. Supports math expressions for number fields (e.g., `+1` to increment). |

---

### 4.3 Set Bot Field (Global Variable)

| Field | Detail |
|-------|--------|
| **UI name** | Set Bot Field |
| **Visual** | Small pill/chip similar to Custom Field but with a globe/bot icon. Shows field name and value. |
| **What it does** | Sets a bot-level (global) field. Unlike custom fields (per subscriber), bot fields are shared across all subscribers. Used for global config like promo codes or feature flags. |
| **How to create** | In an Action Step, click "+" > **Set Bot Field Value**. Choose the bot field. Enter the value. |
| **Key settings** | Bot field name. Value (static or expression). Bot fields are global -- changing one affects all subscribers who reference it. Field types same as custom fields. |

---

### 4.4 Subscribe to Sequence

| Field | Detail |
|-------|--------|
| **UI name** | Subscribe to Sequence |
| **Visual** | Small pill/chip with a list/sequence icon (stacked lines). Shows the sequence name. |
| **What it does** | Enrolls the subscriber into a drip sequence (a series of timed messages). |
| **How to create** | In an Action Step, click "+" > **Subscribe to Sequence**. Select the sequence from the dropdown. |
| **Key settings** | Sequence name. Sequences are created separately under Automation > Sequences. Each sequence has timed steps (e.g., Day 1, Day 3, Day 7). Subscriber receives messages at the defined intervals. |

---

### 4.5 Unsubscribe from Sequence

| Field | Detail |
|-------|--------|
| **UI name** | Unsubscribe from Sequence |
| **Visual** | Small pill/chip with a crossed-out list icon. Shows the sequence name. |
| **What it does** | Removes the subscriber from a specific sequence, stopping future messages in that sequence. |
| **How to create** | In an Action Step, click "+" > **Unsubscribe from Sequence**. Select the sequence. |
| **Key settings** | Sequence name. Unsubscribes only from the selected sequence (does not affect other sequences). |

---

### 4.6 Mark as Seen

| Field | Detail |
|-------|--------|
| **UI name** | Mark Conversation as Done / Mark as Seen |
| **Visual** | Small pill/chip with a checkmark icon. |
| **What it does** | Marks the conversation as "Done" in the Live Chat panel. Clears the unread indicator. Used to keep the inbox clean after an automated flow handles the conversation. |
| **How to create** | In an Action Step, click "+" > **Mark as Seen** (or "Mark Conversation as Done"). |
| **Key settings** | No additional settings. Instant action. |

---

### 4.7 Notify Admin

| Field | Detail |
|-------|--------|
| **UI name** | Notify Admins |
| **Visual** | Small pill/chip with a bell icon. May show the notification channel (email, Messenger, etc.). |
| **What it does** | Sends a notification to one or more admins when a subscriber reaches this point. Used for lead alerts, support escalation, etc. |
| **How to create** | In an Action Step, click "+" > **Notify Admins**. Choose notification method and recipients. |
| **Key settings** | Notification method: Email, Messenger, or both. Recipient(s): specific admin(s) or all admins. Custom notification message (supports personalization tokens). Include subscriber info toggle. |

---

### 4.8 External Request (Webhook / HTTP Call)

| Field | Detail |
|-------|--------|
| **UI name** | External Request |
| **Visual** | Small pill/chip with a cloud/arrow icon (outbound arrow). Shows the URL being called (truncated). On the canvas, it appears slightly wider than other action pills. Clicking it opens a detailed panel with URL, method, headers, and body fields. |
| **What it does** | Makes an HTTP request (GET or POST) to an external URL. Used to send data to n8n, Zapier, webhooks, CRMs, or any API. Can also receive response data back into custom fields. |
| **How to create** | In an Action Step, click "+" > **External Request**. Enter the URL. Configure method, headers, and body. Map response fields. |
| **Key settings** | Request type: GET or POST. URL (supports personalization tokens). Headers (key-value pairs, for auth tokens etc.). Body (JSON, supports tokens). Response mapping: map JSON response keys to ManyChat custom fields. Timeout. Test button to fire a test request. |

---

### 4.9 Condition (If/Else Branching)

| Field | Detail |
|-------|--------|
| **UI name** | Condition |
| **Visual** | Diamond or split-path card with a branching icon. Shows two exit paths: a green "Yes" path (condition met) and a red "No/Otherwise" path (condition not met). The condition summary is displayed in the card body (e.g., "If tag = Lead AND custom field source = Instagram"). On the canvas, this is one of the wider elements due to the two outgoing connection lines. |
| **What it does** | Evaluates subscriber data against one or more conditions and routes them down different paths. The core branching logic of any flow. |
| **How to create** | Drag a **Condition** block from the left panel onto the canvas. Or in a step, click "+" > **Condition**. Define the condition(s). Connect the "Yes" path and the "Otherwise" path to different steps. |
| **Key settings** | Condition types: Tag (has/does not have), Custom Field (equals, contains, greater than, etc.), System Field (subscribed date, last interaction, etc.), Subscribed to Sequence, Widget interaction, Date/Time. Multiple conditions with AND/OR logic. "Yes" and "Otherwise" exit paths. |

---

### 4.10 Randomizer (A/B Split)

| Field | Detail |
|-------|--------|
| **UI name** | Randomizer |
| **Visual** | Card with a dice or split-path icon. Shows multiple exit paths labeled with percentages (e.g., "Path A: 50%" and "Path B: 50%"). Each path has its own blue connection line. |
| **What it does** | Randomly routes subscribers down different paths based on configured percentages. Used for A/B testing messages, offers, or flows. |
| **How to create** | Drag a **Randomizer** onto the canvas. Set the number of paths (2-6) and the percentage split for each. Connect each path to different steps. |
| **Key settings** | Number of paths (2-6). Percentage per path (must total 100%). Path labels (optional). Each path connects to a different downstream step. |

---

### 4.11 Smart Delay

| Field | Detail |
|-------|--------|
| **UI name** | Smart Delay |
| **Visual** | Small pill/chip with a clock icon. Shows the delay duration (e.g., "Wait 5 minutes" or "Wait until 9:00 AM"). |
| **What it does** | Pauses the flow for a specified duration or until a specific time before continuing to the next step. |
| **How to create** | In an Action Step, click "+" > **Smart Delay**. Choose delay type and duration. |
| **Key settings** | Delay type: **Duration** (minutes, hours, days) or **Until specific time** (e.g., 9:00 AM in subscriber's timezone). Timezone handling: subscriber's timezone or bot timezone. "Continue on the next day if time has passed" toggle. |

---

### 4.12 Go to Step

| Field | Detail |
|-------|--------|
| **UI name** | Go to Step |
| **Visual** | Small pill/chip or card with a curved arrow icon (redirect). Shows the target step name. A dashed blue line on the canvas connects to the target step. |
| **What it does** | Redirects the subscriber to another step within the same flow. Used to create loops or consolidate paths. |
| **How to create** | In an Action Step, click "+" > **Go to Step**. Select the target step from the dropdown (lists all steps in the current flow). |
| **Key settings** | Target step (dropdown of all steps in the flow). Cannot jump to steps in other flows (use "Trigger Another Flow" for that). Creates a visual dashed line on the canvas. |

---

### 4.13 Trigger Another Flow

| Field | Detail |
|-------|--------|
| **UI name** | Start Another Flow / Trigger Flow |
| **Visual** | Small pill/chip with a flow/play icon. Shows the name of the target flow. |
| **What it does** | Starts a completely different flow for the subscriber. The current flow can either continue (non-blocking) or hand off entirely. |
| **How to create** | In an Action Step, click "+" > **Start Another Flow** (or **Trigger Flow**). Select the flow from the dropdown. |
| **Key settings** | Target flow (dropdown of all published flows). Execution: the subscriber enters the target flow immediately. The current flow continues to the next step (both flows run in parallel unless the current flow ends). |

---

## 5. Special Elements

These elements have unique behavior or appear in specific contexts outside the standard content/action pattern.

---

### 5.1 One-Time Notification (OTN) Request

| Field | Detail |
|-------|--------|
| **UI name** | One-Time Notification Request |
| **Visual** | White card with a bell/notification icon. Shows a message preview with a special "Notify Me" style button. The button has a distinct blue appearance with a bell icon. On the canvas, the OTN block has a unique border or badge indicating it is a notification opt-in. |
| **What it does** | Asks the subscriber for permission to send one follow-up message outside the 24-hour messaging window (Messenger only). When they tap "Notify Me", you earn one OTN token that can be used to send a single message at any future time. |
| **How to create** | In a Content Step, click "+" > **One-Time Notification**. Write the request message (explaining what you will notify them about). Select or create an OTN Topic. |
| **Key settings** | OTN Topic (a named category for the notification, e.g., "Back in Stock", "Webinar Reminder"). Message text (what the subscriber sees before opting in). Title for the opt-in card. Follow-up flow (what to send when you use the OTN token). Messenger only (not available on Instagram). |

---

### 5.2 Live Chat Handoff

| Field | Detail |
|-------|--------|
| **UI name** | Open Conversation / Live Chat |
| **Visual** | Small pill/chip with a headset or person icon. May show "Pause Automation" text. |
| **What it does** | Pauses all automation for this subscriber and flags the conversation for human handoff in the Live Chat panel. An admin can then reply manually. |
| **How to create** | In an Action Step, click "+" > **Pause Automation** (or **Open Live Chat**). Optionally combine with Notify Admins to alert a team member. |
| **Key settings** | Pause duration: indefinite (until manually resumed), or timed (e.g., pause for 30 minutes then resume automation). Conversation appears in the "Open" tab of Live Chat. Combine with "Notify Admins" for immediate alerts. |

---

### 5.3 Comment Reply (Public Comment Response)

| Field | Detail |
|-------|--------|
| **UI name** | Reply to Comment (within Comment Automation trigger) |
| **Visual** | This is not a standalone canvas block. It appears as a text field inside the Instagram Comment Automation Starting Step configuration panel, labeled "Reply to Comment". Shows a text editor with personalization tokens available. |
| **What it does** | Posts a public reply to the comment that triggered the automation. The reply appears as a visible comment under the original post. |
| **How to create** | In the Comment Automation Starting Step > enable "Reply to Comment" toggle. Write the reply text. Supports `{{first_name}}` and other tokens. |
| **Key settings** | Reply text (supports personalization tokens). Multiple reply variations (ManyChat rotates them to appear less bot-like). Enable/disable toggle. Delay before replying (optional). |

---

### 5.4 Private Reply (DM from Comment)

| Field | Detail |
|-------|--------|
| **UI name** | Send Message in Direct (within Comment Automation trigger) |
| **Visual** | This is not a standalone canvas block. It appears as a toggle and message editor inside the Comment Automation Starting Step config, labeled "Send Message in Direct". Below the toggle is a mini flow builder showing the DM content. |
| **What it does** | Sends a private DM to the person who commented. This is the core mechanism for comment-to-DM funnels (e.g., "Comment GUIDE to get the free PDF"). |
| **How to create** | In the Comment Automation Starting Step > enable "Send Message in Direct" toggle. Build the DM content (text, buttons, quick replies, etc.) in the embedded mini-flow editor. |
| **Key settings** | DM message content (full content blocks available: text, image, card, buttons, quick replies). The DM is sent only once per user per post (by default). Delay before sending DM. Only sends if user has not already received the DM from this automation. |

---

## 6. Canvas Navigation and UI Chrome

These are the surrounding UI elements visible in any Flow Builder screenshot.

| Element | Visual Description | Location |
|---------|--------------------|----------|
| **Flow name** | Bold text at top-left of the canvas, editable. | Top bar, left side |
| **Publish button** | Green button labeled "Publish" (or "Update" if already published). | Top bar, right side |
| **Draft / Published badge** | Yellow "Draft" or green "Published" pill next to the flow name. | Top bar, next to flow name |
| **Channel indicator** | Small icon(s) showing which channels the flow uses (Instagram icon, Messenger icon). | Top bar or Starting Step headers |
| **Zoom controls** | "+" and "-" buttons for zooming the canvas. | Bottom-right corner |
| **Minimap** | Small preview of the full flow layout. | Bottom-right corner (toggleable) |
| **Left panel** | List of all steps in the flow, searchable. Drag blocks from here. | Left sidebar |
| **Step settings panel** | Opens on the right when a step is selected. Shows all configuration options. | Right sidebar |
| **Blue connection lines** | Curved lines connecting steps. Solid for standard paths, dashed for "Go to Step" redirects. | Between steps on canvas |
| **Add Step (+) button** | Blue circle with "+" icon. Appears at the end of connection lines or when hovering between steps. | On canvas, at line endpoints |
| **Starting Step area** | Leftmost column of the canvas, outlined with a subtle dashed border. Only trigger cards go here. | Far left of canvas |
| **Step counter** | Small number badge on each step showing its position in the flow. | Top-left corner of each step card |
| **Error indicator** | Red circle with "!" on the corner of a step that has a configuration error (e.g., empty message, missing field). | Top-right corner of broken steps |

---

## 7. Quick Visual ID Cheat Sheet

Use this table to identify any element from a screenshot at a glance.

| What You See | What It Is |
|-------------|------------|
| Blue header card on far left | Starting Step (trigger) |
| White card with text preview | Text block |
| White card with image thumbnail | Image block or Card |
| White card with multiple side-by-side previews | Gallery |
| Row of rounded pills below a message | Quick Replies |
| Rectangular buttons inside a card | Buttons |
| White card with input field icon and field name tag | User Input block |
| Small grey card with stacked colored pills | Action Step (contains action pills) |
| Green pill with "+" and tag name | Add Tag action |
| Red pill with "-" and tag name | Remove Tag action |
| Pill with pencil icon and "field = value" | Set Custom Field action |
| Diamond/branching card with Yes/No paths | Condition block |
| Card with percentage labels and multiple paths | Randomizer block |
| Pill with clock icon | Smart Delay action |
| Pill with curved arrow | Go to Step action |
| Pill with play icon and flow name | Trigger Another Flow action |
| Pill with bell icon | Notify Admins or OTN action |
| Pill with headset icon | Live Chat handoff |
| Pill with cloud/arrow icon | External Request (webhook) |
| Card with bell icon and "Notify Me" button | OTN Request block |
| Blue curved solid line | Standard connection between steps |
| Blue curved dashed line | "Go to Step" redirect connection |
| Green button top-right | Publish / Update button |
| Red circle with "!" on step corner | Configuration error on that step |

---

## 8. Field Types Reference

When identifying Custom Field or User Input blocks in screenshots, these are the available field types.

| Type | Icon Hint | Accepts |
|------|-----------|---------|
| Text | "Abc" or text icon | Any string |
| Number | "#" or number icon | Integers and decimals |
| Date | Calendar icon | Date (YYYY-MM-DD) |
| DateTime | Calendar + clock icon | Date and time |
| Boolean | Toggle/checkbox icon | True / False |
| URL | Link icon | Valid URLs |
| Email | Envelope icon | Valid email addresses |
| Phone | Phone icon | Phone numbers |

---

## 9. Common Flow Patterns (What They Look Like on Canvas)

### Comment-to-DM Funnel
**Canvas shape:** Comment Automation trigger (blue, far left) > Condition checking if keyword matches > Text block with value message > Quick Reply buttons > User Input for email > Action step (tag + set field) > Text block with link/PDF.

### Welcome + Routing
**Canvas shape:** Welcome Message trigger (blue) > Text block greeting > Quick Replies with 3-4 options > each Quick Reply connects to a different branch of steps.

### Lead Qualification
**Canvas shape:** Trigger > Text question > User Input (saves answer) > Condition (checks answer) > Yes path: tag as qualified + send offer > No path: tag as unqualified + different message.

### A/B Test
**Canvas shape:** Trigger > Randomizer (50/50) > Path A: message variant 1 > Path B: message variant 2 > both paths converge at a shared step or end.

### Drip Sequence Enrollment
**Canvas shape:** Trigger > Action step (add tag + subscribe to sequence + set custom field) > Text confirmation message.

---

## 10. Instagram vs Messenger Feature Availability

Not all elements work on both channels. When identifying screenshots, check the channel indicator.

| Element | Instagram | Messenger |
|---------|-----------|-----------|
| Text | Yes | Yes |
| Image | Yes | Yes |
| Card | Yes | Yes |
| Gallery | Yes (max 10) | Yes (max 10) |
| List | No | Yes |
| Audio | Yes | Yes |
| Video | Yes | Yes |
| File | No | Yes |
| Quick Reply | Yes (max 10) | Yes (max 13) |
| Button | Yes (max 3) | Yes (max 3) |
| User Input | Yes | Yes |
| OTN | No | Yes |
| Comment Automation | Yes | No |
| Story Reply | Yes | No |
| Story Mention | Yes | No |
| Keyword | Yes | Yes |
| Ref URL | No | Yes |
| Customer Chat Plugin | No | Yes |
| Buy Button | No | Yes |
| List Block | No | Yes |
