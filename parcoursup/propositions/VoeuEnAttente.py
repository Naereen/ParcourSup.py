#!/usr/bin/env python3
# -*- coding: utf-8; mode: python -*-
""" VoeuEnAttente, pour https://github.com/Naereen/ParcourSup.py.

- Auteurs : Lilian Besson, Bastien Trotobas et al, (C) 2018.
- Adresse : https://github.com/Naereen/ParcourSup.py
- Licence : MIT License (http://lbesson.mit-license.org).
"""
__author__ = "Lilian Besson, Bastien Trotobas et al"
__version__ = "0.2"

from typing import Union
try:
    from .VoeuUID import VoeuUID
except ImportError:
    from VoeuUID import VoeuUID


class VoeuEnAttente(object):
    """ Classe comprenant les caractéristiques identifiant de manière unique un vœu dans la base de données."""
    voeuxCrees = set()
    verificationUnicite = False

    def __init__(self,
        uid: VoeuUID,
        groupe,
        internat=None,
        rangInternat: int=0,
        ordreAppel: int=0,
    ):
        self.id = uid  #: Caractéristiques identifiant de manière unique le voeu dans la base de données
        self.groupe = groupe  #: Groupe d'affectation du voeu
        self.ordreAppel = ordreAppel  #: Rang du voeu dans l'ordre d'appel

        # autre attributs
        self.internat = internat   #: le groupe de classement internat, qui donne accès à la position d'admission
        self.rangInternat = rangInternat  #: Le rang du candidat au classement internat
        self._aProposer = False  # Résultat du calcul : fait-on une proposition sur ce voeu ?
        # FIXME ces deux quantités ne sont pas utilisées ?
        self.rangListeAttente = 0  #: Rang sur liste attente
        self.rangListeAttenteInternat = 0  #: Rang sur liste attente internat

    @property
    def G_CN_COD(self):
        return self.id.G_CN_COD

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.id}, {self.groupe}, {self.avecInternat()}, {self.internat}, {self.rangInternat})"

    @staticmethod
    def ajouterVoeu(
        G_CN_COD: int,
        groupe,
        ordreAppel: int,
        internat=None,
        rangInternat: int=0,
        avecInternat: bool=False,
    ):
        avecInternat = (internat is not None) or avecInternat
        voeuuid = VoeuUID(G_CN_COD, groupe.id.G_TA_COD, avecInternat)
        voeu = VoeuEnAttente(voeuuid, groupe, internat=internat, rangInternat=rangInternat, ordreAppel=ordreAppel)
        groupe.ajouterVoeu(voeu)
        if internat is not None:
            internat.ajouterVoeu(voeu, groupe)
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
