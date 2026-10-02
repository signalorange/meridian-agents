# Page /templates?locale=en — EN (draft, not published)

## SEO

- **URL:** `https://meridian.signalorange.ca/templates?locale=en`  ·  alternate hreflang: `https://meridian.signalorange.ca/templates` (en-CA ↔ fr-CA, x-default = FR)
- **Title (53 chars):** AI agent templates for Meridian: Grok Bot, Muse, Dots
- **Meta description (131 chars):** 9 ready-to-use AI agent templates for Meridian CRM: prospecting, proposals, invoicing, GST/QST. For Grok Bot, Muse and OpenAI Dots.
- **Canonical:** `https://meridian.signalorange.ca/templates?locale=en`
- **Add to sitemap.xml** (both versions) and link from /docs/meridian-api, /docs/ai-assistant-overview and the footer.

---

# AI agent templates for Meridian — Grok Bot, Muse and OpenAI Dots

Connect your personal AI agent to Meridian, the Quebec-built CRM for service businesses, and hand it prospecting, follow-ups, proposals, meetings, projects, bookkeeping and invoicing.

Every template is free, bilingual (French and English) and uses Meridian's official MCP connector (`https://meridian.signalorange.ca/api/meridian/mcp`): your agent acts as you, with your Meridian permissions, and creates, changes or sends nothing without your approval.

Meridian hosts your data in Quebec (OVH Beauharnois, Law 25 and PIPEDA); the external agent follows its own provider’s policy.

## How it works (3 steps)

1. Connect Meridian to your agent: MCP connector + OAuth sign-in with your Meridian account (no key to copy).
2. Pick a template below and import it: "Add to Grok Bot" link, or a copy-paste prompt for Muse and OpenAI Dots.
3. Test with a starter prompt, then turn on the weekly routine if you want.

<a id="prospection"></a>
## Scout — Prospecting and lead qualification

Finds target companies in Quebec, enriches them, checks Meridian for duplicates and prepares client + opportunity records for your approval.

**Who it's for:** Service-business owner, business developer, B2B consultant.

**Connectors:** Meridian (MCP) · Web search / browser (built into the platform)

**Example prompts:**
- "Find 15 accounting firms with 10-50 employees in Montérégie that are not already in my Meridian."
- "Here is my ideal customer: [description]. Remember it and propose 10 prospects this week."
- "Which open opportunities haven't moved in two weeks? Suggest an action for each."

**Suggested routine:** Monday 8:00 AM ET — Research 10 new prospects matching the ICP, check Meridian for duplicates and send me the table to approve. Create nothing without my OK.

*Buttons:* Grok Bot · Muse · OpenAI Dots · Instructions → `grok-bot/prospection.md`, `muse/prospection.md`, `openai-dots/prospection.md`

<a id="approche"></a>
## Messenger — Outreach and follow-ups

Drafts personalized first-touch emails and follow-ups from Meridian records; you review and send.

**Who it's for:** Anyone doing business development who wants consistent follow-ups without writing every email.

**Connectors:** Meridian (MCP) · Gmail or Outlook (read + drafts)

**Example prompts:**
- "Draft a first email for the opportunity "Website redesign — Lavoie Bakery"."
- "Which follow-ups are due today? Draft them."
- "Rewrite this email in French, more direct tone, 80 words max."

**Suggested routine:** Weekdays 8:30 AM ET — List opportunities with a follow-up due (D+3/D+7/D+14, no reply), draft the emails and wait for my approval before anything is sent.

*Buttons:* Grok Bot · Muse · OpenAI Dots · Instructions → `grok-bot/approche.md`, `muse/approche.md`, `openai-dots/approche.md`

<a id="propositions"></a>
## Quill — Proposal writing

Builds a proposal draft from the opportunity, discovery notes and your past proposals, then files it in Meridian once you approve.

**Who it's for:** Agencies, consultants and service firms that send quotes and statements of work.

**Connectors:** Meridian (MCP) · Google Drive / OneDrive (optional, for attachments)

**Example prompts:**
- "Draft a proposal for opportunity #123 modelled on my last won proposal."
- "Summarise the differences between versions 1 and 2 of the "IT audit — Roy Group" proposal."
- "Propose three pricing options (good, better, best) for this engagement."

*Buttons:* Grok Bot · Muse · OpenAI Dots · Instructions → `grok-bot/propositions.md`, `muse/propositions.md`, `openai-dots/propositions.md`

<a id="reunions"></a>
## Scribe — Meetings and transcripts

Preps every client meeting from Meridian and turns the transcript into a summary, decisions and follow-ups filed on the record.

**Who it's for:** Consultants and account managers with back-to-back meetings (Teams, Meet, Zoom).

**Connectors:** Meridian (MCP) · Google Calendar or Outlook/Microsoft 365 (read) · Google Drive / OneDrive (transcripts)

