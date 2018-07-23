
# coding: utf-8

# # Table of Contents
#  <p><div class="lev1 toc-item"><a href="#Implémentation-simplifiée-des-algorithmes-de-ParcourSup" data-toc-modified-id="Implémentation-simplifiée-des-algorithmes-de-ParcourSup-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Implémentation simplifiée des algorithmes de ParcourSup</a></div><div class="lev2 toc-item"><a href="#Algorithme-1-:-Ordre-d'appel" data-toc-modified-id="Algorithme-1-:-Ordre-d'appel-11"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Algorithme 1 : Ordre d'appel</a></div><div class="lev3 toc-item"><a href="#Types-de-candidats" data-toc-modified-id="Types-de-candidats-111"><span class="toc-item-num">1.1.1&nbsp;&nbsp;</span>Types de candidats</a></div><div class="lev3 toc-item"><a href="#Un-vœu" data-toc-modified-id="Un-vœu-112"><span class="toc-item-num">1.1.2&nbsp;&nbsp;</span>Un vœu</a></div><div class="lev3 toc-item"><a href="#Une-liste-de-vœux" data-toc-modified-id="Une-liste-de-vœux-113"><span class="toc-item-num">1.1.3&nbsp;&nbsp;</span>Une liste de vœux</a></div><div class="lev3 toc-item"><a href="#Contraintes" data-toc-modified-id="Contraintes-114"><span class="toc-item-num">1.1.4&nbsp;&nbsp;</span>Contraintes</a></div><div class="lev3 toc-item"><a href="#Algorithme" data-toc-modified-id="Algorithme-115"><span class="toc-item-num">1.1.5&nbsp;&nbsp;</span>Algorithme</a></div><div class="lev3 toc-item"><a href="#Exemple-(A1)" data-toc-modified-id="Exemple-(A1)-116"><span class="toc-item-num">1.1.6&nbsp;&nbsp;</span>Exemple (A1)</a></div><div class="lev3 toc-item"><a href="#Visualisation-interactive" data-toc-modified-id="Visualisation-interactive-117"><span class="toc-item-num">1.1.7&nbsp;&nbsp;</span>Visualisation interactive</a></div><div class="lev3 toc-item"><a href="#Autres-exemples-(A2,-A4)" data-toc-modified-id="Autres-exemples-(A2,-A4)-118"><span class="toc-item-num">1.1.8&nbsp;&nbsp;</span>Autres exemples (A2, A4)</a></div><div class="lev4 toc-item"><a href="#A2-:-2%-de-boursiers-ères" data-toc-modified-id="A2-:-2%-de-boursiers-ères-1181"><span class="toc-item-num">1.1.8.1&nbsp;&nbsp;</span>A2 : 2% de boursiers-ères</a></div><div class="lev4 toc-item"><a href="#A4-:-10%-de-boursiers-ères" data-toc-modified-id="A4-:-10%-de-boursiers-ères-1182"><span class="toc-item-num">1.1.8.2&nbsp;&nbsp;</span>A4 : 10% de boursiers-ères</a></div><div class="lev3 toc-item"><a href="#Visualisations-colorées" data-toc-modified-id="Visualisations-colorées-119"><span class="toc-item-num">1.1.9&nbsp;&nbsp;</span>Visualisations colorées</a></div><div class="lev3 toc-item"><a href="#Entrée-aléatoire" data-toc-modified-id="Entrée-aléatoire-1110"><span class="toc-item-num">1.1.10&nbsp;&nbsp;</span>Entrée aléatoire</a></div><div class="lev2 toc-item"><a href="#Algorithme-2-:-Calcul-des-propositions" data-toc-modified-id="Algorithme-2-:-Calcul-des-propositions-12"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Algorithme 2 : Calcul des propositions</a></div><div class="lev2 toc-item"><a href="#Conclusion" data-toc-modified-id="Conclusion-13"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Conclusion</a></div>

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
    if typeCandidat == BoursierResident:
        return "BoursierResident"
    elif typeCandidat == BoursierNonResident: 
        return "BoursierNonResident"
    elif typeCandidat == NonBoursierResident: 
        return "NonBoursierResident"
    elif typeCandidat == NonBoursierNonResident: 
        return "NonBoursierNonResident"


