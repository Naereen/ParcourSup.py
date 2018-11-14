#!/usr/bin/env python3
# -*- coding: utf-8; mode: python -*-
""" GroupeAffectation, pour https://github.com/Naereen/ParcourSup.py.

- Auteurs : Lilian Besson, Bastien Trotobas et al, (C) 2018.
- Adresse : https://github.com/Naereen/ParcourSup.py
- Licence : MIT License (http://lbesson.mit-license.org).
"""
__author__ = "Lilian Besson, Bastien Trotobas et al"
__version__ = "0.2"

from typing import Set, List

try:
    from .VoeuEnAttente import VoeuEnAttente
    from .GroupeAffectationUID import GroupeAffectationUID
except ImportError:
    from VoeuEnAttente import VoeuEnAttente
    from GroupeAffectationUID import GroupeAffectationUID


class GroupeAffectation(object):
    """ Classe comprenant les caractéristiques identifiant de manière unique un groupe d'affectation dans la base de données."""

    def __init__(self,
        capacite: int,
        uid: GroupeAffectationUID,
        rangLimite: int,
    ):
        self.id = uid   #: Le id d'affectation identifiant de manière unique le groupe dans la base.

        assert capacite > 0, f"Erreur : {self.__class__.__name__} le paramètre capacite doit être > 0, et pas {capacite}..."  # DEBUG
        self.capacite = capacite   #: La capacité de la formation.

        assert rangLimite >= 0, f"Erreur : {self.__class__.__name__} le paramètre rangLimite doit être >= 0, et pas {rangLimite}..."  # DEBUG
        self.rangLimite = rangLimite   #: Le rang limite des candidats (dans l'ordre d'appel): tous les candidats de rang inférieur reçoivent une proposition.

        # autres attributs
        #: la liste initiale des voeux du groupe, triée dans l'ordre d'appel du candidat.
        #: Remarque: c'est un ordre partiel car il peut y avoir deux voeux du même candidat,
        #: un avec internat et l'autre sans.
        self.voeux: List[VoeuEnAttente] = []

        #: ``True`` si et seulement si les vœux ont été triés.
        self.voeuxSontTries = False

        #: Ensemble des candidats affectés.
        self.candidatsAffectes: Set[int] = set()

    def __repr__(self) -> str:
        # return f"{self.__class__.__name__}({self.id}, {self.capacite}, {self.rangLimite}, {self.voeux}, {self.voeuxSontTries})"
        return f"{self.__class__.__name__}({self.id}, {self.capacite}, {self.rangLimite}, {len(self.voeux)} voeux, {'voeux triés' if self.voeuxSontTries else 'voeux non triés'})"

    def ajouterVoeu(self, voe: VoeuEnAttente) -> None:
        """ Ajoute un voeu dans le groupe."""
        self.voeux.append(voe)
        self.voeuxSontTries = False

    def ajouterCandidatAffecte(self, G_CN_COD: int) -> None:
        """ Ajoute un candidat affecté."""
        self.candidatsAffectes.add(G_CN_COD)

    def estAffecte(self, G_CN_COD: int) -> bool:
        """ Teste si un candidat est affecté."""
        return G_CN_COD in self.candidatsAffectes

    def mettreAJourPropositions(self) -> None:
        """ Met a jour le statut ``aProposer``, pour chaque voeu du groupe."""
        aPourvoir = self.nbPlacesVacantes()
        for voe in self.voeux:
            voe.conserverEnAttente()
        # On calcule le nombre de propositions dues au rang limite.
        # Les voeux désactivés pour cause de demande d'internat impossible à satisfaire
        # ne sont pas pris en compte.

        dernierCandidatAvecProposition = -1
        for v in self.voeuxTries():
            if v.estDesactiveParPositionAdmissionInternat():
                continue
            # Deux voeux consécutifs peuvent concerner un même candidat,
            # ayant deux voeux en attente (un avec et un sans internat).
            # Cela est pris en compte dans le calcul du nombre de places restantes
            # et dans les propositions.

            if aPourvoir > 0 or v.ordreAppel <= self.rangLimite or v.formationDejaObtenue() or dernierCandidatAvecProposition == v.id.G_CN_COD:
                v.proposer()
                if not v.formationDejaObtenue() and dernierCandidatAvecProposition != v.id.G_CN_COD:
                    aPourvoir -= 1
                dernierCandidatAvecProposition = v.id.G_CN_COD

    def nbPlacesVacantes(self) -> int:
        """ Le nombre de places vacantes au lancement du calcul.

        .. warning:: Peut être négatif en cas de modification à la baisse des paramètres de surréservation.
        """
        return self.capacite - len(self.candidatsAffectes)

    def estInitialementEnSurcapacite(self) -> bool:
        """ La formation était elle initialement en surcapacité ?"""
        return self.nbPlacesVacantes() < 0

    def voeuxTries(self) -> List[VoeuEnAttente]:
        """ Trie les voeux dans l'ordre d'appel."""
        if not self.voeuxSontTries:
            self.voeux.sort(key=lambda voeu: voeu.ordreAppel)
            self.voeuxSontTries = True
        return self.voeux