**Example prompts:**
- "Prep me for my 2 PM meeting with Gagnon Construction."
- "Here is the meeting transcript: [text]. Write the notes and propose follow-ups."
- "File these notes on the opportunity and create the agreed tasks."

**Suggested routine:** Weekdays 7:30 AM ET — Check today's calendar; for each external meeting, prepare a one-page brief from Meridian.

*Buttons:* Grok Bot · Muse · OpenAI Dots · Instructions → `grok-bot/reunions.md`, `muse/reunions.md`, `openai-dots/reunions.md`

<a id="projets"></a>
## Foreman — Project management

Tracks your Meridian projects, flags late tasks and produces a clear status report for you or your client.

**Who it's for:** Project managers and owners of agencies, consulting firms or specialized contractors.

**Connectors:** Meridian (MCP) · Gmail or Outlook (status drafts, optional)

**Example prompts:**
- "Which projects are behind this week?"
- "Write the client status report for the "ERP migration" project."
- "Break this phase into tasks and propose due dates."

**Suggested routine:** Friday 3:00 PM ET — Produce the status report for all active projects: delays, next week's deadlines, blockers.

*Buttons:* Grok Bot · Muse · OpenAI Dots · Instructions → `grok-bot/projets.md`, `muse/projets.md`, `openai-dots/projets.md`

<a id="comptabilite"></a>
## Bookkeeper — Expenses, GST/QST and cash

Records and categorizes expenses, prepares GST/QST periods and gives you the income statement and cash position.

**Who it's for:** Quebec small-business owners and self-employed people who keep their books in Meridian (before the outside accountant).

**Connectors:** Meridian (MCP) · Gmail or Outlook (receipts) · Google Drive / OneDrive (supporting documents)

**Example prompts:**
- "Here are 6 September receipts: record them as expenses after showing me the table."
- "How much GST and QST do I owe for the current quarter?"
- "Give me the January-September income statement and my cash position."

**Suggested routine:** 1st of each month, 9:00 AM ET — Find last month's receipts in my email, prepare the expenses to record and summarize accrued GST/QST. Record nothing without my OK.

*Buttons:* Grok Bot · Muse · OpenAI Dots · Instructions → `grok-bot/comptabilite.md`, `muse/comptabilite.md`, `openai-dots/comptabilite.md`

<a id="facturation"></a>
## Collector — Invoicing and collections

Prepares invoices from projects and opportunities, tracks payments and drafts polite reminders for overdue accounts.

**Who it's for:** Service SMBs and freelancers who invoice in Meridian (Stripe).

**Connectors:** Meridian (MCP) · Gmail or Outlook (reminder drafts)

**Example prompts:**
- "Which invoices are overdue and by how much?"
- "Prepare the September invoice for the "Website — Beaulieu Clinic" project."
- "Client Tremblay paid $1,500 by Interac e-Transfer today: record the payment on their invoice."

**Suggested routine:** Tuesday 9:00 AM ET — Review receivables: overdue invoices, aging, total; draft reminders for those without automatic reminders.

*Buttons:* Grok Bot · Muse · OpenAI Dots · Instructions → `grok-bot/facturation.md`, `muse/facturation.md`, `openai-dots/facturation.md`

<a id="suivi-client"></a>
## Guardian Angel — Post-sale client care

Keeps in touch with clients after signature: kickoff check-in, satisfaction follow-up, renewal and referral opportunities.

**Who it's for:** Service firms with recurring engagements (agencies, managed IT, consulting).

**Connectors:** Meridian (MCP) · Gmail or Outlook (drafts) · Google Calendar or Outlook (plan check-ins, as drafts)

**Example prompts:**
- "Which clients haven't heard from us in 60 days?"
- "The "Branding — Côté Cheese Shop" project is done: draft the testimonial request."
- "Turn my clients' 3 most frequent questions into FAQ articles."

**Suggested routine:** Wednesday 10:00 AM ET — List clients due for a touch this week per the care schedule and draft the messages.

*Buttons:* Grok Bot · Muse · OpenAI Dots · Instructions → `grok-bot/suivi-client.md`, `muse/suivi-client.md`, `openai-dots/suivi-client.md`

<a id="rapport-hebdo"></a>
## Lookout — Weekly dashboard

Every Monday, a one-page report: pipeline, proposals, projects, overdue invoices, cash and GST/QST — pulled from Meridian.

**Who it's for:** SMB leaders who want the big picture without opening five screens.

**Connectors:** Meridian (MCP) · None required (optional: Gmail/Outlook to receive the report as a draft)

**Example prompts:**
- "Build my weekly dashboard."
- "Compare this month with last month: revenue, new opportunities, overdue invoices."
- "What are the 3 most urgent decisions this week?"

