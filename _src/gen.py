# -*- coding: utf-8 -*-
# Generates every bilingual (FR + EN, Canadian English) file in /workspace/seo/templates/ from data.py.
import os, json, sys
sys.path.insert(0, os.path.dirname(__file__))
from data import *
OUT = "/workspace/seo/templates"
def en_ops(s):
    for a,b in [("(avec confirmation)","(with confirmation)"),("(sur demande)","(on request)"),("(file d'approbation)","(approval queue)"),("(base de connaissances)","(knowledge base)"),("≤ 1 Mo","≤ 1 MB"),("(DPA)","(CCA)")]: s=s.replace(a,b)
    return s
def w(path, txt):
    p=os.path.join(OUT,path); os.makedirs(os.path.dirname(p),exist_ok=True); open(p,"w").write(txt.rstrip()+"\n")
def bullets(xs): return "\n".join(f"- {x}" for x in xs)
def nums(xs): return "\n".join(f"{i}. {x}" for i,x in enumerate(xs,1))
def short(t,lang): return t[f'{lang}_name'].split(" — ")[0]
def other(lang): return "en" if lang=="fr" else "fr"
def name_line(t,lang):
    # Each section names the agent in its own language and gives the other-language name too.
    return (f"{short(t,'fr')} (nom anglais : {short(t,'en')})" if lang=="fr" else f"{short(t,'en')} (French name: {short(t,'fr')})")
def conn(t,lang):
    m = (f"Meridian — connecteur MCP distant `{MCP_URL}` (OAuth, compte Meridian) **ou** API REST `{API_BASE}` avec `Authorization: Bearer $MERIDIAN_API_KEY` (Paramètres → Intégrations)" if lang=="fr"
         else f"Meridian — remote MCP connector `{MCP_URL}` (OAuth, Meridian account) **or** REST API `{API_BASE}` with `Authorization: Bearer $MERIDIAN_API_KEY` (Settings → Integrations)")
    return [m]+t[f"connectors_extra_{lang}"]
def ops(t,lang): return t["meridian_ops"] if lang=="fr" else [en_ops(o) for o in t["meridian_ops"]]
def instructions(t,lang):
    fr = lang=="fr"
    h = ("Méthode","Opérations Meridian utilisées","Règles non négociables") if fr else ("Method","Meridian operations used","Non-negotiable rules")
    return f"{t[f'{lang}_role']}\n\n## {h[0]}\n{nums(t[f'{lang}_steps'])}\n\n## {h[1]}\n{bullets(ops(t,lang))}\n\n## {h[2]}\n{bullets(COMMON_RULES_FR if fr else COMMON_RULES_EN)}"
def q(s,lang): return f"« {s} »" if lang=="fr" else f"\"{s}\""
def file_list(lang, extra):
    return "\n".join(extra + [f"- `{t['id']}.md` — {t[f'{lang}_name']} ({t[f'{other(lang)}_name']})" for t in T])

