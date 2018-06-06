# :baby: :fr: Un clone en Python 3 de [Parcoursup](http://www.parcoursup.fr/), écrit à but didactique
> [Écrit par](AUTHORS) [Lilian Besson (@Naereen)](https://github.com/Naereen) et [Bastien Trotobas (@BastienTr)](https://github.com/BastienTr), et d'autres collaborateurs.

## Table des matières
- [:baby: :fr: Un clone en Python 3 de Parcoursup, écrit à but didactique](#baby---fr--un-clone-en-python-3-de-parcoursuphttp---wwwparcoursupfr---ecrit-a-but-didactique)
    - [Table des matières](#table-des-matieres)
    - [Présentation](#presentation)
    - [Plan de bataille](#plan-de-batailletodomd)
    - [Explications](#explications)
    - [Organisation de ce dépôt](#organisation-de-ce-depot)
    - [Démonstration dans un notebook Jupyter ?](#demonstration-dans-un-notebook-jupyterhttps---wwwjupyterorg)
    - [Documentation et ressources](#documentation-et-ressources)
    - [Exemples](#exemples)
        - [Installation](#installation)
        - [Tests](#tests)
    - [À propos](#a-propos)
        - [Language ?](#language)
        - [:scroll: Licence ? ![GitHub license](https://github.com/Naereen/badges/blob/master/LICENSE)](#scroll--licence-github-licensehttps---imgshieldsio-github-license-naereen-parcoursuppysvghttps---githubcom-naereen-badges-blob-master-license)

## Présentation

Ce dépôt contient un (petit) clone de l'algorithme régissant la [plateforme Parcoursup](http://www.parcoursup.fr/), qui gère depuis 2018 les affectations des élèves de classe de Terminale dans leur formation dans l'enseignement supérieur.

L'algorithme et son implémentation officielle (en Java), sont disponibles sur [ce site (framagit.org/parcoursup/algorithmes-de-parcoursup)](https://framagit.org/parcoursup/algorithmes-de-parcoursup).

- Nous proposons ici une implémentation simplifiée des différents algorithmes de Parcoursup, en Python et dans un but didactique.
- Nous avons pour objectif de comprendre et d'expliquer ces algorithmes, en utilisant que des notions et des modules Python qui soient abordables compréhensibles par des élèves de classes préparatoires scientifiques (typiquement des MPSI).
- Vous pouvez contribuer si vous le souhaiter !

---

## [Plan de bataille](TODO.md)

## Explications

* TODO expliquer un peu.

## Organisation de ce dépôt

- Le code des algorithmes est [dans le dossier `src/`](src/),
- Les (exemples de) données sont [dans le dossier `donnees/`](donnees/),
- Des utilitaires, notamment les scripts pour générer des données synthétiques sont [dans le dossier `utils/`](utils/),
- Des visualisations sont dans [le dossier `notebooks/`](notebooks/),
- Enfin, une documentation est disponible dans [le dossier `docs/`](docs/).

* TODO enlever ce qui n'est pas nécessaire.

## Démonstration dans un [notebook Jupyter](https://www.Jupyter.org/) ?
* TODO si besoin ?

---

## Documentation et ressources

- La page officielle de présentation de Parcoursup est [ici](http://www.enseignementsup-recherche.gouv.fr/pid37384/parcoursup-plateforme-admission-dans-superieur.html) (en 2018).

- Les indicateurs quotidiennement publiés par le ministère sont sur [cette page là](http://www.enseignementsup-recherche.gouv.fr/cid130714/tableaux-de-bord-des-indicateurs-de-parcoursup.html) (en juin 2018).

- Cette carte qui montre jour après jour les résultats donnés par Parcoursup : [statistique.parcoursup.fr](http://statistique.parcoursup.fr/).

- [Le dossier de presse du ministère](http://cache.media.enseignementsup-recherche.gouv.fr/file/Parcoursup/73/7/DP_Parcoursup_-_Au_service_de_l_orientation_et_de_la_reussite_des_futurs_etudiants_936737.pdf) pour Parcoursup

- [Ce document texte](https://framagit.org/parcoursup/algorithmes-de-parcoursup/blob/master/doc/implementation.txt) et [cet autre document PDF](https://framagit.org/parcoursup/algorithmes-de-parcoursup/blob/master/doc/presentation_algorithmes_parcoursup.pdf) donnent plein d'explications.

- Ces articles sur des blogs du Monde: sur [ingenuingenieur.blog.lemonde.fr](http://ingenuingenieur.blog.lemonde.fr/2018/05/29/parcoursup-2018-les-dessous-de-lalgorithme-racontes-par-ses-createurs/), sur [enseigner.blog.lemonde.fr](http://enseigner.blog.lemonde.fr/2018/04/03/parcoursup-naivete-habilete-ou-machiavelisme-gouvernemental/) ou sur [binaire.blog.lemonde.fr](http://binaire.blog.lemonde.fr/2018/06/05/la-transparence-a-lecole-de-parcoursup/).

----

## Exemples
### Installation

Ces lignes de bash (à exécuter sur une machine type GNU/Linux ou un Mac avec les outils standards) clone ce dépôt, et installent un [`virtualenv` Python](https://virtualenv.pypa.io/) et installent [les dépendances](requirements.txt) dans cet environnement virtuel :

```bash
cd /tmp/
git clone https://GitHub.com/Naereen/Parcoursup.py
cd Parcoursup.py/
make install
```

### Tests

Les tests qui reproduisent [les données d'exemples](donnees) peuvent être exécutés avec les deux commandes suivantes :

- Ordres d'appel :
```bash
$ python3 ./src/ordreappel/__init__.py
...
```

- Proposition de vœux :
```bash
$ python3 ./src/propositions/__init__.py
...
```

----

## À propos
### Language ?
[Python v3.6+](https://docs.python.org/3.6/).  Avec les [modules suivants](requirements.txt) :

- [Numpy](http://numpy.org/) pour les tableaux,
- [matplotlib](http://matplotlib.org/) pour les affichages,
- [pandas](http://pandas.pydata.org/) pour les statistiques,
- [La bibliothèque standard](https://docs.python.org/3.6/) pour tout le reste.


### :scroll: Licence ? [![GitHub license](https://img.shields.io/github/license/Naereen/Parcoursup.py.svg)](https://github.com/Naereen/badges/blob/master/LICENSE)
Code lire, [sous licence MIT](https://lbesson.mit-license.org/) (file [LICENSE](LICENSE)).
© [Lilian Besson](https://GitHub.com/Naereen) et [Bastien Trotobas] et collaborateurs, 2018.

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/Parcoursup.py/graphs/commit-activity)
[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](https://GitHub.com/Naereen/ama)
[![Analytics](https://ga-beacon.appspot.com/UA-38514290-17/github.com/Naereen/Parcoursup.py/README.md?pixel)](https://GitHub.com/Naereen/Parcoursup.py/)

[![ForTheBadge uses-badges](http://ForTheBadge.com/images/badges/uses-badges.svg)](http://ForTheBadge.com)
[![ForTheBadge uses-git](http://ForTheBadge.com/images/badges/uses-git.svg)](https://GitHub.com/)

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![ForTheBadge built-with-science](http://ForTheBadge.com/images/badges/built-with-science.svg)](https://GitHub.com/Naereen/)
