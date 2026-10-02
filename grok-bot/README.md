# Grok Bot — modèles Meridian / Meridian templates

## FR

### Format confirmé (sources : docs.x.ai/grok-bot/bots, docs.x.ai/grok-bot/skills-routines-and-automations, x.ai/bot/guides/templates-for-grok-bot)
Un **Bot** = nom, libellé (label), description (règles durables), avatar, conversation, **skills** (instructions réutilisables), **routines** (déclencheurs planifiés ou par événement), **plugins/connecteurs** et **mémoires**.
Un **template** se crée depuis un Bot existant : menu *Share → Create template* ; le Bot s'empaquette lui-même (instructions, mémoires pertinentes, skills, routines, références aux plugins first-party). Lien *Public* ou *Team-only*. Le destinataire ouvre l'aperçu sur x.ai puis *Add to Grok Bot*.
**Il n'existe pas de fichier d'import documenté** : on ne peut pas téléverser ces fichiers ; on crée le Bot (coller le « prompt de création »), on le teste, puis on publie le template.

**Important pour Meridian :** les serveurs MCP personnalisés, scripts, clés API et identifiants **ne sont pas inclus** dans un template. Chaque fichier contient donc une section *Instructions d'installation* que le Bot doit encoder dans son template (le guide officiel recommande « tell the bot to encode instructions for setup »).

### Procédure (Jacob)
1. Grok Bot → New → Create new Bot. Coller le bloc « Prompt de création » du fichier voulu (section FR ou EN).
2. Connecter Meridian (MCP `https://meridian.signalorange.ca/api/meridian/mcp`, OAuth) et les plugins listés (Gmail, Google Agenda, etc.). Tester les requêtes de départ.
3. Retirer toute donnée client et toute mémoire personnelle, puis *Share → Create template* → *View template details* → vérifier → *Public link*.
4. Coller le lien sur la page /templates (bouton « Ajouter à Grok Bot »).
5. Pour une version anglaise distincte, créer un second Bot à partir de la section EN et publier un second template (lien pour /templates?locale=en).

### Fichiers
- `README.md` — ce fichier
- `prospection.md` — Éclaireur — Prospection et qualification (Scout — Prospecting and lead qualification)
- `approche.md` — Messager — Approche et relances (Messenger — Outreach and follow-ups)
- `propositions.md` — Plume — Rédaction de propositions (Quill — Proposal writing)
- `reunions.md` — Greffier — Réunions et transcriptions (Scribe — Meetings and transcripts)
- `projets.md` — Chef de chantier — Gestion de projets (Foreman — Project management)
- `comptabilite.md` — Comptable — Dépenses, TPS/TVQ et trésorerie (Bookkeeper — Expenses, GST/QST and cash)
- `facturation.md` — Percepteur — Facturation et recouvrement (Collector — Invoicing and collections)
- `suivi-client.md` — Ange gardien — Suivi client après-vente (Guardian Angel — Post-sale client care)
- `rapport-hebdo.md` — Vigie — Tableau de bord hebdomadaire (Lookout — Weekly dashboard)

---

## EN

### Confirmed format (sources: docs.x.ai/grok-bot/bots, docs.x.ai/grok-bot/skills-routines-and-automations, x.ai/bot/guides/templates-for-grok-bot)
A **Bot** = name, label, description (durable rules), avatar, conversation, **skills** (reusable instructions), **routines** (scheduled or event-based triggers), **plugins/connectors** and **memories**.
A **template** is created from an existing Bot: *Share → Create template* menu; the Bot packages itself (instructions, relevant memories, skills, routines, references to first-party plugins). *Public* or *Team-only* link. The recipient opens the preview on x.ai, then *Add to Grok Bot*.
**There is no documented import file**: these files can't be uploaded; you create the Bot (paste the "creation prompt"), test it, then publish the template.

**Important for Meridian:** custom MCP servers, scripts, API keys and credentials are **not included** in a template. Each file therefore contains a *Setup instructions* section that the Bot must encode in its template (the official guide recommends "tell the bot to encode instructions for setup").

### Procedure (Jacob)
1. Grok Bot → New → Create new Bot. Paste the "Creation prompt" block from the file you want (FR or EN section).
2. Connect Meridian (MCP `https://meridian.signalorange.ca/api/meridian/mcp`, OAuth) and the listed plugins (Gmail, Google Calendar, etc.). Test the starter prompts.
3. Remove any client data and personal memories, then *Share → Create template* → *View template details* → review → *Public link*.
4. Paste the link on the /templates page ("Add to Grok Bot" button).
5. For a separate English version, create a second Bot from the EN section and publish a second template (link for /templates?locale=en).

### Files
- `README.md` — this file
- `prospection.md` — Scout — Prospecting and lead qualification (Éclaireur — Prospection et qualification)
- `approche.md` — Messenger — Outreach and follow-ups (Messager — Approche et relances)
- `propositions.md` — Quill — Proposal writing (Plume — Rédaction de propositions)
- `reunions.md` — Scribe — Meetings and transcripts (Greffier — Réunions et transcriptions)
- `projets.md` — Foreman — Project management (Chef de chantier — Gestion de projets)
- `comptabilite.md` — Bookkeeper — Expenses, GST/QST and cash (Comptable — Dépenses, TPS/TVQ et trésorerie)
- `facturation.md` — Collector — Invoicing and collections (Percepteur — Facturation et recouvrement)
- `suivi-client.md` — Guardian Angel — Post-sale client care (Ange gardien — Suivi client après-vente)
- `rapport-hebdo.md` — Lookout — Weekly dashboard (Vigie — Tableau de bord hebdomadaire)