# ### Un vœu
# 
# Ici on représente un vœu comme la donnée d'un type de candidat et d'un rang.
# On pourrait utiliser un tuple ou une liste, par exemple `[BoursierResident, 1, "Harry Potter"]` pour un boursier résident classé 1er et appelé Harry Potter, mais par lisibilité on préfère utiliser un dictionnaire qui contient ces informations :

# > *POUR NOUS* ne même pas parler de nom mais juste d'identifiant ?

# In[5]:


exemple_voeu = {
    "type": BoursierResident,
    "rang": 1,
    "nom": "Harry Potter"
}


# En fait, on n'utilisera jamais le nom des vœux, parce que *la plateforme ParcourSup ne tient compte d'aucune information sur les vœux ou les candidat-s, à part leur identifiant unique et anonymisé*.
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

# In[8]:


voeuxClasses = [
    voeu_alice, voeu_bob, voeu_christophe, voeu_dora,
    voeu_emilie, voeu_florian, voeu_guillaume, voeu_helene
    # le retour à la ligne n'est là que pour une meilleure visibilité
]


# On aura besoin de savoir si un type de candidat est boursier ou non (respectivement, est résident ou non).

# In[9]:


def estBoursier(voeu):
    return voeu["type"] == BoursierResident or voeu["type"] == BoursierNonResident


# In[10]:


def estResident(voeu):
    return voeu["type"] == BoursierResident or voeu["type"] == NonBoursierResident


# In[11]:


print("Le vœu exemple est-il boursier ?", estBoursier(exemple_voeu))
print("Le vœu exemple est-il résident ?", estResident(exemple_voeu))


# ### Contraintes
# 
# On a besoin de connaître ces deux contraintes, exprimées en pourcentage donné comme un *entier* entre $0$ et $100$.
# 
# - Par exemple ici, on demandera à avoir au moins 20% de boursiers-ères, mais aucune contrainte sur le taux de résidents-e-s.

# In[12]:


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

# In[13]:


