# Page /templates — FR (ébauche, non publiée)

## SEO

- **URL :** `https://meridian.signalorange.ca/templates`  ·  hreflang alterné : `https://meridian.signalorange.ca/templates?locale=en` (fr-CA ↔ en-CA, x-default = FR)
- **Title (56 car.) :** Modèles d'agents IA pour Meridian : Grok Bot, Muse, Dots
- **Méta-description (144 car.) :** 9 modèles d'agents IA prêts à l'emploi pour votre CRM Meridian : prospection, propositions, facturation, TPS/TVQ. Grok Bot, Muse et OpenAI Dots.
- **Canonical :** `https://meridian.signalorange.ca/templates`
- **Ajouter au sitemap.xml** (les deux versions) et lier depuis /docs/meridian-api, /docs/ai-assistant-overview et le pied de page.

---

# Modèles d'agents IA pour Meridian — Grok Bot, Muse et OpenAI Dots

Branchez votre agent IA personnel sur Meridian, le CRM québécois pour entreprises de services, et confiez-lui la prospection, les relances, les propositions, les réunions, les projets, la comptabilité et la facturation.

Chaque modèle est gratuit, en français et en anglais, et utilise le connecteur MCP officiel de Meridian (`https://meridian.signalorange.ca/api/meridian/mcp`) : votre agent agit en votre nom, avec vos permissions Meridian, et ne crée, ne modifie ni n'envoie rien sans votre approbation.

Meridian héberge vos données au Québec (OVH Beauharnois, Loi 25 et LPRPDE); l’agent externe applique la politique de son propre fournisseur.

## Comment ça marche (3 étapes)

1. Connectez Meridian à votre agent : connecteur MCP + connexion OAuth avec votre compte Meridian (aucune clé à copier).
2. Choisissez un modèle ci-dessous et importez-le : lien « Ajouter à Grok Bot », ou prompt à copier pour Muse et OpenAI Dots.
3. Testez avec une requête de départ, puis activez la routine hebdomadaire si vous le souhaitez.

<a id="prospection"></a>
## Éclaireur — Prospection et qualification

Trouve des entreprises cibles au Québec, les enrichit, vérifie les doublons dans Meridian et prépare les fiches client + opportunité à valider.

**Pour qui :** Propriétaire de PME de services, développeur·se des affaires, consultant·e B2B.

**Connecteurs :** Meridian (MCP) · Recherche Web / navigateur (intégré à la plateforme)

**Exemples de requêtes :**
- « Trouve 15 cabinets comptables de 10 à 50 employés en Montérégie qui ne sont pas déjà dans mon Meridian. »
- « Voici mon client idéal : [description]. Mémorise-le et propose-moi 10 prospects cette semaine. »
- « Quelles opportunités ouvertes n'ont pas bougé depuis deux semaines? Propose une action pour chacune. »

**Routine suggérée :** Lundi 8 h 00 (HE) — Recherche 10 nouveaux prospects selon le PCI, vérifie les doublons dans Meridian et envoie-moi le tableau à approuver. Ne crée rien sans mon accord.

*Boutons :* Grok Bot · Muse · OpenAI Dots · Instructions → `grok-bot/prospection.md`, `muse/prospection.md`, `openai-dots/prospection.md`

<a id="approche"></a>
## Messager — Approche et relances

Rédige des premiers courriels et des relances personnalisés à partir des fiches Meridian; vous révisez et envoyez.

**Pour qui :** Toute personne qui fait du développement des affaires et veut des relances régulières sans écrire chaque courriel.

**Connecteurs :** Meridian (MCP) · Gmail ou Outlook (lecture + brouillons)

**Exemples de requêtes :**
- « Prépare un premier courriel pour l'opportunité « Refonte site — Boulangerie Lavoie ». »
- « Quelles relances sont dues aujourd'hui? Rédige-les en brouillon. »
- « Réécris ce courriel en anglais, ton plus direct, 80 mots max. »

**Routine suggérée :** Jours ouvrables 8 h 30 (HE) — Liste les opportunités dont une relance est due (J+3/J+7/J+14 sans réponse), rédige les brouillons et attends mon approbation avant tout envoi.

*Boutons :* Grok Bot · Muse · OpenAI Dots · Instructions → `grok-bot/approche.md`, `muse/approche.md`, `openai-dots/approche.md`

<a id="propositions"></a>
## Plume — Rédaction de propositions

