#!/usr/bin/env python3
# -*- coding: utf-8; mode: python -*-
""" VerificationsResultats, pour https://github.com/Naereen/ParcourSup.py.

- Permet de vérifier un certain nombre de propriétés statiques des sorties de l'algorithme.
- Sans garantir la correction du code, cela garantit que les résultats produits satisfont les principales propriétés énoncées dans le document.

.. warning:: FIXME Des tests complémentaires sont effectués en base par des scripts PL/SQL.

- Auteurs : Lilian Besson, Bastien Trotobas et al, (C) 2018.
- Adresse : https://github.com/Naereen/ParcourSup.py
- Licence : MIT License (http://lbesson.mit-license.org).
"""
__author__ = "Lilian Besson, Bastien Trotobas et al"
__version__ = "0.2.1"

from typing import Dict, Set
from datetime import datetime

try:
    from .GroupeAffectation import GroupeAffectation
    from .GroupeInternat import GroupeInternat
except ImportError:
    from GroupeAffectation import GroupeAffectation
    from GroupeInternat import GroupeInternat


def log(*args, **kwargs):
    """ Affiche avec une heure."""
    now = datetime.now()
    print(f"{now:%d-%m-%Y %H:%M:%S}", *args, **kwargs)



def verifierRespectOrdreAppelVoeuxSansInternat(formation: GroupeAffectation):
    """ P1 : respect ordre appel pour les voeux sans internat.

    Si un candidat C1 précède un candidat C2 dans l'ordre d'appel d'une formation F
    et si C1 a un voeu en attente pour F sans demande d'internat
    alors C2 n'a pas de proposition pour F.
    """
    for voeu1 in formation.voeux:
        if not voeu1.avecClassementInternat() and not voeu1.estAProposer():
            for voeu2 in formation.voeux:
                assert voeu2.ordreAppel <= voeu1.ordreAppel or (not voeu2.avecClassementInternat() and not voeu2.estAProposer()), f"Violation respect ordre appel pour deux vœux sans demandes d'internat \nvoeu1 = {voeu1},\nvoeu2 = {voeu2}."


def verifierVoeuxAvecInternat(formation: GroupeAffectation):
    """ P2 respect ordre appel et classement internat pour les voeux avec internat.

    Si un candidat C1 précède un candidat C2
    à la fois dans l'ordre d'appel d'une formation F
    et dans un classement d'internat I
    et si C1 a un voeu en attente pour F avec internat I
    alors C2 n'a pas de proposition pour F avec internat I.
    """
    for voeu1 in formation.voeux:
        if voeu1.avecClassementInternat() and not voeu1.estAProposer():
            for voeu2 in formation.voeux:
                assert not(
                    voeu2.avecClassementInternat()
                    and voeu1.internatID() == voeu2.internatID()
                    and (not voeu2.formationDejaObtenue() and voeu2.ordreAppel > voeu1.ordreAppel)
                    and (not voeu2.internatDejaObtenu() and voeu2.rangInternat > voeu1.rangInternat)
                    and voeu2.avecInternat()
                    and voeu2.estAProposer()
                ), f"Violation respect ordre et classement pour deux vœux sans demandes d'internat \nvoeu1 = {voeu1},\nvoeu2 = {voeu2}."


def verifierRespectClassementInternat(formation: GroupeAffectation):
    """ P3 respect classement internat pour les candidats avec une proposition sans internat.

    Si un candidat C1 a un voeu en attente pour une formation F avec demande d'internat I
    et une proposition acceptée ou en attente de réponse de sa part pour la formation F
    sans demande d'internat,
    et si C2 est un candidat moins bien classé que C1 à l'internat I
    et si une des nouvelles propositions du jour offre l'internat I à C2
    alors que C2 n'avait pas de propositions pour I auparavant
    alors une des nouvelles propositions du jour offre la formation F et l'internat I à C1.
    """
    for voeu1 in formation.voeux:
        if voeu1.formationDejaObtenue() and not voeu1.estAProposer():
            for voeu2 in formation.voeux:
                assert not(
                    voeu1.rangInternat > voeu2.rangInternat
                    and not voeu2.internatDejaObtenu()
                    and voeu2.estAProposer()
                ), f"Violation respect ordre d'appel pour les attributions d'internat \nvoeu1 = {voeu1}\n voeu2 = {voeu2}."


