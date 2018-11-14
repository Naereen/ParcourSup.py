#!/usr/bin/env python3
# -*- coding: utf-8; mode: python -*-
""" Etablissement, pour https://github.com/Naereen/ParcourSup.py.

- Auteurs : Lilian Besson, Bastien Trotobas et al, (C) 2018.
- Adresse : https://github.com/Naereen/ParcourSup.py
- Licence : MIT License (http://lbesson.mit-license.org).
"""
__author__ = "Lilian Besson, Bastien Trotobas et al"
__version__ = "0.2.1"

from typing import List, Dict, Union, Set
from random import random, randint, choice

try:
    from .GroupeAffectation import GroupeAffectation
    from .GroupeAffectationUID import GroupeAffectationUID
    from .GroupeInternat import GroupeInternat
    from .GroupeInternatUID import GroupeInternatUID
    from .VoeuEnAttente import VoeuEnAttente
    from .Candidat import Candidat
except ImportError:
    from GroupeAffectation import GroupeAffectation
    from GroupeAffectationUID import GroupeAffectationUID
    from GroupeInternat import GroupeInternat
    from GroupeInternatUID import GroupeInternatUID
    from VoeuEnAttente import VoeuEnAttente
    from Candidat import Candidat


def randbool() -> bool:
    """ Pile ou face, True avec probabilité 1/2 et False avec probabilité 1/2."""
    return random() < 0.5


def avecproba(p) -> bool:
    """ Pile ou face biaisé, True avec probabilité p et False avec probabilité 1-p."""
    return random() < p

class GroupeClassement(object):
    """ Classe pour représentation un groupe de classement."""
    last_C_G_COD = 1

    def __init__(self, nbEtudiants: int=100):
        self.C_G_COD = self.last_C_G_COD
        self.last_C_G_COD += 1
        self.nbEtudiants = nbEtudiants
        #: le rang le plus haut dans l'ordre d'appel d'un candidat recruté
        self.plusHautRangAffecte = randint(1, int(nbEtudiants / 4))
        self.rangs: Dict[Candidat, int] = dict()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.C_G_COD}, {self.nbEtudiants}, {self.plusHautRangAffecte})"

    def ajouterCandidat(self, c: Candidat, maxEtapes: int=1000) -> int:
        """ Ajoute un candidat et renvoie son rang.

        .. warning:: Ici, on ajoute un compteur ``maxEtapes`` pour borner le nombre de tentative aléatoire.
        """
        if c in self.rangs:
            return self.rangs[c]
        etape = 0
        while etape < maxEtapes:
            rang = randint(1, self.nbEtudiants)
            if rang not in self.rangs:
                self.rangs[c] = rang
                return rang
            etape += 1
        raise RuntimeError(f"Pas assez d'essai aléatoire dans ajouterCandidat, avec candidat {c}, et un nombre maximum d'étapes = {maxEtapes}.")


class FormationAffectation(object):
    """ Classe pour représentation une formation en affectation."""
    last_G_TA_COD = 1

    capaciteMaxFormationNormale = 100
    capaciteMaxFormationCC = 200

    def __init__(self):
        self.G_TA_COD = self.last_G_TA_COD
        self.last_G_TA_COD += 1
        # autre attributs
        self.internat: Union[None, GroupeInternat] = None
        self.juryInternat: Union[None, GroupeClassement] = None
        self.classements: Dict[GroupeAffectation, GroupeClassement] = dict()
        self.groupes: List[GroupeAffectation] = []
        self.vusAvecInternat: Set[Candidat] = set()
        self.vusSansInternat: Set[Candidat] = set()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.G_TA_COD}, {self.internat}, {self.juryInternat}, {self.classements}, {self.groupes}, {self.vusAvecInternat}, {self.vusSansInternat})"

    def ajouterGroupe(self, c: GroupeClassement, G_TI_COD: int, G_TA_COD: int, isConcoursCommun: bool) -> None:
        """ Ajoute un groupe de classement."""
        groupeui = GroupeAffectationUID(c.C_G_COD, G_TI_COD, G_TA_COD)

        capaciteMax = self.capaciteMaxFormationCC if isConcoursCommun else self.capaciteMaxFormationNormale
        capacite = randint(1, capaciteMax)
        rangLimite = int((1 + random()) * capacite)
        ga = GroupeAffectation(capacite, groupeui, rangLimite)

        self.classements[ga] = c
        self.groupes.append(ga)

    def ajouterVoeu(self, candidat: Candidat, avecInternat: bool) -> None:
        """ Ajoute un vœu (un candidat et une demande d'internat)."""
        # pas deux fois le même voeu
        if avecInternat and candidat in self.vusAvecInternat:
            return
        if not avecInternat and candidat in self.vusSansInternat:
            return

        if avecInternat:
            self.vusAvecInternat.add(candidat)
        else:
            self.vusSansInternat.add(candidat)

        ga = choice(self.groupes)
        cl = self.classements[ga]
        rang = cl.ajouterCandidat(candidat)

        if avecInternat or self.internat is None:
            if rang <= cl.plusHautRangAffecte:
                ga.ajouterCandidatAffecte(candidat.G_CN_COD)
            else:
                VoeuEnAttente.ajouterVoeu(candidat.G_CN_COD, avecInternat, ga, rang)
        else:
            rangInternat = self.juryInternat.ajouterCandidat(candidat)

            if rang <= cl.plusHautRangAffecte and rangInternat <= self.juryInternat.plusHautRangAffecte:
                ga.ajouterCandidatAffecte(candidat.G_CN_COD)
                self.internat.ajouterCandidatAffecte(candidat.G_CN_COD)
            else:
                VoeuEnAttente.ajouterVoeu(candidat.G_CN_COD, ga, rang, self.internat, rangInternat)

    def capacite(self) -> int:
        """ Capacité d'une formation = somme des capacités de ses groupe."""
        return sum(groupe.capacite() for groupe in self.groupes)