def calculerOrdreAppel(
        voeuxClasses,
        tauxMinBoursiersPourcents,
        tauxMinResidentsPourcents,
        afficheTout=True
    ):
    if afficheTout == False:
        def affiche(*args, **kwargs): pass
    else: affiche = print

    affiche("\n0. On commence à calculer les ordres d'appel pour cette liste de vœux qui contient", len(voeuxClasses), "voeux.")

    affiche("  On crée des listes de vœux pour chaque types de candidats", TypesCandidats)
    # on crée autant de listes de vœux que de types de candidats,
    # triées par ordre de classement
    filesAttente = {
        BoursierResident: [ ],  # liste vide associée à chaque type
        BoursierNonResident: [ ],  # liste vide associée à chaque type
        NonBoursierResident: [ ],  # liste vide associée à chaque type
        NonBoursierNonResident: [ ],  # liste vide associée à chaque type
    }

    # Chaque voeu classé est ventilé dans la liste correspondante,
    # en fonction du type du candidat.
    # Les quatre listes obtenues sont ordonnées par rang de classement,
    # comme l'est la liste voeuxClasses.
    nbBoursiersTotal = 0
    nbResidentsTotal = 0

    # on trie les vœux par classement
    affiche("\n1. On trie les vœux par classement (rang croissant)...")
    affiche("  Avant le tri :", voeuxClasses, "...")
    voeuxClasses.sort(key=lambda voeu: -voeu["rang"])
    affiche("  Après le tri :", voeuxClasses, "...")

    for voeu in voeuxClasses:
        # on ajoute le voeu à la fin de la file (FIFO) correspondante
        filesAttente[voeu["type"]].append(voeu)
        if estBoursier(voeu):
            nbBoursiersTotal += 1
            affiche("    On compte un-e boursier-e en plus, c'est le", nbBoursiersTotal, "ème...")
        if estResident(voeu):
            nbResidentsTotal += 1
            affiche("    On compte un-e résident-e en plus, c'est le", nbResidentsTotal, "ème...")

    nbVoeuxClasses     = len(voeuxClasses)
    nbAppeles          = 0
    nbBoursiersAppeles = 0
    nbResidentsAppeles = 0

    # la boucle ajoute les candidats un par un à la liste suivante, dans l'ordre d'appel.
    # On commence par un ordre d'appel vide (liste vide).
    ordreAppel = [ ]

    affiche("\n2. Début de la boucle while, on remplit l'ordre d'appel...")

    while len(ordreAppel) < nbVoeuxClasses:
        affiche("\n  L'ordre d'appel contient", len(ordreAppel), "éléments et il y a", nbVoeuxClasses, "vœux à classer.")
        # on calcule lequel ou lesquels des critères boursiers et résidents
        # contraignent le choix du prochain candidat dans l'ordre d'appel

        contrainteTauxBoursier = (nbBoursiersAppeles < nbBoursiersTotal) and ((nbBoursiersAppeles * 100) < tauxMinBoursiersPourcents * (nbAppeles + 1))
        affiche("  La contrainte sur le taux de boursier-e-s est", contrainteTauxBoursier, "...")
        affiche("      Car il y a pour l'instant", nbBoursiersAppeles, "boursier-e-s appelé-e-s sur un total de", nbBoursiersTotal, "et ce n'est pas assez pour dépasser le taux de", tauxMinBoursiersPourcents, "...")

        contrainteTauxResident = (nbResidentsAppeles < nbResidentsTotal) and ((nbResidentsAppeles * 100) < tauxMinResidentsPourcents * (nbAppeles + 1))
        affiche("  La contrainte sur le taux de résident-e-s est", contrainteTauxResident, "...")
        affiche("      Car il y a pour l'instant", nbResidentsAppeles, "résident-e-s appelé-e-s sur un total de", nbResidentsTotal, "et ce n'est pas assez pour dépasser le taux de", tauxMinResidentsPourcents, "...")

        # on fait la liste des voeux satisfaisant
        # les deux contraintes à la fois, ordonnée par rang de classement
        eligibles = [ ]
        for queue in filesAttente.values():
            if queue:
                voeu = queue[-1]  # le meilleur a été ajouté en dernier
                if ((estBoursier(voeu) or not contrainteTauxBoursier)
                    and (estResident(voeu) or not contrainteTauxResident)):
                    eligibles.append(voeu)
        affiche("  Les vœux satisfaisant les deux contraintes à la fois, ordonnés par rang de classement sont :\n", eligibles)

        # stocke le meilleur candidat à appeler tout en respectant
        # les deux contraintes si possible
        # ou à défaut seulement la contrainte sur le taux boursier
        meilleur = None

        if len(eligibles) > 0:
            # on prend le meilleur de cette liste
            meilleur = max(eligibles, key=lambda voeu: -voeu["rang"])
            affiche("  La liste des éligibles n'est pas vide, donc le-la meilleur-e est le-la meilleur-e de cette liste =", meilleur)
        else:
            # la liste peut être vide dans le cas où les deux contraintes
            # ne peuvent être satisfaites à la fois.
            # Dans ce cas nécessairement il y a une contrainte sur chacun des deux taux
            # (donc au moins un boursier non encore sélectionné)
            # et il ne reste plus de boursier résident,
            # donc il reste au moins un boursier non résident
            CandidatsBoursierNonResident = filesAttente[BoursierNonResident]
            meilleur = max(CandidatsBoursierNonResident, key=lambda voeu: -voeu["rang"])
            affiche("  La liste des éligibles est pas vide, donc le-la meilleur-e est le-la meilleur-e de la liste des boursier-e-s non résident-e-s =", meilleur)

        # suppression du candidat choisi de sa file d'attente
        saFileAttente = filesAttente[meilleur["type"]]
        affiche("  On vérifie si le-la meilleur", meilleur, "est aussi le-la meilleur-e de sa liste contenant", len(saFileAttente), "candidat-e-s du type", meilleur['type'])
        meilleur_de_sa_liste = saFileAttente.pop()

        # ajout du meilleur candidat à l'ordre d'appel
        ordreAppel.append(meilleur)
        nbAppeles += 1
        affiche("  On ajoute le meilleur", meilleur, "à l'ordre d'appel, c'est le-la", nbAppeles, "ème à être appelé-e.")

        if estBoursier(meilleur):
            nbBoursiersAppeles += 1
            affiche("    En plus, c'est le-la", nbBoursiersAppeles, "ème boursier-e à être appelé-e.")
        if estResident(meilleur):
            nbResidentsAppeles += 1
            affiche("    En plus, c'est le-la", nbResidentsAppeles, "ème résident-e à être appelé-e.")

    # fin de la boucle while
    affiche("\n3. On a terminé la boucle, on a rempli l'ordre d'appel.")
    return ordreAppel


# ### Exemple (A1)
# 
# Avec les valeurs prisent ci-dessus comme exemple :

# In[14]:


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

# In[15]:


from IPython.display import display
from ipywidgets import interact


