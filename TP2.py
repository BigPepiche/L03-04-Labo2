"""
TP2 : Système de gestion de livres pour une bibliothèque

Groupe de laboratoire : L03
Numéro d'équipe :  04
Noms et matricules : Reginald Rancy (2393346), Zakaria Soudaki (2394358)
"""

import csv
from datetime import datetime , date
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



print(f' \n Bibliotheque initiale : {bibliotheque} \n')


########################################################################################################## 
# PARTIE 2 : Ajout d'une nouvelle collection à la bibliothèque
########################################################################################################## 

# TODO : Écrire votre code ici
file = open("nouvelle_collection.csv", "r")
r = csv.reader(file)

for livre in r:
   titre = livre[0]
   auteur = livre[1]
   date_publication = livre[2]
   clée = livre[3]
   
   if  clée in bibliotheque :
       print("Le livre "+clée+" ---- "+titre+" par "+auteur+" ---- est déjà présent dans la bibliothèque")
   elif clée != "cote_rangement":
       renseignements = {
            "titre":titre,
            "auteur":auteur,
            "date_publication":date_publication
            
        }
       bibliotheque[clée] = renseignements
       print("Le livre "+clée+" ---- "+titre+" par "+auteur+" ---- a été ajouté avec succès")


########################################################################################################## 
# PARTIE 3 : Modification de la cote de rangement d'une sélection de livres
########################################################################################################## 

# TODO : Écrire votre code ici
anciennes_clees = []
for livre in bibliotheque:
    if (bibliotheque.get(livre)).get("auteur") == "William Shakespeare":
        anciennes_clees.append(livre)

for clee in anciennes_clees:
    bibliotheque.update({"W"+clee:bibliotheque.get(clee)})
    bibliotheque.pop(clee)

print(f' \n Bibliotheque avec modifications de cote : {bibliotheque} \n')


########################################################################################################## 
# PARTIE 4 : Emprunts et retours de livres
########################################################################################################## 

# TODO : Écrire votre code ici

dates = open("emprunts.csv", "r")
r = csv.reader(dates)


clées = []

for livre in r:
   
    clée = livre[0]
    #if clée in bibliotheque :
    if clée != "cote_rangement":
        bibliotheque[clée]["emprunts"] = "emprunté"
        bibliotheque[clée]["date_emprunt"] = livre[1]
        clées.append(clée)
 
#clées.remove("cote_rangement")


for  i in bibliotheque :
    if i not in clées :
         bibliotheque[i]["emprunts"] = "disponible"

print(f' \n Bibliotheque avec ajout des emprunts : {bibliotheque} \n')
    

########################################################################################################## 
# PARTIE 5 : Livres en retard 
########################################################################################################## 

# TODO : Écrire votre code ici

for  i in clées :
    date1 = bibliotheque[i]["date_emprunt"]
    
    annee, mois, jours = date1.split("-")
    date2 = date(int(annee), int(mois), int(jours))
    delta = date.today() - date2
    jours_de_retard = delta.days - 30
    #print(delta.days)

    if jours_de_retard >=50:bibliotheque[i]["frais_retard"] = 100
    elif jours_de_retard>0:bibliotheque[i]["frais_retard"] =2*(jours_de_retard)
    else: bibliotheque[i]["frais_retard"] =0

    if delta.days >= 365: bibliotheque[i]["livre_perdu"] = True
    else: bibliotheque[i]["livre_perdu"] = False

print(f' \n Bibliotheque avec ajout des retards et frais : {bibliotheque} \n')


