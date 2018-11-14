#!/usr/bin/env python3
# -*- coding: utf-8; mode: python -*-
""" GroupeInternat, pour https://github.com/Naereen/ParcourSup.py.

- Auteurs : Lilian Besson, Bastien Trotobas et al, (C) 2018.
- Adresse : https://github.com/Naereen/ParcourSup.py
- Licence : MIT License (http://lbesson.mit-license.org).
"""
__author__ = "Lilian Besson, Bastien Trotobas et al"
__version__ = "0.2.1"

from typing import Set, List


try:
    from .VoeuEnAttente import VoeuEnAttente
    from .GroupeAffectation import GroupeAffectation
    from .GroupeInternatUID import GroupeInternatUID
except ImportError:
    from VoeuEnAttente import VoeuEnAttente
    from GroupeAffectation import GroupeAffectation
    from GroupeInternatUID import GroupeInternatUID


class GroupeInternat(object):
    """ Classe comprenant les caractéristiques identifiant de manière unique un internat dans la base de données."""

    nbJoursCampagne: int = 1  #: Le nombre de jours depuis l'ouverture de la campagne, 1 le premier jour.

    def __init__(self,
        uid: GroupeInternatUID,
        capacite: int,
        pourcentageOuverture: int,
    ):
        assert isinstance(uid, GroupeInternatUID), f"Erreur : {self.__class__.__name__} le paramètre uid doit être instance de GroupeInternatUID, et pas {uid} instance de {type(uid)}..."  # DEBUG
        self.id = uid  #: L'identifiant unique de l'internat dans la base de données

        assert capacite > 0, f"Erreur : {self.__class__.__name__} le paramètre capacite doit être > 0, et pas {capacite}..."  # DEBUG
        self.capacite = capacite  #: Le nombre total de places
        assert 0 <= pourcentageOuverture <= 100, f"Erreur : {self.__class__.__name__} le paramètre pourcentageOuverture doit être 0 <= ... <= 100, et pas {pourcentageOuverture}..."  # DEBUG
        self.pourcentageOuverture = pourcentageOuverture  #: Le pourcentage d'ouverture fixé par le chef d'établissement

        # autres attributs
        self.contingentAdmission = 0  #: Le nombre de demandes d'internat considérées Bmax dans le document de spécification
        self.positionAdmission = 0  #: La position d'admission dans cet internat, calculée par l'algorithme
        self.positionMaximaleAdmission = 0  #: La position maximale d'admission dans cet internat, calculée par l'algorithme
        self.groupesConcernes: Set[GroupeAffectation] = set()  #: La liste des groupes de classement concernés par cet internat

        self.voeux: List[VoeuEnAttente] = []  #: La liste des voeux du groupe. Après le calcul de la position initiale d'admission cette liste est triée par ordre de classement internat
        #: ``True`` si et seulement si la position maximale d'admission a été calculée,
        #: ce qui implique que la liste des voeux est triée par ordre de classement internat.
        self.estInitialise = False

        #: Ensemble des candidats affectés.
        self.candidatsAffectes: Set[int] = set()
        #: Ensemble des candidats en attente.
        self.candidatsEnAttente: Set[int] = set()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.id}, {self.capacite}, {self.pourcentageOuverture}, {self.contingentAdmission}, {self.positionAdmission}, {self.positionMaximaleAdmission}, {self.groupesConcernes}, {len(self.voeux)} voeux)"

    def nbPlacesVacantes(self) -> int:
        """ Le nombre de places vacantes dans cet internat."""
        # On utilise un seuil à 0,
        # en cas de réduction du nombre de lits conduisant à une différence négative
        return max(0, self.capacite - len(self.candidatsAffectes))

    def ajouterVoeu(self, voeu: VoeuEnAttente, groupe: GroupeAffectation) -> None:
        """ Ajouter ce vœu à ce groupe d'affectation."""
        assert voeu.avecInternat(), f"Erreur : le vœu {voeu} n'est pas avec internat mais vient de demander à être ajouté dans le groupe d'affectation d'internation {groupe}."
        if self.estInitialise:
            raise RuntimeError(f"Groupe déja initialisé.")
        self.voeux.append(voeu)
        self.groupesConcernes.add(groupe)
        if voeu.id.G_CN_COD not in self.candidatsAffectes:
            self.candidatsEnAttente.add(voeu.id.G_CN_COD)

    def ajouterCandidatAffecte(self, G_CN_CODE: int) -> None:
        """ Ajoute un candidat affecté.

        - Supprime le candidat de la liste des candidats en attente , si il y a lieu."""
        self.candidatsAffectes.add(G_CN_CODE)
        if G_CN_CODE in self.candidatsEnAttente:
            self.candidatsEnAttente.remove(G_CN_CODE)

    def estAffecte(self, G_CN_CODE: int) -> bool:
        """ Vérifie si le candidat est affecté."""
        return G_CN_CODE in self.candidatsAffectes

    def calculeAssietteAdmission(self, M: int, L: int, t: int, p: int) -> int:
        """ Calcule l'assiette d'admission Bmax comme décrit dans l'algorithme."""
        assietteAdmission = -1

        if M <= L:
            assietteAdmission = M
        elif t == 1:
            # le premier jour on s'en tient aux lits disponibles
            assietteAdmission = L
        elif t <= 30:
            # les 30 jours suivants, on élargit progressivement
            # l'assiette, en tenant compte de la correction du proviseur
            assietteAdmission = int(L + (M - L) * (t - 1) * p / 100 / 30)
        elif t < 60:
            # les 29 jours suivants, l'assiette est maximale,
            # possiblement réduite par la correction du proviseur
            assietteAdmission = int(L + (M - L) * p / 100)
        else:
            # finalement, l'assiette est maximale
            assietteAdmission = M

        self.contingentAdmission = max(0, assietteAdmission - len(self.candidatsAffectes))
        return assietteAdmission

    def initialiserPositionAdmission(self) -> None:
        """ Initialise la position d'admission à son maximum Bmax dans le document de référence."""
        # on calcule le nombre de candidats éligibles à une admission
        # dans l'internat aujourd'hui, stocké dans la variable assietteAdmission.
        # On colle aux notations du document de référence (pour les lettres M, L, t, p etc)
        M = len(self.candidatsEnAttente) + len(self.candidatsAffectes)
        L = self.capacite
        t = self.nbJoursCampagne
        p = self.pourcentageOuverture

        assietteAdmission = self.calculeAssietteAdmission(M, L, t, p)

        if t <= 0 or t > 120 or p < 0 or p > 100 or L < 0 or assietteAdmission > M or self.contingentAdmission > len(self.candidatsEnAttente) or self.contingentAdmission < 0:
            raise RuntimeError("Problème de calcul du contingent d'admission, veuillez vérifier les données.")

        if self.contingentAdmission == 0:
            self.positionMaximaleAdmission = 0
        else:
            # tri des voeux par ordre de classement à l'internat
            self.voeux.sort(key=lambda voeu: voeu.rangInternat)

            # on itère les candidats en attente d'internat jusqu'à arriver
            # au contingent calculé. Remarque: il peut y avoir plusieurs voeux pour
            # le même candidat, et les voeux sont triés par rang internat,
            # donc les voeux d'un même candidat sont consécutifs
            compteurCandidat = 0
            dernierRangComptabilise = 0

            for voeu in self.voeux:
                # sortie de boucle: le contingent est atteint
                if compteurCandidat == self.contingentAdmission:
                    break

                # deux cas où le voeu ne change pas la valeur du dernier rang comptabilisé
                # et du nombre de candidat comptés dans le contingent.
                # Premier cas: on a vu le même candidat au passage précédent dans la boucle
                if voeu.rangInternat == dernierRangComptabilise:
                    continue

                # Second cas: l'internat est déjà obtenu par le candidat
                if voeu.internatDejaObtenu():
                    continue

                # Dans les cas restants, on met à jour.
                dernierRangComptabilise = voeu.rangInternat
                compteurCandidat += 1

            self.positionMaximaleAdmission = dernierRangComptabilise

        self.positionAdmission = self.positionMaximaleAdmission
        self.estInitialise = True

    def mettreAJourPositionAdmission(self) -> bool:
        """ Met à jour la position d'admission si nécessaire.

        - Renvoie ``True`` si la position d'admission a été effectivement mise à jour."""
        if not self.estInitialise:
            raise RuntimeError("La position doit être initialisée au préalable.")
        # L'initialisation implique que
        # la liste des voeux est triée par classement internat

        # on compte le nombre de propositions à faire.
        # En cas de dépassement, on met à jour la position d'admission
        comptePlacesProposees = 0
        dernierCandidatComptabilise = -1

        for voeu in self.voeux:
            # si on a dépassé la position d'admission, on arrête
            if voeu.rangInternat > self.positionAdmission:
                return False

            # les propositions à un même candidat comptent pour une seule place
            if voeu.id.G_CN_COD == dernierCandidatComptabilise:
                continue

            # le candidat a déjà l'internat, ignoré pour la mise a jour de la pos admision
            # et du rang sur liste d'attente internat
            if voeu.internatDejaObtenu():
                continue

            # si ok pour déclencher la proposition, on met à jour
            if voeu.formationDejaObtenue() or voeu.estAProposer():
                comptePlacesProposees += 1
                dernierCandidatComptabilise = voeu.id.G_CN_COD

                if comptePlacesProposees > self.nbPlacesVacantes():
                    self.positionAdmission = voeu.rangInternat - 1
                    return True
        return False
