Un clone en Python 3 de `Parcoursup <http://www.parcoursup.fr/>`_, écrit à but didactique
==========================================================================================

    `Écrit par <AUTHORS>`_ deux doctorants de `l'équipe
    SCEE <http://www-scee.rennes.supelec.fr/wp/phd/>`_ de
    `CentraleSupélec, campus de
    Rennes <http://www.rennes.centralesupelec.fr/>`_, `Lilian Besson (Naereen) <https://github.com/Naereen>`_ et `Bastien Trotobas (BastienTr) <https://github.com/BastienTr>`_, et d'`autres
    collaborateur-trice-s <https://github.com/Naereen/ParcourSup.py/graphs/contributors>`_.

|Open Source ? Oui !| |Implementation| |Version de Python| |Maintenance|
|Ask Me Anything !| |Analytics| |Documentation Status| |Build Status|
|Stars of https://github.com/Naereen/ParcourSup.py/| |Releases of
https://github.com/Naereen/ParcourSup.py/|

Présentation
------------

Ce dépôt contient un clone (presque complet) des algorithmes régissant
la `plateforme Parcoursup <http://www.parcoursup.fr/>`_, qui gère
depuis 2018 les affectations des élèves de classe de Terminale (dans
les lycées en France) dans leurs formations dans l'enseignement
supérieur.

Les algorithmes et l'implémentation officielle (en Java) ont été
distribués en accès libre, et sous licence libre (GPL), en mai 2018. En
2018, ils étaient hébergés sur `ce site
(framagit.org/parcoursup/algorithmes-de-parcoursup) <https://framagit.org/parcoursup/algorithmes-de-parcoursup>`_.

-  Nous proposons ici une implémentation complète des différents
   algorithmes de Parcoursup, écrite en Python 3, dans un style très
   clair, avec des commentaires, et `une
   documentation <https://perso.crans.org/besson/publis/ParcourSup.py/parcoursup.html#module-parcoursup>`_.
   |Documentation Status|
-  Nous avons pour objectif de comprendre et d'expliquer ces
   algorithmes, en utilisant au maximum des notions et des modules
   Python qui soient abordables et compréhensibles par des élèves de
   classes préparatoires scientifiques (typiquement des MPSI).
-  *Note* : Vous pouvez contribuer si vous le souhaiter ! `Une erreur à
   signaler ? <https://github.com/Naereen/ParcourSup.py/issues/new>`_,
   ou `une contribution
   possible <https://github.com/Naereen/ParcourSup.py/pulls/>`_ ?
   Merci d'avance !

--------------

Plan de bataille
----------------

    Pour le développement en cours, cf. ce fichier
    `TODO.md <TODO.md>`_ !

..

    |Commits of https://github.com/Naereen/ParcourSup.py/| / |Date of
    last commit of https://github.com/Naereen/ParcourSup.py/| |Issues of
    https://github.com/Naereen/ParcourSup.py/| : |Open issues of
    https://github.com/Naereen/ParcourSup.py/| / |Closed issues of
    https://github.com/Naereen/ParcourSup.py/|

Explications
------------

-  Pour l'instant, nous avons implémenté dans le dossier
   `parcoursup/ <parcoursup/>`_ un clone complet du code Java
   initial, écrit en Python 3.
-  Et dans le dossier `notebooks/ <notebooks/>`_ nous proposons des
   implémentations simplifiées des principaux algorithmes, écrites sans
   dépendances et dans un style très didactique, avec des visualisations
   interactives afin de permettre à tout le monde d'expérimenter un peu
   et de visualiser le comportement des algorithmes. L'accent est mis
   sur la compréhension rapide de l'influence des différents paramètres
   numériques.

-  TODO expliquer l'algorithme dans les grandes lignes, avec notre
   propre vocabulaire, ici.

Organisation de ce dépôt
------------------------

-  Des visualisations sont `aussi dans le dossier
   notebooks/ <notebooks/>`_. TODO encore à travailler !
-  Le code des algorithmes est `dans le dossier
   parcoursup/ <parcoursup/>`_, comme le code Java initial, c'est
   découpé en deux modules, `ordreappel <parcoursup/ordreappel>`_
   et `propositions <parcoursup/propositions>`_,
-  Les (exemples de) données synthétiques générées sont `dans le dossier
   donnees/ <donnees/>`_,
