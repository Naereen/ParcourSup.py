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


def main(numeroExemples=None):
    nombreExemples = len(tous_les_exemples)
    # on fait tous les exemples ?
    tousNumeroExemples = list(range(nombreExemples))
    if numeroExemples:
        for i in numeroExemples.copy():
            if not i in tousNumeroExemples:
                print(f"Erreur, l'exemple numéro #{i} n'est pas disponible.")
                numeroExemples.remove(i)  # on le traite pas
    if not numeroExemples:  # si on en a donné aucun
        numeroExemples = tous_les_exemples
    for i in numeroExemples:
        exemple = tous_les_exemples[i]
        print(f"\n\n\nPour l'exemple #{i} :")  # DEBUG
        ex = exemple()
        ex.execute()


if __name__ == '__main__':
    from sys import argv
    # lance tous les tests ou un seul
    numeroExemples = [int(a) - 1 for a in argv[1:]] if len(argv) > 1 else None
    main(numeroExemples=numeroExemples)
