# Muse (Meta) — modèles Meridian / Meridian templates

## FR

### Quel « Muse » ?
**Muse de Meta** — agent IA personnel lancé le 8 septembre 2026 (app Muse, muse.ai, WhatsApp), qui tourne sur une « Muse Secure VM » (ordinateur infonuagique dédié avec navigateur). C'est le « Muse » le plus probable : OpenAI présente Dots comme son concurrent (The Verge, 9to5Google, 29 sept. 2026). Ne pas confondre avec Subtxt « Muse Personas » (écriture de fiction) ni avec Muse Code (agent de code CLI de Meta).

### Format (sources : meta.com/help Muse, about.fb.com/news/2026/09/introducing-muse-personal-ai-agent)
- **Un seul Muse par personne** (pas de personas multiples ni de partage de template documenté). Les « modèles » Meridian sont donc des **rôles/skills qu'on ajoute à son Muse**, pas des agents séparés.
- Personnalité : fichiers **Soul.md** (vérités de base, limites, personnalité, règles de communication), **Identity.md** (nom, « créature », vibe, slogan), **Memory.md** (faits sur l'utilisateur). Modifiables via l'icône Assistant → Identity, ou en le demandant dans la conversation.
- **Connecteurs** : répertoire de connecteurs Meta (Paramètres → Connecteurs). Pour un serveur MCP hors répertoire, on demande **dans la conversation** de créer un *Custom Connector* (URL HTTPS publique, OAuth); Muse le teste et l'enregistre comme **skill réutilisable**. (Sources tierces : sprites.ai/muse/mcp, sealgate.ai/docs/connect-clients/muse, docs.traveler.md/guides/muse — non confirmé par une page officielle Meta lue directement.)
- **Tâches récurrentes** : on les demande en langage naturel (quotidien, hebdo, intervalle); gestion dans l'onglet *Upcoming*.
- **Approbations** : réglages par connecteur dans Paramètres.

### Procédure
1. Coller `connect-meridian.txt` (section FR ou EN) dans une conversation Muse; se connecter à Meridian quand Muse ouvre la page OAuth.
2. Étant donné qu'il n'y a qu'un Muse, ajouter une seule fois le bloc commun de `soul-meridian-base.md` dans Soul.md.
3. Pour chaque rôle voulu, ouvrir le fichier `<id>.md` : ajouter le bloc **Soul.md** (Assistant → Identity → Soul), puis coller le **prompt de skill**, puis (optionnel) le **prompt de tâche récurrente**.

### Fichiers
- `README.md` — ce fichier
- `connect-meridian.txt` — prompt de création du connecteur (FR + EN)
- `soul-meridian-base.md` — bloc Soul.md commun (FR + EN)
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

### Which "Muse"?
**Meta's Muse** — a personal AI agent launched on September 8, 2026 (Muse app, muse.ai, WhatsApp), running on a "Muse Secure VM" (a dedicated cloud computer with its own browser). It's the most likely "Muse": OpenAI positions Dots as its competitor (The Verge, 9to5Google, Sept. 29, 2026). Not to be confused with Subtxt's "Muse Personas" (fiction writing) or Muse Code (Meta's command-line coding agent).

### Format (sources: meta.com/help Muse, about.fb.com/news/2026/09/introducing-muse-personal-ai-agent)
- **One Muse per person** (no multiple personas and no documented template sharing). Meridian "templates" are therefore **roles/skills you add to your Muse**, not separate agents.
- Personality: **Soul.md** (core truths, boundaries, personality, communication rules), **Identity.md** (name, "creature", vibe, tagline) and **Memory.md** (facts about the user) files. Editable from the Assistant icon → Identity, or by asking in the conversation.
- **Connectors**: Meta's connector directory (Settings → Connectors). For an MCP server outside the directory, you ask **in the conversation** for a *Custom Connector* (public HTTPS URL, OAuth); Muse tests it and saves it as a **reusable skill**. (Third-party sources: sprites.ai/muse/mcp, sealgate.ai/docs/connect-clients/muse, docs.traveler.md/guides/muse — not confirmed by an official Meta page read directly.)
- **Recurring tasks**: requested in plain language (daily, weekly, custom interval); managed in the *Upcoming* tab.
- **Approvals**: per-connector settings in Settings.

### Procedure
1. Paste `connect-meridian.txt` (FR or EN section) into a Muse conversation; sign in to Meridian when Muse opens the OAuth page.
2. Since there's only one Muse, add the common block from `soul-meridian-base.md` to Soul.md once.
3. For each role you want, open the `<id>.md` file: add the **Soul.md** block (Assistant → Identity → Soul), then paste the **skill prompt**, then (optional) the **recurring task prompt**.

### Files
- `README.md` — this file
- `connect-meridian.txt` — connector creation prompt (FR + EN)
- `soul-meridian-base.md` — common Soul.md block (FR + EN)
- `prospection.md` — Scout — Prospecting and lead qualification (Éclaireur — Prospection et qualification)
- `approche.md` — Messenger — Outreach and follow-ups (Messager — Approche et relances)
- `propositions.md` — Quill — Proposal writing (Plume — Rédaction de propositions)
- `reunions.md` — Scribe — Meetings and transcripts (Greffier — Réunions et transcriptions)
- `projets.md` — Foreman — Project management (Chef de chantier — Gestion de projets)
- `comptabilite.md` — Bookkeeper — Expenses, GST/QST and cash (Comptable — Dépenses, TPS/TVQ et trésorerie)
- `facturation.md` — Collector — Invoicing and collections (Percepteur — Facturation et recouvrement)
- `suivi-client.md` — Guardian Angel — Post-sale client care (Ange gardien — Suivi client après-vente)
- `rapport-hebdo.md` — Lookout — Weekly dashboard (Vigie — Tableau de bord hebdomadaire)