# ======================= templates.md (master) =======================
HDR = {
"fr": [f"Version : 2026-10-02 · Plateformes : Grok Bot, Muse (Meta), OpenAI Dots · Langues : français (principal) + anglais canadien", "",
"> Ébauche interne — non publiée. Les fonctionnalités citées proviennent du site public, des docs, du changelog et de la spec OpenAPI de Meridian (v0.107.4) au 2026-10-02. Voir NOTES.md pour les sources et les inconnues.", "",
"### Connexion Meridian commune", "",
f"- **MCP distant (recommandé)** : `{MCP_URL}` — OAuth 2.1 + PKCE, enregistrement dynamique de client, portée `meridian:full`. Découverte : `{SITE}/.well-known/oauth-protected-resource`.",
f"- **API REST (repli)** : `{API_BASE}/*`, en-tête `Authorization: Bearer $MERIDIAN_API_KEY`. Clé personnelle (Paramètres → Intégrations), hérite des rôles de l'utilisateur, 300 req/min. Spec : `{SITE}/api/meridian/docs/spec.json`.",
"- Premier appel : `GET /me` → `permissions`. Toute écriture exige la confirmation de l'utilisateur.", "",
"### Index", ""] ,
"en": [f"Version: 2026-10-02 · Platforms: Grok Bot, Muse (Meta), OpenAI Dots · Languages: French (primary) + Canadian English", "",
"> Internal draft — not published. The features cited come from Meridian's public site, docs, changelog and OpenAPI spec (v0.107.4) as of 2026-10-02. See NOTES.md for sources and unknowns.", "",
"### Common Meridian connection", "",
f"- **Remote MCP (recommended)**: `{MCP_URL}` — OAuth 2.1 + PKCE, dynamic client registration, scope `meridian:full`. Discovery: `{SITE}/.well-known/oauth-protected-resource`.",
f"- **REST API (fallback)**: `{API_BASE}/*`, header `Authorization: Bearer $MERIDIAN_API_KEY`. Personal key (Settings → Integrations), inherits the user's roles, 300 req/min. Spec: `{SITE}/api/meridian/docs/spec.json`.",
"- First call: `GET /me` → `permissions`. Every write requires the user's confirmation.", "",
"### Index", ""]}
EXCL = {"fr":"**Exclu volontairement :** veille d'appels d'offres et de subventions (SEAO). Aucune fonction, intégration ni endpoint SEAO n'existe sur le site, dans les docs ou dans l'API de Meridian (vérifié le 2026-10-02). À ajouter seulement si Meridian livre une telle fonction.",
        "en":"**Deliberately excluded:** tender and grant watch (SEAO). No SEAO feature, integration or endpoint exists on Meridian's site, docs or API (checked 2026-10-02). Add it only if Meridian ships such a feature."}
md = ["# Modèles d'agents Meridian / Meridian agent templates", ""]
for lang,title in (("fr","## Présentation (FR)"),("en","## Overview (EN)")):
    md += [title, ""] + HDR[lang]
    md += [f"{i}. [{t[f'{lang}_name']}](#{t['id']}) — {t[f'{other(lang)}_name']}" for i,t in enumerate(T,1)]
    md += ["", EXCL[lang], ""]
for i,t in enumerate(T,1):
    md += ["---", "", f'<a id="{t["id"]}"></a>', f"## {i}. {t['fr_name']} / {t['en_name']}", ""]
    for lang in ("fr","en"):
        fr = lang=="fr"
        L = (("Nom","Description","Pour qui","Connecteurs requis","Instructions système / persona","Requêtes de départ","Routine suggérée") if fr else
             ("Name","Description","Who it's for","Required connectors","System instructions / persona","Starter prompts","Suggested routine"))
        md += [f"### {lang.upper()}", "", f"**{L[0]} :** {name_line(t,lang)}" if fr else f"**{L[0]}:** {name_line(t,lang)}", "",
               (f"**{L[1]} :** " if fr else f"**{L[1]}:** ")+t[f'{lang}_desc'], "", (f"**{L[2]} :** " if fr else f"**{L[2]}:** ")+t[f'{lang}_target'], "",
               (f"**{L[3]} :**" if fr else f"**{L[3]}:**"), bullets(conn(t,lang)), "", (f"**{L[4]} :**" if fr else f"**{L[4]}:**"), "", "```text", instructions(t,lang), "```", "",
               (f"**{L[5]} :**" if fr else f"**{L[5]}:**"), bullets(t[f'{lang}_prompts']), ""]
        r = t[f'{lang}_routine']
        md += [((f"**{L[6]} :** " if fr else f"**{L[6]}:** ") + (f"{r[0]} — {q(r[1],lang)}" if r else ("aucune — travail à la demande." if fr else "none — works on demand."))), ""]
w("templates.md","\n".join(md))

