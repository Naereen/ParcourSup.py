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
    B_calcule = context.groupeInternat.calculeAssietteAdmission(context.M, context.L, context.jour, context.ouverture)
    assert B == B_calcule, "Erreur dans le calcul de B."

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


@then("les candidat-e-s suivant-e-s reçoivent une proposition pour la formation {prop_formation}")
def step_impl(context, prop_formation: str) -> None:
    context.prop_formation = context.sortie.propositions
    assert context.prop_formation == [
        candidat2VoeuClasse(candidat)
        for candidat in prop_formation.split(' ')
    ]

    # idCandidatsRetenus = sortie.propositions.stream()
    #     .sorted(Comparator.comparing(voeuEnAttente -> voeuEnAttente.ordreAppel))
    #     .map(voeuEnAttente -> voeuEnAttente.id.G_CN_COD)
    #     .distinct()
    #     .collect(Collectors.toList())

    # candidatsRetenusFormationAttendus = Arrays.stream(candidatsRetenusFormation.split(" "))
    #     .filter(candidat -> !candidat.equals(("-")))
    #     .map(candidat -> Integer.parseInt(candidat.substring(1)))
    #     .collect(Collectors.toList())
    # Assertions.assertThat(idCandidatsRetenus).containsExactlyElementsOf(candidatsRetenusFormationAttendus)

@then("les candidat-e-s suivant-e-s reçoivent une proposition pour l'internat {prop_internat}")
def step_impl(context, prop_internat: str) -> None:
    context.prop_internat = context.sortie.internats_sortie
    assert context.prop_internat == [
        candidat2VoeuClasse(candidat)
        for candidat in prop_internat.split(' ')
    ]

    # idCandidatsRetenusInternat = sortie.propositions.stream()
    #     .sorted(Comparator.comparing(voeuEnAttente -> voeuEnAttente.rangInternat))
    #     .filter(voeuEnAttente -> voeuEnAttente.id.I_RH_COD)
    #     .map(voeuEnAttente -> voeuEnAttente.id.G_CN_COD)
    #     .distinct()
    #     .collect(Collectors.toList())

    # candidatsRetenusAttendus = Arrays.stream(candidatsRetenusInternat.split(" "))
    #     .filter(candidat -> !candidat.equals(("-")))
    #     .map(candidat -> Integer.parseInt(candidat.substring(1)))
    #     .collect(Collectors.toList())
    # Assertions.assertThat(idCandidatsRetenusInternat).containsExactlyElementsOf(candidatsRetenusAttendus)

@then("les candidat-e-s suivant-e-s sont en attente pour l'internat {en_attente}")
def step_impl(context, en_attente: str) -> None:
    context.en_attente = context.sortie.enAttentes
    assert context.en_attente == [
        candidat2VoeuClasse(candidat)
        for candidat in en_attente.split(' ')
    ]

    # idCandidatsEnAttente = sortie.enAttente.stream()
    #     .sorted(Comparator.comparing(voeuEnAttente -> voeuEnAttente.rangInternat))
    #     .filter(voeuEnAttente -> voeuEnAttente.id.I_RH_COD)
    #     .map(voeuEnAttente -> voeuEnAttente.id.G_CN_COD)
    #     .distinct()
    #     .collect(Collectors.toList())

    # candidatsEnAttenteAttendusTab = Arrays.stream(candidatsEnAttenteAttendus.split(" "))
    #     .filter(candidat -> !candidat.equals(("-")))
    #     .map(candidat -> Integer.parseInt(candidat.substring(1)))
    #     .collect(Collectors.toList())

    # Assertions.assertThat(idCandidatsEnAttente).containsExactlyElementsOf(candidatsEnAttenteAttendusTab)
