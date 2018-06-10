# :baby: :fr: Un clone en Python 3 de [Parcoursup](http://www.parcoursup.fr/), écrit à but didactique
> [Écrit par](AUTHORS) [Lilian Besson (@Naereen)](https://github.com/Naereen) et [Bastien Trotobas (@BastienTr)](https://github.com/BastienTr), et d'[autres collaborateurs](https://github.com/Naereen/ParcourSup.py/graphs/contributors).

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
        - [:scroll: Licence ? ![GitHub license](https://github.com/Naereen/ParcourSup.py/blob/master/LICENSE)](#scroll--licence-github-licensehttps---imgshieldsio-github-license-naereen-parcoursuppysvghttps---githubcom-naereen-parcoursuppy-blob-master-license)

## Présentation

Ce dépôt contient un clone (presque complet) des algorithmes régissant la [plateforme Parcoursup](http://www.parcoursup.fr/), qui gère depuis 2018 les affectations des élèves de classe de Terminale (🇫🇷 dans les lycées en France) dans leurs formations dans l'enseignement supérieur.

Les algorithmes et l'implémentation officielle (en Java) ont été distribué en accès libre et sous licence libre (GPL) en mai 2018. En 2018, ils étaient hébergés sur [ce site (framagit.org/parcoursup/algorithmes-de-parcoursup)](https://framagit.org/parcoursup/algorithmes-de-parcoursup).

- Nous proposons ici une implémentation des différents algorithmes de Parcoursup, écrite en Python, dans un style très clair, avec moult commentaires et documentation.
- Nous avons pour objectif de comprendre et d'expliquer ces algorithmes, en utilisant au maximum des notions et des modules Python qui soient abordables et compréhensibles par des élèves de classes préparatoires scientifiques (typiquement des MPSI).
- *Note* : Vous pouvez contribuer si vous le souhaiter ! [Une erreur à signaler ?](https://github.com/Naereen/ParcourSup.py/issues/new), ou [une contribution possible](https://github.com/Naereen/ParcourSup.py/pulls/) ? :clap: Merci d'avance !

---

## [Plan de bataille](TODO.md)
> Pour le développement en cours.

## Explications

* TODO expliquer un peu ce qu'on a implémenté et pas encore fait.
* TODO expliquer l'algorithme dans les grandes lignes.

## Organisation de ce dépôt

- Le code des algorithmes est [dans le dossier `src/`](src/), comme le code Java initial, c'est découpé en deux modules, [`ordreappel`](src/ordreappel) et [`propositions`](src/propositions),
- Les (exemples de) données synthétiques générées sont [dans le dossier `donnees/`](donnees/),
- TODO Des visualisations sont dans [le dossier `notebooks/`](notebooks/),
- TODO Enfin, une documentation est disponible dans [le dossier `docs/`](docs/),
- Des utilitaires sont [dans le dossier `utils/`](utils/),

## Démonstration dans un [notebook Jupyter](https://www.Jupyter.org/) ?
* TODO si besoin ?

---

## Documentation officielle et ressources

- La page officielle de présentation de Parcoursup est [ici](http://www.enseignementsup-recherche.gouv.fr/pid37384/parcoursup-plateforme-admission-dans-superieur.html) (en 2018).

Communication journalière, entre le 23 mai 2018 et le 15 juillet 2018 :

- Les indicateurs quotidiennement publiés par le ministère sont sur [cette page là](http://www.enseignementsup-recherche.gouv.fr/cid130714/tableaux-de-bord-des-indicateurs-de-parcoursup.html) (en juin 2018).

- Cette carte qui montre jour après jour les résultats donnés par Parcoursup : [statistique.parcoursup.fr](http://statistique.parcoursup.fr/). <span style="color:red;">C'est bizarre, la carte marchait le 5 juin, elle semble désactivée depuis !</span>

Des détails sur les algorithmes :

- [Ce document texte](https://framagit.org/parcoursup/algorithmes-de-parcoursup/blob/master/doc/implementation.txt) et [cet autre document PDF](https://framagit.org/parcoursup/algorithmes-de-parcoursup/blob/master/doc/presentation_algorithmes_parcoursup.pdf) donnent plein d'explications.

Autres ressources, moins techniques mais plus pédagogiques :

- [Le dossier de presse du ministère](http://cache.media.enseignementsup-recherche.gouv.fr/file/Parcoursup/73/7/DP_Parcoursup_-_Au_service_de_l_orientation_et_de_la_reussite_des_futurs_etudiants_936737.pdf) pour Parcoursup

- Ces articles sur des blogs du Monde: sur [ingenuingenieur.blog.lemonde.fr](http://ingenuingenieur.blog.lemonde.fr/2018/05/29/parcoursup-2018-les-dessous-de-lalgorithme-racontes-par-ses-createurs/), sur [enseigner.blog.lemonde.fr](http://enseigner.blog.lemonde.fr/2018/04/03/parcoursup-naivete-habilete-ou-machiavelisme-gouvernemental/) ou sur [binaire.blog.lemonde.fr](http://binaire.blog.lemonde.fr/2018/06/05/la-transparence-a-lecole-de-parcoursup/).

----

## Exemples
### Installation

Ces lignes de [Bash](https://www.gnu.org/software/bash/) (à exécuter sur une machine type GNU/Linux ou un Mac avec les outils standards) clone ce dépôt, et installent un [`virtualenv` Python](https://virtualenv.pypa.io/) et installent [les dépendances](requirements.txt) dans cet environnement virtuel :

```bash
cd /tmp/
git clone https://GitHub.com/Naereen/Parcoursup.py
cd Parcoursup.py/
make install
```

> Note : notre code n'est pas spécifiquement écrit pour une machine utilisant GNU/Linux, et il devrait fonctionner sur n'importe quelle plateforme qui supporte Python 3.6 (Microsoft Windows et Mac OS X notamment). [N'hésitez pas à signaler un problème](https://github.com/Naereen/ParcourSup.py/issues/new), si besoin. :clap: Merci d'avance !

### Tests

Les tests qui reproduisent [les données d'exemples](donnees) peuvent être exécutés avec les deux commandes suivantes :

- Ordres d'appel :
```bash
$ . env/bin/activate ; python3 ./src/ordreappel/__init__.py
...
```

- Proposition de vœux :
```bash
$ . env/bin/activate ; python3 ./src/propositions/__init__.py
...
```
- Ces deux tests prennent environ 30 secondes chacun.

----

## À propos
### Language et versions ?
[Python v3.6+](https://docs.python.org/3.6/).  Avec les [modules suivants](requirements.txt) :

- [Numpy](http://numpy.org/) pour les tableaux, (TODO enlever si pas nécessaire),
- [matplotlib](http://matplotlib.org/) pour les affichages, (TODO enlever si pas nécessaire),
- [pandas](http://pandas.pydata.org/) pour les statistiques, (TODO enlever si pas nécessaire),
- [La bibliothèque standard](https://docs.python.org/3.6/) pour tout le reste.

### :scroll: Licence ? [![GitHub license](https://img.shields.io/github/license/Naereen/Parcoursup.py.svg)](https://github.com/Naereen/Parcoursup.py/blob/master/LICENSE)
Code libre, [sous licence MIT](https://lbesson.mit-license.org/) (file [LICENSE](LICENSE)).
© [Lilian Besson](https://GitHub.com/Naereen) et [Bastien Trotobas](https://github.com/BastienTr) et collaborateurs, 2018.

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/Parcoursup.py/graphs/commit-activity)
[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](https://GitHub.com/Naereen/ama)
[![Analytics](https://ga-beacon.appspot.com/UA-38514290-17/github.com/Naereen/Parcoursup.py/README.md?pixel)](https://GitHub.com/Naereen/Parcoursup.py/)
[![ForTheBadge uses-badges](http://ForTheBadge.com/images/badges/uses-badges.svg)](http://ForTheBadge.com)
[![ForTheBadge uses-git](http://ForTheBadge.com/images/badges/uses-git.svg)](https://GitHub.com/)
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![ForTheBadge built-with-science](http://ForTheBadge.com/images/badges/built-with-science.svg)](https://GitHub.com/Naereen/)