# ======================= generic JSON =======================
gen = {"_label":"GENERIC FORMAT — not an official import format of Grok Bot, Muse or Dots. System prompt + tools + starter prompts, for any agent platform.",
       "_label_fr":"FORMAT GÉNÉRIQUE — pas un format d'import officiel de Grok Bot, Muse ou Dots. Prompt système + outils + requêtes de départ, pour toute plateforme d'agent.",
       "version":"2026-10-02",
       "meridian":{"mcp_url":MCP_URL,"mcp_auth":"OAuth 2.1 (PKCE, dynamic client registration, scope meridian:full)","mcp_auth_fr":"OAuth 2.1 (PKCE, enregistrement dynamique de client, portée meridian:full)",
                   "rest_base":API_BASE,"rest_auth":"Authorization: Bearer $MERIDIAN_API_KEY","openapi":SITE+"/api/meridian/docs/spec.json"},
       "templates":[]}
for t in T:
    for lang in ("fr","en"):
        r=t[f'{lang}_routine']
        gen["templates"].append({"id":f"meridian-{t['id']}-{lang}","lang":lang,"name":t[f'{lang}_name'],"short_name":short(t,lang),
          "name_other_language":t[f'{other(lang)}_name'],"description":t[f'{lang}_desc'],"target_user":t[f'{lang}_target'],
          "system_prompt":instructions(t,lang),"tools":conn(t,lang),"meridian_operations":ops(t,lang),
          "starter_prompts":t[f'{lang}_prompts'],"routine":({"schedule":r[0],"prompt":r[1]} if r else None)})
w("generic-templates.json", json.dumps(gen, ensure_ascii=False, indent=2))