**Suggested routine:** Monday 7:00 AM ET — Produce the weekly Meridian dashboard and send it to me in this conversation.

*Buttons:* Grok Bot · Muse · OpenAI Dots · Instructions → `grok-bot/rapport-hebdo.md`, `muse/rapport-hebdo.md`, `openai-dots/rapport-hebdo.md`

### Button behaviour (same in every section)

- **Add to Grok Bot** — opens the Grok Bot template link (preview on x.ai → "Add to Grok Bot"). *Link to be generated once the template is published.*
- **Copy for Muse** — copies the Soul.md block + skill prompt (clipboard).
- **Copy for OpenAI Dots** — copies the responsibility message + custom rules.
- **View full instructions** — expands the FR/EN system prompt.

> No tender-watch (SEAO) template is offered: Meridian does not provide that feature today.

## Frequently asked questions

### What is a Meridian agent template?

A ready-to-use bundle — role, instructions, connectors, starter prompts and routine — that teaches an AI agent (Grok Bot, Muse or OpenAI Dots) how to work inside your Meridian CRM.

### How do I connect Meridian to my AI agent?

Add the remote MCP connector https://meridian.signalorange.ca/api/meridian/mcp and sign in with your Meridian account (OAuth). Developers can also use the Meridian REST API with a personal key created in Settings → Integrations.

### Can the agent send emails or change my data without me?

No. The templates require your approval before any write in Meridian and any send. The agent also inherits your Meridian permissions: it cannot do anything you couldn't do yourself.

### Does my data stay in Canada?

Meridian is hosted in Quebec (OVH Beauharnois) and complies with Law 25 and PIPEDA. The external agent (Grok Bot, Muse or Dots) processes the data it reads under its own provider's policy.

### Do the templates handle GST and QST?

Yes. The Bookkeeper template reads Meridian tax periods (accrued GST/QST) and prepares expense entries; closing a period only happens on your request. This is not tax advice.

### How much does it cost?

The templates are free. You need a Meridian account and a subscription to the agent platform you choose (Grok Bot, Muse or ChatGPT with Dots).

### Can I use these templates with Claude or another AI?

Yes: Meridian works with Claude (MCP connector and Claude Skill), and the generic version of the templates (system prompt + tools + prompts) fits any MCP-compatible agent.

---

