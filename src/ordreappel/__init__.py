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


def main(numeroExemple=None):
    if numeroExemple is not None:
        max_numero = len(tous_les_exemples)
        if not 0 <= numeroExemple < max_numero:
            print(f"Erreur, l'exemple numéro #{numeroExemple + 1} n'est pas disponible.")
    for i, exemple in enumerate(tous_les_exemples):
        if numeroExemple is not None and i != numeroExemple:
            continue
        print(f"\n\n\nPour l'exemple #{i} :")  # DEBUG
        ex = exemple()
        ex.execute()
        if numeroExemple is not None and i == numeroExemple:
            return


if __name__ == '__main__':
    from sys import argv
    # lance tous les tests ou un seul
    numeroExemple = int(argv[1]) if len(argv) > 1 else None
    main(numeroExemple=numeroExemple - 1)
