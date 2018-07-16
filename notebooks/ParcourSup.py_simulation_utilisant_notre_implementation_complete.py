
# coding: utf-8

# # Table of Contents
#  <p><div class="lev1 toc-item"><a href="#ParcourSup.py-:-simulation-utilisant-notre-implémentation-complète" data-toc-modified-id="ParcourSup.py-:-simulation-utilisant-notre-implémentation-complète-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>ParcourSup.py : simulation utilisant notre implémentation complète</a></div><div class="lev2 toc-item"><a href="#Version-de-Python-et-importation-de-notre-implémentation" data-toc-modified-id="Version-de-Python-et-importation-de-notre-implémentation-11"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Version de Python et importation de notre implémentation</a></div><div class="lev2 toc-item"><a href="#Contenu-de-notre-implémentation" data-toc-modified-id="Contenu-de-notre-implémentation-12"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Contenu de notre implémentation</a></div><div class="lev2 toc-item"><a href="#ordreappel" data-toc-modified-id="ordreappel-13"><span class="toc-item-num">1.3&nbsp;&nbsp;</span><code>ordreappel</code></a></div><div class="lev2 toc-item"><a href="#propositions" data-toc-modified-id="propositions-14"><span class="toc-item-num">1.4&nbsp;&nbsp;</span><code>propositions</code></a></div><div class="lev2 toc-item"><a href="#Conclusion" data-toc-modified-id="Conclusion-15"><span class="toc-item-num">1.5&nbsp;&nbsp;</span>Conclusion</a></div>

# # ParcourSup.py : simulation utilisant notre implémentation complète
# 
# > - Pour plus de détails, voir [le projet sur GitHub](https://github.com/Naereen/ParcourSup.py/).
# > - Auteur(s) : Lilian Besson.
# > - Date : Juillet 2018.
# > - Licence : [MIT](https://lbesson.mit-license.org/)

# ## Version de Python et importation de notre implémentation

# In[6]:


get_ipython().run_line_magic('load_ext', 'watermark')
get_ipython().run_line_magic('watermark', '-v -m -a "Lilian Besson et al, (c) 2018"')


# Il suffit de tricher un peu sur le `path` pour ajouter [le dossier racine de ce projet](https://github.com/Naereen/ParcourSup.py/tree/master/).

# In[4]:


import sys
sys.path.insert(0, "..")
print("Path :", sys.path)


# Et ensuite, le module [`parcoursup`](https://github.com/Naereen/ParcourSup.py/tree/master/parcoursup) est accessible, ainsi que tous ces sous-modules.

# In[7]:


import parcoursup


# ## Contenu de notre implémentation

# In[10]:


get_ipython().system('ls ../parcoursup/**/*.py')


# In[8]:


print("Contenu de 'parcoursup' :", dir(parcoursup))


# In[9]:


import parcoursup.ordreappel
print("Contenu de 'parcoursup' :", dir(parcoursup.ordreappel))

import parcoursup.propositions
print("Contenu de 'parcoursup' :", dir(parcoursup.propositions))


# ## `ordreappel`

# In[12]:


import parcoursup.ordreappel.AlgoOrdreAppel
print("Contenu de parcoursup.ordreappel.AlgoOrdreAppel :", dir(parcoursup.ordreappel.AlgoOrdreAppel))


# In[13]:


import parcoursup.ordreappel.GroupeClassement
print("Contenu de parcoursup.ordreappel.GroupeClassement :", dir(parcoursup.ordreappel.GroupeClassement))


# In[14]:


import parcoursup.ordreappel.OrdreAppel
print("Contenu de parcoursup.ordreappel.OrdreAppel :", dir(parcoursup.ordreappel.OrdreAppel))


# In[15]:


import parcoursup.ordreappel.VoeuClasse
print("Contenu de parcoursup.ordreappel.VoeuClasse :", dir(parcoursup.ordreappel.VoeuClasse))


# ## `propositions`

# In[16]:


import parcoursup.propositions.AlgoPropositions
print("Contenu de parcoursup.propositions.AlgoPropositions :", dir(parcoursup.propositions.AlgoPropositions))


# In[17]:


import parcoursup.propositions.Candidat
print("Contenu de parcoursup.propositions.Candidat :", dir(parcoursup.propositions.Candidat))


# In[18]:


import parcoursup.propositions.Etablissement
print("Contenu de parcoursup.propositions.Etablissement :", dir(parcoursup.propositions.Etablissement))


# In[19]:


import parcoursup.propositions.exemples
print("Contenu de parcoursup.propositions.exemples :", dir(parcoursup.propositions.exemples))


# In[20]:


import parcoursup.propositions.GroupeAffectation
print("Contenu de parcoursup.propositions.GroupeAffectation :", dir(parcoursup.propositions.GroupeAffectation))


# In[21]:


import parcoursup.propositions.GroupeAffectationUID
print("Contenu de parcoursup.propositions.GroupeAffectationUID :", dir(parcoursup.propositions.GroupeAffectationUID))


# In[22]:


import parcoursup.propositions.GroupeInternat
print("Contenu de parcoursup.propositions.GroupeInternat :", dir(parcoursup.propositions.GroupeInternat))


# In[23]:


import parcoursup.propositions.GroupeInternatUID
print("Contenu de parcoursup.propositions.GroupeInternatUID :", dir(parcoursup.propositions.GroupeInternatUID))


# In[24]:


import parcoursup.propositions.VerificationsResultats
print("Contenu de parcoursup.propositions.VerificationsResultats :", dir(parcoursup.propositions.VerificationsResultats))


# In[25]:


import parcoursup.propositions.VoeuEnAttente
print("Contenu de parcoursup.propositions.VoeuEnAttente :", dir(parcoursup.propositions.VoeuEnAttente))


# In[26]:


import parcoursup.propositions.VoeuUID
print("Contenu de parcoursup.propositions.VoeuUID :", dir(parcoursup.propositions.VoeuUID))


# ## Conclusion
# 
# Ce petit notebook n'est pas terminé, c'est un test *en cours de rédaction*.
