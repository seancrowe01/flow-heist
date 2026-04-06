# Manual Airtable Setup

If the `/flow-setup` wizard fails to create tables automatically, follow these steps.

---

## Step 1: Create or open a base

1. Go to [airtable.com](https://airtable.com)
2. Create a new base called "Flow Machine" (or use an existing base)
3. Copy the Base ID from the URL: `https://airtable.com/appXXXXXXXXXXXXXX/...`

---

## Step 2: Create Table 1 -- Flow Library

Create a new table called "Flow Library" with these fields:

| Field Name | Type | Notes |
|------------|------|-------|
| Flow Name | Single line text | |
| Platform | Single select | Options: ManyChat, GoHighLevel, n8n, Make, Zapier, Other |
| Flow Type | Single select | Options: Lead Magnet, Webinar, Sales, Support, Re-engagement, Launch, Quiz, Content Upgrade, Other |
| Source | Single select | Options: Captured, Template, Adapted, Manual |
| Adapted From | Single line text | |
| Trigger Type | Single line text | |
| Trigger Details | Long text | |
| Flow Map | Long text | |
| Rebuild Guide | Long text | |
| Message Count | Number (integer) | |
| Condition Count | Number (integer) | |
| Action Count | Number (integer) | |
| Copy | Long text | |
| Tags Needed | Long text | |
| Custom Fields Needed | Long text | |
| Strategy Notes | Long text | |
| Improvements | Long text | |
| Screenshot URL | URL | |
| Source URL | URL | |
| Rating | Single select | Options: 1, 2, 3, 4, 5 |
| User Tags | Long text | |
| Date Added | Date (ISO) | |
| Last Adapted | Date (ISO) | |

---

## Step 3: Create Table 2 -- Flow Audits

Create a new table called "Flow Audits" with these fields:

| Field Name | Type | Notes |
|------------|------|-------|
| Flow Name | Single line text | |
| Audit Date | Date (ISO) | |
| Platform | Single select | Options: ManyChat, GoHighLevel, n8n, Make, Other |
| Overall Score | Single select | Options: GREEN, YELLOW, RED |
| Dead Ends | Single select | Options: PASS, FAIL |
| Delay Timing | Single select | Options: PASS, FAIL |
| Segmentation | Single select | Options: PASS, FAIL |
| Fallback Handling | Single select | Options: PASS, FAIL |
| Re-engagement | Single select | Options: PASS, FAIL |
| Button Count | Single select | Options: PASS, FAIL |
| Tag Coverage | Single select | Options: PASS, FAIL |
| Compliance | Single select | Options: PASS, FAIL |
| Copy Quality | Single select | Options: PASS, FAIL |
| Measurement | Single select | Options: PASS, FAIL |
| Issues Found | Number (integer) | |
| Fixes | Long text | |
| Notes | Long text | |

---

## Step 4: Create Table 3 -- Capture Log

Create a new table called "Capture Log" with these fields:

| Field Name | Type | Notes |
|------------|------|-------|
| Screenshot File | Single line text | |
| Capture Date | Date (ISO) | |
| Platform Detected | Single line text | |
| Flow Pattern Match | Single line text | |
| Saved to Library | Checkbox | |
| Library Record | Single line text | |
| Notes | Long text | |

---

## Step 5: Get Table IDs

For each table:
1. Open the table in Airtable
2. Copy the table ID from the URL: `https://airtable.com/appXXX/tblXXXXXXXXXXXXXX/...`

---

## Step 6: Update CLAUDE.md

Add the IDs to your CLAUDE.md:

```
## Airtable

| Field | Value |
|-------|-------|
| Base ID | appXXXXXXXXXXXXXX |
| Flow Library Table | tblXXXXXXXXXXXXXX |
| Flow Audits Table | tblXXXXXXXXXXXXXX |
| Capture Log Table | tblXXXXXXXXXXXXXX |
```
