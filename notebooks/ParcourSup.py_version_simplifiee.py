
# coding: utf-8

# # Table of Contents
#  <p><div class="lev1 toc-item"><a href="#Implémentation-simplifiée-des-algorithmes-de-ParcourSup" data-toc-modified-id="Implémentation-simplifiée-des-algorithmes-de-ParcourSup-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Implémentation simplifiée des algorithmes de ParcourSup</a></div><div class="lev2 toc-item"><a href="#Algorithme-1-:-Ordre-d'appel" data-toc-modified-id="Algorithme-1-:-Ordre-d'appel-11"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Algorithme 1 : Ordre d'appel</a></div><div class="lev3 toc-item"><a href="#Types-de-candidats" data-toc-modified-id="Types-de-candidats-111"><span class="toc-item-num">1.1.1&nbsp;&nbsp;</span>Types de candidats</a></div><div class="lev3 toc-item"><a href="#Un-vœu" data-toc-modified-id="Un-vœu-112"><span class="toc-item-num">1.1.2&nbsp;&nbsp;</span>Un vœu</a></div><div class="lev3 toc-item"><a href="#Une-liste-de-vœux" data-toc-modified-id="Une-liste-de-vœux-113"><span class="toc-item-num">1.1.3&nbsp;&nbsp;</span>Une liste de vœux</a></div><div class="lev3 toc-item"><a href="#Contraintes" data-toc-modified-id="Contraintes-114"><span class="toc-item-num">1.1.4&nbsp;&nbsp;</span>Contraintes</a></div><div class="lev3 toc-item"><a href="#Algorithme" data-toc-modified-id="Algorithme-115"><span class="toc-item-num">1.1.5&nbsp;&nbsp;</span>Algorithme</a></div><div class="lev3 toc-item"><a href="#Exemple-(A1)" data-toc-modified-id="Exemple-(A1)-116"><span class="toc-item-num">1.1.6&nbsp;&nbsp;</span>Exemple (A1)</a></div><div class="lev3 toc-item"><a href="#Visualisation-interactive" data-toc-modified-id="Visualisation-interactive-117"><span class="toc-item-num">1.1.7&nbsp;&nbsp;</span>Visualisation interactive</a></div><div class="lev3 toc-item"><a href="#Autres-exemples-(A2,-A4)" data-toc-modified-id="Autres-exemples-(A2,-A4)-118"><span class="toc-item-num">1.1.8&nbsp;&nbsp;</span>Autres exemples (A2, A4)</a></div><div class="lev4 toc-item"><a href="#A2-:-2%-de-boursiers-ères" data-toc-modified-id="A2-:-2%-de-boursiers-ères-1181"><span class="toc-item-num">1.1.8.1&nbsp;&nbsp;</span>A2 : 2% de boursiers-ères</a></div><div class="lev4 toc-item"><a href="#A4-:-10%-de-boursiers-ères" data-toc-modified-id="A4-:-10%-de-boursiers-ères-1182"><span class="toc-item-num">1.1.8.2&nbsp;&nbsp;</span>A4 : 10% de boursiers-ères</a></div><div class="lev2 toc-item"><a href="#Algorithme-2-:-Calcul-des-propositions" data-toc-modified-id="Algorithme-2-:-Calcul-des-propositions-12"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Algorithme 2 : Calcul des propositions</a></div><div class="lev2 toc-item"><a href="#Conclusion" data-toc-modified-id="Conclusion-13"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Conclusion</a></div>

# # Implémentation simplifiée des algorithmes de ParcourSup
# 
# > - Pour plus de détails, voir [le projet sur GitHub](https://github.com/Naereen/ParcourSup.py/).
# > - Auteur(s) : [Lilian Besson](https://github.com/Naereen/) et [Bastien Trotobas](https://github.com/BastienTr).
# > - Date : Juillet 2018.
# > - Licence : [MIT](https://lbesson.mit-license.org/)

# On utilise Python 3 dans ce document. Je vous conseille de le lire interactivement, en cliquant sur ce bouton là :
# 
# [![FIXME ajouter lien MyBinder](FIXME ajouter lien MyBinder)](FIXME ajouter lien MyBinder)

# In[1]:


get_ipython().run_line_magic('load_ext', 'watermark')
get_ipython().run_line_magic('watermark', '-a "Lilian Besson" -v')


