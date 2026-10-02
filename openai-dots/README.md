# OpenAI Dots — modèles Meridian / Meridian templates

## FR

### Ce que c'est
**Dots** = agents « toujours actifs » d'OpenAI, annoncés au DevDay le 29 septembre 2026, propulsés par GPT-6 Astra, avec leur propre ordinateur et navigateur infonuagique. On leur parle dans ChatGPT (bureau, Web, mobile), Slack, Teams ou par appel vocal. Offerts aux forfaits Pro (hors EEE/R.-U./Suisse), Business Premium et Enterprise (activé par l'admin). **Un seul dot par compte pour l'instant**; des « specialist dots » sont en pilote entreprise.

### Format (sources : learn.chatgpt.com/docs/dots, learn.chatgpt.com/docs/dots/controls, help.openai.com/en/articles/20001529)
- **Profil** : nom (change le handle, ex. @jacob-alfred), apparence (forme, couleur, yeux, lunettes, accessoires).
- **Instructions** : données dans la conversation (ex. « montre-moi les brouillons avant d'envoyer »). Pas de champ « system prompt » documenté.
- **Custom rules** : Paramètres → Personnalisation → Permissions → Custom rules → *Add* : on décrit l'action et on choisit **Take action without asking / Take action when you say so / Ask before taking action / Hand off to you**.
- **Plugins** : ceux de l'onglet Plugins de ChatGPT (partagés avec ChatGPT, Work, Codex). Un serveur MCP personnalisé s'ajoute via **Developer mode** (Paramètres → Sécurité et connexion → Developer mode, puis Plugins → +, URL du serveur) — voir developers.openai.com/api/docs/mcp et help.openai.com/en/articles/12584461. En Business/Enterprise, l'admin doit activer le mode développeur et publier l'app.
- **Tâches récurrentes** : demandées en langage naturel avec fuseau horaire et durée/date de fin; annulation dans *Scheduled*.
- **Aucun format d'import/export de dot documenté** → chaque fichier donne : profil, message de responsabilité, règles personnalisées, tâche planifiée, requêtes de départ.

### Procédure
1. Connecter Meridian : voir `connect-meridian.md`.
2. Comme il n'y a qu'un dot, choisir le rôle principal (ou combiner plusieurs fichiers) et coller le **message de responsabilité** (section FR ou EN) dans la conversation du dot.
3. Ajouter les **custom rules** listées.
4. Coller la **tâche planifiée** et demander au dot de confirmer l'horaire.

### Fichiers
- `README.md` — ce fichier
- `connect-meridian.md` — connexion de Meridian à ChatGPT / dots (FR + EN)
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

### What it is
**Dots** = OpenAI's "always-on" agents, announced at DevDay on September 29, 2026, powered by GPT-6 Astra, each with its own cloud computer and browser. You talk to them in ChatGPT (desktop, web, mobile), Slack, Teams or by voice call. Available on Pro (outside the EEA/UK/Switzerland), Business Premium and Enterprise (enabled by the admin) plans. **One dot per account for now**; "specialist dots" are in an enterprise pilot.

### Format (sources: learn.chatgpt.com/docs/dots, learn.chatgpt.com/docs/dots/controls, help.openai.com/en/articles/20001529)
- **Profile**: name (changes the handle, e.g. @jacob-alfred), appearance (shape, colour, eyes, glasses, accessories).
- **Instructions**: given in the conversation (e.g. "show me drafts before sending"). No documented "system prompt" field.
- **Custom rules**: Settings → Personalization → Permissions → Custom rules → *Add*: describe the action and choose **Take action without asking / Take action when you say so / Ask before taking action / Hand off to you**.
- **Plugins**: those in ChatGPT's Plugins tab (shared with ChatGPT, Work, Codex). A custom MCP server is added through **Developer mode** (Settings → Security and login → Developer mode, then Plugins → +, server URL) — see developers.openai.com/api/docs/mcp and help.openai.com/en/articles/12584461. On Business/Enterprise, the admin must enable developer mode and publish the app.
- **Recurring tasks**: requested in plain language with a time zone and a duration/end date; cancelled in *Scheduled*.
- **No documented dot import/export format** → each file provides: profile, responsibility message, custom rules, scheduled task, starter prompts.

### Procedure
1. Connect Meridian: see `connect-meridian.md`.
2. Since there's only one dot, pick the main role (or combine several files) and paste the **responsibility message** (FR or EN section) into the dot's conversation.
3. Add the listed **custom rules**.
4. Paste the **scheduled task** and ask the dot to confirm the schedule.

### Files
- `README.md` — this file
- `connect-meridian.md` — connecting Meridian to ChatGPT / dots (FR + EN)
- `prospection.md` — Scout — Prospecting and lead qualification (Éclaireur — Prospection et qualification)
- `approche.md` — Messenger — Outreach and follow-ups (Messager — Approche et relances)
- `propositions.md` — Quill — Proposal writing (Plume — Rédaction de propositions)
- `reunions.md` — Scribe — Meetings and transcripts (Greffier — Réunions et transcriptions)
- `projets.md` — Foreman — Project management (Chef de chantier — Gestion de projets)
- `comptabilite.md` — Bookkeeper — Expenses, GST/QST and cash (Comptable — Dépenses, TPS/TVQ et trésorerie)
- `facturation.md` — Collector — Invoicing and collections (Percepteur — Facturation et recouvrement)
- `suivi-client.md` — Guardian Angel — Post-sale client care (Ange gardien — Suivi client après-vente)
- `rapport-hebdo.md` — Lookout — Weekly dashboard (Vigie — Tableau de bord hebdomadaire)
