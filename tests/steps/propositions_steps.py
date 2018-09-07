#!/usr/bin/env python3
# -*- coding: utf8 -*-
""" Fichier Python qui définit les étapes permettant le test du module ordreappel avec Cucumber et le module behave.
"""

# ---------------------
# Import des dépendances
from behave import *

import sys
sys.path.insert(0, '..')

# On importe parcoursup
from parcoursup.ordreappel.VoeuClasse import VoeuClasse

from parcoursup.propositions.AlgoPropositions import AlgoPropositions
from parcoursup.propositions.GroupeAffectation import GroupeAffectation
from parcoursup.propositions.GroupeAffectationUID import GroupeAffectationUID
from parcoursup.propositions.GroupeInternat import GroupeInternat
from parcoursup.propositions.GroupeInternatUID import GroupeInternatUID
from parcoursup.propositions.VoeuEnAttente import VoeuEnAttente
from parcoursup.propositions.Candidat import Candidat
from parcoursup.propositions.Etablissement import Etablissement


# ---------------------
# On définit les fonctions utilitaires

from ordreappel_steps import candidat2VoeuClasse, VoeuClasse2candidat


# ---------------------
# On définit les étapes

@given("un internat disposant de {L:d} places")
def step_impl(context, L: int) -> None:
    context.L = L

@given("une liste de {M:d} candidat-e-s")
def step_impl(context, M: int) -> None:
    context.M = M

@given("un taux d'ouverture de {ouverture:d}")
def step_impl(context, ouverture: int) -> None:
    context.ouverture = ouverture

@when("l'appel est lancé le jour {jour:d}")
def step_impl(context, jour: int) -> None:
    context.jour = jour
    groupeInternatUID = GroupeInternatUID(1, 1)
    groupeInternat = GroupeInternat(groupeInternatUID, context.L, context.ouverture)
    bmax = groupeInternat.calculeAssietteAdmission(context.M, context.L, context.jour, context.ouverture)
    context.bmax = bmax

@then("{candidats:d} sont appelé-e-s")
def step_impl(context, candidats: int) -> None:
    assert context.bmax == candidats


# ---------------------
# On définit les étapes, second fichier

@given("une formation dont le rang limite de proposition est {rangLimite:d} et dont la capacité d'accueil est {capaciteFormation:d}")
def step_impl(context, rangLimite: int, capaciteFormation: int) -> None:
    context.rangLimite = rangLimite
    context.capaciteFormation = capaciteFormation

@given("un internat dont la capacité d'accueil est {capaciteInternat:d}")
def step_impl(context, capaciteInternat: int) -> None:
    context.capaciteInternat = capaciteInternat

@given("la valeur de B est {B:d}")
def step_impl(context, B: int) -> None:
    context.B = B

    context.groupeAffectationUID = GroupeAffectationUID(1, 1, 1)
    context.groupeAffectation = GroupeAffectation(context.capaciteFormation, context.groupeAffectationUID, context.rangLimite)

    context.internatUID = GroupeInternatUID(1, context.groupeAffectation.id.G_TA_COD)
    # XXX pourquoi le pourcentage d'ouverture est hardcodé à 10 ?
    context.ouverture = 10
    context.groupeInternat = GroupeInternat(context.internatUID, context.capaciteInternat, context.ouverture)

    # FIXME valeurs de M, L, jour ?
    context.M = 1
    context.L = 1
    context.jour = 1

    # (M: int, L: int, t: int, p: int) -> int:
    nb_valeurs_essayees = 0
    def essaieNouvellesValeurs(max_M=20, max_L=20, max_jour=20):
        context.M += 1
        if context.M >= max_M:
            context.M = 1
            context.L += 1
        if context.L >= max_L:
            context.M = 1
            context.jour += 1
        if context.jour >= max_jour:
            context.jour = 1

    B_calcule = context.groupeInternat.calculeAssietteAdmission(context.M, context.L, context.jour, context.ouverture)
    while nb_valeurs_essayees < 1000 and B != B_calcule:
        nb_valeurs_essayees += 1
        essaieNouvellesValeurs()
        B_calcule = context.groupeInternat.calculeAssietteAdmission(context.M, context.L, context.jour, context.ouverture)

    print("Nous avons trouvé, par exploration forcée, que M = {}, L = {} et jour = {} fonctionnaient pour retrouver B = {}...".format(context.M, context.L, context.jour, B))  # DEBUG
    assert B == B_calcule, "Erreur dans le calcul de B, la valeur calculée est {} et la valeur du test est {}.".format(B_calcule, B)  # DEBUG

