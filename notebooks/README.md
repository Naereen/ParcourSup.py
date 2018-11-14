# :fr: Un clone en Python 3 de [Parcoursup](http://www.parcoursup.fr/), écrit à but didactique
<a href="https://perso.crans.org/besson/publis/ParcourSup.py/"><img align="right" src="../docs/_static/logo_parcoursuppy.png" alt="Lien vers la documentation Sphinx du projet" width="40%"/></a>

> [Écrit par](AUTHORS) [Lilian Besson (@Naereen)](https://github.com/Naereen) et [Bastien Trotobas (@BastienTr)](https://github.com/BastienTr), et d'autres collaborateur-trice-s.

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/Naereen/ParcourSup.py/master?filepath=notebooks%2FParcourSup.py_version_simplifiee.ipynb)

## Notebooks

Ce dossier contient des ressources supplémentaires pour expliquer les algorithmes de Parcoursup sous forme de [Notebooks Jupyter](https://jupyter.org/).

## Version simplifiée des algorithmes de ParcourSup

### 1) Calcul de l'ordre d'appel
> C'est la partie qui est implémentée [dans ce dossier `parcoursup/ordreappel`](../parcoursup/ordreappel/).

- [Ce notebook](ParcourSup.py_version_simplifiee.ipynb) étudie l'algorithme 1 de calcul des ordres d'appels. Pour une formation, avec N candidats-es l'ayant demandés, les professeurs de la formation classent les N candidats-es, et ensuite l'algorithme s'occupe de réordonner certains vœux en fonction du taux minimum de boursiers-ères et du taux minimum de résidents-entes.

  + L'algorithme est assez simple s'il n'y a que la contrainte du taux de boursiers-ères à respecter :
    ![](images/Algorithme_CalculOrdreAppelJusteTauxBoursiers.png)

  + L'algorithme est plus compliqué s'il y a la contrainte du taux de boursier-ère-s et la contrainte du taux de résident-e à respecter, mais c'est très similaire. La seule chose à savoir est qu'en cas d'incompatibilité des deux contraintes, la priorité est donnée à la première contrainte sur les boursier-ère-s :
    ![](images/Algorithme_CalculOrdreAppel.png)

- Les deux exemples suivants de visualisations montrent l'interface de visualisation interactive que l'on est en train de construire dans cet exemple :

  + Si on regarde une liste de vœux, on représente en gris les vœux ni boursiers ni résidents, en rouge les boursiers, en bleu les résidents et en violet les boursiers résidents. La vidéo montre que l'interface interactive permet de créer des listes de vœux triées aléatoirement, et montre l'influence des deux taux (minimum de boursiers et minimum de résidents) sur le classement final.
    ![Visualisation_OrdreAppel_avec_couleurs](images/Visualisation_OrdreAppel_avec_couleurs.gif)

  + Cette fois on a aussi le contrôle d'un vœu en particulier, représenté en couleur plus vive. La vidéo montre l'influence des deux taux (minimum de boursiers et minimum de résidents) sur le classement final de ce vœu en comparaison à d'autres.
    ![Visualisation_OrdreAppel_focus_sur_un_voeu](images/Visualisation_OrdreAppel_focus_sur_un_voeu.gif)

- Voici un lien qui ouvre le notebook avec [MyBinder](https://mybinder.org/), pour vous laisser exécuter le code par vous-même.
  [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/Naereen/ParcourSup.py/master?filepath=notebooks%2FParcourSup.py_version_simplifiee.ipynb)

- Voici un lien qui ouvre le notebook avec [Google Colab](https://colab.research.google.com/notebook), pour vous laisser exécuter le code par vous-même.
  [![Google Colab](https://badgen.net/badge/Lancer/sur%20Google%20Colab/blue?icon=terminal)](https://colab.research.google.com/github/Naereen/ParcourSup.py/blob/master/notebooks/ParcourSup.py_version_simplifiee.ipynb)

### 2) Calcul des propositions
> C'est la partie qui est implémentée [dans ce dossier `parcoursup/propositions`](../parcoursup/propositions/).

- TODO

---

## Exemples d'utilisation de l'implémentation complète de ParcourSup.py

- TODO

---

### :scroll: Licence ? [![GitHub license](https://img.shields.io/github/license/Naereen/Parcoursup.py.svg)](https://github.com/Naereen/badges/blob/master/LICENSE)
Code libre, [sous licence MIT](https://lbesson.mit-license.org/) (file [LICENSE](LICENSE)).
© [Lilian Besson](https://GitHub.com/Naereen) et [Bastien Trotobas](https://github.com/BastienTr) et collaborateur-trice-s, 2018.

[![PyPI implementation](https://img.shields.io/pypi/implementation/smpybandits.svg)](https://www.python.org/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/smpybandits.svg)](https://docs.python.org/3/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/Parcoursup.py/graphs/commit-activity)
[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](https://GitHub.com/Naereen/ama)
[![Analytics](https://ga-beacon.appspot.com/UA-38514290-17/github.com/Naereen/Parcoursup.py/README.md?pixel)](https://GitHub.com/Naereen/Parcoursup.py/)

[![ForTheBadge uses-badges](http://ForTheBadge.com/images/badges/uses-badges.svg)](http://ForTheBadge.com)
[![ForTheBadge uses-git](http://ForTheBadge.com/images/badges/uses-git.svg)](https://GitHub.com/)
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![ForTheBadge built-with-science](http://ForTheBadge.com/images/badges/built-with-science.svg)](https://GitHub.com/Naereen/)
