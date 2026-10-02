# NOTES — Modèles d'agents Meridian (2026-10-02, 18 h HE)

Rien n'a été publié, envoyé ni ouvert en PR. Tous les fichiers sont des ébauches dans /workspace/seo/templates/.

## Sources Meridian (lues le 2026-10-02 entre 17 h 55 et 18 h HE)
- https://meridian.signalorange.ca/ (accueil), /router, /docs, /llms.txt, /robots.txt, /sitemap.xml, /changelog
- Docs : /docs/meridian-api, /docs/ai-assistant-overview, /docs/crm-leads-ai-scoring, /docs/crm-pipeline-and-stages, /docs/proposals-online-signature, /docs/proposals-templates-and-blocks, /docs/invoicing-stripe-interac, /docs/microsoft-365-integration, /docs/projects-time-tracking, /docs/configuring-your-organization, /router/pricing
- Spec OpenAPI CRM v0.107.4 : https://meridian.signalorange.ca/api/meridian/docs/spec.json (copie : /workspace/seo/raw/meridian-openapi-2026-10-02.json)
- Découverte OAuth : /.well-known/oauth-protected-resource (resource = /api/meridian/mcp) et /.well-known/oauth-authorization-server (authorize/token/register, PKCE S256, scope meridian:full, token auth client_secret_post)
- Sonde : POST /api/meridian/mcp sans jeton → HTTP 401 `WWW-Authenticate: Bearer realm="Meridian API"` (endpoint actif). GET → 404.
- Skill local : /workspace/meridian/SKILL.md