@given("les candidat-e-s à la formation sont {candidats}")
def step_impl(context, candidats: str) -> None:
    context.candidatsFormation = [
        candidat2VoeuClasse(candidat)
        for candidat in candidats.split(' ')
    ]

@given("les candidat-e-s à l'internat sont {cdts_internat}")
def step_impl(context, cdts_internat: str) -> None:
    context.candidatsInternat = [
        candidat2VoeuClasse(candidat)
        for candidat in cdts_internat.split(' ')
    ]

@given("les candidat-e-s à la formation sans internat sont {cdts_sans_internat}")
def step_impl(context, cdts_sans_internat: str) -> None:
    context.candidatsSansInternat = [
        candidat2VoeuClasse(candidat)
        for candidat in cdts_sans_internat.split(' ')
    ]

@given("le classement à l'internat est {cl_internat}")
def step_impl(context, cl_internat: str) -> None:
    context.internesClasses = [
        candidat2VoeuClasse(candidat)
        for candidat in cl_internat.split(' ')
    ]

@when("l'ordre d'appel est calculé")
def step_impl(context) -> None:
    for candidat in context.candidatsInternat:
        G_CN_COD = candidat.G_CN_COD
        ordreAppel = context.candidatsFormation.index(candidat) + 1
        rangInternat = context.internesClasses.index(candidat) + 1
        VoeuEnAttente.ajouterVoeu(
            G_CN_COD,
            context.groupeAffectation,
            ordreAppel,
            avecInternat=True,
            internat=context.groupeInternat,
            rangInternat=rangInternat,
        )

    for candidat in context.candidatsSansInternat:
        G_CN_COD = candidat.G_CN_COD
        ordreAppel = context.candidatsFormation.index(candidat) + 1
        VoeuEnAttente.ajouterVoeu(
            G_CN_COD,
            context.groupeAffectation,
            ordreAppel,
        )

    entree = AlgoPropositions(
        [context.groupeAffectation],
        [context.groupeInternat]
    )
    GroupeInternat.nbJoursCampagne = 1
    # calcule la sortie
    entree.calculePropositions()
    context.sortie = entree


from pprint import pprint

def remove_doubles(a_list):
    """ Simple naive not-efficient function to remove doubles in a list but keep the order!"""
    new_list = []
    for el in a_list:
        if el not in new_list:
            new_list.append(el)
    return new_list


@then("les candidat-e-s suivant-e-s reçoivent une proposition pour la formation {prop_formation}")
def step_impl(context, prop_formation: str) -> None:
    context.prop_formation = context.sortie.propositions
    context.prop_formation_convertie = remove_doubles([
        candidat.G_CN_COD
        for candidat in context.prop_formation
    ])

    if prop_formationf == '-':
        prop_formation_convertie = []
    else:
        prop_formation_convertie = [
            candidat2VoeuClasse(candidat).G_CN_COD
            for candidat in prop_formation.split(' ')
        ]
    assert context.prop_formation_convertie == prop_formation_convertie, "La prop_formation ne correspond pas à celle du contexte.\ncontext.prop_formation_convertie = {} et prop_formation_convertie = {} (prop_formation = {})...".format(context.prop_formation_convertie, prop_formation_convertie, prop_formation)  # DEBUG

    pprint(context.prop_formation_convertie)  # DEBUG
    pprint(prop_formation_convertie)  # DEBUG
    pprint(prop_formation)  # DEBUG

    idCandidatsRetenus = [
        voeu.G_CN_COD
        for voeu in
        sorted(context.prop_formation, key=lambda voeu: voeu.ordreAppel)
    ]
    idCandidatsRetenus = list(set(idCandidatsRetenus))

    if prop_formation == '-':
        candidatsRetenusFormationAttendus = []
    else:
        candidatsRetenusFormationAttendus = [
            # int(candidatStr[1:])
            candidat2VoeuClasse(candidatStr).G_CN_COD  # more complex than just reading the string, but safer/cleaner!
            for candidatStr in prop_formation.split(' ')
            if candidatStr != '-'
        ]

    assert candidatsRetenusFormationAttendus == idCandidatsRetenus, "Erreur : la liste candidatsRetenusFormationAttendus = {} n'est pas contenue dans la liste idCandidatsRetenus = {}...".format(candidatsRetenusFormationAttendus, idCandidatsRetenus)  # DEBUG


