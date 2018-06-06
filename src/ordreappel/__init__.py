#!/usr/bin/env python3
# -*- coding: utf-8; mode: python -*-
""" Calcul de l'ordre d'appel, pour https://github.com/Naereen/ParcourSup.py.

- Auteurs: Lilian Besson, Bastien Trotobas and contributors, (C) 2018.
- Adresse: https://github.com/Naereen/ParcourSup.py
- Licence: MIT License (http://lbesson.mit-license.org).
"""
__author__ = "Lilian Besson, Bastien Trotobas and contributors"
__version__ = "0.0.1"

from exemples import tous_les_exemples


def main():
    for i, exemple in enumerate(tous_les_exemples):
        print(f"\n\n\nPour l'exemple #{i} :")  # DEBUG
        ex = exemple()
        ex.execute()


if __name__ == '__main__':
    # lance tous les tests
    main()
