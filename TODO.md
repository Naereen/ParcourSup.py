# Plan de bataille pour notre ParcoursSup.py.git

1. Comprendre ce qu'on va devoir implémenter,
2. Vérifier qu'on va savoir tout faire, et que tout sera faisable "simplement" en Python,
3. Commencer à écrire des modèles de script ou de notebook, avec des TODO clairs et une architecture déjà bien définie,
4. Travailler morceau par morceau,
5. Générer des données synthétiques, peut-être sous le même format que les exemples ([ordreappel/exemples](https://framagit.org/parcoursup/algorithmes-de-parcoursup/tree/master/java/parcoursup/ordreappel/exemples) et [propositions/exemples](https://framagit.org/parcoursup/algorithmes-de-parcoursup/tree/master/java/parcoursup/propositions/exemples)),
6. Essayer chaque morceau sur de petits exemples de données (par exemple une ville avec 3 lycées, 3 classes de terminales chacun, et 3 établissements supérieur avec 3 formations chacun),
7. Écrire de belles explications,
8. Intégrer les contraintes dans l'algorithme (boursiers, candidats hors académie),
9. Ajouter les vœux dans les établissements avec internats,
10. Simuler sur plusieurs jours en simulant les choix de certains candidats ?
11. ??

---

[Ce document texte](https://framagit.org/parcoursup/algorithmes-de-parcoursup/blob/master/doc/implementation.txt) et [cet autre document PDF](https://framagit.org/parcoursup/algorithmes-de-parcoursup/blob/master/doc/presentation_algorithmes_parcoursup.pdf) donnent plein d'explications.

## Calcul de l'ordre d'appel


## Calcul des propositions de formations


## Calcul des propositions d'hébergement en internat

---

# Bonus

## Carte interactive
- [La carte interactive](http://statistique.parcoursup.fr/) est impressionnante. On pourrait faire pareil (avec des données simulées).
- Dans un notebook Jupyter, [IPyLeaflet](https://github.com/ellisonbg/ipyleaflet) est très facile à utiliser.
- En fait, on pourrait peut-être même utiliser le code de leur carte, mais avec nos données synthétiques !?

## Statistiques
- ?