# ======================= Grok Bot =======================
GROK_README = {
"fr": f"""## FR

### Format confirmé (sources : docs.x.ai/grok-bot/bots, docs.x.ai/grok-bot/skills-routines-and-automations, x.ai/bot/guides/templates-for-grok-bot)
Un **Bot** = nom, libellé (label), description (règles durables), avatar, conversation, **skills** (instructions réutilisables), **routines** (déclencheurs planifiés ou par événement), **plugins/connecteurs** et **mémoires**.
Un **template** se crée depuis un Bot existant : menu *Share → Create template* ; le Bot s'empaquette lui-même (instructions, mémoires pertinentes, skills, routines, références aux plugins first-party). Lien *Public* ou *Team-only*. Le destinataire ouvre l'aperçu sur x.ai puis *Add to Grok Bot*.
**Il n'existe pas de fichier d'import documenté** : on ne peut pas téléverser ces fichiers ; on crée le Bot (coller le « prompt de création »), on le teste, puis on publie le template.

**Important pour Meridian :** les serveurs MCP personnalisés, scripts, clés API et identifiants **ne sont pas inclus** dans un template. Chaque fichier contient donc une section *Instructions d'installation* que le Bot doit encoder dans son template (le guide officiel recommande « tell the bot to encode instructions for setup »).

### Procédure (Jacob)
1. Grok Bot → New → Create new Bot. Coller le bloc « Prompt de création » du fichier voulu (section FR ou EN).
2. Connecter Meridian (MCP `{MCP_URL}`, OAuth) et les plugins listés (Gmail, Google Agenda, etc.). Tester les requêtes de départ.
3. Retirer toute donnée client et toute mémoire personnelle, puis *Share → Create template* → *View template details* → vérifier → *Public link*.
4. Coller le lien sur la page /templates (bouton « Ajouter à Grok Bot »).
5. Pour une version anglaise distincte, créer un second Bot à partir de la section EN et publier un second template (lien pour /templates?locale=en).

### Fichiers
""",
"en": f"""## EN

### Confirmed format (sources: docs.x.ai/grok-bot/bots, docs.x.ai/grok-bot/skills-routines-and-automations, x.ai/bot/guides/templates-for-grok-bot)
A **Bot** = name, label, description (durable rules), avatar, conversation, **skills** (reusable instructions), **routines** (scheduled or event-based triggers), **plugins/connectors** and **memories**.
A **template** is created from an existing Bot: *Share → Create template* menu; the Bot packages itself (instructions, relevant memories, skills, routines, references to first-party plugins). *Public* or *Team-only* link. The recipient opens the preview on x.ai, then *Add to Grok Bot*.
**There is no documented import file**: these files can't be uploaded; you create the Bot (paste the "creation prompt"), test it, then publish the template.

**Important for Meridian:** custom MCP servers, scripts, API keys and credentials are **not included** in a template. Each file therefore contains a *Setup instructions* section that the Bot must encode in its template (the official guide recommends "tell the bot to encode instructions for setup").

### Procedure (Jacob)
1. Grok Bot → New → Create new Bot. Paste the "Creation prompt" block from the file you want (FR or EN section).
2. Connect Meridian (MCP `{MCP_URL}`, OAuth) and the listed plugins (Gmail, Google Calendar, etc.). Test the starter prompts.
3. Remove any client data and personal memories, then *Share → Create template* → *View template details* → review → *Public link*.
4. Paste the link on the /templates page ("Add to Grok Bot" button).
5. For a separate English version, create a second Bot from the EN section and publish a second template (link for /templates?locale=en).

### Files
"""}
w("grok-bot/README.md", "# Grok Bot — modèles Meridian / Meridian templates\n\n" + GROK_README["fr"] + file_list("fr",["- `README.md` — ce fichier"]) + "\n\n---\n\n" + GROK_README["en"] + file_list("en",["- `README.md` — this file"]))
for t in T:
    blocks=[]
    for lang in ("fr","en"):
        fr = lang=="fr"; s=short(t,lang)
        desc_rules = ("Toujours lire Meridian avant d'écrire; aucune écriture ni aucun envoi sans approbation explicite; aucune clé API dans la conversation; français québécois par défaut, anglais sur demande." if fr else
                      "Always read Meridian before writing; no write and no send without explicit approval; never paste API keys in the chat; Quebec French by default, English on request.")
        skill_name = f"meridian-{t['id']}"; routine = t[f'{lang}_routine']
        extra = ', '.join(t[f'connectors_extra_{lang}'])
        setup = (f"""1. Installe/active les plugins : {extra}.
2. Ajoute Meridian comme connecteur MCP personnalisé : URL `{MCP_URL}`, transport HTTP, authentification OAuth (connexion avec ton compte Meridian, portée `meridian:full`). Si ton client MCP ne gère pas OAuth : crée une clé dans Meridian → Paramètres → Intégrations → « + Nouvelle clé API », et fournis-la via le gestionnaire de secrets du Bot (jamais dans le chat) comme `MERIDIAN_API_KEY`, base `{API_BASE}`.
3. Test : « Appelle `me` dans Meridian et dis-moi mon organisation et mes permissions. »""" if fr else
f"""1. Install/enable the plugins: {extra}.
2. Add Meridian as a custom MCP connector: URL `{MCP_URL}`, HTTP transport, OAuth authentication (sign in with your Meridian account, scope `meridian:full`). If your MCP client can't handle OAuth: create a key in Meridian → Settings → Integrations → "+ New API key", and provide it through the Bot's secret store (never in the chat) as `MERIDIAN_API_KEY`, base `{API_BASE}`.
3. Test: "Call `me` in Meridian and tell me my organization and permissions.\"""")
        memories = (["Meridian est la source de vérité pour clients, opportunités, propositions, projets et finances.","Les montants sont en $ CA; taxes TPS (5 %) et TVQ (9,975 %) au Québec.","POST /knowledge entre en file d'approbation : dire « article mis en file pour approbation », jamais « publié »."] if fr else
                    ["Meridian is the source of truth for clients, opportunities, proposals, projects and finances.","Amounts are in CAD; GST (5%) and QST (9.975%) apply in Quebec.","POST /knowledge enters an approval queue: say \"article queued for approval\", never \"published\"."])
        H = (("Profil","Nom","Libellé","Description (règles durables)","Instructions","Skill","Routine","Plugins / connecteurs","Mémoires partageables (non personnelles)","Instructions d'installation (à encoder dans le template)","Requêtes de départ","Prompt de création (coller dans un nouveau Bot)","Aucune routine par défaut — ce Bot travaille à la demande.")
             if fr else ("Profile","Name","Label","Description (durable rules)","Instructions","Skill","Routine","Plugins / connectors","Shareable memories (non-personal)","Setup instructions (to encode in the template)","Starter prompts","Creation prompt (paste into a new Bot)","No default routine — this Bot works on demand."))
        sep = " :" if fr else ":"
        creation = (f"Tu es maintenant le Bot « {s} ». Mets ton profil à jour : nom « {s} », libellé « Meridian », description : « {t['fr_desc']} {desc_rules} ». Crée un skill nommé `{skill_name}` avec les instructions ci-dessus (section Skill)" + (f", puis une routine « {routine[0]} » : « {routine[1]} »" if routine else "") + ". Retiens les mémoires listées. Encode les instructions d'installation dans ton futur template. Ne crée rien dans Meridian pendant la configuration." if fr else
                    f"You are now the \"{s}\" Bot. Update your profile: name \"{s}\", label \"Meridian\", description: \"{t['en_desc']} {desc_rules}\". Create a skill named `{skill_name}` with the instructions above (Skill section)" + (f", then a routine \"{routine[0]}\": \"{routine[1]}\"" if routine else "") + ". Remember the listed memories. Encode the setup instructions in your future template. Do not create anything in Meridian during setup.")
        blocks.append(f"""## {lang.upper()} — {t[f'{lang}_name']}

### {H[0]}
- **{H[1]}{sep}** {name_line(t,lang)}
- **{H[2]}{sep}** Meridian
- **{H[3]}{sep}** {t[f'{lang}_desc']} {desc_rules}

### {H[5]} `{skill_name}` — {H[4]}
```markdown
---
name: {skill_name}
description: {t[f'{lang}_desc']}
---
{instructions(t,lang)}
```

### {H[6]}
{(f"- **{routine[0]}** — {routine[1]}") if routine else H[12]}

### {H[7]}
{bullets(conn(t,lang))}

### {H[8]}
{bullets(memories)}

### {H[9]}
{setup}

### {H[10]}
{bullets(t[f'{lang}_prompts'])}

### {H[11]}
```text
{creation}
```
""")
    w(f"grok-bot/{t['id']}.md", f"# Grok Bot — {t['fr_name']} / {t['en_name']}\n\n" + "\n---\n\n".join(blocks))

