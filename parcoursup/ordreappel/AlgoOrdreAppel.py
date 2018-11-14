#!/usr/bin/env python3
# -*- coding: utf-8; mode: python -*-
""" AlgoOrdreAppel, pour https://github.com/Naereen/ParcourSup.py.

- Auteurs : Lilian Besson, Bastien Trotobas et al, (C) 2018.
- Adresse : https://github.com/Naereen/ParcourSup.py
- Licence : MIT License (http://lbesson.mit-license.org).
"""
__author__ = "Lilian Besson, Bastien Trotobas et al"
__version__ = "0.2"

import xml.etree.ElementTree as ET
from pprint import pprint  # DEBUG
from typing import Dict, List

try:
    from GroupeClassement import GroupeClassement
    from VoeuClasse import typeCandidat_vers_str
except ImportError:
    from .GroupeClassement import GroupeClassement
    from .VoeuClasse import typeCandidat_vers_str


#: En mode débug, on affiche juste le résultat, on n'écrase pas les fichiers de tests.
# DEBUG = True
DEBUG = False


class AlgoOrdreAppel(object):
    """ Stocke les entrées et sorties de l'algorithme de calcul d'ordre d'appel. """

    def __init__(self, groupesClassements: List[GroupeClassement]):
        """ Stocke la liste non-vide de classements."""
        assert groupesClassements, f"Erreur : {self.__class__.__name__} le paramètre groupesClassements doit être non vide, et pas {groupesClassements}..."  # DEBUG
        liste_C_GP_COD = [ga.C_GP_COD for ga in groupesClassements]
        nombres_C_GP_COD = len(liste_C_GP_COD)
        nombres_differents_C_GP_COD = len(set(liste_C_GP_COD))
        assert nombres_C_GP_COD == nombres_differents_C_GP_COD, f"Erreur : {self.__class__.__name__} les différents groupesClassements doivent avoir un C_GP_COD tous différents (ici il y a en {nombres_C_GP_COD} mais seulement {nombres_differents_C_GP_COD} différents..."  # DEBUG
        self.groupesClassements = groupesClassements
        self.ordresAppel = dict()

    def calculeOrdresAppels(self) -> None:
        """ Calcule l'ordre d'appels de chaque groupes de classements."""
        for ga in self.groupesClassements:
            self.ordresAppel[ga.C_GP_COD] = ga.calculerOrdreAppel()

    # --- Exporte vers des arbres XML ou un dictionnaire JSON

    def exporteEntree_XML(self) -> ET.Element:
        """ Converti l'entrée en un arbre XML."""
        racine = ET.Element('algoOrdreAppelEntree')
        groupesXML = ET.Element('groupesClassements')
        for groupe in self.groupesClassements:
            ET.SubElement(groupesXML, 'C_GP_COD').text = str(groupe.C_GP_COD)
            ET.SubElement(groupesXML, 'tauxMinBoursiersPourcents').text = str(groupe.tauxMinBoursiersPourcents)
            ET.SubElement(groupesXML, 'tauxMinResidentsPourcents').text = str(groupe.tauxMinResidentsPourcents)
            for voeu in groupe.voeuxClasses:
                voeuXML = ET.Element('voeuxClasses')
                ET.SubElement(voeuXML, 'typeCandidat').text = typeCandidat_vers_str(voeu.typeCandidat)
                ET.SubElement(voeuXML, 'G_CN_COD').text = str(voeu.G_CN_COD)
                ET.SubElement(voeuXML, 'rang').text = str(voeu.rang)
                groupesXML.append(voeuXML)
        racine.append(groupesXML)
        return racine

    def exporteEntree_JSON(self) -> Dict:
        """ Converti l'entrée en un dictionnaire."""
        racine = {
            'algoOrdreAppelEntree': {
                'groupesClassements': [
                    {
                        'C_GP_COD': groupe.C_GP_COD,
                        'tauxMinBoursiersPourcents': groupe.tauxMinBoursiersPourcents,
                        'tauxMinResidentsPourcents': groupe.tauxMinResidentsPourcents,
                        'voeuxClasses': [
                            {
                                'typeCandidat': typeCandidat_vers_str(voeu.typeCandidat),
                                'G_CN_COD': voeu.G_CN_COD,
                                'rang': voeu.rang,
                            }
                            for voeu in groupe.voeuxClasses
                        ]
                    }
                    for groupe in self.groupesClassements
                ]
            }
        }
        if DEBUG: pprint(racine)  # DEBUG
        return racine

    def exporteSortie_XML(self) -> ET.Element:
        """ Converti les résultats de la sortie en un arbre XML."""
        racine = ET.Element('algoOrdreAppelSortie')
        ordresXML = ET.Element('ordresAppel')
        for numero, ordre in enumerate(self.ordresAppel.values()):
            ordreXML = ET.Element('entry')
            key = ET.Element('key')
            key.text = str(numero)
            ordreXML.append(key)
            value = ET.Element('value')
            for voeu in ordre:
                voeuXML = ET.Element('voeux')
                ET.SubElement(voeuXML, 'typeCandidat').text = typeCandidat_vers_str(voeu.typeCandidat)
                ET.SubElement(voeuXML, 'G_CN_COD').text = str(voeu.G_CN_COD)
                ET.SubElement(voeuXML, 'rang').text = str(voeu.rang)
                value.append(voeuXML)
            ordreXML.append(value)
            ordresXML.append(ordreXML)
        racine.append(ordresXML)
        return racine

    def exporteSortie_JSON(self) -> Dict:
        """ Converti les résultats de la sortie en un dictionnaire."""
        racine = {
            'algoOrdreAppelSortie': {
                'ordresAppel': [
                    {
                        'key': numero,
                        'voeux': [
                            {
                                'typeCandidat': typeCandidat_vers_str(voeu.typeCandidat),
                                'G_CN_COD': voeu.G_CN_COD,
                                'rang': voeu.rang,
                            }
                            for voeu in ordre
                        ]
                    }
                    for numero, ordre in enumerate(self.ordresAppel.values())
                ]
            }
        }
        if DEBUG: pprint(racine)  # DEBUG
        return racine
