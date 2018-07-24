# Tests basés sur le BDD
## Avec [behave](https://behave.readthedocs.io/)

- Ces fichiers de tests (fichiers `*.features`) viennent de [ce dépôt](https://github.com/JosePaumard/tests-pour-parcoursup).
- Les fichiers en Python utilisent [l'implémentation de ParcourSup.py](../parcoursup).

## Comment lancer ces tests ?
- Il faut installer le module `behave` :
  ```bash
  $ sudo pip3 install behave
  ```
- Et ensuite vous pouvez utiliser le [`Makefile`](Makefile) fournit :
  ```bash
  $ make tests
  ```
  qui va lancer tous les tests.

## Exemples
TODO

## À propos
- Merci à [José Paumard](https://github.com/JosePaumard/) pour cette belle initiative.