# ======================= Muse =======================
CONN = {
"fr": f"""Crée un connecteur personnalisé (Custom Connector) pour Meridian, mon CRM.
- Nom : meridian
- Transport : serveur MCP distant, HTTP (streamable HTTP)
- URL : {MCP_URL}
- Authentification : OAuth 2.1 avec PKCE; les points de terminaison OAuth sont découvrables depuis le serveur ({SITE}/.well-known/oauth-protected-resource). Connecte-toi avec mon compte Meridian — il n'y a pas de clé à coller dans le chat.
Ensuite, liste ses outils, appelle l'outil « me » pour confirmer mon organisation et mes permissions, et enregistre la connexion comme skill réutilisable nommé « Meridian ».""",
"en": f"""Create a Custom Connector for Meridian, my CRM.
- Name: meridian
- Transport: remote MCP server, HTTP (streamable HTTP)
- URL: {MCP_URL}
- Authentication: OAuth 2.1 with PKCE; the OAuth endpoints are discoverable from the server ({SITE}/.well-known/oauth-protected-resource). Sign in with my Meridian account — there is no key to paste in the chat.
Then list its tools, call the "me" tool to confirm my organization and permissions, and save the connection as a reusable skill called "Meridian"."""}
MUSE_README = {
"fr": """## FR

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
""",
"en": """## EN

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
"""}
w("muse/README.md", "# Muse (Meta) — modèles Meridian / Meridian templates\n\n" + MUSE_README["fr"] + file_list("fr",["- `README.md` — ce fichier","- `connect-meridian.txt` — prompt de création du connecteur (FR + EN)","- `soul-meridian-base.md` — bloc Soul.md commun (FR + EN)"])
  + "\n\n---\n\n" + MUSE_README["en"] + file_list("en",["- `README.md` — this file","- `connect-meridian.txt` — connector creation prompt (FR + EN)","- `soul-meridian-base.md` — common Soul.md block (FR + EN)"]))
