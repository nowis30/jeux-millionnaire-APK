# Play Console - Préparation soumission v1.0.1

## Artifacts
- `releases/heritier-millionnaire-1.0.1(2)-20251111-1843.aab`
- (Optionnel QA) `releases/heritier-millionnaire-1.0.1(2)-20251111-1842.apk`

## Listing
- Mettre à jour la fiche française avec `mobile/STORE_LISTING_FR.md`
- Notes de version (FR):
  ```
  v1.0.1
  - Centre de confidentialité accessible depuis le menu principal
  - Correctif AdMob lorsque le consentement est refusé (annonces NPA)
  - Écran Debug Ads pour faciliter les tests QA
  ```
- Notes de version (EN - si besoin):
  ```
  v1.0.1
  - Added privacy center for GDPR preferences in-app
  - Fixed AdMob fallback for refused consent (NPA ads)
  - New Debug Ads screen for QA teams
  ```

## Tests fermés (optionnel)
1. Créer une piste "Test interne"
2. Importer l'AAB
3. Ajouter testeurs (compte QA + votre compte)
4. Lancer la publication et vérifier la livraison via Play Store

## Release production
1. Dupliquer la piste stable courante, renommer `v1.0.1`
2. Importer l'AAB
3. Mettre le numéro de version 1.0.1 / code 2
4. Ajoutez les notes de version FR/EN
5. Vérifier les captures et les catégories
6. Lancer la revue

## Post-soumission
- Surveiller l'onglet **Qualité -> Android vitals**
- Vérifier le remplissage AdMob après 24h
- Répondre aux retours utilisateurs sous 48h
