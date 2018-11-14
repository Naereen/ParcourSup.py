#!/usr/bin/env python3
# -*- coding: utf-8; mode: python -*-
""" OrdreAppel, pour https://github.com/Naereen/ParcourSup.py.

- Auteurs : Lilian Besson, Bastien Trotobas et al, (C) 2018.
- Adresse : https://github.com/Naereen/ParcourSup.py
- Licence : MIT License (http://lbesson.mit-license.org).
"""
__author__ = "Lilian Besson, Bastien Trotobas et al"
__version__ = "0.2.1"


# XXX Pour utiliser l'implémentation dans scipy.stats
# import numpy as np
# from scipy.stats import kendalltau


class OrdreAppel(list):
    """ Classe représentant un ordre d'appel. Juste une liste avec une méthode en plus."""

    def coefficientDivergence(self) -> float:
        """
        Calcule une mesure de la différence entre le classement original et l'ordre d'appel, c'est le nombre d'inversions ramené au nombre maximal d'inversions.

        Le nombre maximal d'inversions est obtenu si le classement est totalement inversé
        (cas hypothétique), auquel cas il y a autant d'inversions que de paires non-ordonnées
        de candidat-e c'est-à-dire ``n * (n - 1) / 2``.

        .. note:: C'est la distance de Kendall-tau.
        """
        # Note : on peut aussi la calculer comme ca :
        # if comp is None:
        #     comp = sorted(self)
        # res = 1 - kendalltau(self, comp).pvalue
        # if np.isnan(res):
        #     res = 0
        # return res
        #
        if len(self) <= 1:
            return 0.0
        nbInversions = 0
        for i, voe1 in enumerate(self):
            # for j, voe2 in enumerate(self):
            for voe2 in self[:i]:
                # if j < i and voe1 < voe2:  # une inversion !
                if voe1 < voe2:  # une inversion !
                    nbInversions += 1
        maxNbInversions = (len(self) * (len(self) - 1) / 2)
        return nbInversions / float(maxNbInversions)


def main(taille=10, nbEssaisAleatoires=100000):
    """ Trace un histogramme de la répartition de ce ``coefficientDivergence()`` pour des listes de taille ``taille``."""
    from math import factorial
    from itertools import permutations
    import numpy as np
    import matplotlib.pyplot as plt
    try:
        from tqdm import tqdm
    except:
        def tqdm(iterable=None, **kwargs):
            return iterable
    # on calcule le nombre d'essai à faire si on veut être exhaustif
    taillePermutations = int(factorial(taille))
    if taillePermutations >= 1e8:
        print(f"Il y a {taillePermutations} permutations à essayer, cela fait trop, on va en essayer {nbEssaisAleatoires} aléatoires plutôt.")
        taillePermutations = nbEssaisAleatoires
        def permutations(liste):
            for _ in range(taillePermutations):
                yield np.random.permutation(liste)
    else:
        print(f"Il y a {taillePermutations} permutations à essayer.")
    # on calcule un tableau stockant des coefficients de divergence
    resultats = np.zeros(taillePermutations)
    liste_non_triee = list(range(taille))
    for i, perm in tqdm(enumerate(permutations(liste_non_triee)), total=taillePermutations):
        resultats[i] = OrdreAppel(perm).coefficientDivergence()
    # et ensuite on en affiche un histogramme
    fig = plt.figure()
    plt.hist(resultats, bins=10*taille)
    plt.title(f"Histogramme de coefficientDivergence pour les permutations de [1,...,{taille}] et {taillePermutations} essais")
    plt.grid()
    plt.show()
    return fig


if __name__ == '__main__':
    from sys import argv
    taille = int(argv[1]) if len(argv) > 1 else 10
    nbEssaisAleatoires = int(argv[2]) if len(argv) > 2 else 10000
    main(taille=taille, nbEssaisAleatoires=nbEssaisAleatoires)
