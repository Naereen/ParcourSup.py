#!/usr/bin/env python3
# -*- coding: utf-8; mode: python -*-
""" propositions.exemples, pour https://github.com/Naereen/ParcourSup.py.

- Auteurs : Lilian Besson, Bastien Trotobas et al, (C) 2018.
- Adresse : https://github.com/Naereen/ParcourSup.py
- Licence : MIT License (http://lbesson.mit-license.org).
"""
__author__ = "Lilian Besson, Bastien Trotobas et al"
__version__ = "0.2"

import json
from os import path
import xml.etree.ElementTree as ET
import xml.dom.minidom as DOM
from datetime import datetime
from typing import List, Union
from random import randint, random, choice

try:
    from tqdm import tqdm  # DEBUG Cf. https://github.com/tqdm/tqdm#usage
except ImportError:
    print("Attention : le module 'tqdm' n'a pas été trouvé, installez le avec :\nsudo pip3 install tqdm")
    def tqdm(iterable=None, desc=None):
        return iterable

try:
    from .AlgoPropositions import AlgoPropositions

    from .GroupeAffectation import GroupeAffectation
    from .GroupeAffectationUID import GroupeAffectationUID
    from .GroupeInternat import GroupeInternat
    from .GroupeInternatUID import GroupeInternatUID
    from .VoeuEnAttente import VoeuEnAttente

    from .Candidat import Candidat
    from .Etablissement import Etablissement
except ImportError:
    from AlgoPropositions import AlgoPropositions

    from GroupeAffectation import GroupeAffectation
    from GroupeAffectationUID import GroupeAffectationUID
    from GroupeInternat import GroupeInternat
    from GroupeInternatUID import GroupeInternatUID
    from VoeuEnAttente import VoeuEnAttente

    from Candidat import Candidat
    from Etablissement import Etablissement



def log(*args, **kwargs):
    """ Affiche avec une heure."""
    now = datetime.now()
    print(f"{now:%d-%m-%Y %H:%M:%S}", *args, **kwargs)



def randbool() -> bool:
    """ Pile ou face, True avec probabilité 1/2 et False avec probabilité 1/2."""
    return random() <= 0.5


#: En mode débug, on affiche juste le résultat.
# DEBUG = True
DEBUG = False


# Classe d'un exemple

class Exemple(object):
    """ Un exemple."""

    def __init__(self):
        self.n = 0  #: Nombre total de candidats
        self.nom = "Unknown"  #: Nom pour le fichier .xml ou .json de test.
        self.sortie: Union[None, AlgoPropositions] = None

        self.donneesEntree()
        assert hasattr(self, "nbPlacesTotalInternat"), f"Erreur : cet exemple {self} devrait avoir un attribut 'nbPlacesTotalInternat'. La méthode donneesEntree() doit être mal implémentée."  # DEBUG
        assert hasattr(self, "groupes"), f"Erreur : cet exemple {self} devrait avoir un attribut 'groupes'. La méthode donneesEntree() doit être mal implémentée."  # DEBUG
        assert hasattr(self, "internats"), f"Erreur : cet exemple {self} devrait avoir un attribut 'internats'. La méthode donneesEntree() doit être mal implémentée."  # DEBUG

    def donneesEntree(self):
        """ Construit l'attribut groupes et internat, il ne doit pas être vide."""
        self.nbPlacesTotalInternat = -1  #: Place total des internats
        self.groupes: List[GroupeAffectation] = []  #: List des groupes des affectations
        self.internats: List[GroupeInternat] = []  #: List des groupes des internats
        raise NotImplementedError

    def exporte(self, contenu, entree=True, xml=False, debug=DEBUG):
        """ Exporte l'entrée ou la sortie, dans un fichier XML ou JSON."""
        extension = 'xml' if xml else 'json'
        entree_ou_sortie = 'entree' if entree else 'sortie'
        nom_fichier = path.join(path.dirname(__file__), '..', '..', 'donnees', f'{self.nom}_{entree_ou_sortie}.{extension}')
        if debug:
            print(f"On devrait sauvegarder le contenu suivant dans le fichier '{nom_fichier}'...")  # DEBUG
            print(contenu)  # DEBUG
            return False
        if path.exists(nom_fichier):
            print(f"\nAttention : le fichier de sortie '{nom_fichier}' existe déjà...")  # DEBUG
        with open(nom_fichier, "w") as fichier:
            print(f"Contenu écrit dans le fichier {nom_fichier}...")  # DEBUG
            # print(contenu)  # DEBUG
            fichier.write(contenu)
        return True

    def execute(self, sauvegarde=True):
        """ Calcule les ordre d'appels et sauvegarde les fichiers."""
        # crée l'entrée
        entree = AlgoPropositions(self.groupes, self.internats)

        # calcule la sortie
        entree.calculePropositions()
        self.sortie = entree

        if sauvegarde:
            # et sauvegarde les deux, d'abord en XML
            entreeJSON = entree.exporteEntree_JSON()
            contenu = json.dumps(entreeJSON, sort_keys=True, indent=4)
            self.exporte(contenu, entree=True, xml=False)

            # et sauvegarde l'entrée, d'abord en XML
            entreeXML = entree.exporteEntree_XML()
            contenu = ET.tostring(entreeXML, encoding='unicode', method='xml')
            contenu = DOM.parseString(contenu).toprettyxml(indent=' '*4)
            contenu = contenu.replace('version="1.0" ', 'version="1.0" encoding="UTF-8" standalone="yes"')
            self.exporte(contenu, entree=True, xml=True)

        if sauvegarde:
            # et maintenant le JSON
            sortieJSON = entree.exporteSortie_JSON()
            contenu = json.dumps(sortieJSON, sort_keys=True, indent=4)
            self.exporte(contenu, entree=False, xml=False)

            # et sauvegarde la sortie, d'abord en XML
            sortieXML = entree.exporteSortie_XML()
            contenu = ET.tostring(sortieXML, encoding='unicode', method='xml')
            contenu = DOM.parseString(contenu).toprettyxml(indent=' '*4)
            contenu = contenu.replace('version="1.0" ', 'version="1.0" encoding="UTF-8" standalone="yes"')
            self.exporte(contenu, entree=False, xml=True)


