# 📱 Héritier Millionnaire - APK Android

Application mobile Android du jeu **Héritier Millionnaire** - Simulateur de gestion immobilière, boursière et quiz de culture financière.

## 🎮 À propos du jeu

Héritier Millionnaire est un jeu de simulation financière où vous devez :
- 🏠 **Investir dans l'immobilier** - Acheter et gérer des propriétés
- 📈 **Trader en bourse** - Acheter/vendre des actions sur les marchés
- 🎯 **Participer à des quiz** - Tester vos connaissances financières
- 💰 **Gérer votre portefeuille** - Optimiser vos investissements
- 🏆 **Grimper au classement** - Devenir l'héritier #1

## Dernière version

### v1.0.2 - Tutoriel mobile amélioré (11 novembre 2025)

**Télécharger l'AAB:** [heritier-millionnaire-1.0.2(3)-20251111-1950.aab](../releases/heritier-millionnaire-1.0.2(3)-20251111-1950.aab) (37.26 MB)

**Télécharger l'APK:** [heritier-millionnaire-1.0.2(3)-20251111-1950.apk](../releases/heritier-millionnaire-1.0.2(3)-20251111-1950.apk) (37.66 MB)

#### Nouveautés
- Navigation tutoriel mobile avec balayage gauche/droite (gestes) pour passer d'un volet à l'autre
- Export web et Capacitor sync remis à jour post-correctif
- Build Android 1.0.2 (code 3) signée production

#### Signature
- APK/AAB signés avec le keystore de production
- Validité: jusqu'en 2050
- SHA256: `07:CD:F8:6C:75:2D:78:1D:E8:B7:05:02:5E:B6:2B:BA`

## 🚀 Installation

### Méthode 1 : Téléchargement direct
1. **Activer les sources inconnues** sur votre appareil Android :
   - Paramètres → Sécurité → Autoriser les sources inconnues
2. **Télécharger l'APK** en cliquant sur le lien ci-dessus
3. **Ouvrir le fichier** téléchargé
4. **Suivre les instructions** d'installation
5. **Lancer l'application** !

### Méthode 2 : ADB (pour développeurs)
```bash
adb install "heritier-millionnaire-1.0.2(3)-20251111-1950.apk"
```

## 📱 Prérequis

- Android 7.0 (API 24) ou supérieur
- ~20 MB d'espace de stockage
- Connexion Internet pour le multijoueur

## 🌐 Liens

- **Application web** : https://client-jeux-millionnaire.vercel.app
- **API Backend** : https://server-jeux-millionnaire.onrender.com
- **Code source client** : https://github.com/nowis30/client-jeux-millionnaire
- **Code source serveur** : https://github.com/nowis30/server-jeux-millionnaire

## 🔒 Confidentialité

L'application respecte le RGPD et affiche un bandeau de consentement lors du premier lancement. Consultez notre [politique de confidentialité](https://client-jeux-millionnaire.vercel.app/confidentialite/) pour plus d'informations.

## 📊 Historique des versions

| Version | Date | Taille | Type | Changements |
|---------|------|--------|------|-------------|
| 1.0.2 | 11 nov 2025 | 37.3 MB | Release | Gestes de balayage tutoriel, build 1.0.2 code 3 |
| 1.0.1 | 11 nov 2025 | 37.3 MB | Release | Correctif consentement AdMob, centre confidentialité, page debug |
| 1.0 | 9 nov 2025 | 18.23 MB | Release | Production avec AdMob, RGPD, signature |
| 0.x | 6 nov 2025 | - | Debug | Builds de développement |

## 🏗️ Stack technique

- **Framework** : Capacitor 6
- **Frontend** : Next.js 14 (export statique)
- **Backend** : Fastify + PostgreSQL
- **Publicités** : Google AdMob
- **Temps réel** : Socket.io

---

© 2025 Nowis - Tous droits réservés