### Confirmé
- MCP distant `https://meridian.signalorange.ca/api/meridian/mcp` (changelog v0.89.0, 9 juin 2026 : JSON-RPC initialize/tools/list/tools/call/ping, OAuth avec enregistrement dynamique; remplace l'extension .mcpb). Mentionné aussi dans /docs/meridian-api pour Claude.
- API REST `/api/meridian/v1/*`, clé personnelle Bearer (Paramètres → Intégrations), hérite des permissions, 300 req/min, jusqu'à 50 clés.
- Endpoints : clients, contacts, opportunities, proposals, projects + tasks, knowledge (soumission = file d'approbation), documents (base64 ≤ 1 Mo), suppliers, finance (invoices, payments, void, expenses, approve, categories, accounts, transactions, transfers, tax_periods + close, income_statement, cash_position, export, CCA/DPA, reimbursements, shareholder_balance), webhooks, issues, products, api_keys.
- Fonctions produit : pipeline Kanban, scoring déterministe + enrichissement IA, propositions avec blocs et signature en ligne, facturation Stripe Connect, relances automatiques et intérêts de retard (changelog), TPS/TVQ (rapport de remise, périodes), Trésorerie, Fournisseurs/Dépenses, suivi du temps, projets (phases/jalons/tâches), Microsoft 365 (agenda, Teams, courriel), agents internes (Skills, Triggers, Weekly Digest, @-mentions), transcriptions de réunions dans le CRM, FAQ publique et `/discover/:org/mcp` (lecture seule publique; ex. /discover/signalorange/mcp répond 200).

### Non confirmé / à vérifier par Jacob
1. **Liste réelle des outils MCP** (noms, schémas) : tools/list exige l'authentification. Le changelog indique que les outils sont générés depuis la spec OpenAPI (OpenApiToTools); les templates citent donc les endpoints REST, pas des noms d'outils.
2. **Transport MCP** : POST JSON-RPC confirmé; support SSE / « streamable HTTP » complet non testé (Muse l'exige selon des sources tierces).
3. **Compatibilité OAuth** avec ChatGPT/Dots, Muse et Grok Bot : Meridian n'annonce que `client_secret_post` (pas `none`, pas CIMD). À tester de bout en bout avant publication.
4. **Réunions / transcriptions** : pas d'endpoint meetings/transcripts dans l'API publique → le modèle Greffier travaille à partir d'une transcription fournie et la classe via /documents.
5. **Temps** : pas d'endpoint time entries dans l'API → les modèles ne saisissent pas de temps.
6. **Pipelines/étapes** : POST /opportunities exige pipeline_id + stage_id; aucun endpoint de liste dédié — supposé lisible via /me (« catalogues et statuts configurés »). À confirmer.
7. **Envoi de courriels** : aucun endpoint d'envoi → brouillons via Gmail/Outlook de la plateforme d'agent.
8. **Incohérences du site** : l'accueil dit « paiements Stripe ou Interac, relances automatiques » et « propositions signées → factures »; la doc facturation dit Interac, relances et conversion proposition→facture « À venir », alors que le changelog annonce les relances automatiques. Interac n'apparaît que comme texte d'instructions de paiement. La page de modèles évite de promettre Interac et la conversion automatique.
9. **Prix de la plateforme Meridian** : pas de page /pricing publique (404); seulement /router/pricing.
10. **Exigence de permissions** exactes (noms) au-delà de l'exemple crm_read/crm_write/proposals_read/proposals_write.
11. **/agents** est une route de l'app (302 → /login) : la page publique proposée est donc **/templates** (404 aujourd'hui, libre).

### Exclu
- **Veille SEAO / appels d'offres / subventions** : aucune mention sur le site, les docs, le changelog ou l'API → pas de modèle.

## Plateformes — sources et confiance
### Grok Bot (SpaceXAI / Cursor) — format CONFIRMÉ
- https://docs.x.ai/grok-bot/bots (profil : nom, libellé, description, avatar; Share → Create template; Public/Team-only; Add to Grok Bot)
- https://docs.x.ai/grok-bot/skills-routines-and-automations (skills, routines, plugins, 50 routines max)
- https://x.ai/bot/guides/templates-for-grok-bot (8 sept. 2026 : templates = instructions + mémoires pertinentes + skills + plugins first-party; **MCP personnalisés et scripts non inclus**)
- Sources tierces (non officielles) : grokbot.dev/news/grok-bot-templates-explained, grokbotemplate.com/learn/what-goes-in-a-grok-bot-template
- Pas de format de fichier d'import : les fichiers grok-bot/*.md servent à créer le Bot puis publier le template depuis l'app.

### Muse — identifié comme **Meta Muse** (confiance élevée), format PARTIELLEMENT confirmé
- https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/ (lancement, Muse Secure VM)
- https://www.meta.com/help/artificial-intelligence/995796179982326/ (nom, personnalité, style, mémoires, avatar/slogan)
- Aide Meta : skills (…/2797651547267109/), connecteurs (…/1687253048996149/), approbations (…/1385290430137537/), tâches planifiées (…/1484325780075655/) — vus dans les résultats de recherche, non ouverts un par un.
- Soul.md / Identity.md / Memory.md et « Custom Connector » MCP en conversation : sources tierces (agent-tune.com/guides/muse-personality, sprites.ai/muse/mcp, sealgate.ai/docs/connect-clients/muse, docs.traveler.md/guides/muse). **Non vérifié sur une page Meta officielle.**
- Un seul Muse par personne, pas de partage de template documenté → modèles livrés comme blocs Soul.md + prompts de skill + tâches récurrentes.
- Écartés : Subtxt « Muse Personas » (fiction), Muse Code (agent CLI de Meta, qui supporte `mcp_servers` — utile pour des devs mais hors sujet).

### OpenAI Dots — format PARTIELLEMENT confirmé
- https://learn.chatgpt.com/docs/dots, https://learn.chatgpt.com/docs/dots/controls, https://help.openai.com/en/articles/20001529-dots-privacy-security-and-safety-faqs
- Presse : 9to5google.com/2026/09/29/openai-dots-agent/, theverge.com (…/openai-dots-launch-muse-competitor), techcrunch.com/2026/09/29/openai-launches-dots-its-bubbly-agentic-avatar/
- MCP personnalisé : https://developers.openai.com/api/docs/mcp, https://help.openai.com/en/articles/12584461 (Developer mode)
- Un seul dot par compte; instructions données en conversation; Custom rules à 4 modes; aucun format d'import/export → modèles livrés comme message de responsabilité + règles + tâche planifiée.
- Non confirmé : disponibilité du Developer mode/MCP personnalisé pour les comptes **Pro** (la doc officielle décrit surtout Business/Enterprise avec admin) et au Canada pour Business Premium (« rolling out worldwide »).

## Format générique
- generic-templates.json : **format générique étiqueté** (prompt système + outils + requêtes), pas un format officiel des trois plateformes.

## Régénération
- Source unique : _src/data.py ; `python3 _src/gen.py && python3 _src/page.py`.

## Bilinguisme (mise à jour 2026-10-02, 18 h 15 HE)
- Tous les fichiers de modèles contiennent une section FR et une section EN (anglais canadien) de même structure, générées depuis `_src/` ; `page-templates-fr.md` et `page-templates-en.md` forment une paire (une langue par page). Vérification de parité : script structurel (titres, puces, étapes numérotées, blocs de code, lignes de tableau, ratio de longueur EN/FR) + recherche de français résiduel dans les sections EN.
- Noms anglais : Éclaireur → Scout, Messager → Messenger, Plume → Quill, Greffier → Scribe, Chef de chantier → Foreman, Comptable → Bookkeeper, Percepteur → Collector, Ange gardien → Guardian Angel, Vigie → Lookout.
- Attention : Meridian a déjà un agent interne mentionné comme « @Scout » dans son changelog (Agents v1.0). Risque de confusion avec le modèle « Scout » ; à valider par Jacob.

---

# NOTES — Meridian agent templates (EN)

Nothing was published, sent or opened as a PR. All files are drafts in /workspace/seo/templates/.

## Meridian sources (read on 2026-10-02 between 5:55 and 6:00 PM ET)
- https://meridian.signalorange.ca/ (home), /router, /docs, /llms.txt, /robots.txt, /sitemap.xml, /changelog
- Docs: /docs/meridian-api, /docs/ai-assistant-overview, /docs/crm-leads-ai-scoring, /docs/crm-pipeline-and-stages, /docs/proposals-online-signature, /docs/proposals-templates-and-blocks, /docs/invoicing-stripe-interac, /docs/microsoft-365-integration, /docs/projects-time-tracking, /docs/configuring-your-organization, /router/pricing
- CRM OpenAPI spec v0.107.4: https://meridian.signalorange.ca/api/meridian/docs/spec.json (copy: /workspace/seo/raw/meridian-openapi-2026-10-02.json)
- OAuth discovery: /.well-known/oauth-protected-resource (resource = /api/meridian/mcp) and /.well-known/oauth-authorization-server (authorize/token/register, PKCE S256, scope meridian:full, token auth client_secret_post)
- Probe: POST /api/meridian/mcp without a token → HTTP 401 `WWW-Authenticate: Bearer realm="Meridian API"` (endpoint is live). GET → 404.
- Local skill: /workspace/meridian/SKILL.md

### Confirmed
- Remote MCP `https://meridian.signalorange.ca/api/meridian/mcp` (changelog v0.89.0, June 9, 2026: JSON-RPC initialize/tools/list/tools/call/ping, OAuth with dynamic registration; replaces the .mcpb extension). Also mentioned in /docs/meridian-api for Claude.
- REST API `/api/meridian/v1/*`, personal Bearer key (Settings → Integrations), inherits permissions, 300 req/min, up to 50 keys.
- Endpoints: clients, contacts, opportunities, proposals, projects + tasks, knowledge (submission = approval queue), documents (base64 ≤ 1 MB), suppliers, finance (invoices, payments, void, expenses, approve, categories, accounts, transactions, transfers, tax_periods + close, income_statement, cash_position, export, CCA classes, reimbursements, shareholder_balance), webhooks, issues, products, api_keys.
- Product features: Kanban pipeline, deterministic scoring + AI enrichment, block-based proposals with online signature, Stripe Connect invoicing, automatic reminders and late interest (changelog), GST/QST (remittance report, periods), Treasury (Trésorerie), Suppliers/Expenses, time tracking, projects (phases/milestones/tasks), Microsoft 365 (calendar, Teams, email), internal agents (Skills, Triggers, Weekly Digest, @-mentions), meeting transcripts in the CRM, public FAQ and `/discover/:org/mcp` (public read-only; e.g. /discover/signalorange/mcp returns 200).

### Unconfirmed / for Jacob to check
1. **Actual MCP tool list** (names, schemas): tools/list requires authentication. The changelog says tools are generated from the OpenAPI spec (OpenApiToTools); the templates therefore cite REST endpoints, not tool names.
2. **MCP transport**: JSON-RPC POST confirmed; full SSE / "streamable HTTP" support not tested (Muse requires it, per third-party sources).
3. **OAuth compatibility** with ChatGPT/Dots, Muse and Grok Bot: Meridian only advertises `client_secret_post` (not `none`, not CIMD). Test end to end before publishing.
4. **Meetings / transcripts**: no meetings/transcripts endpoint in the public API → the Scribe template works from a supplied transcript and files it through /documents.
5. **Time**: no time-entry endpoint in the API → the templates don't log time.
6. **Pipelines/stages**: POST /opportunities requires pipeline_id + stage_id; no dedicated list endpoint — assumed readable through /me ("configured catalogues and statuses"). To be confirmed.
7. **Sending email**: no send endpoint → drafts through the agent platform's Gmail/Outlook.
8. **Site inconsistencies**: the home page says "online payments via Stripe or Interac, automatic reminders" and "signed proposals become invoices"; the invoicing doc lists Interac, reminders and proposal→invoice conversion as "coming soon", while the changelog announces automatic reminders. Interac only appears as payment-instruction text. The templates page avoids promising Interac or automatic conversion.
9. **Meridian platform pricing**: no public /pricing page (404); only /router/pricing.
10. **Exact permission names** beyond the crm_read/crm_write/proposals_read/proposals_write example.
11. **/agents** is an app route (302 → /login): the proposed public page is therefore **/templates** (404 today, available).

### Excluded
- **SEAO / tender / grant watch**: no mention on the site, docs, changelog or API → no template.

## Platforms — sources and confidence
### Grok Bot (SpaceXAI / Cursor) — format CONFIRMED
- https://docs.x.ai/grok-bot/bots (profile: name, label, description, avatar; Share → Create template; Public/Team-only; Add to Grok Bot)
- https://docs.x.ai/grok-bot/skills-routines-and-automations (skills, routines, plugins, 50 routines max)
- https://x.ai/bot/guides/templates-for-grok-bot (Sept. 8, 2026: templates = instructions + relevant memories + skills + first-party plugins; **custom MCP servers and scripts not included**)
- Third-party (unofficial) sources: grokbot.dev/news/grok-bot-templates-explained, grokbotemplate.com/learn/what-goes-in-a-grok-bot-template
- No import file format: the grok-bot/*.md files are used to create the Bot, then publish the template from the app.

### Muse — identified as **Meta Muse** (high confidence), format PARTIALLY confirmed
- https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/ (launch, Muse Secure VM)
- https://www.meta.com/help/artificial-intelligence/995796179982326/ (name, personality, style, memories, avatar/tagline)
- Meta Help: skills (…/2797651547267109/), connectors (…/1687253048996149/), approvals (…/1385290430137537/), scheduled tasks (…/1484325780075655/) — seen in search results, not opened one by one.
- Soul.md / Identity.md / Memory.md and the in-conversation MCP "Custom Connector": third-party sources (agent-tune.com/guides/muse-personality, sprites.ai/muse/mcp, sealgate.ai/docs/connect-clients/muse, docs.traveler.md/guides/muse). **Not verified on an official Meta page.**
- One Muse per person, no documented template sharing → templates delivered as Soul.md blocks + skill prompts + recurring tasks.
- Ruled out: Subtxt "Muse Personas" (fiction), Muse Code (Meta's CLI agent, which supports `mcp_servers` — useful for developers but out of scope).

### OpenAI Dots — format PARTIALLY confirmed
- https://learn.chatgpt.com/docs/dots, https://learn.chatgpt.com/docs/dots/controls, https://help.openai.com/en/articles/20001529-dots-privacy-security-and-safety-faqs
- Press: 9to5google.com/2026/09/29/openai-dots-agent/, theverge.com (…/openai-dots-launch-muse-competitor), techcrunch.com/2026/09/29/openai-launches-dots-its-bubbly-agentic-avatar/
- Custom MCP: https://developers.openai.com/api/docs/mcp, https://help.openai.com/en/articles/12584461 (Developer mode)
- One dot per account; instructions given in conversation; 4-mode custom rules; no import/export format → templates delivered as a responsibility message + rules + scheduled task.
- Unconfirmed: Developer mode / custom MCP availability for **Pro** accounts (official docs mostly describe Business/Enterprise with an admin), and Business Premium availability in Canada ("rolling out worldwide").

## Generic format
- generic-templates.json: **labelled generic format** (system prompt + tools + starter prompts), not an official format of the three platforms.

## Bilingual update (2026-10-02, 6:15 PM ET)
- Every template file contains a FR section and an EN (Canadian English) section with the same structure, generated from `_src/`; `page-templates-fr.md` and `page-templates-en.md` are a pair (one language per page). Parity check: structural script (headings, bullets, numbered steps, code blocks, table rows, EN/FR length ratio) + search for leftover French in EN sections.
- English names: Éclaireur → Scout, Messager → Messenger, Plume → Quill, Greffier → Scribe, Chef de chantier → Foreman, Comptable → Bookkeeper, Percepteur → Collector, Ange gardien → Guardian Angel, Vigie → Lookout.
- Caution: Meridian already has an internal agent referred to as "@Scout" in its changelog (Agents v1.0). Possible confusion with the "Scout" template; Jacob to confirm.

## Regeneration
- Single source: _src/data.py; `python3 _src/gen.py && python3 _src/page.py`.
