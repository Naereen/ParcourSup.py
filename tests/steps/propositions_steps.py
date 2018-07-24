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
def step_impl(context, L):
    context.L = L

@given("une liste de {M:d} candidats")
def step_impl(context, M):
    context.M = M

@given("un taux d'ouverture de {ouverture:d}")
def step_impl(context, ouverture):
    context.ouverture = ouverture

@when("l'appel est lancé le jour {jour:d}")
def step_impl(context, jour):
    context.jour = jour
    groupeInternatUID = GroupeInternatUID(1, 1)
    groupeInternat = GroupeInternat(groupeInternatUID, context.L, context.ouverture)
    bmax = groupeInternat.calculeAssietteAdmission(context.M, context.L, context.jour, context.ouverture)
    context.bmax = bmax

@then("{candidats:d} sont appelés")
def step_impl(context, candidats):
    assert context.bmax == candidats