## JSON-LD

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "SoftwareApplication",
      "@id": "https://meridian.signalorange.ca/#software",
      "name": "Meridian",
      "applicationCategory": "BusinessApplication",
      "applicationSubCategory": "CRM",
      "operatingSystem": "Web",
      "url": "https://meridian.signalorange.ca/",
      "inLanguage": [
        "fr-CA",
        "en-CA"
      ],
      "description": "Canadian CRM software for service businesses: CRM, proposals, invoicing, projects, bookkeeping and AI assistant, with an MCP connector for AI agents.",
      "featureList": [
        "Scout — Prospecting and lead qualification",
        "Messenger — Outreach and follow-ups",
        "Quill — Proposal writing",
        "Scribe — Meetings and transcripts",
        "Foreman — Project management",
        "Bookkeeper — Expenses, GST/QST and cash",
        "Collector — Invoicing and collections",
        "Guardian Angel — Post-sale client care",
        "Lookout — Weekly dashboard"
      ],
      "publisher": {
        "@type": "Organization",
        "name": "SignalOrange Inc.",
        "url": "https://signalorange.ca/"
      },
      "areaServed": {
        "@type": "AdministrativeArea",
        "name": "Québec"
      }
    },
    {
      "@type": "WebPage",
      "@id": "https://meridian.signalorange.ca/templates?locale=en",
      "url": "https://meridian.signalorange.ca/templates?locale=en",
      "name": "AI agent templates for Meridian: Grok Bot, Muse, Dots",
      "description": "9 ready-to-use AI agent templates for Meridian CRM: prospecting, proposals, invoicing, GST/QST. For Grok Bot, Muse and OpenAI Dots.",
      "inLanguage": "en-CA",
      "about": {
        "@id": "https://meridian.signalorange.ca/#software"
      }
    },
    {
      "@type": "HowTo",
      "name": "Connect Meridian to an AI agent",
      "inLanguage": "en-CA",
      "step": [
        {
          "@type": "HowToStep",
          "position": 1,
          "text": "Connect Meridian to your agent: MCP connector + OAuth sign-in with your Meridian account (no key to copy)."
        },
        {
          "@type": "HowToStep",
          "position": 2,
          "text": "Pick a template below and import it: \"Add to Grok Bot\" link, or a copy-paste prompt for Muse and OpenAI Dots."
        },
        {
          "@type": "HowToStep",
          "position": 3,
          "text": "Test with a starter prompt, then turn on the weekly routine if you want."
        }
      ]
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What is a Meridian agent template?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "A ready-to-use bundle — role, instructions, connectors, starter prompts and routine — that teaches an AI agent (Grok Bot, Muse or OpenAI Dots) how to work inside your Meridian CRM."
          }
        },
        {
          "@type": "Question",
          "name": "How do I connect Meridian to my AI agent?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Add the remote MCP connector https://meridian.signalorange.ca/api/meridian/mcp and sign in with your Meridian account (OAuth). Developers can also use the Meridian REST API with a personal key created in Settings → Integrations."
          }
        },
        {
          "@type": "Question",
          "name": "Can the agent send emails or change my data without me?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "No. The templates require your approval before any write in Meridian and any send. The agent also inherits your Meridian permissions: it cannot do anything you couldn't do yourself."
          }
        },
        {
          "@type": "Question",
          "name": "Does my data stay in Canada?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Meridian is hosted in Quebec (OVH Beauharnois) and complies with Law 25 and PIPEDA. The external agent (Grok Bot, Muse or Dots) processes the data it reads under its own provider's policy."
          }
        },
        {
          "@type": "Question",
          "name": "Do the templates handle GST and QST?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Yes. The Bookkeeper template reads Meridian tax periods (accrued GST/QST) and prepares expense entries; closing a period only happens on your request. This is not tax advice."
          }
        },
        {
          "@type": "Question",
          "name": "How much does it cost?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The templates are free. You need a Meridian account and a subscription to the agent platform you choose (Grok Bot, Muse or ChatGPT with Dots)."
          }
        },
        {
          "@type": "Question",
          "name": "Can I use these templates with Claude or another AI?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Yes: Meridian works with Claude (MCP connector and Claude Skill), and the generic version of the templates (system prompt + tools + prompts) fits any MCP-compatible agent."
          }
        }
      ]
    },
    {
      "@type": "ItemList",
      "name": "AI agent templates for Meridian — Grok Bot, Muse and OpenAI Dots",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "name": "Scout — Prospecting and lead qualification",
          "url": "https://meridian.signalorange.ca/templates?locale=en#prospection",
          "description": "Finds target companies in Quebec, enriches them, checks Meridian for duplicates and prepares client + opportunity records for your approval."
        },
        {
          "@type": "ListItem",
          "position": 2,
          "name": "Messenger — Outreach and follow-ups",
          "url": "https://meridian.signalorange.ca/templates?locale=en#approche",
          "description": "Drafts personalized first-touch emails and follow-ups from Meridian records; you review and send."
        },
        {
          "@type": "ListItem",
          "position": 3,
          "name": "Quill — Proposal writing",
          "url": "https://meridian.signalorange.ca/templates?locale=en#propositions",
          "description": "Builds a proposal draft from the opportunity, discovery notes and your past proposals, then files it in Meridian once you approve."
        },
        {
          "@type": "ListItem",
          "position": 4,
          "name": "Scribe — Meetings and transcripts",
          "url": "https://meridian.signalorange.ca/templates?locale=en#reunions",
          "description": "Preps every client meeting from Meridian and turns the transcript into a summary, decisions and follow-ups filed on the record."
        },
        {
          "@type": "ListItem",
          "position": 5,
          "name": "Foreman — Project management",
          "url": "https://meridian.signalorange.ca/templates?locale=en#projets",
          "description": "Tracks your Meridian projects, flags late tasks and produces a clear status report for you or your client."
        },
        {
          "@type": "ListItem",
          "position": 6,
          "name": "Bookkeeper — Expenses, GST/QST and cash",
          "url": "https://meridian.signalorange.ca/templates?locale=en#comptabilite",
          "description": "Records and categorizes expenses, prepares GST/QST periods and gives you the income statement and cash position."
        },
        {
          "@type": "ListItem",
          "position": 7,
          "name": "Collector — Invoicing and collections",
          "url": "https://meridian.signalorange.ca/templates?locale=en#facturation",
          "description": "Prepares invoices from projects and opportunities, tracks payments and drafts polite reminders for overdue accounts."
        },
        {
          "@type": "ListItem",
          "position": 8,
          "name": "Guardian Angel — Post-sale client care",
          "url": "https://meridian.signalorange.ca/templates?locale=en#suivi-client",
          "description": "Keeps in touch with clients after signature: kickoff check-in, satisfaction follow-up, renewal and referral opportunities."
        },
        {
          "@type": "ListItem",
          "position": 9,
          "name": "Lookout — Weekly dashboard",
          "url": "https://meridian.signalorange.ca/templates?locale=en#rapport-hebdo",
          "description": "Every Monday, a one-page report: pipeline, proposals, projects, overdue invoices, cash and GST/QST — pulled from Meridian."
        }
      ]
    }
  ]
}
</script>
```