# ## Algorithme 1 : Ordre d'appel
# 
# On va donner ici une implémentation simplifiée de la fonction du calcul d'ordre d'appel, avec plusieurs exemples.
# 
# > *CONSIGNE POUR NOUS*
#   - sans typage,
#   - sans classes ni objects,
#   - avec des commentaires.

# ### Types de candidats
# 
# Un candidat ou une candidate peut être boursier-ère ou non, et résident-e ou non.
# On a besoin de 4 types de candidats, qu'on représente simplement par un entier.

# In[2]:


# Les différents types de candidats
BoursierResident       = 1
BoursierNonResident    = 2
NonBoursierResident    = 3
NonBoursierNonResident = 4


# In[3]:


# Liste des différents types
TypesCandidats = [
    BoursierResident,
    BoursierNonResident,
    NonBoursierResident,
    NonBoursierNonResident
]


# In[4]:


def afficheTypeCandidat(typeCandidat):
    return {
        BoursierResident: "BoursierResident",
        BoursierNonResident: "BoursierNonResident",
        NonBoursierResident: "NonBoursierResident",
        NonBoursierNonResident: "NonBoursierNonResident",
    }[typeCandidat]


# ### Un vœu
# 
# Ici on représente un vœu comme la donnée d'un type de candidat et d'un rang.
# On pourrait utiliser un tuple ou une liste, par exemple `[BoursierResident, 1, "Harry Potter"]` pour un boursier résident classé 1er et appelé Harry Potter, mais par lisibilité on préfère utiliser un dictionnaire qui contient ces informations :

# In[5]:


exemple_voeu = {
    "type": BoursierResident,
    "rang": 1,
    "nom": "Harry Potter"
}


# En plus, on n'utilisera jamais le nom des vœux, parce que *la plateforme ParcourSup ne tient compte d'aucune information sur les vœux ou les candidat-s, à part leur identifiant unique et anonymisé*.
# 
# On ajoute un nom dans les premiers exemples simplement pour être un peu plus visuel.
# Les seules chosent que l'algorithme de ParourSup utilise à propos des vœux sont leur type et leur rang.
# Dans le code ci-dessous, ils seront lu comme ça : `voeu["type"]` et `voeu["rang"]`.

# In[6]:


print("Vœu de type", afficheTypeCandidat(exemple_voeu["type"]), "et de rang", exemple_voeu["rang"])


# ### Une liste de vœux

# Ensuite, une liste de vœux est une liste de dictionnaires de cette forme.
# Prenons un exemple avec 8 vœux, qui reprend l'exemple "A1" donné dans le document de référence.
# 
# > Note : les prénoms sont choisis pour être dans l'ordre alphabétique.

# In[7]:


voeu_alice      = { "type": NonBoursierNonResident, "rang": 1, "nom": "Alice" }
voeu_bob        = { "type": NonBoursierNonResident, "rang": 2, "nom": "Bob" }
voeu_christophe = { "type": NonBoursierNonResident, "rang": 3, "nom": "Christophe" }
voeu_dora       = { "type": NonBoursierNonResident, "rang": 4, "nom": "Dora" }
voeu_emilie     = { "type": NonBoursierNonResident, "rang": 5, "nom": "Emilie" }
voeu_florian    = { "type": BoursierNonResident,    "rang": 6, "nom": "Florian" }
voeu_guillaume  = { "type": BoursierNonResident,    "rang": 7, "nom": "Guillaume" }
voeu_helene     = { "type": NonBoursierNonResident, "rang": 8, "nom": "Hélène" }


# On a juste à les mettre dans une liste ensuite (en Python, une liste commence par `[`, chaque valeur est séparée par `,` et termine par `]`).

# In[10]:


voeuxClasses = [
    voeu_alice, voeu_bob, voeu_christophe, voeu_dora,
    voeu_emilie, voeu_florian, voeu_guillaume, voeu_helene
    # le retour à la ligne n'est là que pour une meilleure visibilité
]


# On aura besoin de savoir si un type de candidat est boursier ou non (respectivement, est résident ou non).

# In[11]:


def estBoursier(voeu):
    return voeu["type"] == BoursierResident or voeu["type"] == BoursierNonResident


# In[12]:


def estResident(voeu):
    return voeu["type"] == BoursierResident or voeu["type"] == NonBoursierResident


# In[13]:


print("Le vœu exemple est-il boursier ?", estBoursier(exemple_voeu))
print("Le vœu exemple est-il résident ?", estResident(exemple_voeu))