# Exemples


class exempleB7base(Exemple):
    """ Exemple B7 de base."""

    def donneesEntree(self):
        self.nom = 'Exemple_B7'
        groupe = GroupeAffectation(
            40,
            GroupeAffectationUID(1, 1, 1),
            0
        )
        self.groupes = [groupe]
        self.nbPlacesTotalInternat = 10
        self.internats = [GroupeInternat(
            GroupeInternatUID(1, groupe.id.G_TA_COD),
            self.nbPlacesTotalInternat,
            100   # pourcentageOuverture
        )]


class exempleB7Jour1(exempleB7base):
    """ Exemple B7 du jour 1."""

    def donneesEntree(self) -> None:
        GroupeInternat.nbJoursCampagne = 1
        super().donneesEntree()
        self.n = 332  #: Nombre total de candidats
        self.nom = 'ExempleB7Jour1'
        groupe = self.groupes[0]
        internat = self.internats[0]

        VoeuEnAttente.ajouterVoeu(1,  groupe, 1,  internat=internat, rangInternat=28)
        VoeuEnAttente.ajouterVoeu(2,  groupe, 2,  internat=internat, rangInternat=15)
        VoeuEnAttente.ajouterVoeu(20, groupe, 20, internat=internat, rangInternat=5)
        VoeuEnAttente.ajouterVoeu(21, groupe, 21, internat=internat, rangInternat=6)

        for i in range(1, self.n + 1):
            # 1 -- 28
            # 2 -- 15
            # 3 -- 1
            # 4 -- 2
            # 5 -- 3
            # 6 -- 4
            # 7 -- 7
            # ...
            # 14 -- 14
            # 15 -- 16
            # ...
            # 19 -- 20
            # 20 -- 5
            # 21 -- 6
            # 22 -- 21
            # ...
            # 28 -- 27
            # 29 -- 29
            # ...
            if i in {1, 2, 20, 21}:
                continue
            G_CN_COD = i
            ordreAppel = i
            rangInternat = i
            if i <= 6:
                rangInternat = i - 2
            elif i <= 14:
                rangInternat = i
            elif i <= 20:
                rangInternat = i + 1
            elif i <= 28:
                rangInternat = i - 1
            VoeuEnAttente.ajouterVoeu(G_CN_COD, groupe, ordreAppel, internat=internat, rangInternat=rangInternat)


class exempleB7Jour2(exempleB7base):
    """ Exemple B7 du jour 2."""

    def donneesEntree(self) -> None:
        J1 = exempleB7Jour1()
        J1.execute(sauvegarde=False)
        sortie = J1.sortie

        super().donneesEntree()
        self.n = 332  #: Nombre total de candidats
        self.nom = 'ExempleB7Jour2'
        groupe = self.groupes[0]
        internat = self.internats[0]

        # C21 et C30 déclinent.
        for voeu in sortie.propositions:
            if voeu.id.G_CN_COD in {21, 30}:
                continue
            internat.ajouterCandidatAffecte(voeu.id.G_CN_COD)

        # Cf. https://framagit.org/parcoursup/algorithmes-de-parcoursup/issues/13
        # for voeu in sortie.enAttentes:
        #     if voeu.id.G_CN_COD in {21, 30}:
        #         continue
        #     # FIXME dans le code de référence, cette ligne n'est pas là !
        #     # Cf. https://framagit.org/parcoursup/algorithmes-de-parcoursup/blob/9ef555/java/parcoursup/propositions/exemples/ExempleB7Jour2.java#L48
        #     internat.ajouterCandidatAffecte(voeu.id.G_CN_COD)

        GroupeInternat.nbJoursCampagne = 2

        for voeu in sortie.enAttentes:
            if voeu.id.G_CN_COD in {21, 30}:
                continue
            VoeuEnAttente.ajouterVoeu(voeu.id.G_CN_COD, groupe, voeu.ordreAppel, internat=internat, rangInternat=voeu.rangInternat)


