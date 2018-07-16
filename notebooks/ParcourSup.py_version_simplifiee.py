
# coding: utf-8

# # Table of Contents
#  <p><div class="lev1 toc-item"><a href="#Implémentation-simplifiée-des-algorithmes-de-ParcourSup" data-toc-modified-id="Implémentation-simplifiée-des-algorithmes-de-ParcourSup-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Implémentation simplifiée des algorithmes de ParcourSup</a></div><div class="lev2 toc-item"><a href="#Algorithme-1-:-Ordre-d'appel" data-toc-modified-id="Algorithme-1-:-Ordre-d'appel-11"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Algorithme 1 : Ordre d'appel</a></div><div class="lev3 toc-item"><a href="#Types-de-candidats" data-toc-modified-id="Types-de-candidats-111"><span class="toc-item-num">1.1.1&nbsp;&nbsp;</span>Types de candidats</a></div><div class="lev3 toc-item"><a href="#Un-vœu" data-toc-modified-id="Un-vœu-112"><span class="toc-item-num">1.1.2&nbsp;&nbsp;</span>Un vœu</a></div><div class="lev3 toc-item"><a href="#Contraintes" data-toc-modified-id="Contraintes-113"><span class="toc-item-num">1.1.3&nbsp;&nbsp;</span>Contraintes</a></div><div class="lev3 toc-item"><a href="#Algorithme" data-toc-modified-id="Algorithme-114"><span class="toc-item-num">1.1.4&nbsp;&nbsp;</span>Algorithme</a></div><div class="lev3 toc-item"><a href="#Exemple" data-toc-modified-id="Exemple-115"><span class="toc-item-num">1.1.5&nbsp;&nbsp;</span>Exemple</a></div><div class="lev2 toc-item"><a href="#Algorithme-2-:-Calcul-des-propositions" data-toc-modified-id="Algorithme-2-:-Calcul-des-propositions-12"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Algorithme 2 : Calcul des propositions</a></div><div class="lev2 toc-item"><a href="#Conclusion" data-toc-modified-id="Conclusion-13"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Conclusion</a></div>

# # Implémentation simplifiée des algorithmes de ParcourSup
# 
# > - Pour plus de détails, voir [le projet sur GitHub](https://github.com/Naereen/ParcourSup.py/).
# > - Auteur(s) : Lilian Besson.
# > - Date : Juillet 2018.
# > - Licence : [MIT](https://lbesson.mit-license.org/)

# ## Algorithme 1 : Ordre d'appel
# 
# On va donner ici une implémentation simplifiée de la fonction du calcul d'ordre d'appel.
# 
# - sans typage
# - sans classes ni objects
# - avec beaucoup de commentaires

# ### Types de candidats
# 
# Un candidat ou une candidate peut être boursier-ère ou non, et résident-e ou non.

# In[2]:


# Les différents types de candidats
BoursierResident       = 1
BoursierNonResident    = 2
NonBoursierResident    = 3
NonBoursierNonResident = 4

# Liste des différents types
TypesCandidats = [
    BoursierResident,
    BoursierNonResident,
    NonBoursierResident,
    NonBoursierNonResident
]


# ### Un vœu
# 
# Ici on représente un vœu comme la donnée d'un type de candidat et d'un rang.
# On pourrait utiliser un tuple ou une liste, par exemple `[BoursierResident, 1]` pour un-e boursier-ère résident-e classé-e 1er-ère, mais par lisibilité on préfère utiliser un dictionnaire qui contient ces deux informations :

# In[ ]:


exemple_voeu = {
    "type": BoursierResident,
    "rang": 1
}


# Ensuite, une liste de vœux est une liste de dictionnaires de cette forme.
# Prenons un exemple avec 8 vœux.
# 
# > Note : les prénoms sont choisis pour être dans l'ordre alphabétique.

# In[6]:


voeu_alice   = { "type": NonBoursierNonResident, "rang": 1 }
voeu_bob     = { "type": NonBoursierNonResident, "rang": 2 }
voeu_carlos  = { "type": NonBoursierNonResident, "rang": 3 }
voeu_dora    = { "type": NonBoursierNonResident, "rang": 4 }
voeu_enzo    = { "type": NonBoursierNonResident, "rang": 5 }
voeu_florian = { "type": BoursierNonResident,    "rang": 6 }
voeu_gaelle  = { "type": BoursierNonResident,    "rang": 7 }
voeu_helene  = { "type": NonBoursierNonResident, "rang": 8 }


# On a juste à les mettre dans une liste ensuite.

# In[9]:


voeuxClasses = [
    voeu_alice, voeu_bob, voeu_carlos, voeu_dora,
    voeu_enzo, voeu_florian, voeu_gaelle, voeu_helene
    # le retour à la ligne n'est là que pour une meilleure visibilité
]


# On aura besoin de savoir si un type de candidat est boursier ou non (respectivement, est résident ou non).

# In[24]:


def estBoursier(voeu):
    return voeu["type"] == BoursierResident or voeu["type"] == BoursierNonResident


# In[25]:


def estResident(voeu):
    return voeu["type"] == BoursierResident or voeu["type"] == NonBoursierResident


# ### Contraintes
# 
# On a besoin de connaître ces deux contraintes, exprimées en pourcentage.
# 
# - Par exemple ici, on demandera à avoir au moins 20% de boursiers-ères, mais aucune contrainte sur le taux de résidents-es.

# In[26]:


tauxMinBoursiersPourcents = 20
tauxMinResidentsPourcents = 0


# ### Algorithme
# 
# On devrait avoir tout ce qu'il faut.

# In[27]:


list.sort


# In[31]:


def calculerOrdreAppel(
        voeuxClasses,
        tauxMinBoursiersPourcents,
        tauxMinResidentsPourcents
    ):
    """ Calcule de l'ordre d'appel."""

    print(f"\n0. On commence à calculer les ordres d'appel pour cette liste de vœux qui contient {len(voeuxClasses)} voeux.")

    print(f"  On crée des listes de vœux pour chaque types de candidats ({TypesCandidats}).")
    # on crée autant de listes de vœux que de types de candidats,
    # triées par ordre de classement
    filesAttente = {
        typeCandidat: [ ]  # liste vide associée à chaque type
        for typeCandidat in TypesCandidats
    }

    # Chaque voeu classé est ventilé dans la liste correspondante,
    # en fonction du type du candidat.
    # Les quatre listes obtenues sont ordonnées par rang de classement,
    # comme l'est la liste voeuxClasses.
    nbBoursiersTotal = 0
    nbResidentsTotal = 0

    # on trie les vœux par classement
    print("\n1. On trie les vœux par classement...")
    print(f"  Avant le tri : {voeuxClasses}...")
    voeuxClasses.sort(key=lambda voeu: voeu["rang"])
    # FIXME
    print(f"  Après le tri : {voeuxClasses}...")

    for indice in range(len(voeuxClasses)):
        voeu = voeuxClasses[indice]
        # on ajoute le voeu à la fin de la file (FIFO) correspondante
        filesAttente[voeu["type"]].append(voeu)
        # print(f"  On ajoute le voeu {voeu} à la file du type {voeu["type"]}, c'est le {i+1}ème à être ajouté.")
        if estBoursier(voeu):
            nbBoursiersTotal += 1
            print(f"    On compte un-e boursier-e en plus, c'est le {nbBoursiersTotal}ème...")
        if estResident(voeu):
            nbResidentsTotal += 1
            print(f"    On compte un-e résident-e en plus, c'est le {nbResidentsTotal}ème...")

    nbVoeuxClasses     = len(voeuxClasses)
    nbAppeles          = 0
    nbBoursiersAppeles = 0
    nbResidentsAppeles = 0

    # la boucle ajoute les candidats un par un à la liste suivante, dans l'ordre d'appel.
    # On commence par un ordre d'appel vide (liste vide).
    ordreAppel = [ ]

    print(f"\n2. Début de la boucle while, on remplit l'ordre d'appel...")

    while len(ordreAppel) < nbVoeuxClasses:
        print(f"\n  L'ordre d'appel contient {len(ordreAppel)} éléments et il y a {nbVoeuxClasses} vœux à classer.")
        # on calcule lequel ou lesquels des critères boursiers et résidents
        # contraignent le choix du prochain candidat dans l'ordre d'appel

        contrainteTauxBoursier = (nbBoursiersAppeles < nbBoursiersTotal) and ((nbBoursiersAppeles * 100) < tauxMinBoursiersPourcents * (nbAppeles + 1))
        print(f"  La contrainte sur le taux de boursier-es est {contrainteTauxBoursier}...")
        print(f"      Car il y a pour l'instant {nbBoursiersAppeles} boursier-es appelé-es sur un total de {nbBoursiersTotal}, et ce n'est pas assez pour dépasser le taux de {tauxMinBoursiersPourcents}...")

        contrainteTauxResident = (nbResidentsAppeles < nbResidentsTotal) and ((nbResidentsAppeles * 100) < tauxMinResidentsPourcents * (nbAppeles + 1))
        print(f"  La contrainte sur le taux de résident-es est {contrainteTauxResident}...")
        print(f"      Car il y a pour l'instant {nbResidentsAppeles} résident-es appelé-es sur un total de {nbResidentsTotal}, et ce n'est pas assez pour dépasser le taux de {tauxMinResidentsPourcents}...")

        # on fait la liste des voeux satisfaisant
        # les deux contraintes à la fois, ordonnée par rang de classement
        liste_eligibles = [ ]
        eligibles = [ ]
        for queue in filesAttente.values():
            if queue:
                voeu = queue[-1]  # le meilleur a été ajouté en dernier
                if (estBoursier(voeu) or not contrainteTauxBoursier) and (estResident(voeu) or not contrainteTauxResident):
                    eligibles.append(voeu)
                    liste_eligibles.append(voeu)
        print(f"  Les vœux satisfaisant les deux contraintes à la fois, ordonnés par rang de classement sont :\n{liste_eligibles}")
        del liste_eligibles  # juste pour l'afficher

        # stocke le meilleur candidat à appeler tout en respectant
        # les deux contraintes si possible
        # ou à défaut seulement la contrainte sur le taux boursier
        meilleur = None

        if eligibles:
            # on prend le meilleur de cette liste
            meilleur = max(eligibles, key=lambda voeu: voeu["rang"])
            print(f"  La liste des éligibles n'est pas vide, donc le-la meilleur-e est le-la meilleur-e de cette liste = {meilleur}")
        else:
            # la liste peut être vide dans le cas où les deux contraintes
            # ne peuvent être satisfaites à la fois.
            # Dans ce cas nécessairement il y a une contrainte sur chacun des deux taux
            # (donc au moins un boursier non encore sélectionné)
            # et il ne reste plus de boursier résident,
            # donc il reste au moins un boursier non résident
            assert contrainteTauxBoursier and contrainteTauxResident, "Erreur : ce cas où la file de priorité est vide mais les deux contraintes ne sont pas vérifiées ne devrait pas arriver."  # DEBUG

            assert not filesAttente[BoursierResident], "Erreur : ce cas où la file de priorité est vide mais il reste des candidats-es boursiers-ères et résident-es ne devrait pas arriver."  # DEBUG
            assert filesAttente[BoursierNonResident], "Erreur : ce cas où la file de priorité est vide mais il ne reste pas de candidats-es boursiers-ères et non résident-es ne devrait pas arriver."  # DEBUG

            CandidatsBoursierNonResident = filesAttente[BoursierNonResident]
            meilleur = max(CandidatsBoursierNonResident)
            print(f"  La liste des éligibles est pas vide, donc le-la meilleur-e est le-la meilleur-e de la liste des boursier-es non résident-es = {meilleur}")

        # suppression du candidat choisi de sa file d'attente
        saFileAttente = filesAttente[meilleur["type"]]
        print(f"  On vérifie si le-la meilleur {meilleur} est aussi le-la meilleur-e de sa liste contenant {len(saFileAttente)} candidat-es (du type {meilleur['type']}).")
        meilleur_de_sa_liste = saFileAttente.pop()
        assert meilleur == meilleur_de_sa_liste, "Erreur : ce cas où le-la meilleur-e candidat-e n'est pas le meilleur candidat de la liste d'attente des autres candidat-e de sa liste ne devrait pas arriver."  # DEBUG

        # ajout du meilleur candidat à l'ordre d'appel
        ordreAppel.append(meilleur)
        nbAppeles += 1
        print(f"  On ajoute le meilleur {meilleur} à l'ordre d'appel, c'est le-la {nbAppeles}ème à être appelé-e.")

        if estBoursier(meilleur):
            nbBoursiersAppeles += 1
            print(f"    En plus, c'est le-la {nbBoursiersAppeles}ème boursier-e à être appelé-e.")
        if estResident(meilleur):
            nbResidentsAppeles += 1
            print(f"    En plus, c'est le-la {nbResidentsAppeles}ème résident-e à être appelé-e.")

    # fin de la boucle while
    print(f"\n3. On a terminé la boucle, on a remplit l'ordre d'appel.")

    return ordreAppel


# ### Exemple
# 
# Avec les valeurs prisent ci-dessus comme exemple :

# In[32]:


calculerOrdreAppel(
    voeuxClasses,
    tauxMinBoursiersPourcents,
    tauxMinResidentsPourcents
)


# ## Algorithme 2 : Calcul des propositions

# In[33]:


from IPython import display


# In[46]:


display.HTML(f"<center><span style='color:red; font-size: xx-large;'>{'TODO '*54}</span></center>")


# ## Conclusion
# 
# Ce petit notebook n'est pas terminé, c'est un test *en cours de rédaction*.