-  Des tests (plusieurs centaines) sont présents dans le dossier
   `tests/ <tests/>`_, inspirés par `ce
   projet <https://github.com/JosePaumard/tests-pour-parcoursup>`_,
   |Build Status|
-  Une documentation de notre implémentation complète est disponible en
   ligne, `sur la page
   suivante <https://perso.crans.org/besson/publis/ParcourSup.py/>`_,
   construite avec Sphinx à partir des fichiers présents dans `le
   dossier docs/ <docs/>`_,
-  Des utilitaires sont `dans le dossier utils/ <utils/>`_,

Démonstration dans un `notebook Jupyter <https://www.Jupyter.org/>`_
---------------------------------------------------------------------

-  Des visualisations sont dans `le dossier
   notebooks/ <notebooks/>`_.

|Binder|

|Google Colab|

--------------

Documentation officielle et ressources
--------------------------------------

-  La page officielle de présentation de Parcoursup est
   `ici <http://www.enseignementsup-recherche.gouv.fr/pid37384/parcoursup-plateforme-admission-dans-superieur.html>`_
   (en 2018).

Communications journalistiques, entre le 23 mai 2018 et le 15 juillet
2018 :

-  Les indicateurs quotidiennement publiés par le ministère sont sur
   `cette page
   là <http://www.enseignementsup-recherche.gouv.fr/cid130714/tableaux-de-bord-des-indicateurs-de-parcoursup.html>`_
   (en juin 2018).

-  Cette carte qui montre jour après jour les résultats donnés par
   Parcoursup :
   `statistiques.parcoursup.fr <http://statistiques.parcoursup.fr/>`_.
   > Nous voulons proposer notre propre carte de visualisation, `c'est
   en cours <https://github.com/Naereen/ParcourSup.py/issues/8>`_…

Des détails sur les algorithmes :

-  `Ce document
   texte <https://framagit.org/parcoursup/algorithmes-de-parcoursup/blob/master/doc/implementation.txt>`_
   et `cet autre document
   PDF <https://framagit.org/parcoursup/algorithmes-de-parcoursup/blob/master/doc/presentation_algorithmes_parcoursup.pdf>`_
   donnent plein d'explications.

-  `Ce texte du Journal
   Officiel <https://www.legifrance.gouv.fr/affichTexte.do?cidTexte=JORFTEXT000036748597&dateTexte=20180724>`_
   montre l'autorisation donnée par la CNIL pour la création de la base
   de données pour Parcoursup, et détaille un peu toutes les
   informations stockées pour le service. Il est important de garder en
   tête que ces données ne sont **pas** utilisées par les algorithmes de
   Parcoursup, qui n'utilisent qu'un identifiant unique et anonyme pour
   identifier chaque candidat-e.

Autres ressources, moins techniques mais plus pédagogiques :

-  `Le dossier de presse du
   ministère <http://cache.media.enseignementsup-recherche.gouv.fr/file/Parcoursup/73/7/DP_Parcoursup_-_Au_service_de_l_orientation_et_de_la_reussite_des_futurs_etudiants_936737.pdf>`_
   pour Parcoursup

-  Ces articles sur des blogs du Monde: sur
   `ingenuingenieur.blog.lemonde.fr <http://ingenuingenieur.blog.lemonde.fr/2018/05/29/parcoursup-2018-les-dessous-de-lalgorithme-racontes-par-ses-createurs/>`_,
   sur
   `enseigner.blog.lemonde.fr <http://enseigner.blog.lemonde.fr/2018/04/03/parcoursup-naivete-habilete-ou-machiavelisme-gouvernemental/>`_
   ou sur
   `binaire.blog.lemonde.fr <http://binaire.blog.lemonde.fr/2018/06/05/la-transparence-a-lecole-de-parcoursup/>`_.

-  `Cet autre article par Clémence Réda est
   instructif <https://theconversation.com/apb-la-vie-apres-le-bac-66848>`_.

--------------

Exemples
--------

Installation
~~~~~~~~~~~~

Ces lignes de `Bash <https://www.gnu.org/software/bash/>`_ (à exécuter
sur une machine type GNU/Linux ou un Mac avec les outils standards)
clone ce dépôt, et installent un `virtualenv
Python <https://virtualenv.pypa.io/>`_ et installent `les
dépendances <requirements.txt>`_ dans cet environnement virtuel :

