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
from parcoursup.ordreappel.GroupeClassement import GroupeClassement
from parcoursup.ordreappel.AlgoOrdreAppel import AlgoOrdreAppel


# ---------------------
# On définit les fonctions utilitaires

def candidat2VoeuClasse(candidat: str) -> VoeuClasse:
    """Transforme une chaîne du type "C1", "B2", "R3" ou "T4" en un VoeuClasse. """

    estBoursier = candidat[0] in {'B', 'T'}
    estResident = candidat[0] in {'R', 'T'}
    rang = int(candidat[1:])
    return VoeuClasse(rang, rang, estBoursier, estResident)


def chaineTypeCandidat(voeu: VoeuClasse) -> str:
    estBoursier = voeu.estBoursier()
    estResident = voeu.estResident()
    if estBoursier and not estResident:
        return "B"
    elif estBoursier and estResident:
        return "T"
    elif not estBoursier and estResident:
        return "R"
    elif not estBoursier and not estResident:
        return "C"
    else:
        return "C"


def VoeuClasse2candidat(voeu: VoeuClasse) -> str:
    """Transforme un VoeuClasse en une chaîne du type "C1", "B2", "R3" ou "T4". """
    return "{}{}".format(chaineTypeCandidat(voeu), voeu.rang)


# ---------------------
# On définit les étapes

@given("les candidat-e-s sont {liste_candidats}")
def step_impl(context, liste_candidats):
    liste_candidats = liste_candidats.split(' ')
    context.liste_candidats = liste_candidats

@given("le taux minimum de boursier-ère-s est {qb:d}")
def step_impl(context, qb):
    context.qb = qb

@given("le taux minimum de résident-e-s est {qr:d}")
def step_impl(context, qr):
    context.qr = qr

@when("l'appel est calculé")
def step_impl(context):
    if not hasattr(context, "qb"): context.qb = 0
    if not hasattr(context, "qr"): context.qr = 0
    groupe = GroupeClassement(0, context.qb, context.qr)
    for candidat in context.liste_candidats:
        groupe.ajouterVoeu(candidat2VoeuClasse(candidat))
    groupes = [groupe]
    entree = AlgoOrdreAppel(groupes)
    entree.calculeOrdresAppels()
    # un seul à extraire
    ordreAppel = list(entree.ordresAppel.values())[0]
    order_appel_calcule = [VoeuClasse2candidat(voeu) for voeu in ordreAppel]
    context.order_appel_calcule = ' '.join(order_appel_calcule)

@then("l'ordre d'appel est {ordre_appel}")
def step_impl(context, ordre_appel):
    assert len(context.order_appel_calcule) == len(ordre_appel)
    # print("Ordre calculé =\n", context.order_appel_calcule)
    # print("Ordre correct =\n", ordre_appel)
    assert context.order_appel_calcule == ordre_appel
