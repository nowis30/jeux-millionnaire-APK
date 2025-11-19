# QA Checklist - Version 1.0.1 (11 nov 2025)

## Préparation
- [x] Installer l'APK `releases/heritier-millionnaire-1.0.1(2)-20251111-1842.apk` sur 2 appareils (Android 13 + Android 10)
- [ ] Réinitialiser les données de l'application entre chaque scénario (`Paramètres -> Applications -> Effacer les données`)
- [ ] Activer les logs via `adb logcat | findstr AdMob` si un PC est disponible

## Flux consentement RGPD
- [x] Premier lancement: bandeau UMP s'affiche, accepter les pubs personnalisées
- [x] Vérifier que `/confidentialite` reflète l'état "Pubs personnalisées"
- [ ] Revenir au menu, forcer "Pubs non personnalisées" puis redémarrer l'app -> vérifier la persistance
- [ ] Réinitialiser le consentement depuis `/confidentialite` et s'assurer que le bandeau réapparaît au prochain lancement

## Publicités (via `/debug-ads`)
- [ ] Bouton "Initialiser" retourne succès (toast + logcat `onInitializationComplete`)
- [ ] Bouton "Charger interstitiel" puis "Afficher interstitiel" fonctionnent au moins 1 fois/apparareil
- [ ] Rejeter le consentement dans `/confidentialite`, relancer l'app, recharger les pubs (doivent s'afficher en mode NPA)
- [ ] Bouton "Charger récompensée" puis "Afficher récompensée" déclenchent la récompense (vérifier log `onUserEarnedReward`)

## Parcours principal
- [x] Navigation complète du menu: Bonus, Bourse, Quiz, Tutoriel, etc.
- [x] Lancer une partie de quiz et valider qu'un score s'enregistre
- [ ] Vérifier la page Portefeuille hors connexion (activer mode avion) -> lecture des données locales OK
- [ ] Jouer avec le son activé/désactivé -> pas de crash audio

## Régressions fixes
- [ ] Après consentement "refusé", lancer une session de jeu de 5 minutes -> Ads apparaissent néanmoins (en NPA)
- [ ] Les boutons "Accepter / NPA / Réinitialiser" réagissent sans timeout
- [ ] La page `/debug-ads` n'est pas accessible depuis les pages publiques du site web (version web -> vérifier 404)

## Post-QA
- [ ] Capturer 4 captures d'écran actualisées (home, consentement, debug-ads, quiz)
- [ ] Exporter un logcat de 2 cycles d'annonces (`adb logcat -d > logs/admob-qa-20251111.txt`)
- [ ] Archiver captures + log dans `releases/qa-assets-1.0.1/`
- [ ] Noter toute anomalie restante dans `tests/KNOWN_ISSUES.md`