.. code:: bash

    cd /tmp/
    git clone https://GitHub.com/Naereen/ParcourSup.py
    cd Parcoursup.py/
    make install

..

    Note : Il n'est pas nécessaire d'utiliser un virtualenv, mais
    c'est recommandé. Vous pouvez simplement installer les modules
    requis avec sudo pip install -r requirements.txt.

..

    Note : notre code n'est pas spécifiquement écrit pour une machine
    utilisant GNU/Linux, et il devrait fonctionner sur n'importe quelle
    plateforme qui supporte Python 3.6 (Microsoft Windows et Mac OS X
    notamment). Il est testé sous GNU/Linux (XUbuntu) *et* sous
    Microsoft Windows 7. `N'hésitez pas à signaler un
    problème <https://github.com/Naereen/ParcourSup.py/issues/new>`_,
    si besoin. Merci d'avance !

Tests |Build Status|
~~~~~~~~~~~~~~~~~~~~

Les tests qui reproduisent
(`presque <https://github.com/Naereen/ParcourSup.py/issues/1>`_)
parfaitement `les données d'exemples <donnees>`_ peuvent être exécutés
avec les deux commandes suivantes :

-  Ordres d'appel :

.. code:: bash

    $ . env/bin/activate ; python3 ./parcoursup/ordreappel/__init__.py
    ...

-  Proposition de vœux :

.. code:: bash

    $ . env/bin/activate ; python3 ./parcoursup/propositions/__init__.py
    ...

-  Ces deux tests prennent environ 30 secondes chacun.

    Note : Il n'est pas nécessaire d'utiliser un virtualenv, mais
    c'est recommandé. Vous pouvez simplement faire les tests avec
    python3 ./parcoursup/ordreappel/__init__.py et
    python3 ./parcoursup/propositions/__init__.py.

-  Des tests supplémentaires ont été récemment ajoutés (voir
   `#3 <https://github.com/Naereen/ParcourSup.py/issues/3>`_).

--------------

Construire la documentation ? |Documentation Status|
----------------------------------------------------

-  Demande d'avoir le module `sphinx <http://sphinx-doc.org/>`_
   installé. (sudo pip3 install sphinx si besoin).
-  Puis, dans le dossier principal, il suffit de faire :

.. code:: bash

    $ make docs

-  Sous Windows ou si GNU Make n'est pas disponible, vous pouvez
   construire la documentation manuellement avec les deux commandes
   suivantes :

.. code:: bash

    $ sphinx-apidoc -f -o ./docs -e -M ./parcoursup/
    $ sphinx-build -M html ./docs ./_build
    $ ./docs/.fixes_html_in_doc.sh

--------------

À propos
--------

Language et versions ?
~~~~~~~~~~~~~~~~~~~~~~

`Python v3.6+ <https://docs.python.org/3.6/>`_. Avec les `modules
suivants <requirements.txt>`_ :

-  `Numpy <http://numpy.org/>`_ pour les tableaux,
-  `La bibliothèque standard <https://docs.python.org/3.6/>`_ pour tout
   le reste.
-  `ipython <http://ipython.org>`_,
   `Jupyter <https://www.jupyter.org/>`_ pour les notebooks.
-  `tqdm <https://github.com/tqdm/tqdm#usage>`_ sont optionnels.

Licence ? |GitHub license|
~~~~~~~~~~~~~~~~~~~~~~~~~~

Code libre, `sous licence MIT <https://lbesson.mit-license.org/>`_
(file `LICENSE <LICENSE>`_). © `Lilian
Besson <https://GitHub.com/Naereen>`_ et `Bastien
Trotobas <https://github.com/BastienTr>`_ et collaborateur-trice-s,
2018.

|Open Source ? Oui !| |Implementation| |Version de Python| |Maintenance|
|Ask Me Anything !| |Analytics| |Documentation Status| |Build Status|
|Stars of https://github.com/Naereen/ParcourSup.py/| |Releases of
https://github.com/Naereen/ParcourSup.py/|

|ForTheBadge uses-badges| |ForTheBadge uses-git| |forthebadge
made-with-python| |ForTheBadge built-with-science|

