# Play Console - Préparation soumission v1.0.2

## Artifacts
- `releases/heritier-millionnaire-1.0.2(3)-20251111-1950.aab`
- (Optionnel QA) `releases/heritier-millionnaire-1.0.2(3)-20251111-1950.apk`

## Listing
- Mettre à jour la fiche française avec `mobile/STORE_LISTING_FR.md`
- Notes de version (FR):
  ```
  v1.0.2
  - Navigation du tutoriel par gestes (balayage gauche/droite)
  - Maintien des correctifs consentement AdMob / Debug Ads
  - Build Android 1.0.2 (code 3)
  ```
- Notes de version (EN - si besoin):
  ```
  v1.0.2
  - Added swipe gestures to the onboarding tutorial
  - Keeps GDPR consent / AdMob fixes from 1.0.1
  - Android build 1.0.2 (code 3)
  ```

## Tests fermés (optionnel)
1. Créer une piste "Test interne"
2. Importer l'AAB
3. Ajouter testeurs (compte QA + votre compte)
4. Lancer la publication et vérifier la livraison via Play Store

## Release production
1. Dupliquer la piste stable courante, renommer `v1.0.2`
2. Importer l'AAB
3. Mettre le numéro de version 1.0.2 / code 3
4. Ajouter les notes de version FR/EN
5. Vérifier les captures et les catégories
6. Lancer la revue

## Post-soumission
- Surveiller l'onglet **Qualité -> Android vitals**
- Vérifier le remplissage AdMob après 24h
- Répondre aux retours utilisateurs sous 48h