# On définit la fonction que l'on souhaite explorer :

# In[16]:


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
        return res

    return fonctionATester


# Par exemple, si on demande $90%$ de boursiers, on voit que les candidats classés 6ème (Florian) et 7ème (Guillaume) sont mis en avant.

# In[17]:


fait_fonctionATester(voeuxClasses)(90, 0)


# Mais la visualisation interactive suivante permet de suivre l'influence des deux paramètres sur la liste des rangs finaux beaucoup plus facilement.

# In[18]:


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

# In[19]:


C1 = { "type": NonBoursierNonResident, "rang": 1 }
C2 = { "type": NonBoursierNonResident, "rang": 2 }
C3 = { "type": NonBoursierNonResident, "rang": 3 }
C4 = { "type": NonBoursierNonResident, "rang": 4 }
C5 = { "type": NonBoursierNonResident, "rang": 5 }
B6 = { "type": BoursierNonResident,    "rang": 6 }
C7 = { "type": NonBoursierNonResident, "rang": 7 }
C8 = { "type": NonBoursierNonResident, "rang": 8 }


# In[20]:


voeuxClasses_A2 = [C1, C2, C3, C4, C5, B6, C7, C8]


# On reproduit l'exemple du document de référence, avant de vous laisser explorer l'influence des deux taux.

# In[21]:


fait_fonctionATester(voeuxClasses_A2)(2, 0)


# In[22]:


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

# In[23]:


fait_fonctionATester(voeuxClasses_A2)(0, 0)


# #### A4 : 10% de boursiers-ères
# 
# Comme dans le document de référence : C1 B2 B3 C4 C5 C6 C7 B8 C9 C10, où B2 B3 et B8 sont boursiers et tous sont non résidents.

# In[24]:


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


# In[25]:


voeuxClasses_A4 = [C1, B2, B3, C4, C5, C6, C7, B8, C9, C10]


# On reproduit l'exemple du document de référence, avant de vous laisser explorer l'influence des deux taux.

# In[26]:


fait_fonctionATester(voeuxClasses_A4)(10, 0)


# In[27]:


interact(
    fait_fonctionATester(
        voeuxClasses_A4, tauxMinBoursiersPourcents=10, tauxMinResidentsPourcents=0
    ),
    tauxMinBoursiersPourcents=(0, 100, 1),
    tauxMinResidentsPourcents=(0, 100, 1)
);


# ### Visualisations colorées
# On va utiliser [ipythonblocks](http://www.ipythonblocks.org/).

# In[28]:


from ipythonblocks import BlockGrid


# In[29]:


couleursTypeCandidat = {
    NonBoursierNonResident: (200, 200, 200),  # gris
    NonBoursierResident:    (0, 0, 200),      # bleu
    BoursierNonResident:    (200, 0, 0),      # rouge
    BoursierResident:       (200, 0, 200),    # violet
}


# In[30]:


def voirListeVoeu(voeuxClasses):
    nbVoeux = len(voeuxClasses)
    grille = BlockGrid(nbVoeux, 1, fill=(200, 200, 200))
    for i, voeu in enumerate(voeuxClasses):
        typeCandidat = voeu["type"]
        couleur = couleursTypeCandidat[typeCandidat]
        grille[0, i].set_colors(*couleur)
    return grille


# In[31]:


voeuxClasses_A4


# In[32]:


voirListeVoeu(voeuxClasses_A2)


# In[33]:


voirListeVoeu(voeuxClasses_A4)


# Les candidats-ates boursiers-ères sont en rouges. On peut visualiser que le calcul de l'ordre d'appel va faire remonter un-e candidat-e boursier-ère :

# In[34]:


voirListeVoeu(calculerOrdreAppel(voeuxClasses_A2, 20, 20, False))


# In[35]:


voirListeVoeu(calculerOrdreAppel(voeuxClasses_A4, 20, 20, False))


# ### Entrée aléatoire
# 
# Pour des exemples plus complets, on génère ici une liste de vœux de taille fixée, où chaque vœu sera aléatoirement boursier ou non, résident ou non.
# Cela va permettre de mieux comprendre l'algorithme sur des entrées de taille plus grande.

# In[36]:


import random
import math


# In[62]:


def fait_voeuxClasses_aleatoire(
    taille=100,
    tauxBoursiers=20,
    tauxResidents=20,
    random_seed=0,
):
    random.seed(random_seed)
    # on commence par avoir une liste triée de non boursier non résident
    voeuxClasses = [
        {'type': NonBoursierNonResident, 'rang': i}
        for i in range(1, taille + 1)
    ]
    # pour certains candidats aléatoires on les transforme en boursier et/ou en résident
    nbBoursiers = int(math.ceil(taille * tauxBoursiers / 100.0))
    for voeu in random.sample(voeuxClasses, nbBoursiers):
        voeu['type'] = BoursierNonResident
    nbResidents = int(math.ceil(taille * tauxResidents / 100.0))
    for voeu in random.sample(voeuxClasses, nbResidents):
        if estBoursier(voeu): voeu['type'] = BoursierResident
        else: voeu['type'] = NonBoursierResident
    # on la mélange enfin et on la renvoie
    random.shuffle(voeuxClasses)
    return voeuxClasses


# In[63]:


voeuxClasses_exemple = fait_voeuxClasses_aleatoire(
    70,
    tauxBoursiers=20,  # ~14 boursiers
    tauxResidents=20   # ~14 résidents
)


# On va avoir en moyenne 14 boursiers-ères et 14 résidents-entes, avec quelques intersections.

# In[64]:


voirListeVoeu(voeuxClasses_exemple)


# In[65]:


voeuxClasses_exemple_sortie = calculerOrdreAppel(
    voeuxClasses_exemple,
    tauxMinBoursiersPourcents=100,
    tauxMinResidentsPourcents=100,
    afficheTout=False
)


# In[66]:


voirListeVoeu(voeuxClasses_exemple_sortie)


# On visualise assez bien : avec une contrainte un peu folle qui impose de prendre 100% des boursiers-ères (en rouge ou violet) et 100% des résidents (en bleu ou violet), l'algorithme d'appel a d'abord pris les candidats de types `BoursierResident` (violet), puis `BoursierNonResident` (rouge) car le décret officiel demande de favoriser les boursiers, puis les `NonBoursierResident` (bleu) et enfin les autres.

# ### Une visualisation interactive plus complète

# On peut combiner la visualisation interactive et la visualisation avec des couleurs.
# On va d'abord avoir une 

# In[67]:


def fait_fonctionATester_couleurs(
    taille=70,
    tauxBoursiers=20,
    tauxResidents=20,
    random_seed=0,
    tauxMinBoursiersPourcents=10,
    tauxMinResidentsPourcents=0
):
    def fonctionATester(
        taille=taille,
        tauxBoursiers=tauxBoursiers,
        tauxResidents=tauxResidents,
        random_seed=random_seed,
        tauxMinBoursiersPourcents=tauxMinBoursiersPourcents,
        tauxMinResidentsPourcents=tauxMinResidentsPourcents
    ):
        voeuxClasses = fait_voeuxClasses_aleatoire(
            taille,
            tauxBoursiers=tauxBoursiers,
            tauxResidents=tauxResidents,
            random_seed=random_seed
        )
        print("Visualisation de l'algorithme de calcul de l'ordre d'appel.")
        print("1. Vœux non triés par rang :")
        display(voirListeVoeu(voeuxClasses))
        print("2. Vœux triés par rang, mais pas par l'algorithme :")
        voeuxClasses_tries = sorted(voeuxClasses, key=lambda voeu: -voeu["rang"])
        display(voirListeVoeu(voeuxClasses_tries))
        print("3. Vœux triés par l'algorithme :")
        ordreAppel = calculerOrdreAppel(
            voeuxClasses,
            tauxMinBoursiersPourcents,
            tauxMinResidentsPourcents,
            afficheTout=False  # on cache la sortie
        )
        display(voirListeVoeu(ordreAppel))

    return fonctionATester


# In[68]:


interact(
    fait_fonctionATester_couleurs(
        taille=70,
        tauxBoursiers=20,
        tauxResidents=20,
        random_seed=0,
        tauxMinBoursiersPourcents=10,
        tauxMinResidentsPourcents=0
    ),
    taille=(1, 500, 1),
    tauxBoursiers=(0, 100, 1),
    tauxResidents=(0, 100, 1),
    random_seed=(0, 1000, 1),
    tauxMinBoursiersPourcents=(0, 100, 1),
    tauxMinResidentsPourcents=(0, 100, 1)
);


# ### Focalisation sur un candidat
# 
# Jusqu'ici on a visualisé l'ordre d'appel de toute la liste.
# On va se focaliser sur un seul candidat pour voir l'influence du comportement de tous les paramètres sur son ordre d'appel final.

