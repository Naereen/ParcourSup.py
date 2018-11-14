#!/usr/bin/env python3
# -*- coding: utf-8; mode: python -*-
""" ordreappel.exemples, pour https://github.com/Naereen/ParcourSup.py.

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


try:
    from .VoeuClasse import VoeuClasse
    from .GroupeClassement import GroupeClassement
    from .AlgoOrdreAppel import AlgoOrdreAppel
except ImportError:
    from VoeuClasse import VoeuClasse
    from GroupeClassement import GroupeClassement
    from AlgoOrdreAppel import AlgoOrdreAppel


#: En mode débug, on affiche juste le résultat, on n'écrase pas les fichiers de tests.
# DEBUG = True
DEBUG = False


# Classe d'un exemple

class Exemple(object):
    """ Un exemple."""

    def __init__(self):
        self.nom = "Unknown"  #: Nom pour le fichier .xml ou .json de test.
        self.initialise()
        assert hasattr(self, "groupes"), f"Erreur : cet exemple {self} devrait avoir un attribut 'groupes'. La méthode initialise() doit être mal implémentée."  # DEBUG

    def initialise(self) -> None:
        """ Construit l'attribut groupes, il ne doit pas être vide."""
        self.groupes = []
        raise NotImplementedError

    def exporte(self, contenu, entree=True, xml=False, debug=DEBUG) -> bool:
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

    def execute(self) -> None:
        """ Calcule les ordre d'appels et sauvegarde les fichiers."""
        # crée l'entrée
        entree = AlgoOrdreAppel(self.groupes)

        # et sauvegarde l'entrée, d'abord en XML
        entreeXML = entree.exporteEntree_XML()
        contenu = ET.tostring(entreeXML, encoding='unicode', method='xml')
        contenu = DOM.parseString(contenu).toprettyxml(indent=' '*4)
        contenu = contenu.replace('version="1.0" ', 'version="1.0" encoding="UTF-8" standalone="yes"')
        self.exporte(contenu, entree=True, xml=True)

        # et maintenant le JSON
        entreeJSON = entree.exporteEntree_JSON()
        contenu = json.dumps(entreeJSON, sort_keys=True, indent=4)
        self.exporte(contenu, entree=True, xml=False)

        # calcule la sortie
        entree.calculeOrdresAppels()

        # et sauvegarde la sortie, d'abord en XML
        sortieXML = entree.exporteSortie_XML()
        contenu = ET.tostring(sortieXML, encoding='unicode', method='xml')
        contenu = DOM.parseString(contenu).toprettyxml(indent=' '*4)
        contenu = contenu.replace('version="1.0" ', 'version="1.0" encoding="UTF-8" standalone="yes"')
        self.exporte(contenu, entree=False, xml=True)

        # et maintenant le JSON
        sortieJSON = entree.exporteSortie_JSON()
        contenu = json.dumps(sortieJSON, sort_keys=True, indent=4)
        self.exporte(contenu, entree=False, xml=False)


# Exemples


class exempleA1(Exemple):
    """ Exemple A1 avec une contrainte de 20% de boursiers-ère-s et de 0% de non résidents-e-s."""

    def initialise(self) -> None:
        self.nom = 'exemple_A1'
        groupe = GroupeClassement(0, 20, 0)
        # C1 C2 C3 C4 C5 B6 B7 C8
        for i in range(1, 5 + 1):
            groupe.ajouterVoeu(VoeuClasse(i, i, False, False))
        groupe.ajouterVoeu(VoeuClasse(6, 6, True, False))
        groupe.ajouterVoeu(VoeuClasse(7, 7, True, False))
        groupe.ajouterVoeu(VoeuClasse(8, 8, False, False))
        self.groupes = [groupe]  #: GroupeClassement de cet exemple.


class exempleA2(Exemple):
    """ Exemple A2 avec une contrainte de 2% de boursiers-ère-s et de 0% de non résidents-e-s."""

    def initialise(self) -> None:
        self.nom = 'exemple_A2'
        groupe = GroupeClassement(0, 2, 0)
        # C1 C2 C3 C4 C5 B6 C7 C8
        for i in range(1, 5 + 1):
            groupe.ajouterVoeu(VoeuClasse(i, i, False, False))
        groupe.ajouterVoeu(VoeuClasse(6, 6, True, False))
        groupe.ajouterVoeu(VoeuClasse(7, 7, False, False))
        groupe.ajouterVoeu(VoeuClasse(8, 8, False, False))
        self.groupes = [groupe]  #: GroupeClassement de cet exemple.