Monte un brouillon de proposition à partir de l'opportunité, des notes de découverte et de vos propositions passées, puis le dépose dans Meridian après votre accord.

**Pour qui :** Agences, consultant·es et firmes de services qui envoient des soumissions et des offres de service.

**Connecteurs :** Meridian (MCP) · Google Drive / OneDrive (optionnel, pour des annexes)

**Exemples de requêtes :**
- « Rédige une proposition pour l'opportunité #123 en t'inspirant de ma dernière proposition gagnée. »
- « Résume les différences entre la version 1 et 2 de la proposition « Audit TI — Groupe Roy ». »
- « Propose trois options de prix (bon, mieux, meilleur) pour ce mandat. »

*Boutons :* Grok Bot · Muse · OpenAI Dots · Instructions → `grok-bot/propositions.md`, `muse/propositions.md`, `openai-dots/propositions.md`

<a id="reunions"></a>
## Greffier — Réunions et transcriptions

Prépare chaque rencontre client à partir de Meridian et transforme la transcription en résumé, décisions et suivis à classer dans le dossier.

**Pour qui :** Consultant·es et gestionnaires de comptes qui enchaînent les rencontres (Teams, Meet, Zoom).

**Connecteurs :** Meridian (MCP) · Google Agenda ou Outlook/Microsoft 365 (lecture) · Google Drive / OneDrive (transcriptions)

**Exemples de requêtes :**
- « Prépare-moi pour ma rencontre de 14 h avec Construction Gagnon. »
- « Voici la transcription de la rencontre : [texte]. Fais le compte rendu et propose les suivis. »
- « Classe ce compte rendu dans l'opportunité et crée les tâches convenues. »

**Routine suggérée :** Jours ouvrables 7 h 30 (HE) — Regarde mon agenda du jour; pour chaque rencontre externe, prépare une fiche d'une page à partir de Meridian.

*Boutons :* Grok Bot · Muse · OpenAI Dots · Instructions → `grok-bot/reunions.md`, `muse/reunions.md`, `openai-dots/reunions.md`

<a id="projets"></a>
## Chef de chantier — Gestion de projets

Suit vos projets Meridian, repère les tâches en retard et produit un rapport de statut clair pour vous ou votre client.

**Pour qui :** Gestionnaires de projets et propriétaires d'agences, de firmes-conseils ou d'entrepreneurs spécialisés.

**Connecteurs :** Meridian (MCP) · Gmail ou Outlook (brouillons de statut, optionnel)

**Exemples de requêtes :**
- « Quels projets sont en retard cette semaine? »
- « Fais le rapport de statut du projet « Migration ERP » pour le client. »
- « Découpe cette phase en tâches et propose des échéances. »

**Routine suggérée :** Vendredi 15 h 00 (HE) — Fais le rapport de statut de tous les projets actifs : retards, échéances de la semaine prochaine, blocages.

*Boutons :* Grok Bot · Muse · OpenAI Dots · Instructions → `grok-bot/projets.md`, `muse/projets.md`, `openai-dots/projets.md`

<a id="comptabilite"></a>
## Comptable — Dépenses, TPS/TVQ et trésorerie

Saisit et catégorise vos dépenses, prépare les périodes de TPS/TVQ et vous donne l'état des résultats et la position de trésorerie.

**Pour qui :** Propriétaires de PME et travailleurs autonomes au Québec qui tiennent leurs livres dans Meridian (avant le comptable externe).

**Connecteurs :** Meridian (MCP) · Gmail ou Outlook (reçus) · Google Drive / OneDrive (pièces justificatives)

**Exemples de requêtes :**
- « Voici 6 reçus de septembre : saisis-les en dépenses après m'avoir montré le tableau. »
- « Combien de TPS et de TVQ dois-je pour le trimestre en cours? »
- « Donne-moi l'état des résultats de janvier à septembre et ma position de trésorerie. »

**Routine suggérée :** 1er de chaque mois, 9 h 00 (HE) — Cherche les reçus du mois précédent dans mes courriels, prépare les dépenses à saisir et résume la TPS/TVQ courue. Ne saisis rien sans mon accord.

*Boutons :* Grok Bot · Muse · OpenAI Dots · Instructions → `grok-bot/comptabilite.md`, `muse/comptabilite.md`, `openai-dots/comptabilite.md`

<a id="facturation"></a>
## Percepteur — Facturation et recouvrement

Prépare les factures à partir des projets et des opportunités, suit les paiements et rédige des relances polies pour les comptes en souffrance.

