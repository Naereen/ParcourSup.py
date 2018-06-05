#!/usr/bin/env python3
# -*- coding: utf-8; mode: python -*-
""" VoeuClasse, pour https://github.com/Naereen/ParcourSup.py.

- Auteurs: Lilian Besson, Bastien Trotobas and contributors, (C) 2018.
- Adresse: https://github.com/Naereen/ParcourSup.py
- Licence: MIT License (http://lbesson.mit-license.org).
"""
__author__ = "Lilian Besson, Bastien Trotobas and contributors"
__version__ = "0.0.1"

from enum import Enum


#: Les différents types de candidats
TypeCandidat = Enum('TypeCandidat', [
    'BoursierResident',
    'BoursierNonResident',
    'NonBoursierResident',
    'NonBoursierNonResident',
])


def typeCandidat_si_Boursier_etou_Resident(
        estBoursier: bool,
        estResident: bool
    ):
    """ Donne le type de candidat selon qu'il/elle soit boursier-e et/ou résident-e. """
    if estBoursier and estResident:
        return TypeCandidat.BoursierResident
    elif estBoursier and not estResident:
        return TypeCandidat.BoursierNonResident
    elif not estBoursier and estResident:
        return TypeCandidat.NonBoursierResident
    elif not estBoursier and not estResident:
        return TypeCandidat.NonBoursierNonResident
    raise ValueError(f"Impossible d'avoir ce cas là dans typeCandidat_si_Boursier_etou_Resident({estBoursier}, {estResident})")


class VoeuClasse(object):
    """ Classe représentant un vœu d'un candidat."""
    def __init__(self,
        G_CN_COD: int,
        rang: int,
        estBoursier: bool,
        estResident: bool,
    ):
        assert G_CN_COD > 0, f"Erreur : {self.__class__.__name__} le paramètre G_CN_COD doit être > 0, et pas {G_CN_COD}..."  # DEBUG
        self.G_CN_COD = G_CN_COD  #: G_CN_COD
        assert rang > 0, f"Erreur : {self.__class__.__name__} le paramètre rang doit être > 0, et pas {rang}..."  # DEBUG
        self.rang = rang  #: rang
        self.typeCandidat = typeCandidat_si_Boursier_etou_Resident(estBoursier, estResident)  #: typeCandidat

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.G_CN_COD}, {self.rang}, {self.estBoursier()}, {self.estResident()})"

    def estBoursier(self) -> bool:
        """ Pour savoir si le candidat est boursier-e."""
        return self.typeCandidat == TypeCandidat.BoursierResident or self.typeCandidat == TypeCandidat.BoursierNonResident

    def estResident(self) -> bool:
        """ Pour savoir si le candidat est résident-e."""
        return self.typeCandidat == TypeCandidat.BoursierResident or self.typeCandidat == TypeCandidat.NonBoursierResident

    def __lt__(self, voeu) -> bool:
        """ Comparateur permettant de trier les vœux par ordre du groupe de classement."""
        return self.rang - voeu.rang