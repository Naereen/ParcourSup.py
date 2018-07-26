# :fr: Un clone en Python 3 de [Parcoursup](http://www.parcoursup.fr/), écrit à but didactique
<a href="https://perso.crans.org/besson/publis/ParcourSup.py/"><img align="right" src="../docs/_static/logo_parcoursuppy.png" alt="Lien vers la documentation Sphinx du projet" width="40%"/></a>

> [Écrit par](AUTHORS) [Lilian Besson (@Naereen)](https://github.com/Naereen) et [Bastien Trotobas (@BastienTr)](https://github.com/BastienTr), et d'autres collaborateur-trice-s.

## Données

Ce dossier contient des données **synthétiques** et de tests.

---

## Tests

> [Ce petit script Bash](compare_avec_donnees_references.sh) permet de vérifier que les fichiers XML produit par notre implémentation sont identiques à ceux [des exemples fournis](https://framagit.org/parcoursup/algorithmes-de-parcoursup/tree/master/doc/exemples).

```bash
$ ./compare_avec_donnees_references.sh
- Checking exemple_A1_entree.xml ...
  Perfectly matching algorithmes-de-parcoursup.git/doc/exemples/exemple_A1_entree.xml
...  # more
- Checking exemple_A6_sortie.xml ...
  Perfectly matching algorithmes-de-parcoursup.git/doc/exemples/exemple_A6_sortie.xml
```

### Ordre d'appels

Les 6 fichiers de tests pour [l'algorithme de calcul d'ordre d'appel](src/ordreappel/) qui [sont fournis](https://framagit.org/parcoursup/algorithmes-de-parcoursup/tree/master/doc/exemples) pour le code de l'outil officiel sont reproduits par notre implémentation :

- Exemple A1 : [entrée en XML](exemple_A1_entree.xml) ([aussi en JSON](exemple_A1_entree.json)), et [sortie en XML](exemple_A1_sortie.xml) ([aussi en JSON](exemple_A1_sortie.json)),
- Exemple A2 : [entrée en XML](exemple_A2_entree.xml) ([aussi en JSON](exemple_A2_entree.json)), et [sortie en XML](exemple_A2_sortie.xml) ([aussi en JSON](exemple_A2_sortie.json)),
- Exemple A3 : [entrée en XML](exemple_A3_entree.xml) ([aussi en JSON](exemple_A3_entree.json)), et [sortie en XML](exemple_A3_sortie.xml) ([aussi en JSON](exemple_A3_sortie.json)),
- Exemple A4 : [entrée en XML](exemple_A4_entree.xml) ([aussi en JSON](exemple_A4_entree.json)), et [sortie en XML](exemple_A4_sortie.xml) ([aussi en JSON](exemple_A4_sortie.json)),
- Exemple A5 : [entrée en XML](exemple_A5_entree.xml) ([aussi en JSON](exemple_A5_entree.json)), et [sortie en XML](exemple_A5_sortie.xml) ([aussi en JSON](exemple_A5_sortie.json)),
- Exemple A6 : [entrée en XML](exemple_A6_entree.xml) ([aussi en JSON](exemple_A6_entree.json)), et [sortie en XML](exemple_A6_sortie.xml) ([aussi en JSON](exemple_A6_sortie.json)).

### Propositions des affectations

TODO

Les 7 fichiers de tests pour [l'algorithme de propositions des affectations](src/propositions/) qui [sont fournis](https://framagit.org/parcoursup/algorithmes-de-parcoursup/tree/master/doc/exemples) pour le code de l'outil officiel sont reproduits par notre implémentation :

- Exemple d'une entrée aléatoire [en XML](ExempleAleatoire_entree.xml) ([aussi en JSON](ExempleAleatoire_entree.json)),
- Exemple B7, jour 1 : [entrée en XML](ExempleB7Jour1_entree.xml) ([aussi en JSON](ExempleB7Jour1_entree.xml)), et [sortie en XML](ExempleB7Jour1_sortie.xml) ([aussi en JSON](ExempleB7Jour1_sortie.xml)),
- Exemple B7, jour 2 : [entrée en XML](ExempleB7Jour2_entree.xml) ([aussi en JSON](ExempleB7Jour2_entree.xml)), et [sortie en XML](ExempleB7Jour2_sortie.xml) ([aussi en JSON](ExempleB7Jour2_sortie.xml)),
- Exemple B7, jour 3 : [entrée en XML](ExempleB7Jour3_entree.xml) ([aussi en JSON](ExempleB7Jour3_entree.xml)), et [sortie en XML](ExempleB7Jour3_sortie.xml) ([aussi en JSON](ExempleB7Jour3_sortie.xml)).

---

### :scroll: Licence ? [![GitHub license](https://img.shields.io/github/license/Naereen/Parcoursup.py.svg)](https://github.com/Naereen/badges/blob/master/LICENSE)
Code libre, [sous licence MIT](https://lbesson.mit-license.org/) (file [LICENSE](LICENSE)).
© [Lilian Besson](https://GitHub.com/Naereen) et [Bastien Trotobas](https://github.com/BastienTr) et collaborateur-trice-s, 2018.

![PyPI implementation](https://img.shields.io/pypi/implementation/smpybandits.svg)
![PyPI pyversions](https://img.shields.io/pypi/pyversions/smpybandits.svg)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/Parcoursup.py/graphs/commit-activity)
[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](https://GitHub.com/Naereen/ama)
[![Analytics](https://ga-beacon.appspot.com/UA-38514290-17/github.com/Naereen/Parcoursup.py/README.md?pixel)](https://GitHub.com/Naereen/Parcoursup.py/)

[![ForTheBadge uses-badges](http://ForTheBadge.com/images/badges/uses-badges.svg)](http://ForTheBadge.com)
[![ForTheBadge uses-git](http://ForTheBadge.com/images/badges/uses-git.svg)](https://GitHub.com/)
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![ForTheBadge built-with-science](http://ForTheBadge.com/images/badges/built-with-science.svg)](https://GitHub.com/Naereen/)
