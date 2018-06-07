#!/usr/bin/env python3
# -*- coding: utf-8; mode: python -*-
""" AlgoPropositions, pour https://github.com/Naereen/ParcourSup.py.

- Auteurs: Lilian Besson, Bastien Trotobas et al, (C) 2018.
- Adresse: https://github.com/Naereen/ParcourSup.py
- Licence: MIT License (http://lbesson.mit-license.org).
"""
__author__ = "Lilian Besson, Bastien Trotobas et al"
__version__ = "0.0.1"

import xml.etree.ElementTree as ET
# from pprint import pprint  # DEBUG
from typing import Dict, List, Set
from datetime import datetime

try:
    from tqdm import tqdm  # DEBUG Cf. https://github.com/tqdm/tqdm#usage
except ImportError:
    print("Attention : le module 'tqdm' n'a pas été trouvé, installez le avec :\nsudo pip3 install tqdm")
    def tqdm(iterator, desc=None):
        return iterator


from GroupeAffectation import GroupeAffectation
from GroupeAffectationUID import GroupeAffectationUID
from GroupeInternat import GroupeInternat
from GroupeInternatUID import GroupeInternatUID
from VerificationsResultats import verifierRespectOrdreAppelVoeuxSansInternat, verifierVoeuxAvecInternat, verifierRespectClassementInternat, verifierSurcapaciteEtRemplissage, verifierSurcapaciteEtRemplissage_avec_rangDernierAppeles, verifierMaximalitePositionsAdmission
from VoeuEnAttente import VoeuEnAttente
from VoeuUID import VoeuUID


def log(*args, **kwargs):
    """ Affiche avec une heure."""
    now = datetime.now()
    print(f"{now:%d-%m-%Y %H:%M:%S}", *args, **kwargs)


