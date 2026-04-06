# Platform Visual Elements Guide

How to identify automation platforms from screenshots and understand their visual language.

---

## ManyChat Flow Builder

### Identification Cues
- White canvas background with light gray grid
- Blue accent color throughout (buttons, links, selected states)
- "Flow Builder" tab active in the top navigation
- ManyChat logo (blue chat bubble) in top-left corner
- Left sidebar with flow list; right panel for node editing

### Node Types
- **Message blocks:** Rounded rectangles with white background, thin gray border. Content preview visible inside (text, images, buttons). Blue header bar shows block name.
- **Condition blocks:** Diamond shapes with yellow/orange fill. Two outgoing paths labeled "Yes" and "No."
- **Action blocks:** Smaller rectangles with purple or green accent. Icon indicates action type (tag, field, subscribe).
- **Smart Delay:** Clock icon in a small rounded block. Shows delay duration.
- **Randomizer:** Dice icon block with multiple percentage-labeled outputs.

### Connections
- Blue directional lines with arrow endpoints
- Lines curve smoothly between blocks
- Drag from bottom connector of one block to top connector of next

### Triggers
- Appear at the very top of the flow as a colored banner
- Trigger type shown with icon: keyword, comment, story reply, ref URL
- Green "Starting Step" label on the entry point

### Actions
- Inline within message blocks (buttons that link to next block)
- Standalone action nodes for tagging, setting fields, subscribing to sequences

### Color Coding
- Blue: messages and primary UI
- Yellow/orange: conditions and branching
- Green: starting points and success states
- Purple: actions and integrations
- Red: errors or stop nodes

---

## ManyChat Automation Tab

### Identification Cues
- Simplified card-based layout (not a canvas)
- "Automation" tab active in top navigation
- Each automation is a horizontal card with trigger on left, flow name on right
- Toggle switch on each card (active/inactive)
- No visible connection lines between elements

### Layout
- Vertical list of automation rules
- Each rule shows: trigger type icon, trigger description, arrow, flow name
- Filter bar at top (All, Active, Inactive)
- Bulk actions toolbar when cards are selected

### Triggers Shown
- Small icons: comment icon, DM icon, story icon, keyword icon
- Trigger text displayed inline: "User sends message containing..."
- Platform badge (Instagram, Messenger, WhatsApp) next to trigger

---

## GoHighLevel Workflows

### Identification Cues
- Dark left sidebar with navigation icons (contacts, opportunities, etc.)
- White/light gray canvas area
- "Workflows" section in sidebar or breadcrumb
- Orange/amber accent color for primary actions
- GHL logo or "HighLevel" text in sidebar

### Node Types
- **Trigger cards:** Rounded rectangles at the top with lightning bolt icon. Blue or teal background. Shows trigger type (form submitted, tag added, etc.)
- **Action cards:** White rounded rectangles with left-side colored icon strip. Each shows action name, brief description, and small app icon.
- **If/Else conditions:** Diamond or branching card with green (Yes) and red (No) output paths.
- **Wait steps:** Hourglass icon in a smaller card. Shows duration or event-based wait.
- **Go To:** Arrow icon card that jumps to another point in the workflow.

### Connections
- Thin gray lines connecting cards vertically
- Green lines for "Yes" condition path (left)
- Red lines for "No" condition path (right)
- Plus (+) button between cards to insert steps

### Triggers
- Always the first card in the workflow
- Lightning bolt icon with colored background
- Text describes the trigger event
- One workflow can have multiple triggers stacked at top

### Actions
- Stacked vertically below the trigger
- Each card shows the action type and target
- Common icons: envelope (email), phone (SMS), tag, webhook

### Color Coding
- Teal/blue: triggers
- White with colored icon: actions
- Green: positive condition path
- Red: negative condition path
- Gray: inactive or disabled steps
- Orange: warnings or setup required

---

## n8n

### Identification Cues
- Light gray canvas with subtle dot grid
- Nodes are rounded rectangles with colored header bars
- "n8n" logo in top-left (lowercase, orange)
- Left sidebar with node search panel
- Execution status indicators (green checkmarks, red X) on nodes after running

### Node Types
- **Trigger nodes:** Rounded rectangle with a small play-button triangle in the top-left corner. Colored header matches the integration (e.g., orange for webhook, blue for Telegram).
- **Regular nodes:** Same rounded rectangle shape. Colored header indicates the service. White body shows node name and brief config.
- **Function/Code nodes:** Purple or gray header. Code icon visible.
- **If node:** Yellow header. Two outputs labeled "true" and "false."
- **Switch node:** Yellow header. Multiple labeled outputs.
- **Merge node:** Blue/purple header. Multiple inputs, single output.
- **Set node:** Green header. Used for data transformation.