.. |Open Source ? Oui !| image:: https://badgen.net/badge/Open%20Source%20%3F/Oui%20%21/blue?icon=github
   :target: https://github.com/Naereen/ParcourSup.py/
.. |Implementation| image:: https://img.shields.io/pypi/implementation/parcoursup.svg
   :target: https://www.python.org/
.. |Version de Python| image:: https://img.shields.io/pypi/pyversions/parcoursup.svg
   :target: https://docs.python.org/3/
.. |Maintenance| image:: https://img.shields.io/badge/Maintenu%3F-Oui%20%21-green.svg
   :target: https://GitHub.com/Naereen/ParcourSup.py/graphs/commit-activity
.. |Ask Me Anything !| image:: https://img.shields.io/badge/Posez-une%20question-1abc9c.svg
   :target: https://GitHub.com/Naereen/ama
.. |Analytics| image:: https://ga-beacon.appspot.com/UA-38514290-17/github.com/Naereen/ParcourSup.py/README.md?pixel
   :target: https://GitHub.com/Naereen/ParcourSup.py/
.. |Documentation Status| image:: https://readthedocs.org/projects/parcoursuppy/badge/?version=latest
   :target: https://parcoursuppy.readthedocs.io/fr/latest/?badge=latest
.. |Build Status| image:: https://travis-ci.org/Naereen/ParcourSup.py.svg?branch=master
   :target: https://travis-ci.org/Naereen/ParcourSup.py
.. |Stars of https://github.com/Naereen/ParcourSup.py/| image:: https://badgen.net/github/stars/Naereen/ParcourSup.py
   :target: https://GitHub.com/Naereen/ParcourSup.py/stargazers
.. |Releases of https://github.com/Naereen/ParcourSup.py/| image:: https://badgen.net/github/release/Naereen/ParcourSup.py
   :target: https://github.com/Naereen/ParcourSup.py/releases
.. |Commits of https://github.com/Naereen/ParcourSup.py/| image:: https://badgen.net/github/commits/Naereen/ParcourSup.py
   :target: https://github.com/Naereen/ParcourSup.py/commits/master
.. |Date of last commit of https://github.com/Naereen/ParcourSup.py/| image:: https://badgen.net/github/last-commit/Naereen/ParcourSup.py
   :target: https://github.com/Naereen/ParcourSup.py/commits/master
.. |Issues of https://github.com/Naereen/ParcourSup.py/| image:: https://badgen.net/github/issues/Naereen/ParcourSup.py
   :target: https://GitHub.com/Naereen/ParcourSup.py/issues
.. |Open issues of https://github.com/Naereen/ParcourSup.py/| image:: https://badgen.net/github/open-issues/Naereen/ParcourSup.py
   :target: https://github.com/Naereen/ParcourSup.py/issues?q=is%3Aopen+is%3Aissue
.. |Closed issues of https://github.com/Naereen/ParcourSup.py/| image:: https://badgen.net/github/closed-issues/Naereen/ParcourSup.py
   :target: https://github.com/Naereen/ParcourSup.py/issues?q=is%3Aclosed+is%3Aissue
.. |Binder| image:: https://mybinder.org/badge.svg
   :target: https://mybinder.org/v2/gh/Naereen/ParcourSup.py/master?filepath=notebooks%2FParcourSup.py_version_simplifiee.ipynb
.. |Google Colab| image:: https://badgen.net/badge/Lancer/sur%20Google%20Colab/blue?icon=terminal
   :target: https://colab.research.google.com/github/Naereen/ParcourSup.py/blob/master/notebooks/ParcourSup.py_version_simplifiee.ipynb
.. |GitHub license| image:: https://img.shields.io/github/license/Naereen/ParcourSup.py.svg
   :target: https://github.com/Naereen/ParcourSup.py/blob/master/LICENSE
.. |ForTheBadge uses-badges| image:: http://ForTheBadge.com/images/badges/uses-badges.svg
   :target: http://ForTheBadge.com
.. |ForTheBadge uses-git| image:: http://ForTheBadge.com/images/badges/uses-git.svg
   :target: https://GitHub.com/
.. |forthebadge made-with-python| image:: http://ForTheBadge.com/images/badges/made-with-python.svg
   :target: https://www.python.org/
.. |ForTheBadge built-with-science| image:: http://ForTheBadge.com/images/badges/built-with-science.svg
   :target: https://GitHub.com/Naereen/
