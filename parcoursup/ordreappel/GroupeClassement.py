#!/usr/bin/env python3
# -*- coding: utf-8; mode: python -*-
""" GroupeClassement, pour https://github.com/Naereen/ParcourSup.py.

- Auteurs : Lilian Besson, Bastien Trotobas et al, (C) 2018.
- Adresse : https://github.com/Naereen/ParcourSup.py
- Licence : MIT License (http://lbesson.mit-license.org).
"""
__author__ = "Lilian Besson, Bastien Trotobas et al"
__version__ = "0.2.1"

from typing import List, Dict

try:
    from .VoeuClasse import VoeuClasse, TypeCandidat
    from .OrdreAppel import OrdreAppel
except ImportError:
    from VoeuClasse import VoeuClasse, TypeCandidat
    from OrdreAppel import OrdreAppel


#: En mode débug, on affiche juste le résultat.
# DEBUG = True
DEBUG = False


class GroupeClassement(object):
    """ Classe représentant un groupe d'appel."""
    def __init__(self, C_GP_COD: int, tauxMinBoursiersPourcents: int, tauxMinResidentsPourcents: int):
        assert C_GP_COD >= 0, f"Erreur : {self.__class__.__name__} le paramètre C_GP_COD doit être > 0, et pas {C_GP_COD}..."  # DEBUG
        self.C_GP_COD = C_GP_COD  #: C_GP_COD

        assert 0 <= tauxMinBoursiersPourcents <= 100, f"Erreur : {self.__class__.__name__} le paramètre tauxMinBoursiersPourcents doit être 0<=...<=100 , et pas {tauxMinBoursiersPourcents}..."  # DEBUG
        assert isinstance(tauxMinBoursiersPourcents, int), f"Erreur : {self.__class__.__name__} le paramètre tauxMinBoursiersPourcents doit être entier, et pas {tauxMinBoursiersPourcents}..."  # DEBUG
        self.tauxMinBoursiersPourcents = tauxMinBoursiersPourcents  #: tauxMinBoursiersPourcents

        assert 0 <= tauxMinBoursiersPourcents <= 100, f"Erreur : {self.__class__.__name__} le paramètre tauxMinBoursiersPourcents doit être 0<=...<=100 , et pas {tauxMinBoursiersPourcents}..."  # DEBUG
        assert isinstance(tauxMinBoursiersPourcents, int), f"Erreur : {self.__class__.__name__} le paramètre tauxMinBoursiersPourcents doit être entier, et pas {tauxMinBoursiersPourcents}..."  # DEBUG
        self.tauxMinResidentsPourcents = tauxMinResidentsPourcents  #: tauxMinResidentsPourcents
        self.voeuxClasses: List[VoeuClasse] = []  #: La liste des vœux du groupe de classement

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.C_GP_COD})"

    def ajouterVoeu(self, voeu: VoeuClasse) -> None:
        """ Ajouter ce voeu à la liste actuelle."""
        self.voeuxClasses.append(voeu)

    def calculerOrdreAppel(self, verbeux: bool=DEBUG) -> OrdreAppel:
        """ Calcule de l'ordre d'appel."""
        def log(*args, **kwargs) -> None:
            if verbeux:
                print(*args, **kwargs)

        log(f"\n0. On commence à calculer les ordres d'appel pour cette liste de vœux qui contient {len(self.voeuxClasses)} voeux.")

        log(f"  On crée des listes de vœux pour chaque types de candidats ({list(TypeCandidat)}).")
        # on crée autant de listes de vœux que de types de candidats,
        # triées par ordre de classement
        filesAttente: Dict[TypeCandidat, List[VoeuClasse]] = {
            t: []
            for t in list(TypeCandidat)
        }

        # Chaque voeu classé est ventilé dans la liste correspondante,
        # en fonction du type du candidat.
        # Les quatre listes obtenues sont ordonnées par rang de classement,
        # comme l'est la liste voeuxClasses.
        nbBoursiersTotal = 0
        nbResidentsTotal = 0

        # on trie les vœux par classement
        log("\n1. On trie les vœux par classement...")
        log(f"  Avant tri : {self.voeuxClasses}...")
        self.voeuxClasses.sort()
        log(f"  Après tri : {self.voeuxClasses}...")

        for voeu in self.voeuxClasses:
            # on ajoute le voeu à la fin de la file (FIFO) correspondante
            filesAttente[voeu.typeCandidat].append(voeu)
            # log(f"  On ajoute le voeu {voeu} à la file du type {voeu.typeCandidat}, c'est le {i+1}ème à être ajouté.")
            if voeu.estBoursier():
                nbBoursiersTotal += 1
                log(f"    On compte un-e boursier-e en plus, c'est le {nbBoursiersTotal}ème...")
            if voeu.estResident():
                nbResidentsTotal += 1
                log(f"    On compte un-e résident-e en plus, c'est le {nbResidentsTotal}ème...")

        nbVoeuxClasses     = len(self.voeuxClasses)
        nbAppeles          = 0
        nbBoursiersAppeles = 0
        nbResidentsAppeles = 0

        # la boucle ajoute les candidats un par un à la liste suivante,
        # dans l'ordre d'appel
        ordreAppel = OrdreAppel()

        log(f"\n2. Début de la boucle while, on remplit l'ordre d'appel...")

        while len(ordreAppel) < nbVoeuxClasses:
            log(f"\n  L'ordre d'appel contient {len(ordreAppel)} éléments et il y a {nbVoeuxClasses} vœux à classer.")
            # on calcule lequel ou lesquels des critères boursiers et résidents
            # contraignent le choix du prochain candidat dans l'ordre d'appel

            contrainteTauxBoursier = (nbBoursiersAppeles < nbBoursiersTotal) and ((nbBoursiersAppeles * 100) < self.tauxMinBoursiersPourcents * (nbAppeles + 1))
            log(f"  La contrainte sur le taux de boursier-ère-s est {contrainteTauxBoursier}...")
            log(f"      Car il y a pour l'instant {nbBoursiersAppeles} boursier-ère-s appelé-e-s sur un total de {nbBoursiersTotal}, et ce n'est pas assez pour dépasser le taux de {self.tauxMinBoursiersPourcents}...")

            contrainteTauxResident = (nbResidentsAppeles < nbResidentsTotal) and ((nbResidentsAppeles * 100) < self.tauxMinResidentsPourcents * (nbAppeles + 1))
            log(f"  La contrainte sur le taux de résident-e-s est {contrainteTauxResident}...")
            log(f"      Car il y a pour l'instant {nbResidentsAppeles} résident-e-s appelé-e-s sur un total de {nbResidentsTotal}, et ce n'est pas assez pour dépasser le taux de {self.tauxMinResidentsPourcents}...")

            # on fait la liste des voeux satisfaisant
            # les deux contraintes à la fois, ordonnée par rang de classement
            if verbeux: liste_eligibles = []
            eligibles = []
            for queue in filesAttente.values():
                if queue:
                    voeu = queue[-1]  # le meilleur a été ajouté en dernier
                    # assert voeu == max(queue), f"Erreur : ce candidat-e {voeu} est sensé-e être le-la meilleur-e de sa liste, mais ce n'est pas le cas."
                    if (voeu.estBoursier() or not contrainteTauxBoursier) and (voeu.estResident() or not contrainteTauxResident):
                        eligibles.append(voeu)
                        if verbeux: liste_eligibles.append(voeu)
            if verbeux: log(f"  Les vœux satisfaisant les deux contraintes à la fois, ordonnés par rang de classement sont :\n{liste_eligibles}")
            if verbeux: del liste_eligibles  # juste pour l'afficher

            # stocke le meilleur candidat à appeler tout en respectant
            # les deux contraintes si possible
            # ou à défaut seulement la contrainte sur le taux boursier
            meilleur = None

            if eligibles:
                meilleur = max(eligibles)  # on prend le meilleur de cette liste
                log(f"  La liste des éligibles n'est pas vide, donc le-la meilleur-e est le-la meilleur-e de cette liste = {meilleur}")
            else:
                # la liste peut être vide dans le cas où les deux contraintes
                # ne peuvent être satisfaites à la fois.
                # Dans ce cas nécessairement il y a une contrainte sur chacun des deux taux
                # (donc au moins un boursier non encore sélectionné)
                # et il ne reste plus de boursier résident,
                # donc il reste au moins un boursier non résident
                assert contrainteTauxBoursier and contrainteTauxResident, "Erreur : ce cas où la file de priorité est vide mais les deux contraintes ne sont pas vérifiées ne devrait pas arriver."  # DEBUG

                assert not filesAttente[TypeCandidat.BoursierResident], "Erreur : ce cas où la file de priorité est vide mais il reste des candidats-es boursiers-ères et résident-e-s ne devrait pas arriver."  # DEBUG
                assert filesAttente[TypeCandidat.BoursierNonResident], "Erreur : ce cas où la file de priorité est vide mais il ne reste pas de candidats-es boursiers-ères et non résident-e-s ne devrait pas arriver."  # DEBUG

                CandidatsBoursierNonResident = filesAttente[TypeCandidat.BoursierNonResident]
                meilleur = max(CandidatsBoursierNonResident)
                log(f"  La liste des éligibles est pas vide, donc le-la meilleur-e est le-la meilleur-e de la liste des boursier-ère-s non résident-e-s = {meilleur}")

            # suppression du candidat choisi de sa file d'attente
            saFileAttente = filesAttente[meilleur.typeCandidat]
            log(f"  On vérifie si le-la meilleur {meilleur} est aussi le-la meilleur-e de sa liste contenant {len(saFileAttente)} candidat-es (du type {meilleur.typeCandidat}).")
            meilleur_de_sa_liste = saFileAttente.pop()
            # saFileAttente.append(meilleur_de_sa_liste)  # XXX on ne le supprime pas ? si il faut !
            assert meilleur == meilleur_de_sa_liste, "Erreur : ce cas où le-la meilleur-e candidat-e n'est pas le meilleur candidat de la liste d'attente des autres candidat-e de sa liste ne devrait pas arriver."  # DEBUG

            # ajout du meilleur candidat à l'ordre d'appel
            ordreAppel.append(meilleur)
            nbAppeles += 1
            log(f"  On ajoute le meilleur {meilleur} à l'ordre d'appel, c'est le-la {nbAppeles}ème à être appelé-e.")

            if meilleur.estBoursier():
                nbBoursiersAppeles += 1
                log(f"    En plus, c'est le-la {nbBoursiersAppeles}ème boursier-e à être appelé-e.")
            if meilleur.estResident():
                nbResidentsAppeles += 1
                log(f"    En plus, c'est le-la {nbResidentsAppeles}ème résident-e à être appelé-e.")

        # fin de la boucle while
        log(f"\n3. On a terminé la boucle, on a remplit l'ordre d'appel.")

        return ordreAppel
