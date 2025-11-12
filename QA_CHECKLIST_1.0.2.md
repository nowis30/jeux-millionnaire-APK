# QA Checklist - Version 1.0.2 (11 nov 2025)

## Préparation
- [ ] Installer l'APK `releases/heritier-millionnaire-1.0.2(3)-20251111-1950.apk` sur au moins 2 appareils (Android 13 + Android 10)
- [ ] Réinitialiser les données entre chaque scénario (`Paramètres -> Applications -> Effacer les données`)
- [ ] Activer les logs `adb logcat | findstr AdMob` pour suivre les impressions

## Tutoriel & gestes
- [ ] Ouvrir le tutoriel d'accueil ("C'est parti")
- [ ] Balayer vers la gauche pour passer au volet suivant (doit fonctionner sans appui sur "Suivant")
- [ ] Balayer vers la droite pour revenir en arrière (sans appui sur "Précédent")
- [ ] Tester sur écran tactile + tablette (si dispo) pour confirmer sensibilité >40px OK
- [ ] Vérifier que les boutons restent fonctionnels en plus du geste

## Flux consentement RGPD
- [ ] Bandeau UMP initial toujours présent (pas de régression)
- [ ] `/confidentialite` affiche l'état actuel et peut passer de "personnalisées" à "non personnalisées"
- [ ] Réinitialisation du consentement relance UMP au prochain démarrage

## Publicités via `/debug-ads`
- [ ] Initialiser AdMob -> message succès + logcat `onInitializationComplete`
- [ ] Charger/afficher interstitiel (profil consentement accepté)
- [ ] Basculer en NPA (consentement refusé) -> recharger interstitiel et confirmer l'affichage
- [ ] Charger/afficher récompensée -> log `onUserEarnedReward`

## Parcours principal
- [ ] Navigation complète: Bonus, Bourse, Quiz, Tutoriel, Telecharger
- [ ] Quiz: lancer une session et vérifier la sauvegarde du score
- [ ] Mode avion: page Portefeuille affiche les dernières infos en local
- [ ] Audio: activer/désactiver sons sans crash

## Post-QA
- [ ] Captures mises à jour (tutoriel avec geste, consentement, debug-ads, home)
- [ ] Export `adb logcat -d > logs/admob-qa-20251111-gestures.txt`
- [ ] Archiver assets dans `releases/qa-assets-1.0.2/`
- [ ] Reporter anomalies dans `tests/KNOWN_ISSUES.md`