### Connections
- Gray lines with small circular connectors (pins) on left (input) and right (output) of nodes
- Lines are straight with right-angle bends
- Drag from output pin to input pin
- Multiple outputs shown as stacked pins on the right side

### Triggers
- First node in the workflow (leftmost position)
- Identified by the play-button triangle icon
- Common: Webhook, Schedule, App trigger (e.g., "On new email")

### Actions
- All subsequent nodes after the trigger
- Each node header color corresponds to the app/service
- Node body shows the operation selected (e.g., "Create Row," "Send Message")

### Color Coding
- Orange: webhooks, HTTP requests
- Blue: communication tools (Slack, Telegram, email)
- Green: data/spreadsheet tools (Google Sheets, Airtable)
- Purple: code, function, and utility nodes
- Yellow: logic nodes (If, Switch, Filter)
- Red border: node error after execution
- Green checkmark overlay: node ran successfully

---

## Make.com (formerly Integromat)

### Identification Cues
- White canvas with faint grid
- Modules are circles or large rounded shapes (not rectangles)
- Purple/violet accent color throughout
- "Make" logo in top-left corner
- Scenario toolbar at bottom with play/pause controls

### Node Types
- **Modules:** Large circles with the app icon centered inside. App name below. A small gear/wrench icon appears on hover for settings.
- **Triggers:** Circle with a clock or lightning bolt overlay in top-left. Always the leftmost module.
- **Actions:** Standard circles. The app icon indicates the service.
- **Search modules:** Circle with magnifying glass overlay.
- **Aggregators:** Circle with stacked-lines icon. Collects multiple items into one.
- **Iterators:** Circle with branching-arrows icon. Splits one bundle into many.

### Connections
- Purple/violet directional lines between modules
- Lines are straight or gently curved
- Small filter icon (funnel shape) can appear on a connection line -- click to set conditions
- Dotted lines indicate an inactive or error route

### Triggers
- Leftmost module in the scenario
- Clock icon overlay for scheduled triggers
- Lightning bolt for instant (webhook) triggers
- "Watch" label in module name (e.g., "Watch Emails")

### Actions
- All modules after the trigger
- "Create," "Update," "Send," "Delete" in module names
- Connected left-to-right in execution order

### Branching
- **Router:** A small diamond or split icon that creates multiple paths
- Each path goes to a separate chain of modules
- Filters on router outputs control which path executes
- Filter icon (funnel) on the connection line between router and next module

### Color Coding
- Purple: connections and UI accents
- White: module backgrounds
- App-specific icons are full color inside the circle
- Red glow: module error
- Green glow: module ran successfully
- Gray: disabled module

---

## Zapier

### Identification Cues
- NOT a visual canvas -- it is a vertical step list
- Each step is a card with the app logo on the left
- Orange accent color (Zapier brand)
- "Zap" in the page title or breadcrumb
- Left sidebar with Zap list; main area shows a single Zap's steps

### Step Types
- **Trigger:** First card at the top, labeled "1. Trigger" with app icon and event name. Orange lightning bolt badge.
- **Action:** Subsequent numbered cards (2, 3, 4...). App icon and action name. Blue gear badge.
- **Filter:** Card with a funnel icon. No app logo -- it is a Zapier built-in. Shows conditions as text.
- **Path:** Branching card that splits into multiple lettered paths (Path A, Path B). Each path has its own condition and sub-steps.
- **Formatter:** Zapier icon with text transformation description.
- **Delay:** Clock icon card. Shows duration.

### Connections
- No visible lines -- steps are implicitly connected by their vertical order
- Indentation shows path nesting
- Drag-and-drop reordering by grabbing the step number

### Layout
- Strictly vertical, top to bottom
- Each step card expands on click to show configuration
- Collapsed view shows: step number, app icon, event/action name, status indicator
- "+" button between steps to add new steps

### Color Coding
- Orange: trigger badge and Zapier branding
- Blue: action badges
- Green: step tested successfully
- Red: step has errors
- Gray: step is off or skipped
- Yellow: filter or path conditions

---

## Quick Identification Cheat Sheet

| Visual Cue | Platform |
|---|---|
| Blue rectangular message blocks on white grid | ManyChat Flow Builder |
| Card list with toggle switches, no canvas | ManyChat Automation Tab |
| Dark sidebar, white canvas, green/red condition paths | GoHighLevel Workflows |
| Rounded rectangles with colored headers, dot grid, pin connectors | n8n |
| Circular modules, purple lines, filter funnels | Make.com |
| Vertical numbered step cards, no canvas, orange accents | Zapier |
