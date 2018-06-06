#!/usr/bin/env python3
# -*- coding: utf-8; mode: python -*-
""" OrdreAppel, pour https://github.com/Naereen/ParcourSup.py.

- Auteurs: Lilian Besson, Bastien Trotobas et al, (C) 2018.
- Adresse: https://github.com/Naereen/ParcourSup.py
- Licence: MIT License (http://lbesson.mit-license.org).
"""
__author__ = "Lilian Besson, Bastien Trotobas et al"
__version__ = "0.0.1"


class OrdreAppel(list):
    """ Classe représentant un ordre d'appel. Juste une liste avec une méthode en plus."""

    def coefficientDivergence(self) -> float:
        """
        Calcule une mesure de la différence entre le classement original et l'ordre d'appel, c'est le nombre d'inversions ramené au nombre maximal d'inversions.

        Le nombre maximal d'inversions est obtenu si le classement est totalement inversé
        (cas hypothétique), auquel cas il y a autant d'inversions que de paires non-ordonnées
        de candidat-e c'est-à-dire ``n * (n - 1) / 2``.
        """
        if len(self) <= 1:
            return 0.0
        nbInversions = 0
        for i, voe1 in enumerate(self):
            for j, voe2 in enumerate(self):
                if j < i and voe1 < voe2:  # une inversion !
                    nbInversions += 1
        maxNbInversions = (len(self) * (len(self) - 1) / 2)
        return nbInversions / float(maxNbInversions)
