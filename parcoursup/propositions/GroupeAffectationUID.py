#!/usr/bin/env python3
# -*- coding: utf-8; mode: python -*-
""" GroupeAffectationUID, pour https://github.com/Naereen/ParcourSup.py.

- Auteurs : Lilian Besson, Bastien Trotobas et al, (C) 2018.
- Adresse : https://github.com/Naereen/ParcourSup.py
- Licence : MIT License (http://lbesson.mit-license.org).
"""
__author__ = "Lilian Besson, Bastien Trotobas et al"
__version__ = "0.2.1"


class GroupeAffectationUID(object):
    """ Classe comprenant les caractéristiques identifiant de manière unique une affectation dans la base de données."""

    def __init__(self,
        C_GP_COD: int,
        G_TI_COD: int,
        G_TA_COD: int,
    ):
        assert C_GP_COD >= 0, f"Erreur : {self.__class__.__name__} le paramètre C_GP_COD doit être >= 0, et pas {C_GP_COD}..."  # DEBUG
        self.C_GP_COD = C_GP_COD  #: L'identifiant unique du groupe de classement pédagogique dans la base de données.
        assert G_TI_COD >= 0, f"Erreur : {self.__class__.__name__} le paramètre G_TI_COD doit être >= 0 et pas {G_TI_COD}..."  # DEBUG
        self.G_TI_COD = G_TI_COD  #: L'identifiant unique de la formation d'inscription dans la base de données.
        assert G_TA_COD >= 0, f"Erreur : {self.__class__.__name__} le paramètre G_TA_COD doit être >= 0 et pas {G_TA_COD}..."  # DEBUG
        self.G_TA_COD = G_TA_COD  #: L'identifiant unique de la formation d'affectation dans la base de données.

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.C_GP_COD}, {self.G_TI_COD}, {self.G_TA_COD})"

    def __eq__(self, groupeaffectationuid) -> bool:
        if isinstance(groupeaffectationuid, self.__class__):
            return (self.C_GP_COD == groupeaffectationuid.C_GP_COD) and (self.G_TI_COD == groupeaffectationuid.G_TI_COD) and (self.G_TA_COD == groupeaffectationuid.G_TA_COD)
        else:
            raise RuntimeError(f"Test d'égalité imprévu, entre self = {self} et {groupeaffectationuid} de classe {groupeaffectationuid.__class__}.")

    def __hash__(self) -> int:
        """ FIXME il n'y a aucune chance qu'on obtienne les mêmes hashCode qu'en Java...

        - Je ne crois pas que ça posera problème, mais peut-être...
        """
        return hash(
            (self.C_GP_COD)
            ^ (self.G_TI_COD << 10)
            ^ (self.G_TA_COD << 20)
        )
