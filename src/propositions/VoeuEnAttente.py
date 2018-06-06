#!/usr/bin/env python3
# -*- coding: utf-8; mode: python -*-
""" VoeuEnAttente, pour https://github.com/Naereen/ParcourSup.py.

- Auteurs: Lilian Besson, Bastien Trotobas et al, (C) 2018.
- Adresse: https://github.com/Naereen/ParcourSup.py
- Licence: MIT License (http://lbesson.mit-license.org).
"""
__author__ = "Lilian Besson, Bastien Trotobas et al"
__version__ = "0.0.1"

from typing import Union
from VoeuUID import VoeuUID
from GroupeAffectation import GroupeAffectation
from GroupeInternat import GroupeInternat
from GroupeInternatUID import GroupeInternatUID


class VoeuEnAttente(object):
    """ Classe comprenant les caractéristiques identifiant de manière unique un vœu dans la base de données."""
    voeuxCrees = set()
    verificationUnicite = False

    def __init__(self,
        uid: VoeuUID,
        groupe: GroupeAffectation,
        avecInternat: bool,
        internat: Union[None, GroupeAffectation]=None,
        rangInternat: int=0,
    ):
        self.id = uid  #: Caractéristiques identifiant de manière unique le voeu dans la base de données
        self.groupe = groupe  #: Groupe d'affectation du voeu
        self.ordreAppel = 0  #: Rang du voeu dans l'ordre d'appel

        # autre attributs
        self.rangInternat = rangInternat  #: Le rang du candidat au classement internat
        self.internat = internat   #: le groupe de classement internat, qui donne accès à la position d'admission
        self._aProposer = False  # Résultat du calcul: fait-on une proposition sur ce voeu?
        self.rangListeAttente = 0  #: Rang sur liste attente
        self.rangListeAttenteInternat = 0  #: Rang sur liste attente internat

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.id}, {self.G_TA_COD}, {self.I_RH_COD})"

    @staticmethod
    def ajouterVoeu(
        G_CN_COD: int,
        avecInternat: bool,
        groupe: GroupeAffectation,
        ordreAppel: int,
        internat: Union[None, GroupeAffectation]=None,
        rangInternat: int=0,
    ):
        voeuuid = VoeuUID(G_CN_COD, groupe.id.G_TA_COD, avecInternat)
        voeu = VoeuEnAttente(VoeuUID, groupe, internat=internat, rangInternat=rangInternat)
        groupe.ajouterVoeu(voeu)
        internat.ajouterVoeu(voeu)
        return voeu

    def avecInternat(self) -> bool:
        """ Y a-t-il une demande d'internat sur ce voeu ?"""
        return self.id.I_RH_COD

    def avecClassementInternat(self) -> bool:
        """ Y a-t-il une demande d'internat avec classement sur ce voeux ?"""
        return self.internat is not None

    def internatDejaObtenu(self) -> bool:
        """ Le-la candidat-a a-t-il/elle déjà une offre dans cet internat (pour une autre formation)"""
        return self.internat is not None and self.internat.estAffecte(self.id.G_CN_COD)

    def formationDejaObtenue(self) -> bool:
        """ Le-la candidat-a a-t-il/elle déjà une offre dans cette formation (sans internat)"""
        return self.groupe is not None and self.groupe.estAffecte(self.id.G_CN_COD)

    def internatID(self) -> Union[None, int]:
        """ Identifiant de l'internat obtenu, None sinon."""
        return self.internat.id if self.internat is not None else None

    def estAProposer(self) -> bool:
        """ Méthode triviale, pour accéder au résultat du calcul : fait-on une proposition sur ce vœu ?"""
        return self._aProposer

    def proposer(self) -> None:
        """ Méthode triviale, pour accéder au résultat du calcul : fait-on une proposition sur ce vœu ?"""
        self._aProposer = True

    def conserverEnAttente(self) -> None:
        """ Méthode triviale, pour accéder au résultat du calcul : fait-on une proposition sur ce vœu ?"""
        self._aProposer = False

    def estDesactiveParPositionAdmissionInternat(self) -> bool:
        """ Vérifie si le voeu est désactivé du fait d'une demande d'internat"""
        return (self.internat is not None) and not self.internatDejaObtenu() and self.rangInternat > self.internat.positionAdmission
