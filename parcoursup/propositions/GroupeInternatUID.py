#!/usr/bin/env python3
# -*- coding: utf-8; mode: python -*-
""" GroupeInternatUID, pour https://github.com/Naereen/ParcourSup.py.

- Auteurs : Lilian Besson, Bastien Trotobas et al, (C) 2018.
- Adresse : https://github.com/Naereen/ParcourSup.py
- Licence : MIT License (http://lbesson.mit-license.org).
"""
__author__ = "Lilian Besson, Bastien Trotobas et al"
__version__ = "0.2.1"


class GroupeInternatUID(object):
    """ Classe comprenant les caractéristiques identifiant de manière unique un internat dans la base de données."""

    def __init__(self,
        C_GI_COD: int,
        G_TA_COD: int,
    ):
        assert C_GI_COD >= 0, f"Erreur : {self.__class__.__name__} le paramètre C_GI_COD doit être >= 0, et pas {C_GI_COD}..."  # DEBUG
        self.C_GI_COD = C_GI_COD  #: L'identifiant unique de l'internat dans la base de données
        assert G_TA_COD >= 0, f"Erreur : {self.__class__.__name__} le paramètre G_TA_COD doit être >= 0, et pas {G_TA_COD}..."  # DEBUG
        self.G_TA_COD = G_TA_COD  #: L'identifiant unique de la formation d'affectation dans la base de données. Positionné à 0 pour un internat commun à plusieurs formations.
        # FIXME le code java dit un fois à -1 une fois à 0 ?

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.C_GI_COD}, {self.G_TA_COD})"

    def __eq__(self, groupeinternatuid) -> bool:
        if isinstance(groupeinternatuid, self.__class__):
            return (self.C_GI_COD == groupeinternatuid.C_GI_COD) and (self.G_TA_COD == groupeinternatuid.G_TA_COD)
        else:
            raise RuntimeError(f"Test d'égalité imprévu, entre self = {self} et {groupeinternatuid} de classe {groupeinternatuid.__class__}.")

    def __hash__(self) -> int:
        """ FIXME il n'y a aucune chance qu'on obtienne les mêmes hashCode qu'en Java...

        - Je ne crois pas que ça posera problème, mais peut-être...
        """
        return hash(
            (self.C_GI_COD)
            ^ (self.G_TA_COD << 16)
        )
