# Héritier Millionnaire — distribution Android

Ce dépôt conserve les APK et AAB historiques. Le code de l’application Android est maintenu dans [mobile-jeux-millionnaire](https://github.com/nowis30/mobile-jeux-millionnaire), le client dans [client-jeux-millionnaire](https://github.com/nowis30/client-jeux-millionnaire), et l’API dans [server-jeux-millionnaire](https://github.com/nowis30/server-jeux-millionnaire).

## Télécharger une version publiée

Consultez les [GitHub Releases](https://github.com/nowis30/jeux-millionnaire-APK/releases). Un fichier présent dans la branche principale, un build `debug` ou un numéro figurant dans son nom ne constitue pas une publication validée. Un AAB sert à la distribution par une boutique; ce n’est pas un APK installable directement.

Le [manifeste des fichiers](artifact-manifest.json) donne le nom, la taille et le SHA-256 des binaires suivis par Git. Ces empreintes détectent une modification du fichier; elles ne certifient ni son signataire Android, ni son fonctionnement, ni le commit source qui a servi à le compiler. Les anciens binaires ne sont pas reconstruits par cette maintenance.

## Vérifier les fichiers

Avec Python 3, après clonage :

```sh
python3 scripts/artifact_manifest.py --check
```

Pour recalculer le manifeste après l’ajout volontaire d’un binaire :

```sh
python3 scripts/artifact_manifest.py
```

La CI compare les fichiers avec le manifeste et refuse une différence non documentée.

## Préparer les prochaines publications

Construire depuis un commit précis de `mobile-jeux-millionnaire`, puis joindre à chaque Release l’APK ou l’AAB, son SHA-256, la version et le code Android, le commit source, les notes de changements et les résultats de validation sur appareil. Vérifier la signature avec les outils Android avant publication. Conserver les clés de signature hors du dépôt.

Les nouveaux binaires devraient être joints aux Releases afin d’éviter de grossir l’historique Git. Les fichiers existants sont conservés pour ne pas casser les anciens liens. Les instructions de 2025 sont archivées dans [README-legacy-2025.md](docs/README-legacy-2025.md); elles décrivent une ancienne architecture et ne doivent pas servir de procédure actuelle.
