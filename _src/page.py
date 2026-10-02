# -*- coding: utf-8 -*-
import os,sys,json
sys.path.insert(0,os.path.dirname(__file__))
from data import *
OUT="/workspace/seo/templates"
P = {
"fr": dict(
  url=SITE+"/templates", alt=SITE+"/templates?locale=en",
  title="Modèles d'agents IA pour Meridian : Grok Bot, Muse, Dots",
  meta="9 modèles d'agents IA prêts à l'emploi pour votre CRM Meridian : prospection, propositions, facturation, TPS/TVQ. Grok Bot, Muse et OpenAI Dots.",
  h1="Modèles d'agents IA pour Meridian — Grok Bot, Muse et OpenAI Dots",
  intro=["Branchez votre agent IA personnel sur Meridian, le CRM québécois pour entreprises de services, et confiez-lui la prospection, les relances, les propositions, les réunions, les projets, la comptabilité et la facturation.",
         f"Chaque modèle est gratuit, en français et en anglais, et utilise le connecteur MCP officiel de Meridian (`{MCP_URL}`) : votre agent agit en votre nom, avec vos permissions Meridian, et ne crée, ne modifie ni n'envoie rien sans votre approbation.",
         "Meridian héberge vos données au Québec (OVH Beauharnois, Loi 25 et LPRPDE); l’agent externe applique la politique de son propre fournisseur."],
  how_h="Comment ça marche (3 étapes)",
  how=["Connectez Meridian à votre agent : connecteur MCP + connexion OAuth avec votre compte Meridian (aucune clé à copier).","Choisissez un modèle ci-dessous et importez-le : lien « Ajouter à Grok Bot », ou prompt à copier pour Muse et OpenAI Dots.","Testez avec une requête de départ, puis activez la routine hebdomadaire si vous le souhaitez."],
  labels=dict(who="Pour qui", conn="Connecteurs", prompts="Exemples de requêtes", routine="Routine suggérée", buttons="Boutons"),
  btns=["**Ajouter à Grok Bot** — ouvre le lien du template Grok Bot (aperçu sur x.ai → « Add to Grok Bot »). *Lien à générer après publication du template.*","**Copier pour Muse** — copie le bloc Soul.md + prompt de skill (presse-papiers).","**Copier pour OpenAI Dots** — copie le message de responsabilité + règles personnalisées.","**Voir les instructions complètes** — déplie le prompt système FR/EN."],
  faq_h="Questions fréquentes",
  faq=[("Qu'est-ce qu'un modèle d'agent Meridian?","C'est un ensemble prêt à l'emploi — rôle, instructions, connecteurs, requêtes de départ et routine — qui apprend à un agent IA (Grok Bot, Muse ou OpenAI Dots) à travailler dans votre CRM Meridian."),
       ("Comment connecter Meridian à mon agent IA?",f"Ajoutez le connecteur MCP distant {MCP_URL} et connectez-vous avec votre compte Meridian (OAuth). Les développeurs peuvent aussi utiliser l'API REST Meridian avec une clé personnelle créée dans Paramètres → Intégrations."),
       ("L'agent peut-il envoyer des courriels ou modifier mes données sans moi?","Non. Les modèles exigent votre approbation avant toute écriture dans Meridian et tout envoi. L'agent hérite aussi de vos permissions Meridian : il ne peut rien faire que vous ne pourriez pas faire vous-même."),
       ("Mes données restent-elles au Canada?","Meridian est hébergé au Québec (OVH Beauharnois) et conforme à la Loi 25 et à la LPRPDE. L'agent externe (Grok Bot, Muse ou Dots) traite toutefois les données qu'il lit selon la politique de son propre fournisseur."),
       ("Les modèles gèrent-ils la TPS et la TVQ?","Oui. Le modèle Comptable lit les périodes de taxes de Meridian (TPS/TVQ courues) et prépare la saisie des dépenses; la fermeture d'une période se fait seulement sur votre demande. Ce n'est pas un avis fiscal."),
       ("Combien ça coûte?","Les modèles sont gratuits. Il faut un compte Meridian et un abonnement à la plateforme d'agent choisie (Grok Bot, Muse ou ChatGPT avec Dots)."),
       ("Puis-je utiliser ces modèles avec Claude ou une autre IA?","Oui : Meridian fonctionne avec Claude (connecteur MCP et Skill Claude), et la version générique des modèles (prompt système + outils + requêtes) s'adapte à tout agent compatible MCP.")],
  howto_name="Connecter Meridian à un agent IA",
),
"en": dict(
  url=SITE+"/templates?locale=en", alt=SITE+"/templates",
  title="AI agent templates for Meridian: Grok Bot, Muse, Dots",
  meta="9 ready-to-use AI agent templates for Meridian CRM: prospecting, proposals, invoicing, GST/QST. For Grok Bot, Muse and OpenAI Dots.",
  h1="AI agent templates for Meridian — Grok Bot, Muse and OpenAI Dots",
  intro=["Connect your personal AI agent to Meridian, the Quebec-built CRM for service businesses, and hand it prospecting, follow-ups, proposals, meetings, projects, bookkeeping and invoicing.",
         f"Every template is free, bilingual (French and English) and uses Meridian's official MCP connector (`{MCP_URL}`): your agent acts as you, with your Meridian permissions, and creates, changes or sends nothing without your approval.",
         "Meridian hosts your data in Quebec (OVH Beauharnois, Law 25 and PIPEDA); the external agent follows its own provider’s policy."],
  how_h="How it works (3 steps)",
  how=["Connect Meridian to your agent: MCP connector + OAuth sign-in with your Meridian account (no key to copy).","Pick a template below and import it: \"Add to Grok Bot\" link, or a copy-paste prompt for Muse and OpenAI Dots.","Test with a starter prompt, then turn on the weekly routine if you want."],
  labels=dict(who="Who it's for", conn="Connectors", prompts="Example prompts", routine="Suggested routine", buttons="Buttons"),
  btns=["**Add to Grok Bot** — opens the Grok Bot template link (preview on x.ai → \"Add to Grok Bot\"). *Link to be generated once the template is published.*","**Copy for Muse** — copies the Soul.md block + skill prompt (clipboard).","**Copy for OpenAI Dots** — copies the responsibility message + custom rules.","**View full instructions** — expands the FR/EN system prompt."],
  faq_h="Frequently asked questions",
  faq=[("What is a Meridian agent template?","A ready-to-use bundle — role, instructions, connectors, starter prompts and routine — that teaches an AI agent (Grok Bot, Muse or OpenAI Dots) how to work inside your Meridian CRM."),
       ("How do I connect Meridian to my AI agent?",f"Add the remote MCP connector {MCP_URL} and sign in with your Meridian account (OAuth). Developers can also use the Meridian REST API with a personal key created in Settings → Integrations."),
       ("Can the agent send emails or change my data without me?","No. The templates require your approval before any write in Meridian and any send. The agent also inherits your Meridian permissions: it cannot do anything you couldn't do yourself."),
       ("Does my data stay in Canada?","Meridian is hosted in Quebec (OVH Beauharnois) and complies with Law 25 and PIPEDA. The external agent (Grok Bot, Muse or Dots) processes the data it reads under its own provider's policy."),
       ("Do the templates handle GST and QST?","Yes. The Bookkeeper template reads Meridian tax periods (accrued GST/QST) and prepares expense entries; closing a period only happens on your request. This is not tax advice."),
       ("How much does it cost?","The templates are free. You need a Meridian account and a subscription to the agent platform you choose (Grok Bot, Muse or ChatGPT with Dots)."),
       ("Can I use these templates with Claude or another AI?","Yes: Meridian works with Claude (MCP connector and Claude Skill), and the generic version of the templates (system prompt + tools + prompts) fits any MCP-compatible agent.")],
  howto_name="Connect Meridian to an AI agent",
)}
for lang,p in P.items():
    fr = lang=="fr"
    L=p["labels"]
    SEP=" :" if fr else ":"
    ld = {"@context":"https://schema.org","@graph":[
      {"@type":"SoftwareApplication","@id":SITE+"/#software","name":"Meridian","applicationCategory":"BusinessApplication","applicationSubCategory":"CRM","operatingSystem":"Web",
       "url":SITE+"/","inLanguage":["fr-CA","en-CA"],"description":("Logiciel CRM canadien pour entreprises de services : CRM, propositions, facturation, projets, comptabilité et assistant IA, avec connecteur MCP pour agents IA." if fr else "Canadian CRM software for service businesses: CRM, proposals, invoicing, projects, bookkeeping and AI assistant, with an MCP connector for AI agents."),
       "featureList":[t[f"{lang}_name"] for t in T],"publisher":{"@type":"Organization","name":"SignalOrange Inc.","url":"https://signalorange.ca/"},
       "areaServed":{"@type":"AdministrativeArea","name":"Québec"}},
      {"@type":"WebPage","@id":p["url"],"url":p["url"],"name":p["title"],"description":p["meta"],"inLanguage":"fr-CA" if fr else "en-CA","about":{"@id":SITE+"/#software"}},
      {"@type":"HowTo","name":p["howto_name"],"inLanguage":"fr-CA" if fr else "en-CA","step":[{"@type":"HowToStep","position":i,"text":s} for i,s in enumerate(p["how"],1)]},
      {"@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in p["faq"]]},
      {"@type":"ItemList","name":p["h1"],"itemListElement":[{"@type":"ListItem","position":i,"name":t[f"{lang}_name"],"url":(p["url"].split("?")[0]+("?locale=en" if not fr else "")+"#"+t["id"]),"description":t[f"{lang}_desc"]} for i,t in enumerate(T,1)]}
    ]}
    o=[f"# {'Page /templates — FR (ébauche, non publiée)' if fr else 'Page /templates?locale=en — EN (draft, not published)'}","",
       "## SEO","",*( [f"- **URL :** `{p['url']}`  ·  hreflang alterné : `{p['alt']}` (fr-CA ↔ en-CA, x-default = FR)",
       f"- **Title ({len(p['title'])} car.) :** {p['title']}",f"- **Méta-description ({len(p['meta'])} car.) :** {p['meta']}",
       f"- **Canonical :** `{p['url']}`","- **Ajouter au sitemap.xml** (les deux versions) et lier depuis /docs/meridian-api, /docs/ai-assistant-overview et le pied de page."] if fr else
       [f"- **URL:** `{p['url']}`  ·  alternate hreflang: `{p['alt']}` (en-CA ↔ fr-CA, x-default = FR)",
       f"- **Title ({len(p['title'])} chars):** {p['title']}",f"- **Meta description ({len(p['meta'])} chars):** {p['meta']}",
       f"- **Canonical:** `{p['url']}`","- **Add to sitemap.xml** (both versions) and link from /docs/meridian-api, /docs/ai-assistant-overview and the footer."] ),"",
       "---","",f"# {p['h1']}",""]+[x+"\n" for x in p["intro"]]+[f"## {p['how_h']}",""]+[f"{i}. {s}" for i,s in enumerate(p["how"],1)]+[""]
    for t in T:
        o+=[f'<a id="{t["id"]}"></a>',f"## {t[f'{lang}_name']}","",t[f"{lang}_desc"],"",f"**{L['who']}{SEP}** {t[f'{lang}_target']}","",
            f"**{L['conn']}{SEP}** Meridian (MCP) · "+" · ".join(t[f"connectors_extra_{lang}"]),"",f"**{L['prompts']}{SEP}**"]+[f"- « {x} »" if fr else f'- "{x}"' for x in t[f"{lang}_prompts"]]+[""]
        if t[f"{lang}_routine"]: o+=[f"**{L['routine']}{SEP}** {t[f'{lang}_routine'][0]} — {t[f'{lang}_routine'][1]}",""]
        o+=[f"*{L['buttons']}{SEP}* Grok Bot · Muse · OpenAI Dots · {'Instructions' if fr else 'Instructions'} → `grok-bot/{t['id']}.md`, `muse/{t['id']}.md`, `openai-dots/{t['id']}.md`",""]
    o+=[f"### {'Description des boutons (commune à chaque section)' if fr else 'Button behaviour (same in every section)'}",""]+[f"- {b}" for b in p["btns"]]+["",
        ("> Aucun modèle de veille d'appels d'offres (SEAO) n'est proposé : Meridian n'offre pas cette fonction aujourd'hui." if fr else "> No tender-watch (SEAO) template is offered: Meridian does not provide that feature today."),"",
        f"## {p['faq_h']}",""]
    for q,a in p["faq"]: o+=[f"### {q}","",a,""]
    o+=["---","","## JSON-LD","","```html",'<script type="application/ld+json">',json.dumps(ld,ensure_ascii=False,indent=2),"</script>","```"]
    open(f"{OUT}/page-templates-{lang}.md","w").write("\n".join(o)+"\n")
print("ok")