class Etablissement(object):
    """ Classe comprenant les caractéristiques d'un établissement (aléatoire)."""
    last_G_TI_COD = 1

    # Tous les paramètres de la simulation aléatoire
    maxNbVoeuxParConcoursCommun = 80
    proportionConcoursCommuns = 0.1
    nbFormationsParConcours = 100
    proportionInternatsCommuns = 0.5
    proportionInternats = 0.5
    nbFormationsParEtablissement = 5
    capaciteMaxInternat = 30
    maxNbGroupesParFormation = 5

    def __init__(self, nbEtudiants: int=100):
        self.G_TI_COD = self.last_G_TI_COD
        self.last_G_TI_COD += 1
        self.nbEtudiants = nbEtudiants
        self.isConcoursCommun = avecproba(self.proportionConcoursCommuns)

        self.formations: List[FormationAffectation] = []
        self.jurys: List[GroupeClassement] = []
        self.internatsCommuns: Dict[GroupeClassement, GroupeInternat] = dict()

        if self.isConcoursCommun:
            groupe1 = GroupeClassement(nbEtudiants=self.nbEtudiants)
            self.jurys.append(groupe1)
            groupe2 = GroupeClassement(nbEtudiants=self.nbEtudiants)
            self.jurys.append(groupe2)

            nbFormations = randint(1, self.nbFormationsParConcours)
            for i in range(nbFormations):
                formation = FormationAffectation()
                formation.ajouterGroupe(groupe1, self.G_TI_COD, formation.G_TA_COD, self.isConcoursCommun)
                formation.ajouterGroupe(groupe2, self.G_TI_COD, formation.G_TA_COD, self.isConcoursCommun)

            self.isInternatCommun = False
            self.isInternatParFormation = False
        else:
            self.isInternatCommun = avecproba(self.proportionInternatsCommuns)
            self.isInternatParFormation = avecproba(self.proportionInternats)
            if self.isInternatCommun:
                ifilles = GroupeClassement(nbEtudiants=self.nbEtudiants)
                ifillesid = GroupeInternatUID(ifilles.C_G_COD, 0)
                self.internatsCommuns[ifilles] = GroupeInternat(
                    ifillesid,
                    randint(1, self.capaciteMaxInternat),
                    randint(0, 100)
                )
                igarcons = GroupeClassement(nbEtudiants=self.nbEtudiants)
                igarconsid = GroupeInternatUID(igarcons.C_G_COD, 0)
                self.internatsCommuns[igarcons] = GroupeInternat(
                    igarconsid,
                    randint(1, self.capaciteMaxInternat),
                    randint(0, 100)  # FIXME code de réference différent de ifilles ici
                )

            nbFormations = randint(1, self.nbFormationsParEtablissement)
            for i in range(nbFormations):
                formation = FormationAffectation()
                self.formations.append(formation)

                if self.isInternatParFormation:
                    formation.juryInternat = GroupeClassement(nbEtudiants=self.nbEtudiants)
                    iid = GroupeInternatUID(
                        formation.juryInternat.C_G_COD,
                        formation.G_TA_COD
                    )
                    formation.internat = GroupeInternat(
                        iid,
                        randint(1, self.capaciteMaxInternat),
                        randint(0, 100)
                    )

                nbGroupes = randint(1, self.maxNbGroupesParFormation)
                for j in range(nbGroupes):
                    groupe = GroupeClassement(nbEtudiants=self.nbEtudiants)
                    formation.ajouterGroupe(groupe, self.G_TI_COD, formation.G_TA_COD, self.isConcoursCommun)
                    self.jurys.append(groupe)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.G_TI_COD}, {self.nbEtudiants}, {self.isConcoursCommun}, {self.formations}, {self.jurys}, {self.internatsCommuns})"

    def capacite(self) -> int:
        """ Capacité d'un établissement = somme des capacités de ses formations."""
        return sum(formation.capacite() for formation in self.formations)

    def ajouterVoeux(self, candidat: Candidat) -> int:
        """ Ajoute un vœu (id du candidat)."""
        nbVoeux = 1 + randint(1, self.maxNbVoeuxParConcoursCommun) if self.isConcoursCommun else 1
        for _ in range(nbVoeux):
            fa = choice(self.formations)
            fa.ajouterVoeu(candidat, randbool())
        return nbVoeux