class exempleB7Jour3(exempleB7base):
    """ Exemple B7 du jour 3."""

    def donneesEntree(self) -> None:
        J2 = exempleB7Jour2()
        J2.execute(sauvegarde=False)
        sortie = J2.sortie

        super().donneesEntree()
        self.n = 332  #: Nombre total de candidats
        self.nom = 'ExempleB7Jour3'
        groupe = self.groupes[0]
        internat = self.internats[0]

        # C1 à C20 déclinent.
        for voeu in sortie.propositions:
            if voeu.id.G_CN_COD <= 20:
                continue
            internat.ajouterCandidatAffecte(voeu.id.G_CN_COD)

        # Cf. https://framagit.org/parcoursup/algorithmes-de-parcoursup/issues/13
        # FIXME dans le code de référence, cette ligne est là mais ne devrait pas !
        # # Cf. https://framagit.org/parcoursup/algorithmes-de-parcoursup/blob/9ef555/java/parcoursup/propositions/exemples/ExempleB7Jour3.java#L57
        # for voeu in sortie.enAttentes:
        #     if voeu.id.G_CN_COD <= 20:
        #         continue
        #     internat.ajouterCandidatAffecte(voeu.id.G_CN_COD)

        GroupeInternat.nbJoursCampagne = 3

        for voeu in sortie.enAttentes:
            if voeu.id.G_CN_COD <= 20:
                continue
            VoeuEnAttente.ajouterVoeu(voeu.id.G_CN_COD, groupe, voeu.ordreAppel, internat=internat, rangInternat=voeu.rangInternat)


class exempleAleatoire(exempleB7base):
    """ Exemple aléatoire très complet et compliqué.
    """
    maxNbVoeuxParCandidat = 40

    def __init__(self,
        nbEtudiants: int=100
    ):
        super().__init__()
        nbEtudiants = min(nbEtudiants, 100)
        self.nbEtudiants = nbEtudiants

    def donneesEntree(self) -> None:
        Etablissement.last_G_TI_COD = 1
        etablissements: List[Etablissement] = []

        GroupeInternat.nbJoursCampagne = 1 + randint(1, 70)
        log(f"Jours de campagne : {GroupeInternat.nbJoursCampagne}")

        log("\n\nGénération aléatoire des établissements et formations...")
        capacite_totale = 0
        while capacite_totale < self.nbEtudiants:
            etablissement = Etablissement(self.nbEtudiants)
            etablissements.append(etablissement)
            capacite_totale += etablissement.capacite()
            log(f"  Un nouvel établissement de capacité {etablissement.capacite()} ajouté. Capacité total {capacite_totale}...")

        log("\n\nGénération aléatoire des vœux et classements...")
        for etudiant in tqdm(iterable=range(self.nbEtudiants), desc="Etudiants"):
            candidat = Candidat()
            nbVoeux = randint(0, self.maxNbVoeuxParCandidat)
            while nbVoeux > 0:
                etablissement = choice(etablissements)
                nbVoeux -= etablissement.ajouterVoeux(candidat)
            if (etudiant + 1) % 1000 == 0:
                log(f"{etudiant + 1} nouveaux-elles étudiant-es généré-es ...")

        log("\n\nGénération données entrée algorithme...")

        entree = AlgoPropositions([], [])

        for etablissement in tqdm(iterable=etablissements, desc="Etablissements"):
            for fa in tqdm(iterable=etablissement.formations, desc="Formations"):
                entree.groupesAffectations.update(fa.groupes)
                if fa.internat is not None and fa.internat.candidatsEnAttente:
                    entree.internats.append(fa.internat)

            for internat in tqdm(iterable=etablissement.internatsCommuns.values(), desc="InternatsCommuns"):
                if internat.candidatsEnAttente:
                    entree.internats.append(internat)


#: Liste de tous les exemples.
tous_les_exemples = [
    exempleB7base,
    exempleB7Jour1,
    exempleB7Jour2,
    exempleB7Jour3,
    # exempleAleatoire,
]