# ### Contraintes
# 
# On a besoin de connaître ces deux contraintes, exprimées en pourcentage donné comme un *entier* entre $0$ et $100$.
# 
# - Par exemple ici, on demandera à avoir au moins 20% de boursiers-ères, mais aucune contrainte sur le taux de résidents-es.

# In[14]:


tauxMinBoursiersPourcents = 20
tauxMinResidentsPourcents = 0


# ### Algorithme
# 
# On devrait avoir tout ce qu'il faut.
# 
# L'algorithme est présenté comme suit dans [le document de référence](https://framagit.org/parcoursup/algorithmes-de-parcoursup/blob/master/doc/presentation_algorithmes_parcoursup.pdf) :
# 
# <img src="images/Algorithme_CalculOrdreAppel.png" width=50%>
# 
# Nous avons essayé de rendre le code suivant le plus clair possible mais il est nécessairement un peu long. Forcez vous à le lire jusqu'au bout !

# In[18]:


def calculerOrdreAppel(
        voeuxClasses,
        tauxMinBoursiersPourcents,
        tauxMinResidentsPourcents,
        afficheTout=True
    ):
    if afficheTout == False:
        def affiche(*args, **kwargs): pass
    else: affiche = print

    affiche(f"\n0. On commence à calculer les ordres d'appel pour cette liste de vœux qui contient {len(voeuxClasses)} voeux.")

    affiche(f"  On crée des listes de vœux pour chaque types de candidats ({TypesCandidats}).")
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
    affiche("\n1. On trie les vœux par classement...")
    affiche(f"  Avant le tri : {voeuxClasses}...")
    voeuxClasses.sort(key=lambda voeu: -voeu["rang"])
    affiche(f"  Après le tri : {voeuxClasses}...")

    for indice in range(len(voeuxClasses)):
        voeu = voeuxClasses[indice]
        # on ajoute le voeu à la fin de la file (FIFO) correspondante
        filesAttente[voeu["type"]].append(voeu)
        # affiche(f"  On ajoute le voeu {voeu} à la file du type {voeu["type"]}, c'est le {i+1}ème à être ajouté.")
        if estBoursier(voeu):
            nbBoursiersTotal += 1
            affiche(f"    On compte un-e boursier-e en plus, c'est le {nbBoursiersTotal}ème...")
        if estResident(voeu):
            nbResidentsTotal += 1
            affiche(f"    On compte un-e résident-e en plus, c'est le {nbResidentsTotal}ème...")

    nbVoeuxClasses     = len(voeuxClasses)
    nbAppeles          = 0
    nbBoursiersAppeles = 0
    nbResidentsAppeles = 0

    # la boucle ajoute les candidats un par un à la liste suivante, dans l'ordre d'appel.
    # On commence par un ordre d'appel vide (liste vide).
    ordreAppel = [ ]

    affiche(f"\n2. Début de la boucle while, on remplit l'ordre d'appel...")

    while len(ordreAppel) < nbVoeuxClasses:
        affiche(f"\n  L'ordre d'appel contient {len(ordreAppel)} éléments et il y a {nbVoeuxClasses} vœux à classer.")
        # on calcule lequel ou lesquels des critères boursiers et résidents
        # contraignent le choix du prochain candidat dans l'ordre d'appel

        contrainteTauxBoursier = (nbBoursiersAppeles < nbBoursiersTotal) and ((nbBoursiersAppeles * 100) < tauxMinBoursiersPourcents * (nbAppeles + 1))
        affiche(f"  La contrainte sur le taux de boursier-es est {contrainteTauxBoursier}...")
        affiche(f"      Car il y a pour l'instant {nbBoursiersAppeles} boursier-es appelé-es sur un total de {nbBoursiersTotal}, et ce n'est pas assez pour dépasser le taux de {tauxMinBoursiersPourcents}...")

        contrainteTauxResident = (nbResidentsAppeles < nbResidentsTotal) and ((nbResidentsAppeles * 100) < tauxMinResidentsPourcents * (nbAppeles + 1))
        affiche(f"  La contrainte sur le taux de résident-es est {contrainteTauxResident}...")
        affiche(f"      Car il y a pour l'instant {nbResidentsAppeles} résident-es appelé-es sur un total de {nbResidentsTotal}, et ce n'est pas assez pour dépasser le taux de {tauxMinResidentsPourcents}...")

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
        affiche(f"  Les vœux satisfaisant les deux contraintes à la fois, ordonnés par rang de classement sont :\n{liste_eligibles}")
        del liste_eligibles  # juste pour l'afficher

        # stocke le meilleur candidat à appeler tout en respectant
        # les deux contraintes si possible
        # ou à défaut seulement la contrainte sur le taux boursier
        meilleur = None

        if eligibles:
            # on prend le meilleur de cette liste
            meilleur = max(eligibles, key=lambda voeu: -voeu["rang"])
            affiche(f"  La liste des éligibles n'est pas vide, donc le-la meilleur-e est le-la meilleur-e de cette liste = {meilleur}")
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
            affiche(f"  La liste des éligibles est pas vide, donc le-la meilleur-e est le-la meilleur-e de la liste des boursier-es non résident-es = {meilleur}")

        # suppression du candidat choisi de sa file d'attente
        saFileAttente = filesAttente[meilleur["type"]]
        affiche(f"  On vérifie si le-la meilleur {meilleur} est aussi le-la meilleur-e de sa liste contenant {len(saFileAttente)} candidat-es (du type {meilleur['type']}).")
        meilleur_de_sa_liste = saFileAttente.pop()
        assert meilleur == meilleur_de_sa_liste, "Erreur : ce cas où le-la meilleur-e candidat-e n'est pas le meilleur candidat de la liste d'attente des autres candidat-e de sa liste ne devrait pas arriver."  # DEBUG

        # ajout du meilleur candidat à l'ordre d'appel
        ordreAppel.append(meilleur)
        nbAppeles += 1
        affiche(f"  On ajoute le meilleur {meilleur} à l'ordre d'appel, c'est le-la {nbAppeles}ème à être appelé-e.")

        if estBoursier(meilleur):
            nbBoursiersAppeles += 1
            affiche(f"    En plus, c'est le-la {nbBoursiersAppeles}ème boursier-e à être appelé-e.")
        if estResident(meilleur):
            nbResidentsAppeles += 1
            affiche(f"    En plus, c'est le-la {nbResidentsAppeles}ème résident-e à être appelé-e.")

    # fin de la boucle while
    affiche(f"\n3. On a terminé la boucle, on a remplit l'ordre d'appel.")

    return ordreAppel


