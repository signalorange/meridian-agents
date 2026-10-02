# Meridian Agents

**[Français](#français) · [English](#english)**

---

## Français

Modèles d'agents IA (personas) prêts à l'emploi pour utiliser **[Meridian](https://meridian.signalorange.ca)** — CRM, prospection, propositions, réunions, gestion de projets et comptabilité — dans **Grok Bot**, **Muse (Meta)** et **OpenAI Dots**. Tous les modèles sont bilingues (FR/EN).

### Les 9 modèles

| Fichier | Français | English |
|---|---|---|
| `prospection.md` | Éclaireur — Prospection et qualification | Scout — Prospecting and lead qualification |
| `approche.md` | Messager — Approche et relances | Messenger — Outreach and follow-ups |
| `propositions.md` | Plume — Rédaction de propositions | Quill — Proposal writing |
| `reunions.md` | Greffier — Réunions et transcriptions | Scribe — Meetings and transcripts |
| `projets.md` | Chef de chantier — Gestion de projets | Foreman — Project management |
| `comptabilite.md` | Comptable — Dépenses, TPS/TVQ et trésorerie | Bookkeeper — Expenses, GST/QST and cash |
| `facturation.md` | Percepteur — Facturation et recouvrement | Collector — Invoicing and collections |
| `suivi-client.md` | Ange gardien — Suivi client après-vente | Guardian Angel — Post-sale client care |
| `rapport-hebdo.md` | Vigie — Tableau de bord hebdomadaire | Lookout — Weekly dashboard |

### Par plateforme

- **[Grok Bot](grok-bot/README.md)** — créez un Bot en collant le « prompt de création » d'un fichier, connectez Meridian, testez, puis publiez-le comme template (*Share → Create template*).
- **[Muse (Meta)](muse/README.md)** — collez `muse/connect-meridian.txt` pour créer le connecteur, ajoutez `muse/soul-meridian-base.md` à Soul.md, puis ajoutez les rôles voulus comme skills.
- **[OpenAI Dots](openai-dots/README.md)** — connectez Meridian (voir `openai-dots/connect-meridian.md`), collez le message de responsabilité du rôle, ajoutez les règles personnalisées et la tâche planifiée.

### Connexion à Meridian

Point de terminaison MCP : `https://meridian.signalorange.ca/api/meridian/mcp` (OAuth, connexion avec un compte Meridian). Aucune clé ni donnée client n'est incluse dans ce dépôt.

### Autres fichiers

- `templates.md` — vue d'ensemble des modèles
- `page-templates-fr.md`, `page-templates-en.md` — contenu de la page /templates de Meridian
- `llms-additions.txt` — ajouts proposés pour `llms.txt`
- `generic-templates.json` — modèles en format structuré
- `_src/` — scripts Python qui génèrent les fichiers

### Licence

À déterminer.

---

## English

Ready-to-use AI agent templates (personas) for using **[Meridian](https://meridian.signalorange.ca)** — CRM, prospecting, proposals, meetings, project management and bookkeeping — in **Grok Bot**, **Muse (Meta)** and **OpenAI Dots**. Every template is bilingual (FR/EN).

### The 9 templates

| File | English | Français |
|---|---|---|
| `prospection.md` | Scout — Prospecting and lead qualification | Éclaireur — Prospection et qualification |
| `approche.md` | Messenger — Outreach and follow-ups | Messager — Approche et relances |
| `propositions.md` | Quill — Proposal writing | Plume — Rédaction de propositions |
| `reunions.md` | Scribe — Meetings and transcripts | Greffier — Réunions et transcriptions |
| `projets.md` | Foreman — Project management | Chef de chantier — Gestion de projets |
| `comptabilite.md` | Bookkeeper — Expenses, GST/QST and cash | Comptable — Dépenses, TPS/TVQ et trésorerie |
| `facturation.md` | Collector — Invoicing and collections | Percepteur — Facturation et recouvrement |
| `suivi-client.md` | Guardian Angel — Post-sale client care | Ange gardien — Suivi client après-vente |
| `rapport-hebdo.md` | Lookout — Weekly dashboard | Vigie — Tableau de bord hebdomadaire |

### By platform

- **[Grok Bot](grok-bot/README.md)** — create a Bot by pasting a file's "creation prompt", connect Meridian, test it, then publish it as a template (*Share → Create template*).
- **[Muse (Meta)](muse/README.md)** — paste `muse/connect-meridian.txt` to create the connector, add `muse/soul-meridian-base.md` to Soul.md, then add the roles you want as skills.
- **[OpenAI Dots](openai-dots/README.md)** — connect Meridian (see `openai-dots/connect-meridian.md`), paste the role's responsibility message, then add the custom rules and the scheduled task.

### Connecting to Meridian

MCP endpoint: `https://meridian.signalorange.ca/api/meridian/mcp` (OAuth, sign in with a Meridian account). No keys or client data are included in this repository.

### Other files

- `templates.md` — overview of the templates
- `page-templates-fr.md`, `page-templates-en.md` — content for Meridian's /templates page
- `llms-additions.txt` — proposed additions to `llms.txt`
- `generic-templates.json` — templates in structured form
- `_src/` — Python scripts that generate the files

### License

To be decided.
