"""
TP2 : Système de gestion de livres pour une bibliothèque

Groupe de laboratoire : L03
Numéro d'équipe :  04
Noms et matricules : Reginald Rancy (2393346), Zakaria Soudaki (matricule)
"""

import csv

########################################################################################################## 
# PARTIE 1 : Création du système de gestion et ajout de la collection actuelle
########################################################################################################## 

# TODO : Écrire votre code ici
fichier = open("collection_bibliotheque.csv", "r")
bibliotheque = {}
r = csv.reader(fichier)
for ligne in r:
    titre = ligne[0]
    auteur = ligne[1]
    date_publication = ligne[2]
    clée = ligne[3]
    renseignements = {
            "titre":titre,
            "auteur":auteur,
            "date_publication":date_publication
    }
    bibliotheque.update({clée:renseignements})
bibliotheque.pop("cote_rangement")









########################################################################################################## 
# PARTIE 2 : Ajout d'une nouvelle collection à la bibliothèque
########################################################################################################## 

# TODO : Écrire votre code ici






########################################################################################################## 
# PARTIE 3 : Modification de la cote de rangement d'une sélection de livres
########################################################################################################## 

# TODO : Écrire votre code ici







########################################################################################################## 
# PARTIE 4 : Emprunts et retours de livres
########################################################################################################## 

# TODO : Écrire votre code ici







########################################################################################################## 
# PARTIE 5 : Livres en retard 
########################################################################################################## 

# TODO : Écrire votre code ici