w("muse/connect-meridian.txt", "Meridian — connecteur personnalisé Muse / Muse custom connector\n\n=== FR — à coller dans une conversation Muse ===\n"+CONN["fr"]+"\n\n=== EN — paste into a Muse conversation ===\n"+CONN["en"])
w("muse/soul-meridian-base.md", "# Soul.md — bloc Meridian commun / Common Meridian block\n\n## FR\nÀ ajouter une seule fois dans Soul.md (icône Assistant → Identity → Soul), avant les blocs de rôle.\n\n```markdown\n## Travail dans Meridian\n"+bullets(COMMON_RULES_FR)+"\n```\n\n## EN\nAdd once to Soul.md (Assistant icon → Identity → Soul), before the role blocks.\n\n```markdown\n## Working in Meridian\n"+bullets(COMMON_RULES_EN)+"\n```\n")
for t in T:
    parts=[]
    for lang in ("fr","en"):
        fr=lang=="fr"; s=short(t,lang); r=t[f'{lang}_routine']; extra=', '.join(t[f'connectors_extra_{lang}'])
        soul = (f"## Rôle : {t['fr_name']}\n{t['fr_role']}\n\n### Quand ce rôle s'applique\n{t['fr_desc']}\n\n### Pour qui\n{t['fr_target']}" if fr else
                f"## Role: {t['en_name']}\n{t['en_role']}\n\n### When this role applies\n{t['en_desc']}\n\n### Who it's for\n{t['en_target']}")
        skill = (f"Crée un skill réutilisable nommé « {s} (Meridian) ». Il utilise le skill/connecteur « Meridian » et, si connectés : {extra}.\n\nObjectif : {t['fr_desc']}\n\nQuand je te demande quelque chose lié à cet objectif, suis ces étapes :\n{nums(t['fr_steps'])}\n\nOpérations Meridian permises :\n{bullets(ops(t,'fr'))}\n\nRègles :\n{bullets(COMMON_RULES_FR)}\n\nConfirme quand le skill est enregistré et résume-le en 3 lignes." if fr else
                 f"Create a reusable skill called \"{s} (Meridian)\". It uses the \"Meridian\" skill/connector and, if connected: {extra}.\n\nGoal: {t['en_desc']}\n\nWhen I ask for something related to this goal, follow these steps:\n{nums(t['en_steps'])}\n\nAllowed Meridian operations:\n{bullets(ops(t,'en'))}\n\nRules:\n{bullets(COMMON_RULES_EN)}\n\nConfirm when the skill is saved and summarize it in 3 lines.")
        rec = ((f"Crée une tâche récurrente — {r[0]} : « {r[1]} » Confirme l'horaire (fuseau America/Toronto) et dis-moi comment l'annuler." if fr else
                f"Create a recurring task — {r[0]}: \"{r[1]}\" Confirm the schedule (America/Toronto time zone) and tell me how to cancel it.") if r
               else ("Aucune tâche récurrente par défaut — ce rôle travaille à la demande." if fr else "No default recurring task — this role works on demand."))
        H = (("Nom","Pour qui","Soul.md (bloc à ajouter)","Prompt de skill (coller dans Muse)","Tâche récurrente","Connecteurs","Requêtes de départ") if fr else
             ("Name","Who it's for","Soul.md (block to add)","Skill prompt (paste into Muse)","Recurring task","Connectors","Starter prompts"))
        sep = " :" if fr else ":"
        parts.append(f"## {lang.upper()} — {t[f'{lang}_name']}\n\n{t[f'{lang}_desc']}\n\n- **{H[0]}{sep}** {name_line(t,lang)}\n- **{H[1]}{sep}** {t[f'{lang}_target']}\n\n### 1. {H[2]}\n```markdown\n{soul}\n```\n\n### 2. {H[3]}\n```text\n{skill}\n```\n\n### 3. {H[4]}\n```text\n{rec}\n```\n\n### 4. {H[5]}\n{bullets(conn(t,lang))}\n\n### 5. {H[6]}\n{bullets(t[f'{lang}_prompts'])}\n")
    pre = ("> **Prérequis :** connecteur Meridian créé (`connect-meridian.txt`) + bloc commun `soul-meridian-base.md` ajouté à Soul.md.\n>\n"
           "> **Prerequisites:** Meridian connector created (`connect-meridian.txt`) + common `soul-meridian-base.md` block added to Soul.md.")
    w(f"muse/{t['id']}.md", f"# Muse — {t['fr_name']} / {t['en_name']}\n\n{pre}\n\n" + "\n---\n\n".join(parts))

