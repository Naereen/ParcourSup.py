# :fr: Un clone en Python 3 de [Parcoursup](http://www.parcoursup.fr/), écrit à but didactique
<a href="https://perso.crans.org/besson/publis/ParcourSup.py/"><img align="right" src="../docs/_static/logo_parcoursuppy.png" alt="Lien vers la documentation Sphinx du projet" width="40%"/></a>

> [Écrit par](AUTHORS) [Lilian Besson (@Naereen)](https://github.com/Naereen) et [Bastien Trotobas (@BastienTr)](https://github.com/BastienTr), et d'autres collaborateurs.

## Documentation

- Ce dossier contiendra des ressources supplémentaires pour expliquer les algorithmes de Parcoursup,
- Il contient déjà les fichiers nécessaires à générer une [documentation Sphinx](http://sphinx-doc.org/) pour ce projet Python.

## Plan de bataille

- La documentation est hébergée sur [mon site](https://perso.crans.org/besson), dans [ce dossier](https://perso.crans.org/besson/publis/ParcourSup.py/parcoursup.html#module-parcoursup): https://perso.crans.org/besson/publis/ParcourSup.py/parcoursup.html#module-parcoursup

- TODO héberger la documentation sur GitHub pages d'abord ? Peut-être pas nécessaire.
- TODO si tout marche, héberger la documentation sur ReadTheDocs, e.g., https://parcoursup-python.rtfd.io/ serait pas mal (il faut [importer le projet](https://readthedocs.org/dashboard/import/), c'est très rapide).

## Construire la documentation ?

- Demande d'avoir le module [`sphinx`](http://sphinx-doc.org/) installé. (`sudo pip3 install sphinx` si besoin).
- Puis, dans le dossier principal, il suffit de faire :

```bash
$ make docs
```

- Sous Windows ou si GNU Make n'est pas disponible, vous pouvez construire la documentation manuellement avec les deux commandes suivantes :

```bash
$ sphinx-apidoc -f -o ./docs -e -M ./parcoursup/
$ sphinx-build -M html ./docs ./_build
$ ./docs/.fixes_html_in_doc.sh
```

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
