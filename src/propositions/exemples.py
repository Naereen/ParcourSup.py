#!/usr/bin/env python3
# -*- coding: utf-8; mode: python -*-
""" propositions.exemples, pour https://github.com/Naereen/ParcourSup.py.

- Auteurs: Lilian Besson, Bastien Trotobas et al, (C) 2018.
- Adresse: https://github.com/Naereen/ParcourSup.py
- Licence: MIT License (http://lbesson.mit-license.org).
"""
__author__ = "Lilian Besson, Bastien Trotobas et al"
__version__ = "0.0.1"

import json
from os import path
import xml.etree.ElementTree as ET
import xml.dom.minidom as DOM

from AlgoProposition import AlgoProposition


#: En mode débug, on affiche juste le résultat.
# DEBUG = True
DEBUG = False


# Classe d'un exemple

class Exemple(object):
    """ Un exemple."""

    def __init__(self):
        self.nom = "Unknown"  #: Nom pour le fichier .xml ou .json de test.
        self.initialise()
        assert hasattr(self, "groupes"), f"Erreur : cet exemple {self} devrait avoir un attribut 'groupes'. La méthode initialise() doit être mal implémentée."  # DEBUG

    def initialise(self):
        """ Construit l'attribut groupes, il ne doit pas être vide."""
        self.groupes = []
        raise NotImplementedError

    def exporte(self, contenu, entree=True, xml=False, debug=False):
        """ Exporte l'entrée ou la sortie, dans un fichier XML ou JSON."""
        extension = 'xml' if xml else 'json'
        entree_ou_sortie = 'entree' if entree else 'sortie'
        nom_fichier = path.join('..', '..', 'donnees', f'{self.nom}_{entree_ou_sortie}.{extension}')
        if debug:
            print(f"On devrait sauvegarder le contenu suivant dans le fichier '{nom_fichier}'...")  # DEBUG
            print(contenu)  # DEBUG
            return False
        if path.exists(nom_fichier):
            print(f"Attention : le fichier de sortie '{nom_fichier}' existe déjà...")  # DEBUG
        with open(nom_fichier, "w") as fichier:
            print(f"\nContenu écrit dans le fichier {nom_fichier}...")  # DEBUG
            print(contenu)  # DEBUG
            fichier.write(contenu)
        return True

    def execute(self):
        """ Calcule les ordre d'appels et sauvegarde les fichiers."""
        # crée l'entrée
        entree = AlgoProposition(self.groupes)
        # calcule la sortie
        entree.calculeOrdresAppels()
        # et sauvegarde les deux, en XML ou en JSON

        entreeXML = entree.exporteEntree_XML()
        contenu = ET.tostring(entreeXML, encoding='unicode', method='xml')
        contenu = DOM.parseString(contenu).toprettyxml(indent=' '*4)
        contenu = contenu.replace('version="1.0" ', 'version="1.0" encoding="UTF-8" standalone="yes"')
        self.exporte(contenu, entree=True, xml=True)

        sortieXML = entree.exporteSortie_XML()
        contenu = ET.tostring(sortieXML, encoding='unicode', method='xml')
        contenu = DOM.parseString(contenu).toprettyxml(indent=' '*4)
        contenu = contenu.replace('version="1.0" ', 'version="1.0" encoding="UTF-8" standalone="yes"')
        self.exporte(contenu, entree=False, xml=True)

        # et maintenant le JSON
        entreeJSON = entree.exporteEntree_JSON()
        contenu = json.dumps(entreeJSON, sort_keys=True, indent=4)
        self.exporte(contenu, entree=True, xml=False)

        sortieJSON = entree.exporteSortie_JSON()
        contenu = json.dumps(sortieJSON, sort_keys=True, indent=4)
        self.exporte(contenu, entree=False, xml=False)


# Exemples


class exempleB1(Exemple):
    """ Exemple B1 avec 20% de boursiers et 0% de non-résidents."""

    def initialise(self):
        self.nom = 'exemple_B1'
        raise NotImplementedError


#: Liste de tous les exemples.
tous_les_exemples = [
    exempleB1
]