**Pour qui :** PME de services et travailleurs autonomes qui facturent dans Meridian (Stripe).

**Connecteurs :** Meridian (MCP) · Gmail ou Outlook (brouillons de relance)

**Exemples de requêtes :**
- « Quelles factures sont en retard et de combien? »
- « Prépare la facture de septembre pour le projet « Site Web — Clinique Beaulieu ». »
- « Le client Tremblay a payé 1 500 $ par virement Interac aujourd'hui : enregistre le paiement sur sa facture. »

**Routine suggérée :** Mardi 9 h 00 (HE) — Fais le point sur les comptes clients : factures en retard, âge, montant total; rédige les relances en brouillon pour celles qui n'ont pas de relance automatique.

*Boutons :* Grok Bot · Muse · OpenAI Dots · Instructions → `grok-bot/facturation.md`, `muse/facturation.md`, `openai-dots/facturation.md`

<a id="suivi-client"></a>
## Ange gardien — Suivi client après-vente

Garde le contact avec vos clients après la signature : bilan de démarrage, suivi de satisfaction, occasions de renouvellement ou de recommandation.

**Pour qui :** Firmes de services à mandats récurrents (agences, TI gérées, conseil).

**Connecteurs :** Meridian (MCP) · Gmail ou Outlook (brouillons) · Google Agenda ou Outlook (planifier des bilans, en brouillon)

**Exemples de requêtes :**
- « Quels clients n'ont pas eu de nouvelles de nous depuis 60 jours? »
- « Le projet « Image de marque — Fromagerie Côté » est terminé : prépare la demande de témoignage. »
- « Transforme les 3 questions les plus fréquentes de mes clients en articles pour ma FAQ. »

**Routine suggérée :** Mercredi 10 h 00 (HE) — Liste les clients à contacter cette semaine selon le calendrier de soins et rédige les messages en brouillon.

*Boutons :* Grok Bot · Muse · OpenAI Dots · Instructions → `grok-bot/suivi-client.md`, `muse/suivi-client.md`, `openai-dots/suivi-client.md`

<a id="rapport-hebdo"></a>
## Vigie — Tableau de bord hebdomadaire

Chaque lundi, un rapport d'une page : pipeline, propositions, projets, factures en retard, trésorerie et TPS/TVQ — tiré de Meridian.

**Pour qui :** Dirigeant·es de PME qui veulent une vue d'ensemble sans ouvrir cinq écrans.

**Connecteurs :** Meridian (MCP) · Aucun requis (optionnel : Gmail/Outlook pour recevoir le rapport en brouillon)

**Exemples de requêtes :**
- « Fais mon tableau de bord de la semaine. »
- « Compare ce mois-ci au mois dernier : revenus, nouvelles opportunités, factures en retard. »
- « Quelles sont les 3 décisions les plus urgentes cette semaine? »

**Routine suggérée :** Lundi 7 h 00 (HE) — Produis le tableau de bord hebdomadaire Meridian et envoie-le-moi dans cette conversation.

*Boutons :* Grok Bot · Muse · OpenAI Dots · Instructions → `grok-bot/rapport-hebdo.md`, `muse/rapport-hebdo.md`, `openai-dots/rapport-hebdo.md`

### Description des boutons (commune à chaque section)

- **Ajouter à Grok Bot** — ouvre le lien du template Grok Bot (aperçu sur x.ai → « Add to Grok Bot »). *Lien à générer après publication du template.*
- **Copier pour Muse** — copie le bloc Soul.md + prompt de skill (presse-papiers).
- **Copier pour OpenAI Dots** — copie le message de responsabilité + règles personnalisées.
- **Voir les instructions complètes** — déplie le prompt système FR/EN.

> Aucun modèle de veille d'appels d'offres (SEAO) n'est proposé : Meridian n'offre pas cette fonction aujourd'hui.

## Questions fréquentes

### Qu'est-ce qu'un modèle d'agent Meridian?

C'est un ensemble prêt à l'emploi — rôle, instructions, connecteurs, requêtes de départ et routine — qui apprend à un agent IA (Grok Bot, Muse ou OpenAI Dots) à travailler dans votre CRM Meridian.

### Comment connecter Meridian à mon agent IA?

Ajoutez le connecteur MCP distant https://meridian.signalorange.ca/api/meridian/mcp et connectez-vous avec votre compte Meridian (OAuth). Les développeurs peuvent aussi utiliser l'API REST Meridian avec une clé personnelle créée dans Paramètres → Intégrations.

