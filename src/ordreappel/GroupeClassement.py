#!/usr/bin/env python3
# -*- coding: utf-8; mode: python -*-
""" GroupeClassement, pour https://github.com/Naereen/ParcourSup.py.

- Auteurs: Lilian Besson, Bastien Trotobas and contributors, (C) 2018.
- Adresse: https://github.com/Naereen/ParcourSup.py
- Licence: MIT License (http://lbesson.mit-license.org).
"""
__author__ = "Lilian Besson, Bastien Trotobas and contributors"
__version__ = "0.0.1"

from queue import Queue, PriorityQueue

from VoeuClasse import VoeuClasse, TypeCandidat
from OrdreAppel import OrdreAppel


class GroupeClassement(object):
    """ Classe représentant un groupe d'appel."""
    def __init__(self,
        C_GP_COD: int,
        tauxMinBoursiersPourcents: int,
        tauxMinResidentsPourcents: int,
    ):
        assert C_GP_COD > 0, f"Erreur : {self.__class__.__name__} le paramètre C_GP_COD doit être > 0, et pas {C_GP_COD}..."  # DEBUG
        self.C_GP_COD = C_GP_COD  #: C_GP_COD

        assert 0 <= tauxMinBoursiersPourcents <= 100, f"Erreur : {self.__class__.__name__} le paramètre tauxMinBoursiersPourcents doit être 0<=...<=100 , et pas {tauxMinBoursiersPourcents}..."  # DEBUG
        assert isinstance(tauxMinBoursiersPourcents, int), f"Erreur : {self.__class__.__name__} le paramètre tauxMinBoursiersPourcents doit être entier, et pas {tauxMinBoursiersPourcents}..."  # DEBUG
        self.tauxMinBoursiersPourcents = tauxMinBoursiersPourcents  #: tauxMinBoursiersPourcents

        assert 0 <= tauxMinBoursiersPourcents <= 100, f"Erreur : {self.__class__.__name__} le paramètre tauxMinBoursiersPourcents doit être 0<=...<=100 , et pas {tauxMinBoursiersPourcents}..."  # DEBUG
        assert isinstance(tauxMinBoursiersPourcents, int), f"Erreur : {self.__class__.__name__} le paramètre tauxMinBoursiersPourcents doit être entier, et pas {tauxMinBoursiersPourcents}..."  # DEBUG
        self.tauxMinResidentsPourcents = tauxMinResidentsPourcents  #: tauxMinResidentsPourcents
        self.voeuxClasses = []  #: La liste des vœux du groupe de classement

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.C_GP_COD})"

    def ajouterVoeu(self, voeu: VoeuClasse) -> None:
        """ Ajouter ce voeu à la liste actuelle."""
        self.voeuxClasses.append(voeu)

    def calculerOrdreAppel(self) -> OrdreAppel:
        """ Calcule de l'ordre d'appel."""
        # on crée autant de listes de vœux que de types de candidats,
        # triées par ordre de classement
        filesAttente = {
            t: Queue()
            for t in list(TypeCandidat)
        }

        # Chaque voeu classé est ventilé dans la liste correspondante,
        # en fonction du type du candidat.
        # Les quatre listes obtenues sont ordonnées par rang de classement,
        # comme l'est la liste voeuxClasses.
        nbBoursiersTotal = 0
        nbResidentsTotal = 0

        # on trie les vœux par classement
        self.voeuxClasses.sort()

        for voeu in self.voeuxClasses:
            # on ajoute le voeu à la fin de la file (FIFO) correspondante
            filesAttente[voeu.typeCandidat].put(voeu)
            if voeu.estBoursier():
                nbBoursiersTotal += 1
            if voeu.estResident():
                nbResidentsTotal += 1

        nbAppeles          = 0
        nbBoursiersAppeles = 0
        nbResidentsAppeles = 0

        # la boucle ajoute les candidats un par un à la liste suivante,
        # dans l'ordre d'appel
        ordreAppel = OrdreAppel()

        while len(ordreAppel) < len(self.voeuxClasses):
            # on calcule lequel ou lesquels des critères boursiers et résidents
            # contraignent le choix du prochain candidat dans l'ordre d'appel

            contrainteTauxBoursier = (nbBoursiersAppeles < nbBoursiersTotal) and ((nbBoursiersAppeles * 100) < self.tauxMinBoursiersPourcents * (1 + nbAppeles))

            contrainteTauxResident = (nbResidentsAppeles < nbResidentsTotal) and ((nbResidentsAppeles * 100) < self.tauxMinResidentsPourcents * (1 + nbAppeles))

            # on fait la liste des voeux satisfaisant
            # les deux contraintes à la fois, ordonnée par rang de classement
            eligibles = PriorityQueue()
            for queue in filesAttente.values():
                if not queue.empty():
                    voeu = queue.get()
                    if (voeu.estBoursier() or not contrainteTauxBoursier) and (voeu.estResident() or not contrainteTauxResident):
                        eligibles.put(voeu)

            # stocke le meilleur candidat à appeler tout en respectant
            # les deux contraintes si possible
            # ou à défaut seulement la contrainte sur le taux boursier
            meilleur = None

            if not eligibles.empty():
                meilleur = eligibles.get()
            else:
                # la liste peut être vide dans le cas où les deux contraintes
                # ne peuvent être satisfaites à la fois.
                # Dans ce cas nécessairement il y a une contrainte sur chacun des deux taux
                # (donc au moins un boursier non encore sélectionné)
                # et il ne reste plus de boursier résident,
                # donc il reste au moins un boursier non résident
                assert contrainteTauxBoursier and contrainteTauxResident, "Erreur : ce cas où la file de priorité est vide mais les deux contraintes ne sont pas vérifiées ne devrait pas arriver."  # DEBUG

                assert filesAttente[TypeCandidat.BoursierResident].empty(), "Erreur : ce cas où la file de priorité est vide mais il reste des candidats-es boursiers-ères et résident-es ne devrait pas arriver."  # DEBUG
                assert not filesAttente[TypeCandidat.BoursierNonResident].empty(), "Erreur : ce cas où la file de priorité est vide mais il ne reste pas de candidats-es boursiers-ères et non résident-es ne devrait pas arriver."  # DEBUG

                CandidatsBoursierNonResident = filesAttente[TypeCandidat.BoursierNonResident]
                meilleur = CandidatsBoursierNonResident.get()

            # suppression du candidat choisi de sa file d'attente
            queue = filesAttente[meilleur.typeCandidat]
            meilleur_de_sa_liste = queue.get()
            assert meilleur == meilleur_de_sa_liste, "Erreur : ce cas où le-la meilleur-e candidat-e n'est pas le meilleur candidat de la liste d'attente des autres candidat-e de sa liste ne devrait pas arriver."  # DEBUG

            # ajout du meilleur candidat à l'ordre d'appel
            ordreAppel.append(meilleur)
            nbAppeles += 1

            if meilleur.estBoursier():
                nbBoursiersAppeles += 1
            if meilleur.estResident():
                nbResidentsAppeles += 1
        # fin de la boucle while
        return ordreAppel