class exempleA3(Exemple):
    """ Exemple A3 avec une contrainte de 10% de boursiers-ère-s et de 0% de non résidents-e-s."""

    def initialise(self) -> None:
        self.nom = 'exemple_A3'
        groupe = GroupeClassement(0, 10, 0)
        # C1 C2 C3 ...C900 B901 B902 B903 ...B1000
        for i in range(1, 900 + 1):
            groupe.ajouterVoeu(VoeuClasse(i, i, False, False))
        for i in range(901, 1000 + 1):
            groupe.ajouterVoeu(VoeuClasse(i, i, True, False))
        self.groupes = [groupe]  #: GroupeClassement de cet exemple.


class exempleA4(Exemple):
    """ Exemple A4 avec une contrainte de 10% de boursiers-ère-s et de 0% de non résidents-e-s."""

    def initialise(self) -> None:
        self.nom = 'exemple_A4'
        groupe = GroupeClassement(0, 10, 0)
        # C1 B2 B3 C4 C5 C6 C7 B8 C9 C10
        groupe.ajouterVoeu(VoeuClasse(1, 1, False, False))
        groupe.ajouterVoeu(VoeuClasse(2, 2, True, False))
        groupe.ajouterVoeu(VoeuClasse(3, 3, True, False))
        groupe.ajouterVoeu(VoeuClasse(4, 4, False, False))
        groupe.ajouterVoeu(VoeuClasse(5, 5, False, False))
        groupe.ajouterVoeu(VoeuClasse(6, 6, False, False))
        groupe.ajouterVoeu(VoeuClasse(7, 7, False, False))
        groupe.ajouterVoeu(VoeuClasse(8, 8, True, False))
        groupe.ajouterVoeu(VoeuClasse(9, 9, False, False))
        groupe.ajouterVoeu(VoeuClasse(10, 10, False, False))
        self.groupes = [groupe]  #: GroupeClassement de cet exemple.


class exempleA5(Exemple):
    """ Exemple A5 avec une contrainte de 10% de boursiers-ère-s et de 95% de non résidents-e-s."""

    def initialise(self) -> None:
        self.nom = 'exemple_A5'
        groupe = GroupeClassement(0, 10, 95)
        # (BR)1(BR)2R3 . . . R19C20
        # (BR)21(BR)22R23 . . . R39C40
        # (BR)41R42 . . . R50
        # B51R52 . . . R60
        # B61R62 . . . R70
        # B71R72 . . . R80
        # B81R82 . . . R90
        # B91R92 . . . R100.
        for i in range(0, 1 + 1):
            groupe.ajouterVoeu(VoeuClasse(20 * i + 1, 20 * i + 1, True, True))
            groupe.ajouterVoeu(VoeuClasse(20 * i + 2, 20 * i + 2, True, True))
            for j in range(3, 19 + 1):
                groupe.ajouterVoeu(VoeuClasse(20 * i + j, 20 * i + j, False, True))
            groupe.ajouterVoeu(VoeuClasse(20 * i + 20, 20 * i + 20, False, False))

        groupe.ajouterVoeu(VoeuClasse(41, 41, True, True))
        for k in range(42, 50 + 1):
            groupe.ajouterVoeu(VoeuClasse(k, k, False, True))

        for l in range(51, 91 + 1, 10):
            groupe.ajouterVoeu(VoeuClasse(l, l, True, False))
            for m in range(l + 1, l + 9 + 1):
                groupe.ajouterVoeu(VoeuClasse(m, m, False, True))
        self.groupes = [groupe]  #: GroupeClassement de cet exemple.


class exempleA6(Exemple):
    """ Exemple A6 avec une contrainte de 10% de boursiers-ère-s et de 95% de non résidents-e-s."""

    def initialise(self) -> None:
        self.nom = 'exemple_A6'
        groupe = GroupeClassement(0, 10, 95)
        # R1 ... R100
        for i in range(1, 100 + 1):
            groupe.ajouterVoeu(VoeuClasse(i, i, False, True))
        # B101 ... B111
        for i in range(101, 111 + 1):
            groupe.ajouterVoeu(VoeuClasse(i, i, True, False))
        self.groupes = [groupe]  #: GroupeClassement de cet exemple.


#: Liste de tous les exemples.
tous_les_exemples = [
    exempleA1,
    exempleA2,
    exempleA3,
    exempleA4,
    exempleA5,
    exempleA6,
]