### L'agent peut-il envoyer des courriels ou modifier mes données sans moi?

Non. Les modèles exigent votre approbation avant toute écriture dans Meridian et tout envoi. L'agent hérite aussi de vos permissions Meridian : il ne peut rien faire que vous ne pourriez pas faire vous-même.

### Mes données restent-elles au Canada?

Meridian est hébergé au Québec (OVH Beauharnois) et conforme à la Loi 25 et à la LPRPDE. L'agent externe (Grok Bot, Muse ou Dots) traite toutefois les données qu'il lit selon la politique de son propre fournisseur.

### Les modèles gèrent-ils la TPS et la TVQ?

Oui. Le modèle Comptable lit les périodes de taxes de Meridian (TPS/TVQ courues) et prépare la saisie des dépenses; la fermeture d'une période se fait seulement sur votre demande. Ce n'est pas un avis fiscal.

### Combien ça coûte?

Les modèles sont gratuits. Il faut un compte Meridian et un abonnement à la plateforme d'agent choisie (Grok Bot, Muse ou ChatGPT avec Dots).

### Puis-je utiliser ces modèles avec Claude ou une autre IA?

Oui : Meridian fonctionne avec Claude (connecteur MCP et Skill Claude), et la version générique des modèles (prompt système + outils + requêtes) s'adapte à tout agent compatible MCP.

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
      "description": "Logiciel CRM canadien pour entreprises de services : CRM, propositions, facturation, projets, comptabilité et assistant IA, avec connecteur MCP pour agents IA.",
      "featureList": [
        "Éclaireur — Prospection et qualification",
        "Messager — Approche et relances",
        "Plume — Rédaction de propositions",
        "Greffier — Réunions et transcriptions",
        "Chef de chantier — Gestion de projets",
        "Comptable — Dépenses, TPS/TVQ et trésorerie",
        "Percepteur — Facturation et recouvrement",
        "Ange gardien — Suivi client après-vente",
        "Vigie — Tableau de bord hebdomadaire"
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
      "@id": "https://meridian.signalorange.ca/templates",
      "url": "https://meridian.signalorange.ca/templates",
      "name": "Modèles d'agents IA pour Meridian : Grok Bot, Muse, Dots",
      "description": "9 modèles d'agents IA prêts à l'emploi pour votre CRM Meridian : prospection, propositions, facturation, TPS/TVQ. Grok Bot, Muse et OpenAI Dots.",
      "inLanguage": "fr-CA",
      "about": {
        "@id": "https://meridian.signalorange.ca/#software"
      }
    },
    {
      "@type": "HowTo",
      "name": "Connecter Meridian à un agent IA",
      "inLanguage": "fr-CA",
      "step": [
        {
          "@type": "HowToStep",
          "position": 1,
          "text": "Connectez Meridian à votre agent : connecteur MCP + connexion OAuth avec votre compte Meridian (aucune clé à copier)."
        },
        {
          "@type": "HowToStep",
          "position": 2,
          "text": "Choisissez un modèle ci-dessous et importez-le : lien « Ajouter à Grok Bot », ou prompt à copier pour Muse et OpenAI Dots."
        },
        {
          "@type": "HowToStep",
          "position": 3,
          "text": "Testez avec une requête de départ, puis activez la routine hebdomadaire si vous le souhaitez."
        }
      ]
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Qu'est-ce qu'un modèle d'agent Meridian?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "C'est un ensemble prêt à l'emploi — rôle, instructions, connecteurs, requêtes de départ et routine — qui apprend à un agent IA (Grok Bot, Muse ou OpenAI Dots) à travailler dans votre CRM Meridian."
          }
        },
        {
          "@type": "Question",
          "name": "Comment connecter Meridian à mon agent IA?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Ajoutez le connecteur MCP distant https://meridian.signalorange.ca/api/meridian/mcp et connectez-vous avec votre compte Meridian (OAuth). Les développeurs peuvent aussi utiliser l'API REST Meridian avec une clé personnelle créée dans Paramètres → Intégrations."
          }
        },
        {
          "@type": "Question",
          "name": "L'agent peut-il envoyer des courriels ou modifier mes données sans moi?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Non. Les modèles exigent votre approbation avant toute écriture dans Meridian et tout envoi. L'agent hérite aussi de vos permissions Meridian : il ne peut rien faire que vous ne pourriez pas faire vous-même."
          }
        },
        {
          "@type": "Question",
          "name": "Mes données restent-elles au Canada?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Meridian est hébergé au Québec (OVH Beauharnois) et conforme à la Loi 25 et à la LPRPDE. L'agent externe (Grok Bot, Muse ou Dots) traite toutefois les données qu'il lit selon la politique de son propre fournisseur."
          }
        },
        {
          "@type": "Question",
          "name": "Les modèles gèrent-ils la TPS et la TVQ?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Oui. Le modèle Comptable lit les périodes de taxes de Meridian (TPS/TVQ courues) et prépare la saisie des dépenses; la fermeture d'une période se fait seulement sur votre demande. Ce n'est pas un avis fiscal."
          }
        },
        {
          "@type": "Question",
          "name": "Combien ça coûte?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Les modèles sont gratuits. Il faut un compte Meridian et un abonnement à la plateforme d'agent choisie (Grok Bot, Muse ou ChatGPT avec Dots)."
          }
        },
        {
          "@type": "Question",
          "name": "Puis-je utiliser ces modèles avec Claude ou une autre IA?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Oui : Meridian fonctionne avec Claude (connecteur MCP et Skill Claude), et la version générique des modèles (prompt système + outils + requêtes) s'adapte à tout agent compatible MCP."
          }
        }
      ]
    },
    {
      "@type": "ItemList",
      "name": "Modèles d'agents IA pour Meridian — Grok Bot, Muse et OpenAI Dots",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "name": "Éclaireur — Prospection et qualification",
          "url": "https://meridian.signalorange.ca/templates#prospection",
          "description": "Trouve des entreprises cibles au Québec, les enrichit, vérifie les doublons dans Meridian et prépare les fiches client + opportunité à valider."
        },
        {
          "@type": "ListItem",
          "position": 2,
          "name": "Messager — Approche et relances",
          "url": "https://meridian.signalorange.ca/templates#approche",
          "description": "Rédige des premiers courriels et des relances personnalisés à partir des fiches Meridian; vous révisez et envoyez."
        },
        {
          "@type": "ListItem",
          "position": 3,
          "name": "Plume — Rédaction de propositions",
          "url": "https://meridian.signalorange.ca/templates#propositions",
          "description": "Monte un brouillon de proposition à partir de l'opportunité, des notes de découverte et de vos propositions passées, puis le dépose dans Meridian après votre accord."
        },
        {
          "@type": "ListItem",
          "position": 4,
          "name": "Greffier — Réunions et transcriptions",
          "url": "https://meridian.signalorange.ca/templates#reunions",
          "description": "Prépare chaque rencontre client à partir de Meridian et transforme la transcription en résumé, décisions et suivis à classer dans le dossier."
        },
        {
          "@type": "ListItem",
          "position": 5,
          "name": "Chef de chantier — Gestion de projets",
          "url": "https://meridian.signalorange.ca/templates#projets",
          "description": "Suit vos projets Meridian, repère les tâches en retard et produit un rapport de statut clair pour vous ou votre client."
        },
        {
          "@type": "ListItem",
          "position": 6,
          "name": "Comptable — Dépenses, TPS/TVQ et trésorerie",
          "url": "https://meridian.signalorange.ca/templates#comptabilite",
          "description": "Saisit et catégorise vos dépenses, prépare les périodes de TPS/TVQ et vous donne l'état des résultats et la position de trésorerie."
        },
        {
          "@type": "ListItem",
          "position": 7,
          "name": "Percepteur — Facturation et recouvrement",
          "url": "https://meridian.signalorange.ca/templates#facturation",
          "description": "Prépare les factures à partir des projets et des opportunités, suit les paiements et rédige des relances polies pour les comptes en souffrance."
        },
        {
          "@type": "ListItem",
          "position": 8,
          "name": "Ange gardien — Suivi client après-vente",
          "url": "https://meridian.signalorange.ca/templates#suivi-client",
          "description": "Garde le contact avec vos clients après la signature : bilan de démarrage, suivi de satisfaction, occasions de renouvellement ou de recommandation."
        },
        {
          "@type": "ListItem",
          "position": 9,
          "name": "Vigie — Tableau de bord hebdomadaire",
          "url": "https://meridian.signalorange.ca/templates#rapport-hebdo",
          "description": "Chaque lundi, un rapport d'une page : pipeline, propositions, projets, factures en retard, trésorerie et TPS/TVQ — tiré de Meridian."
        }
      ]
    }
  ]
}
</script>
```
