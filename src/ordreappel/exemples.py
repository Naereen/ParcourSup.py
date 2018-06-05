#!/usr/bin/env python3
# -*- coding: utf-8; mode: python -*-
""" ordreappel.exemples, pour https://github.com/Naereen/ParcourSup.py.

- Auteurs: Lilian Besson, Bastien Trotobas and contributors, (C) 2018.
- Adresse: https://github.com/Naereen/ParcourSup.py
- Licence: MIT License (http://lbesson.mit-license.org).
"""
__author__ = "Lilian Besson, Bastien Trotobas and contributors"
__version__ = "0.0.1"

from os import path

from VoeuClasse import VoeuClasse
from GroupeClassement import GroupeClassement
import AlgoOrdreAppelEntree
import AlgoOrdreAppelSortie

# Classe d'un exemple

class Exemple(object):
    """ Un exemple."""
    # tous_les_exemples = []  # XXX Est-ce nécessaire ?

    def __init__(self):
        # tous_les_exemples.append(self)  # XXX Est-ce nécessaire ?
        self.nom = self.__name__.replace('exemple', 'exemple_')  #: Nom du fichier .xml de test.
        self.initialise()
        assert hasattr(self, groupe), f"Erreur : cet exemple {self} devrait avoir un attribut groupe. La méthode initialise() doit être mal implémentée."  # DEBUG

    def initialise(self):
        pass

    def to_string(self):
        return ""

    def exporte(self, ordre, xml=False):
        extension = 'xml' if xml else 'json'
        nom_fichier = path.join(['..', '..', 'donnees', self.nom + '.' + extension])
        if path.exists(nom_fichier):
            print(f"Attention : le fichier de sortie '{nom_fichier}' existe déjà...")  # DEBUG

        contenu = self.to_string()
        with open(nom_fichier, "w") as fichier:
            fichier.write(contenu)

    def execute(self, xml=False):
        liste_groupes = [self.groupe]
        entree = AlgoOrdreAppelEntree(liste_groupes)
        sortie = AlgoOrdreAppelSortie(entree)
        # ordre = self.groupe.calculerOrdreAppel()
        # self.exporte(ordre, xml=xml)
        return ordre


# Exemples


class exempleA1(Exemple):
    """ Exemple A1 avec 20% de boursiers et 0% de non-résidents."""

    def initialise(self):
        groupe = GroupeClassement(0, 20, 0)
        # C1 C2 C3 C4 C5 B6 B7 C8
        for i in range(1, 5 + 1):
            groupe.ajouterVoeu(VoeuClasse(i, i, False, False))
        groupe.ajouterVoeu(VoeuClasse(6, 6, True, False))
        groupe.ajouterVoeu(VoeuClasse(7, 7, True, False))
        groupe.ajouterVoeu(VoeuClasse(8, 8, False, False))
        self.groupe = groupe  #: GroupeClassement de cet exemple.


class exempleA2(Exemple):
    """ Exemple A2 avec 2% de boursiers et 0% de non-résidents."""

    def initialise(self):
        groupe = GroupeClassement(0, 2, 0)
        # C1 C2 C3 C4 C5 B6 C7 C8
        for i in range(1, 5 + 1):
            groupe.ajouterVoeu(VoeuClasse(i, i, False, False))
        groupe.ajouterVoeu(VoeuClasse(6, 6, True, False))
        groupe.ajouterVoeu(VoeuClasse(7, 7, False, False))
        groupe.ajouterVoeu(VoeuClasse(8, 8, False, False))
        self.groupe = groupe  #: GroupeClassement de cet exemple.


class exempleA3(Exemple):
    """ Exemple A3 avec 10% de boursiers et 0% de non-résidents."""

    def initialise(self):
        groupe = GroupeClassement(0, 10, 0)
        # C1 C2 C3 ...C900 B901 B902 B903 ...B1000
        for i in range(1, 900 + 1):
            groupe.ajouterVoeu(VoeuClasse(i, i, False, False))
        for i in range(901, 1000 + 1):
            groupe.ajouterVoeu(VoeuClasse(i, i, True, False))
        self.groupe = groupe  #: GroupeClassement de cet exemple.


class exempleA4(Exemple):
    """ Exemple A4 avec 10% de boursiers et 0% de non-résidents."""

    def initialise(self):
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
        self.groupe = groupe  #: GroupeClassement de cet exemple.


class exempleA5(Exemple):
    """ Exemple A5 avec 10% de boursiers et 95% de non-résidents."""

    def initialise(self):
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
            for j in range(3, 19 + 1)
                groupe.ajouterVoeu(VoeuClasse(20 * i + j, 20 * i + j, False, True))
            groupe.ajouterVoeu(VoeuClasse(20 * i + 20, 20 * i + 20, False, False))

        groupe.ajouterVoeu(VoeuClasse(41, 41, True, True))
        for k in range(42, 50 + 1):
            groupe.ajouterVoeu(VoeuClasse(k, k, False, True))

        for l in range(51, 91 + 1, 10):
            groupe.ajouterVoeu(VoeuClasse(l, l, True, False))
            for m in range(l + 1, l + 9 + 1):
                groupe.ajouterVoeu(VoeuClasse(m, m, False, True))
        self.groupe = groupe  #: GroupeClassement de cet exemple.


class exempleA6(Exemple):
    """ Exemple A6 avec 10% de boursiers et 95% de non-résidents."""

    def initialise(self):
        groupe = GroupeClassement(0, 10, 95)
        # R1 ... R100
        for i in range(1, 100 + 1):
            groupe.ajouterVoeu(new VoeuClasse(i, i, False, True))
        # B101 ... B111
        for i in range(101, 110 + 1):
            groupe.ajouterVoeu(new VoeuClasse(i, i, True, False))
        self.groupe = groupe  #: GroupeClassement de cet exemple.


#: Liste de tous les exemples.
tous_les_exemples = [value for name, value in globals() if name.startswith('exemple')]
