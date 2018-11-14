#!/usr/bin/env python3
# -*- coding: utf-8; mode: python -*-
""" VoeuUID, pour https://github.com/Naereen/ParcourSup.py.

- Auteurs : Lilian Besson, Bastien Trotobas et al, (C) 2018.
- Adresse : https://github.com/Naereen/ParcourSup.py
- Licence : MIT License (http://lbesson.mit-license.org).
"""
__author__ = "Lilian Besson, Bastien Trotobas et al"
__version__ = "0.2.1"


class VoeuUID(object):
    """ Classe comprenant les caractéristiques identifiant de manière unique un vœu dans la base de données."""
    voeuxCrees = set()
    verificationUnicite = False

    def __init__(self,
        G_CN_COD: int,
        G_TA_COD: int,
        avecInternat: bool,
    ):
        self.G_CN_COD = G_CN_COD  #: L'identifiant unique du candidat dans la base de données
        assert G_TA_COD >= -1, f"Erreur : {self.__class__.__name__} le paramètre G_TA_COD doit être >= -1, et pas {G_TA_COD}..."  # DEBUG
        self.G_TA_COD = G_TA_COD  #: L'identifiant unique de la formation d'affectation dans la base de données. Positionné à -1 pour les internats commun à plusieurs formations
        self.I_RH_COD = avecInternat  #: tauxMinBoursiersPourcents

        # Vérification de l'unicité
        if self.verificationUnicite:
            if self in self.voeuxCrees:
                raise RuntimeError(f"Deux vœux créés avec le même id G_CN_COD = {self.G_CN_COD} et G_TA_COD = {self.G_TA_COD}...")
            self.voeuxCrees.add(self)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.G_CN_COD}, {self.G_TA_COD}, {self.I_RH_COD})"

    def __eq__(self, voeuuid) -> bool:
        if isinstance(voeuuid, self.__class__):
            return (self.G_CN_COD == voeuuid.G_CN_COD) and (self.G_TA_COD == voeuuid.G_TA_COD) and (self.I_RH_COD == voeuuid.I_RH_COD)
        else:
            raise RuntimeError(f"Test d'égalité imprévu, entre self = {self} et {voeuuid} de classe {voeuuid.__class__}.")

    def __hash__(self) -> int:
        """ FIXME il n'y a aucune chance qu'on obtienne les mêmes hashCode qu'en Java...

        - Je ne crois pas que ça posera problème, mais peut-être...
        """
        return hash(
            (1 if self.I_RH_COD else 0)
            ^ (self.G_CN_COD << 1)
            ^ (self.G_TA_COD << 32)
        )

    def debuterVerificationUnicite(self) -> None:
        """ Vérifie qu'un identifiant est créé au plus une fois."""
        self.verificationUnicite = True
        self.voeuxCrees.clear()