# ### Exemple (A1)
# 
# Avec les valeurs prisent ci-dessus comme exemple :

# In[19]:


calculerOrdreAppel(
    voeuxClasses,
    tauxMinBoursiersPourcents,
    tauxMinResidentsPourcents
)


# - Sur cet exemple, on constate que la contrainte sur les boursiers a pu aider le candidat Florian, qui étais classé 6ème (le meilleur parmi les boursiers) à remonter devant certains candidats non boursiers.
# 
# - La suite est logique, entre Alice, Bob, Christophe et Dora, puis on voit que Guillaume est aussi passé devant d'autres candidats avec la contrainte de 20% de boursiers (après les 5 premiers candidats, dont un boursier, il faut ajouter Guillaume pour continuer à satisfaire la contrainte de minimum 20% de boursiers).

# ### Visualisation interactive
# 
# Les morceaux suivants sont hors programme, *ne regardez pas le détail du code*.
# 
# Ils vont permettre d'explorer interactivement l'influence des deux taux minimums (taux de boursiers-ères et résidents-entes) sur le résultat de l'ordre d'appel.

# In[21]:


from IPython.display import display
from ipywidgets import interact


# On définit la fonction que l'on souhaite explorer :

# In[22]:


def fait_fonctionATester(
    voeuxClasses,
    tauxMinBoursiersPourcents=20,
    tauxMinResidentsPourcents=0
):
    def fonctionATester(
        tauxMinBoursiersPourcents=tauxMinBoursiersPourcents,
        tauxMinResidentsPourcents=tauxMinResidentsPourcents
    ):
        ordreAppel = calculerOrdreAppel(
            voeuxClasses,
            tauxMinBoursiersPourcents,
            tauxMinResidentsPourcents,
            afficheTout=False  # on cache la sortie
        )
        res = [voeu["rang"] for voeu in ordreAppel]
        display(res)
        return res

    return fonctionATester


# Par exemple, si on demande $90%$ de boursiers, on voit que les candidats classés 6ème (Florian) et 7ème (Guillaume) sont mis en avant.

# In[23]:


fait_fonctionATester(voeuxClasses)(90, 0)


