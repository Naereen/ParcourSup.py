#!/usr/bin/env python3
# -*- coding: utf-8; mode: python -*-
""" AlgoOrdreAppelEntree, pour https://github.com/Naereen/ParcourSup.py.

- Auteurs: Lilian Besson, Bastien Trotobas and contributors, (C) 2018.
- Adresse: https://github.com/Naereen/ParcourSup.py
- Licence: MIT License (http://lbesson.mit-license.org).
"""
__author__ = "Lilian Besson, Bastien Trotobas and contributors"
__version__ = "0.0.1"

from lxml.etree import Element


class AlgoOrdreAppel(object):
    """ Stocke les entrées et sorties de l'algorithme de calcul d'ordre d'appel.
    """

    def __init__(self, groupesClassements):
        """ Stocke la liste non-vide de classements."""
        assert groupesClassements, f"Erreur : {self.__class__.__name__} le paramètre groupesClassements doit être non vide, et pas {groupesClassements}..."  # DEBUG
        liste_C_GP_COD = [ga.C_GP_COD for ga in groupesClassements]
        nombres_C_GP_COD = len(liste_C_GP_COD)
        nombres_differents_C_GP_COD = len(set(liste_C_GP_COD))
        assert nombres_C_GP_COD == nombres_differents_C_GP_COD, f"Erreur : {self.__class__.__name__} les différents groupesClassements doivent avoir un C_GP_COD tous différents (ici il y a en {nombres_C_GP_COD} mais seulement {nombres_differents_C_GP_COD} différents..."  # DEBUG
        self.groupesClassements = groupesClassements
        self.ordresAppel = dict()

    def calculeOrdresAppels(self):
        """ Calcule l'ordre d'appels de chaque groupes de classements."""
        for ga in self.groupesClassements:
            self.ordresAppel[ga.C_GP_COD] = ga.calculerOrdreAppel()

    # --- Exporte vers des arbres XML ou un dictionnaire JSON

    def exporteEntree_XML(self):
        """ Converti l'entrée en un arbre XML."""
        racine = Element('algoOrdreAppelEntree')
        groupesXML = Element('groupesClassements')
        for groupe in self.groupesClassements:
            groupesXML.append(Element('C_GP_COD', attrib={'text': groupe.C_GP_COD}))
            groupesXML.append(Element('tauxMinBoursiersPourcents', attrib={'text': groupe.tauxMinBoursiersPourcents}))
            groupesXML.append(Element('tauxMinResidentsPourcents', attrib={'text': groupe.tauxMinResidentsPourcents}))
            for voeu in groupe.voeuxClasses:
                voeuXML = Element('voeuxClasses')
                voeuXML.append(Element('typeCandidat', attrib={'text': voeu.typeCandidat}))
                voeuXML.append(Element('G_CN_COD', attrib={'text': voeu.G_CN_COD}))
                voeuXML.append(Element('rang', attrib={'text': voeu.rang}))
                groupesXML.append(voeuXML)
        racine.append(groupesXML)
        return racine

    def exporteEntree_JSON(self):
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
                                'typeCandidat': voeu.typeCandidat,
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
        return racine

    def exporteSortie_XML(self):
        """ Converti les résultats de la sortie en un arbre XML."""
        racine = Element('algoOrdreAppelSortie')
        ordresXML = Element('ordresAppel')
        for numOrdre, ordre in enumerate(self.ordresAppel):
            ordreXML = Element('entry')
            key = Element('key', attrib={'text': numOrdre})
            ordreXML.append(key)
            value = Element('value')
            for voeu in ordre.voeuxClasses:
                voeuXML = Element('voeux')
                voeuXML.append(Element('typeCandidat', attrib={'text': voeu.typeCandidat}))
                voeuXML.append(Element('G_CN_COD', attrib={'text': voeu.G_CN_COD}))
                voeuXML.append(Element('rang', attrib={'text': voeu.rang}))
                value.append(voeuXML)
            ordreXML.append(value)
            ordresXML.append(ordreXML)
        racine.append(ordresXML)
        return racine

    def exporteSortie_JSON(self):
        """ Converti les résultats de la sortie en un dictionnaire."""
        racine = {
            'algoOrdreAppelSortie': {
                'ordresAppel': {
                    'voeux': [
                        {
                            'typeCandidat': voeu.typeCandidat,
                            'G_CN_COD': voeu.G_CN_COD,
                            'rang': voeu.rang,
                        }
                        for voeu in groupe.voeuxClasses
                    ]
                    for groupe in self.groupesClassements
                }
            }
        }
        return racine