class AlgoPropositions(object):
    """ Stocke les entrées et sorties de l'algorithme de calcul d'ordre d'appel. """

    def __init__(self,
        groupesAffectations: List[GroupeAffectation]=[],
        internats: List[GroupeInternat]=[],
    ):
        """ Stocke la liste non-vide de classements."""
        assert groupesAffectations, f"Erreur : {self.__class__.__name__} le paramètre groupesAffectations doit être non vide, et pas {groupesAffectations}..."  # DEBUG
        #: La liste des groupes d'affectation, contenant leurs voeux respectifs.
        self.groupesAffectations: List[GroupeAffectation] = groupesAffectations

        assert internats, f"Erreur : {self.__class__.__name__} le paramètre internats doit être non vide, et pas {internats}..."  # DEBUG
        #: La liste des internats, contenant leurs voeux respectifs.
        self.internats: List[GroupeInternat] = internats
        #: Liste des internats, permettant de récupérer les positions max d'admission
        self.internats_sortie: List[GroupeInternat] = []

        self.groupesAMettreAJour: Set[GroupeInternat] = set()

        #: Liste des propositions à faire.
        self.propositions: List[VoeuEnAttente] = []

        #: Liste des voeux restant en attente.
        self.enAttentes: List[VoeuEnAttente] = []

        self.rangsMaxNouvelArrivant: Dict[GroupeAffectation, int] = dict()


    def verifierIntegrite(self) -> bool:
        """ Vérifie l'intégrité des données d'entrée, et lève une exception si nécessaire.

        Propriétés :

        - a) tous les vœux sont en attente,
        - b) pas deux vœux distincts avec la même id,
        - c) pas deux candidats distincts avec le même classement, formation et internat,
        - d) pas le même candidat avec deux classements distincts, formation et internat,
        - e) classements positifs,
        - f) chaque voeu avec internat se retrouve dans l'internat correspondant.

        .. warning:: Une exception ``AssertionError`` est lancée avec un message commençant par ``a)`` ou ... ou ``f)``.
        """
        # intégrité des classements : un classement == un candidat
        for groupeAffectation in tqdm(self.groupesAffectations, desc="groupesAffectations"):
            ordreVersCandidat: Dict[int, int] = dict()
            candidatVersOrdre: Dict[int, int] = dict()
            voeuxVus: Set[VoeuUID] = set()
            for voeu in tqdm(groupeAffectation.voeux, desc="voeux"):
                assert not (voeu.internatDejaObtenu() and voeu.formationDejaObtenue()), f"a) ce vœu {voeu} n'est pas en attente !"
                assert voeu.id not in voeuxVus, f"b) deux vœux avec le même identifiant {voeu.id} !"
                voeuxVus.add(voeu.id)

                if voeu.ordreAppel in ordreVersCandidat:
                    assert ordreVersCandidat[voeu.ordreAppel] == voeu.id.G_CN_COD, f"c) candidats distincts avec le même classement {voeu.id.G_CN_COD} et {ordreVersCandidat[voeu.ordreAppel]} !"
                else:
                    ordreVersCandidat[voeu.ordreAppel] = voeu.id.G_CN_COD
                if voeu.id.G_CN_COD in candidatVersOrdre:
                    assert candidatVersOrdre[voeu.id.G_CN_COD] == voeu.ordreAppel, f"d) candidats distincts avec le même classement { voeu.ordreAppel} et {candidatVersOrdre[voeu.id.G_CN_COD]} !"
                else:
                    candidatVersOrdre[voeu.id.G_CN_COD] = voeu.ordreAppel

                assert voeu.ordreAppel > 0, f"e) ordre appel de la formation est négatif = {voeu.ordreAppel} !"

                # remarque le voeu peut-être marqué "avecInternat"
                # et en même temps internat==None car c'est un internat sans classement
                # (obligatoire ou non-sélectif)
                if voeu.avecClassementInternat():
                    assert voeu in voeu.internat.voeux, f"f) erreur intégrité données ! Le vœu {voeu} n'est pas dans les vœux de son internat {voeu.internat.voeux} !"

        # intégrité des classements : un classement == un candidat
        for internat in tqdm(self.internats, "internats"):
            ordreVersCandidat: Dict[int, int] = dict()
            candidatVersOrdre: Dict[int, int] = dict()
            for voeu in tqdm(internat.voeux, "voeux"):
                assert voeu.avecInternat(), f"g) erreur intégrité données ! Le voeu {voeu} est dans les vœux de l'internat {internat} mais n'est pas un vœu avec internat !"
                assert voeu.internat == internat, f"h) erreur intégrité données ! Le voeu {voeu} est dans les vœux de l'internat {internat} mais n'est pas un vœu de cet internat !"
                assert voeu.rangInternat > 0, f"e) classement internat négatif !"

                if voeu.rangInternat in ordreVersCandidat:
                    assert ordreVersCandidat[voeu.rangInternat] == voeu.id.G_CN_COD, f"c) candidats distincts avec le même classement, {voeu.id.G_CN_COD} et {ordreVersCandidat[voeu.rangInternat]} !"
                else:
                    ordreVersCandidat[voeu.rangInternat] = voeu.id.G_CN_COD
                if voeu.id.G_CN_COD in candidatVersOrdre:
                    assert candidatVersOrdre[voeu.id.G_CN_COD] == voeu.rangInternat, f"d) candidats distincts avec le même classement {voeu.rangInternat} et {candidatVersOrdre[voeu.id.G_CN_COD]} !"
                else:
                    candidatVersOrdre[voeu.id.G_CN_COD] = voeu.rangInternat

    def calculePropositions(self) -> None:
        """ Calcule les propositions à envoyer."""
        self.verifierIntegrite()
        log("Début calcul propositions...")

        # groupes à mettre à jour
        self.groupesAMettreAJour.update(self.groupesAffectations)

        # initialisation des positions maximales d'admission dans les internats
        for internat in self.internats:
            internat.initialiserPositionAdmission()

        compteurBoucle = 0
        while self.groupesAMettreAJour:
            # calcul des propositions à effectuer,
            # étant données les positions actuelles d'admissions aux internats
            for groupe in self.groupesAMettreAJour:
                groupe.mettreAJourPropositions()

            # Test de surcapacité des internats, avec
            # mise à jour de la position d'admission si nécessaire.
            #
            # Baisser la position d'admission d'un internat ne diminue
            # pas le nombre de candidats dans les autres internats, voire augmente ces nombres,
            # car les formations devront potentiellement descendre plus bas dans l'ordre d'appel.
            #
            # Par conséquent, on peut mettre à jour toutes les positions d'admission
            # de tous les internats sans mettre à jour systématiquement les propositions:
            # si un internat est détecté en surcapacité avant la mise
            # à jour des propositions, il l'aurait été également après la mise à jour des propositions.
            # (Mais la réciproque est fausse en général).
            #
            # De cette manière, on reste bien dans l'ensemble E des vecteurs de positions
            # d'admission supérieurs sur chaque composante au vecteur de positions d'admission
            # le plus permissif possible parmi tous ceux respectant les contraintes
            # de capacité des internats et situés en deçà des positions maximales d'admission.
            #
            # Ce vecteur est égal, sur chaque composante, à la valeur minimum de cette
            # composante parmi les éléments de E.
            #
            # La boucle termine quand les contraintes de capacité des internats
            # sont satisfaites, c'est-à-dire quand ce minimum global est atteint.
            #
            # Une propriété de symétrie i.e. d'équité intéressante : le résultat
            # ne dépend pas de l'ordre dans lequel on itère sur les internats et les formations.
            self.groupesAMettreAJour.clear()

            for internat in self.internats:
                maj = internat.mettreAJourPositionAdmission()
                if maj:
                    self.groupesAMettreAJour.update(internat.groupesConcernes)
            compteurBoucle += 1

        log(f"Calcul terminé après {compteurBoucle} itération{'(s)' if compteurBoucle > 1 else ''}.")

        log(f"Vérification des propriétés attendues des propositions pour un des {len(self.groupesAffectations)} groupes d'affectation.")
        for groupe in tqdm(self.groupesAffectations, desc="groupesAffectations"):
            verifierRespectOrdreAppelVoeuxSansInternat(groupe)
            verifierVoeuxAvecInternat(groupe)
            verifierSurcapaciteEtRemplissage(groupe)
        log("Vérifications ok (1/2)...")

        # précalcul des rangs d'appel maximum dans chaque groupe parmi les nouveaux entrants
        for groupe in tqdm(self.groupesAffectations, desc="groupesAffectations"):
            rangMax = 0
            for voeu in groupe.voeuxTries():
                if voeu.estAProposer() and not voeu.formationDejaObtenue():
                    rangMax = max(rangMax, voeu.ordreAppel)
            self.rangsMaxNouvelArrivant[groupe] = rangMax

        log(f"Vérification des propriétés attendues des propositions d'un des {len(self.internats)} internats.")
        for internat in tqdm(self.internats, desc="internats"):
            verifierRespectClassementInternat(internat)
            verifierSurcapaciteEtRemplissage_avec_rangDernierAppeles(internat, self.rangsMaxNouvelArrivant)
        log("Vérifications ok (2/2)...")

        log("\n\nPréparation données de sortie...")

        for groupeAffectation in tqdm(self.groupesAffectations, desc="groupesAffectations"):
            for voeu in groupeAffectation.voeux:
                if voeu.estAProposer():
                    self.propositions.append(voeu)
                else:
                    self.enAttentes.append(voeu)

        self.internats_sortie.extend(self.internats)

    # --- Exporte vers des arbres XML ou un dictionnaire JSON

    def exporteEntree_XML(self) -> ET.Element:
        """ Converti l'entrée en un arbre XML."""
        raise NotImplementedError
        racine = ET.Element('algoPropositionsEntree')
        groupesXML = ET.Element('groupesAffectations')
        for groupe in self.groupesAffectations:
            ET.SubElement(groupesXML, 'C_GP_COD').text = str(groupe.C_GP_COD)
            ET.SubElement(groupesXML, 'tauxMinBoursiersPourcents').text = str(groupe.tauxMinBoursiersPourcents)
            ET.SubElement(groupesXML, 'tauxMinResidentsPourcents').text = str(groupe.tauxMinResidentsPourcents)
            for voeu in groupe.voeuxClasses:
                voeuXML = ET.Element('voeuxClasses')
                ET.SubElement(voeuXML, 'typeCandidat').text = str(voeu.typeCandidat)
                ET.SubElement(voeuXML, 'G_CN_COD').text = str(voeu.G_CN_COD)
                ET.SubElement(voeuXML, 'rang').text = str(voeu.rang)
                groupesXML.append(voeuXML)
        racine.append(groupesXML)
        return racine

    def exporteEntree_JSON(self) -> Dict:
        """ Converti l'entrée en un dictionnaire."""
        racine = {
            'algoPropositionsEntree': {
                'groupesAffectations': [
                    {
                        'id': {
                            'C_GP_COD': groupe.id.C_GP_COD,
                            'G_TI_COD': groupe.id.G_TI_COD,
                            'G_TA_COD': groupe.id.G_TA_COD,
                        },
                        'nbPlacesVacantes': groupe.nbPlacesVacantes(),
                        'rangLimite': groupe.rangLimite,
                        'rangDernierAppele': self.rangsMaxNouvelArrivant.get(groupe, -1),
                        # FIXME pourquoi -1 ? Faut-il sauver l'entrée APRES avoir lancer execute ?
                        'voeux': [
                            {
                                'id': {
                                    'G_CN_COD': voeu.id.G_CN_COD,
                                    'G_TA_COD': voeu.id.G_TA_COD,
                                    'I_RH_COD': voeu.id.I_RH_COD,
                                },
                                'ordreAppel': voeu.ordreAppel,
                                'rangInternat': voeu.rangInternat,
                                'rangListeAttente': voeu.rangListeAttente,
                            }
                            for voeu in groupe.voeux
                        ]
                    }
                    for groupe in self.groupesAffectations
                ],
                'internats': [
                    {
                        'id': {
                            'C_GI_COD': internat.id.C_GI_COD,
                            'G_TA_COD': internat.id.G_TA_COD,
                        },
                        'contingentAdmission': internat.contingentAdmission,
                        'positionAdmission': internat.positionAdmission,
                        'positionMaximaleAdmission': internat.positionMaximaleAdmission,
                        'voeux': [
                            {
                                'id': {
                                    'G_CN_COD': voeu.id.G_CN_COD,
                                    'G_TA_COD': voeu.id.G_TA_COD,
                                    'I_RH_COD': voeu.id.I_RH_COD,
                                },
                                'ordreAppel': voeu.ordreAppel,
                                'rangInternat': voeu.rangInternat,
                                'rangListeAttente': voeu.rangListeAttente,
                            }
                            for voeu in internat.voeux
                        ],
                        'candidatsEnAttente': [
                            voeu.id.G_CN_COD
                            for voeu in internat.voeux
                        ]
                    }
                    for internat in self.internats
                ],
            }
        }
        # pprint(racine)  # DEBUG
        return racine

    def exporteSortie_XML(self) -> ET.Element:
        """ Converti les résultats de la sortie en un arbre XML."""
        raise NotImplementedError
        racine = ET.Element('algoPropositionsSortie')
        ordresXML = ET.Element('ordresAppel')
        for numero, ordre in enumerate(self.ordresAppel.values()):
            ordreXML = ET.Element('entry')
            key = ET.Element('key')
            key.text = str(numero)
            ordreXML.append(key)
            value = ET.Element('value')
            for voeu in ordre:
                voeuXML = ET.Element('voeux')
                ET.SubElement(voeuXML, 'typeCandidat').text = str(voeu.typeCandidat)
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
            'algoPropositionsSortie': {
                'propositions': [
                    {
                        'id': {
                            'G_CN_COD': proposition.id.G_CN_COD,
                            'G_TA_COD': proposition.id.G_TA_COD,
                            'I_RH_COD': proposition.id.I_RH_COD,
                        },
                        'ordreAppel': proposition.ordreAppel,
                        'rangInternat': proposition.rangInternat,
                        'rangListeAttente': proposition.rangListeAttente,
                    }
                    for proposition in self.propositions
                ],
                'enAttentes': [
                    {
                        'id': {
                            'G_CN_COD': enAttente.id.G_CN_COD,
                            'G_TA_COD': enAttente.id.G_TA_COD,
                            'I_RH_COD': enAttente.id.I_RH_COD,
                        },
                        'ordreAppel': enAttente.ordreAppel,
                        'rangInternat': enAttente.rangInternat,
                        'rangListeAttente': enAttente.rangListeAttente,
                    }
                    for enAttente in self.enAttentes
                ],
                'internats': [
                    {
                        'id': {
                            'C_GI_COD': internat.id.C_GI_COD,
                            'G_TA_COD': internat.id.G_TA_COD,
                        },
                        'contingentAdmission': internat.contingentAdmission,
                        'positionAdmission': internat.positionAdmission,
                        'positionMaximaleAdmission': internat.positionMaximaleAdmission,
                        'voeux': [
                            {
                                'id': {
                                    'G_CN_COD': voeu.id.G_CN_COD,
                                    'G_TA_COD': voeu.id.G_TA_COD,
                                    'I_RH_COD': voeu.id.I_RH_COD,
                                },
                                'ordreAppel': voeu.ordreAppel,
                                'rangInternat': voeu.rangInternat,
                                'rangListeAttente': voeu.rangListeAttente,
                            }
                            for voeu in internat.voeux
                        ],
                        'candidatsEnAttente': [
                            voeu.id.G_CN_COD
                            for voeu in internat.voeux
                        ]
                    }
                    for internat in self.internats
                ],
            }
        }
        # pprint(racine)  # DEBUG
        return racine