def verifierSurcapaciteEtRemplissage(formation: GroupeAffectation):
    """ P4 remplissage maximal des formations dans le respect des positions d'admission à l'internat.

    Le nombre de propositions doit être inférieur au nombre de places vacantes.

    Si le nombre de nouvelles propositions dans une formation est strictement inférieur
    au nombre de places vacantes dans cette formation, alors tous les voeux en attente
    pour cette formation sont des voeux avec internat,
    effectués par des candidats dont le rang de classement dans l'internat correspondant
    est strictement supérieur à la position d'admission dans cet internat.
    """
    candidatsProposes: Set[int] = set()

    rangDernierNouvelAppele = 0
    for voeu in formation.voeux:
        if voeu.estAProposer() and not voeu.formationDejaObtenue():
            candidatsProposes.add(voeu.id.G_CN_COD)
            rangDernierNouvelAppele = max(rangDernierNouvelAppele, voeu.ordreAppel)
    nbPropositions = len(candidatsProposes)

    if nbPropositions > formation.nbPlacesVacantes() and rangDernierNouvelAppele > formation.rangLimite:
        log(f"Surcapacité formation non expliquée par le rang limite, veuillez vérifier qu'une diminution de la surréseravation a eu lieu pour le groupe de classement C_GP_COD = {formation.id.C_GP_COD}, G_TA_COD = {formation.id.G_TA_COD}, G_TI_COD = {formation.id.G_TI_COD}.")
    assert not(
        nbPropositions > formation.nbPlacesVacantes()
        and not formation.estInitialementEnSurcapacite()
        and (rangDernierNouvelAppele > formation.rangLimite)
    ), f"Surcapacité de la formation C_GP_COD = {formation.id.C_GP_COD}, G_TA_COD = {formation.id.G_TA_COD}, G_TI_COD = {formation.id.G_TI_COD}."

    if nbPropositions < formation.nbPlacesVacantes():
        for voeu in formation.voeux:
            if not voeu.estAProposer():
                assert voeu.avecClassementInternat(), "Souscapacité formation compensable par un voeu sans classement internat."
                assert voeu.estDesactiveParPositionAdmissionInternat(), "Souscapacité compensable par un voeu avec classement internat classé sous la position d'admission internat."


def verifierSurcapaciteEtRemplissage_avec_rangDernierAppeles(
        internat: GroupeInternat,
        rangsMaxNouvelArrivant: Dict[GroupeInternat, int]
    ):
    """ P5 remplissage maximal des internats dans le respect des ordres d'appel.

    Le nombre de propositions doit être inférieur au nombre de places vacantes.

    Si le nombre de nouvelles propositions dans un internat I est strictement inférieur
    au nombre de places vacantes dans I, alors tous les voeux en attente
    pour une formation F et demande d'internat I sont
    soit effectués par des candidats
    dont le classement à l'internat I est strictement supérieur
    à la position d'admission dans I ou bien situés plus bas dans l'ordre d'appel de F
    que tous les candidats ayant reçu une estAProposer de F ce jour là.
    """
    # un même candidat peut avoir plusieurs propositions
    # pour le même internat, émanant de différentes formations
    candidatsProposes: Set[int] = set()

    for voeu in internat.voeux:
        if voeu.estAProposer() and not voeu.internatDejaObtenu():
            candidatsProposes.add(voeu.id.G_CN_COD)

    nbNouveauxArrivants = len(candidatsProposes)
    assert not (nbNouveauxArrivants > 0 and nbNouveauxArrivants > internat.nbPlacesVacantes()), "Surcapacité internat"

    if nbNouveauxArrivants < internat.nbPlacesVacantes():
        for voeu in internat.voeux:
            if not voeu.estAProposer():
                formation = voeu.groupe
                assert formation in internat.groupesConcernes, "formation inconnue (?)"
                assert not(
                    (voeu.internatDejaObtenu() or voeu.rangInternat <= internat.positionAdmission)
                    and (voeu.formationDejaObtenue() or voeu.ordreAppel <= rangsMaxNouvelArrivant[voeu.groupe])
                ), "Souscapacité internat compensable par un voeu classé sous la position d'admission internat et classé sous le rang du dernier appelé dans la formation"

def verifierMaximalitePositionsAdmission(internat: GroupeInternat):
    """ P6 : maximalité des positions d'admission.

    Pour tout internat, la position d'admission est inférieure ou égale à la position maximale d'admission.
    Dans le cas où elle est strictement inférieure, augmenter d'une unité la position d'admission
    entrainerait une surcapacité d'un des internats.

    .. warning:: FIXME le code de référence ne l'a pas fait ("Non-implémenté."), mais nous pouvons essayer ?
    """
    raise NotImplementedError