@then("les candidat-e-s suivant-e-s reçoivent une proposition pour l'internat {prop_internat}")
def step_impl(context, prop_internat: str) -> None:
    context.prop_internat = context.sortie.internats_sortie
    context.prop_internat_convertie = remove_doubles([
        candidat.G_CN_COD
        for candidat in context.prop_formation
    ])

    if prop_internat == '-':
        prop_internat_convertie = []
    else:
        prop_internat_convertie = [
            candidat2VoeuClasse(candidat).G_CN_COD
            for candidat in prop_internat.split(' ')
        ]
    assert context.prop_internat_convertie == prop_internat_convertie, "La prop_internat_convertie ne correspond pas à celle du contexte.\ncontext.prop_internat_convertie = {} et prop_internat_convertie = {} (prop_internat_convertie = {})...".format(context.prop_internat_convertie, prop_internat_convertie, prop_internat_convertie)  # DEBUG

    pprint(context.prop_internat_convertie)  # DEBUG
    pprint(prop_internat_convertie)  # DEBUG
    pprint(prop_internat)  # DEBUG

    idCandidatsRetenusInternat = [
        voeu.G_CN_COD
        for voeu in
        sorted(context.prop_formation, key=lambda voeu: voeu.rangInternat)
        if voeu.id.I_RH_COD > 0  # FIXME is this the goal of this .filter(voeu -> voeu.id.I_RH_COD) above?
    ]
    idCandidatsRetenusInternat = list(set(idCandidatsRetenusInternat))

    if prop_internat == '-':
        candidatsRetenusAttendus = []
    else:
        candidatsRetenusAttendus = [
            # int(candidatStr[1:])
            candidat2VoeuClasse(candidatStr).G_CN_COD  # more complex than just reading the string, but safer/cleaner!
            for candidatStr in prop_internat.split(' ')
            if candidatStr != '-'
        ]

    assert candidatsRetenusAttendus == idCandidatsRetenusInternat, "Erreur : la liste candidatsRetenusAttendus = {} n'est pas contenue dans la liste idCandidatsRetenusInternat = {}...".format(candidatsRetenusAttendus, idCandidatsRetenusInternat)  # DEBUG


@then("les candidat-e-s suivant-e-s sont en attente pour l'internat {en_attente}")
def step_impl(context, en_attente: str) -> None:
    context.en_attente = context.sortie.enAttentes
    context.en_attente_convertie = remove_doubles([
        candidat.G_CN_COD
        for candidat in context.prop_formation
    ])

    if en_attente == '-':
        en_attente_convertie = []
    else:
        en_attente_convertie = [
            candidat2VoeuClasse(candidat).G_CN_COD
            for candidat in en_attente.split(' ')
        ]
    assert context.en_attente_convertie == en_attente_convertie, "La en_attente_convertie ne correspond pas à celle du contexte.\n\ncontext.en_attente_convertie = {} et en_attente_convertie = {} (en_attente_convertie = {})...".format(context.en_attente_convertie, en_attente_convertie, en_attente)  # DEBUG

    pprint(context.en_attente_convertie)  # DEBUG
    pprint(en_attente_convertie)  # DEBUG
    pprint(en_attente)  # DEBUG

    idCandidatsEnAttente = [
        voeu.G_CN_COD
        for voeu in
        sorted(context.prop_formation, key=lambda voeu: voeu.rangInternat)
        if voeu.id.I_RH_COD > 0  # FIXME is this the goal of this .filter(voeu -> voeu.id.I_RH_COD) above?
    ]
    idCandidatsEnAttente = list(set(idCandidatsEnAttente))

    if en_attente == '-':
        candidatsEnAttenteAttendusTab = []
    else:
        candidatsEnAttenteAttendusTab = [
            # int(candidatStr[1:])
            candidat2VoeuClasse(candidatStr).G_CN_COD  # more complex than just reading the string, but safer/cleaner!
            for candidatStr in en_attente.split(' ')
            if candidatStr != '-'
        ]

    assert candidatsEnAttenteAttendusTab == idCandidatsEnAttente, "Erreur : la liste candidatsEnAttenteAttendusTab = {} n'est pas contenue dans la liste idCandidatsEnAttente = {}...".format(candidatsEnAttenteAttendusTab, idCandidatsEnAttente)  # DEBUG