# ======================= OpenAI Dots =======================
DOTS_README = {
"fr": """## FR

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
""",
"en": """## EN

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
"""}
w("openai-dots/README.md", "# OpenAI Dots — modèles Meridian / Meridian templates\n\n" + DOTS_README["fr"] + file_list("fr",["- `README.md` — ce fichier","- `connect-meridian.md` — connexion de Meridian à ChatGPT / dots (FR + EN)"])
  + "\n\n---\n\n" + DOTS_README["en"] + file_list("en",["- `README.md` — this file","- `connect-meridian.md` — connecting Meridian to ChatGPT / dots (FR + EN)"]))
w("openai-dots/connect-meridian.md", f"""# Connecter Meridian à ChatGPT / dots — Connect Meridian to ChatGPT / dots

## FR
1. ChatGPT → Paramètres → Sécurité et connexion → activer **Developer mode** (en Business/Enterprise : l'admin active « Create custom MCP connectors » et publie l'app pour l'espace de travail).
2. ChatGPT → **Plugins** → **+** → URL du serveur : `{MCP_URL}` ; authentification **OAuth** (Meridian annonce l'enregistrement dynamique de client et PKCE S256).
3. Se connecter avec son compte Meridian et accepter la portée `meridian:full`.
4. Dans la conversation du dot : « Appelle l'outil `me` de Meridian et dis-moi mon organisation et mes permissions. »
5. Plugins → Meridian : laisser les outils d'écriture sur **approbation requise**.

> Non vérifié de bout en bout : la compatibilité réelle ChatGPT ↔ OAuth Meridian (Meridian n'annonce que `client_secret_post` au point de terminaison de jeton, pas CIMD ni `none`). Tester avant de publier la page.

## EN
1. ChatGPT → Settings → Security and login → turn on **Developer mode** (on Business/Enterprise: the admin enables "Create custom MCP connectors" and publishes the app for the workspace).
2. ChatGPT → **Plugins** → **+** → server URL: `{MCP_URL}`; **OAuth** authentication (Meridian advertises dynamic client registration and PKCE S256).
3. Sign in with your Meridian account and accept the `meridian:full` scope.
4. In the dot's conversation: "Call Meridian's `me` tool and tell me my organization and permissions."
5. Plugins → Meridian: keep write tools on **approval required**.

> Not verified end to end: actual ChatGPT ↔ Meridian OAuth compatibility (Meridian only advertises `client_secret_post` at the token endpoint, not CIMD or `none`). Test before publishing the page.
""")
MODES = {"ask":("Demander avant d'agir (*Ask before taking action*)","Ask before taking action"),
         "hand":("Me laisser faire (*Hand off to you*)","Hand off to you"),
         "free":("Agir sans demander (*Take action without asking*)","Take action without asking")}