# Mais la visualisation interactive suivante permet de suivre l'influence des deux paramètres sur la liste des rangs finaux beaucoup plus facilement.

# In[24]:


interact(
    fait_fonctionATester(voeuxClasses, tauxMinBoursiersPourcents=20, tauxMinResidentsPourcents=0),
    tauxMinBoursiersPourcents=(0, 100, 1),
    tauxMinResidentsPourcents=(0, 100, 1)
);


# > <span style="color:red;">Ca ne marche pas sur ma machine</span>, mais sur une installation neuve ou sur [MyBinder](http://mybinder.org/), tout fonctionne bien…

# ### Autres exemples (A2, A4)
# 
# Le document de référence propose deux autres exemples de petite taille, notés A2 et A4.

# #### A2 : 2% de boursiers-ères
# 
# Comme dans le document de référence : C1 C2 C3 C4 C5 B6 C7 C8, où B6 est boursier, et tous sont non résidents.
# (Plus besoin des noms dans cet exemple là, on les enlève)

# In[26]:


C1 = { "type": NonBoursierNonResident, "rang": 1 }
C2 = { "type": NonBoursierNonResident, "rang": 2 }
C3 = { "type": NonBoursierNonResident, "rang": 3 }
C4 = { "type": NonBoursierNonResident, "rang": 4 }
C5 = { "type": NonBoursierNonResident, "rang": 5 }
B6 = { "type": BoursierNonResident,    "rang": 6 }
C7 = { "type": NonBoursierNonResident, "rang": 7 }
C8 = { "type": NonBoursierNonResident, "rang": 8 }


# In[27]:


voeuxClasses_A2 = [C1, C2, C3, C4, C5, B6, C7, C8]


# On reproduit l'exemple du document de référence, avant de vous laisser explorer l'influence des deux taux.

# In[29]:


fait_fonctionATester(voeuxClasses_A2)(2, 0)


# In[28]:


interact(
    fait_fonctionATester(
        voeuxClasses_A2, tauxMinBoursiersPourcents=2, tauxMinResidentsPourcents=0
    ),
    tauxMinBoursiersPourcents=(0, 100, 1),
    tauxMinResidentsPourcents=(0, 100, 1)
);


# On remarque que même un minimum de $2%$ de boursiers-ères suffit à faire remonter le candidat B6 en tête.
# 
# L'ordre des rangs est respecté seulement si on a aucune contrainte sur le taux de boursiers.

# In[31]:


fait_fonctionATester(voeuxClasses_A2)(0, 0)


# #### A4 : 10% de boursiers-ères
# 
# Comme dans le document de référence : C1 B2 B3 C4 C5 C6 C7 B8 C9 C10, où B2 B3 et B8 sont boursiers et tous sont non résidents.

# In[32]:


C1  = { "type": NonBoursierNonResident, "rang": 1 }
B2  = { "type": BoursierNonResident,    "rang": 2 }
B3  = { "type": BoursierNonResident,    "rang": 3 }
C4  = { "type": NonBoursierNonResident, "rang": 4 }
C5  = { "type": NonBoursierNonResident, "rang": 5 }
C6  = { "type": NonBoursierNonResident, "rang": 6 }
C7  = { "type": NonBoursierNonResident, "rang": 7 }
B8  = { "type": BoursierNonResident,    "rang": 8 }
C9  = { "type": NonBoursierNonResident, "rang": 9 }
C10 = { "type": NonBoursierNonResident, "rang": 10 }


# In[33]:


voeuxClasses_A4 = [C1, B2, B3, C4, C5, C6, C7, B8, C9, C10]


# On reproduit l'exemple du document de référence, avant de vous laisser explorer l'influence des deux taux.

# In[34]:


fait_fonctionATester(voeuxClasses_A4)(10, 0)


# In[35]:


interact(
    fait_fonctionATester(
        voeuxClasses_A4, tauxMinBoursiersPourcents=10, tauxMinResidentsPourcents=0
    ),
    tauxMinBoursiersPourcents=(0, 100, 1),
    tauxMinResidentsPourcents=(0, 100, 1)
);


# ----
# ## Algorithme 2 : Calcul des propositions

# In[21]:


from IPython.display import HTML


# In[22]:


HTML(f"<center><span style='color:red; font-size: xx-large;'>{'TODO '*54}</span></center>")


# ## Conclusion
# 
# Ce petit notebook n'est pas terminé, c'est un test *en cours de rédaction*.
