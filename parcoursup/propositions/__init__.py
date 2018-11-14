#!/usr/bin/env python3
# -*- coding: utf-8; mode: python -*-
""" Calcul des propositions à envoyer, pour https://github.com/Naereen/ParcourSup.py.

- Auteurs : Lilian Besson, Bastien Trotobas et al, (C) 2018.
- Adresse : https://github.com/Naereen/ParcourSup.py
- Licence : MIT License (http://lbesson.mit-license.org).
"""
__author__ = "Lilian Besson, Bastien Trotobas et al"
__version__ = "0.2"


if __name__ == '__main__':
    try:
        from .exemples import tous_les_exemples
    except ImportError:
        from exemples import tous_les_exemples


    def main(numeroExemples=None):
        nombreExemples = len(tous_les_exemples)
        # on fait tous les exemples ?
        tousNumeroExemples = list(range(nombreExemples))
        if numeroExemples is not None and len(numeroExemples) > 0:
            for i in numeroExemples.copy():
                if not i in tousNumeroExemples:
                    print(f"Erreur, l'exemple numéro #{i} n'est pas disponible.")
                    numeroExemples.remove(i)  # on le traite pas
        if numeroExemples is None or len(numeroExemples) == 0:  # si on en a donné aucun
            numeroExemples = tousNumeroExemples
        for i in numeroExemples:
            exemple = tous_les_exemples[i]
            print(f"\n\n\nPour l'exemple #{i} :")  # DEBUG
            ex = exemple()
            ex.execute()


    from sys import argv
    # lance tous les tests ou un seul
    nums = [int(a) - 1 for a in argv[1:]] if len(argv) > 1 else None
    main(numeroExemples=nums)