RULES = [("Créer ou modifier un enregistrement dans Meridian (client, contact, opportunité, proposition, facture, dépense, tâche)","Create or update a Meridian record (client, contact, opportunity, proposal, invoice, expense, task)","ask"),
         ("Envoyer un courriel ou un message à quelqu'un d'autre que moi","Send an email or message to anyone other than me","ask"),
         ("Annuler (void) une facture, fermer une période de taxes, supprimer quoi que ce soit dans Meridian","Void an invoice, close a tax period, delete anything in Meridian","hand"),
         ("Lire des données Meridian, de l'agenda et des courriels pour préparer un brouillon","Read Meridian, calendar and email data to prepare a draft","free")]
for t in T:
    parts=[]
    for lang in ("fr","en"):
        fr=lang=="fr"; s=short(t,lang); r=t[f'{lang}_routine']
        resp = (f"Je te confie une responsabilité : {t['fr_desc']}\n\n" + instructions(t,'fr') + "\n\nRésume en 3 lignes ce que tu as compris, puis attends ma première demande." if fr else
                f"I'm giving you a responsibility: {t['en_desc']}\n\n" + instructions(t,'en') + "\n\nSummarize in 3 lines what you understood, then wait for my first request.")
        rt = ("| Action | Comportement |\n|---|---|\n" if fr else "| Action | Behaviour |\n|---|---|\n") + "\n".join(f"| {a if fr else b} | {MODES[m][0] if fr else MODES[m][1]} |" for a,b,m in RULES)
        sched = ((f"{r[1]} Fais-le {r[0]} (heure de l'Est, America/Toronto) pendant les 12 prochaines semaines. Garde les mises à jour de routine dans ChatGPT et écris-moi seulement si une décision est requise. Confirme l'horaire." if fr else
                  f"{r[1]} Do this {r[0]} (Eastern time, America/Toronto) for the next 12 weeks. Keep routine updates in ChatGPT and only message me when a decision is needed. Confirm the schedule.") if r
                 else ("Aucune tâche planifiée par défaut — ce rôle travaille à la demande." if fr else "No default scheduled task — this role works on demand."))
        H = (("Pour qui","Profil suggéré","Nom","Apparence","au choix (orange SignalOrange suggéré)","Plugins requis","Message de responsabilité (coller dans la conversation du dot)","Règles personnalisées (Custom rules)","Tâche planifiée","Requêtes de départ") if fr else
             ("Who it's for","Suggested profile","Name","Appearance","your choice (SignalOrange orange suggested)","Required plugins","Responsibility message (paste into the dot's conversation)","Custom rules","Scheduled task","Starter prompts"))
        sep = " :" if fr else ":"
        parts.append(f"## {lang.upper()} — {t[f'{lang}_name']}\n\n{t[f'{lang}_desc']}\n\n**{H[0]}{sep}** {t[f'{lang}_target']}\n\n### {H[1]}\n- {H[2]}{sep} {name_line(t,lang)}\n- {H[3]}{sep} {H[4]}\n\n### {H[5]}\n{bullets(conn(t,lang))}\n\n### {H[6]}\n```text\n{resp}\n```\n\n### {H[7]}\n{rt}\n\n### {H[8]}\n```text\n{sched}\n```\n\n### {H[9]}\n{bullets(t[f'{lang}_prompts'])}\n")
    w(f"openai-dots/{t['id']}.md", f"# OpenAI Dots — {t['fr_name']} / {t['en_name']}\n\n" + "\n---\n\n".join(parts))
print("ok")