# In[114]:


def voirListeVoeu_avecFocus(voeuxClasses, randDuFocus):
    grille = voirListeVoeu(voeuxClasses)
    for i, voeu in enumerate(voeuxClasses):
        if voeu['rang'] != randDuFocus:
            r, g, b = grille[0, i].rgb
            grille[0, i].rgb = (max(0, int(r*0.65)), max(0, int(g*0.65)), max(0, int(b*0.65)))
    return grille


# In[115]:


def fait_fonctionATester_unSeulFocus(
    taille=70,
    tauxBoursiers=20,
    tauxResidents=20,
    random_seed=0,
    rangDuFocus=1,
    focusEstBoursier=False,
    focusEstResident=False,
    tauxMinBoursiersPourcents=10,
    tauxMinResidentsPourcents=0
):
    def fonctionATester(
        taille=taille,
        tauxBoursiers=tauxBoursiers,
        tauxResidents=tauxResidents,
        random_seed=random_seed,
        rangDuFocus=1,
        focusEstBoursier=False,
        focusEstResident=False,
        tauxMinBoursiersPourcents=tauxMinBoursiersPourcents,
        tauxMinResidentsPourcents=tauxMinResidentsPourcents
    ):
        voeuxClasses = fait_voeuxClasses_aleatoire(
            taille,
            tauxBoursiers=tauxBoursiers,
            tauxResidents=tauxResidents,
            random_seed=random_seed
        )
        for voeu in voeuxClasses:
            if voeu['rang'] == rangDuFocus:
                if focusEstBoursier and focusEstResident:
                    voeu['type'] = BoursierResident
                elif focusEstBoursier and not focusEstResident:
                    voeu['type'] = BoursierNonResident
                elif not focusEstBoursier and focusEstResident:
                    voeu['type'] = NonBoursierResident
                else:
                    voeu['type'] = NonBoursierNonResident
        print("Visualisation de l'algorithme de calcul de l'ordre d'appel.")
        print("1. Vœux non triés par rang :")
        display(voirListeVoeu_avecFocus(voeuxClasses, rangDuFocus))
        print("2. Vœux triés par rang, mais pas par l'algorithme :")
        voeuxClasses_tries = sorted(voeuxClasses, key=lambda voeu: voeu["rang"])
        display(voirListeVoeu_avecFocus(voeuxClasses_tries, rangDuFocus))
        print("3. Vœux triés par l'algorithme :")
        ordreAppel = calculerOrdreAppel(
            voeuxClasses,
            tauxMinBoursiersPourcents,
            tauxMinResidentsPourcents,
            afficheTout=False  # on cache la sortie
        )
        display(voirListeVoeu_avecFocus(ordreAppel, rangDuFocus))

    return fonctionATester


# In[116]:


# https://ipywidgets.readthedocs.io/en/latest/examples/Using%20Interact.html#Arguments-that-are-dependent-on-each-other
import ipywidgets
taille_widget = ipywidgets.IntSlider(min=1, max=200, step=1, value=10)
rang_widget = ipywidgets.IntSlider(min=1, max=200, step=1, value=1)

def update_taille_max(*args):
    rang_widget.max = taille_widget.value
rang_widget.observe(update_taille_max, 'value')


# In[117]:


interact(
    fait_fonctionATester_unSeulFocus(
        taille=70,
        tauxBoursiers=20,
        tauxResidents=20,
        random_seed=0,
        rangDuFocus=1,
        focusEstBoursier=False,
        focusEstResident=False,
        tauxMinBoursiersPourcents=10,
        tauxMinResidentsPourcents=0
    ),
    taille=taille_widget,
    tauxBoursiers=(0, 100, 1),
    tauxResidents=(0, 100, 1),
    random_seed=(0, 1000, 1),
    rangDuFocus=rang_widget,
    focusEstBoursier=False,
    focusEstResident=False,
    tauxMinBoursiersPourcents=(0, 100, 1),
    tauxMinResidentsPourcents=(0, 100, 1)
);


# ----
# ## Algorithme 2 : Calcul des propositions

# In[73]:


from IPython.display import HTML


# In[74]:


HTML("<center><span style='color:red; font-size: xx-large;'>{}</span></center>".format('TODO '*54))


# ## Conclusion
# 
# Ce petit notebook n'est pas terminé, c'est un test *en cours de rédaction*.
