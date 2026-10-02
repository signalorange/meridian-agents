# Connecter Meridian à ChatGPT / dots — Connect Meridian to ChatGPT / dots

## FR
1. ChatGPT → Paramètres → Sécurité et connexion → activer **Developer mode** (en Business/Enterprise : l'admin active « Create custom MCP connectors » et publie l'app pour l'espace de travail).
2. ChatGPT → **Plugins** → **+** → URL du serveur : `https://meridian.signalorange.ca/api/meridian/mcp` ; authentification **OAuth** (Meridian annonce l'enregistrement dynamique de client et PKCE S256).
3. Se connecter avec son compte Meridian et accepter la portée `meridian:full`.
4. Dans la conversation du dot : « Appelle l'outil `me` de Meridian et dis-moi mon organisation et mes permissions. »
5. Plugins → Meridian : laisser les outils d'écriture sur **approbation requise**.

> Non vérifié de bout en bout : la compatibilité réelle ChatGPT ↔ OAuth Meridian (Meridian n'annonce que `client_secret_post` au point de terminaison de jeton, pas CIMD ni `none`). Tester avant de publier la page.

## EN
1. ChatGPT → Settings → Security and login → turn on **Developer mode** (on Business/Enterprise: the admin enables "Create custom MCP connectors" and publishes the app for the workspace).
2. ChatGPT → **Plugins** → **+** → server URL: `https://meridian.signalorange.ca/api/meridian/mcp`; **OAuth** authentication (Meridian advertises dynamic client registration and PKCE S256).
3. Sign in with your Meridian account and accept the `meridian:full` scope.
4. In the dot's conversation: "Call Meridian's `me` tool and tell me my organization and permissions."
5. Plugins → Meridian: keep write tools on **approval required**.

> Not verified end to end: actual ChatGPT ↔ Meridian OAuth compatibility (Meridian only advertises `client_secret_post` at the token endpoint, not CIMD or `none`). Test before publishing the page.
