# Plan de bataille pour notre ParcoursSup.py.git

1. OK Comprendre ce qu'on va devoir implémenter,
2. OK Vérifier qu'on va savoir tout faire, et que tout sera faisable "simplement" en Python,
3. OK Commencer à écrire des modèles de script ou de notebook, avec des TODO clairs et une architecture déjà bien définie,
4. OK Travailler morceau par morceau,
5. OK Générer des données synthétiques, peut-être sous le même format que les exemples ([ordreappel/exemples](https://framagit.org/parcoursup/algorithmes-de-parcoursup/tree/master/java/parcoursup/ordreappel/exemples) et [propositions/exemples](https://framagit.org/parcoursup/algorithmes-de-parcoursup/tree/master/java/parcoursup/propositions/exemples)),
6. TODO Débogguer les algorithmes pour coller aux fichiers d'exemple de l'implémentation en Java.
7. Essayer chaque morceau sur de petits exemples de données (par exemple une ville avec 3 lycées, 3 classes de terminales chacun, et 3 établissements supérieur avec 3 formations chacun),
8. Écrire de belles explications,
9. Intégrer les contraintes dans l'algorithme (boursiers, candidats hors académie),
10. Ajouter les vœux dans les établissements avec internats,
11. Simuler sur plusieurs jours en simulant les choix de certains candidats ?
12. ??

---

[Ce document texte](https://framagit.org/parcoursup/algorithmes-de-parcoursup/blob/master/doc/implementation.txt) et [cet autre document PDF](https://framagit.org/parcoursup/algorithmes-de-parcoursup/blob/master/doc/presentation_algorithmes_parcoursup.pdf) donnent plein d'explications.

## Calcul de l'ordre d'appel
> TODO

## Calcul des propositions de formations
> TODO

## Calcul des propositions d'hébergement en internat
> TODO

---

# Bonus

## Carte interactive
- [La carte interactive](http://statistique.parcoursup.fr/) est impressionnante. On pourrait faire pareil (avec des données simulées, à l'échelle de la France ?!).
- Dans un notebook Jupyter, [IPyLeaflet](https://github.com/ellisonbg/ipyleaflet) est très facile à utiliser.
- En fait, on pourrait peut-être même utiliser le code de leur carte, mais avec nos données synthétiques !?

## Statistiques
- ?

---

### :scroll: Licence ? [![GitHub license](https://img.shields.io/github/license/Naereen/Parcoursup.py.svg)](https://github.com/Naereen/badges/blob/master/LICENSE)
Code libre, [sous licence MIT](https://lbesson.mit-license.org/) (file [LICENSE](LICENSE)).
© [Lilian Besson](https://GitHub.com/Naereen) et [Bastien Trotobas](https://github.com/BastienTr) et collaborateurs, 2018.

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/Parcoursup.py/graphs/commit-activity)
[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](https://GitHub.com/Naereen/ama)
[![Analytics](https://ga-beacon.appspot.com/UA-38514290-17/github.com/Naereen/Parcoursup.py/README.md?pixel)](https://GitHub.com/Naereen/Parcoursup.py/)
[![ForTheBadge uses-badges](http://ForTheBadge.com/images/badges/uses-badges.svg)](http://ForTheBadge.com)
[![ForTheBadge uses-git](http://ForTheBadge.com/images/badges/uses-git.svg)](https://GitHub.com/)
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![ForTheBadge built-with-science](http://ForTheBadge.com/images/badges/built-with-science.svg)](https://GitHub.com/Naereen/)
