import datetime

date ="2333-03-4"
#date1 ="2003-5-8"
annee, mois, jour = date.split("-")
#annee1, mois1, jour1 = date1.split("-")
#print(annee, mois, jour)

nouvelleDate = datetime.date(int(annee), int(mois), int(jour))
#ancienneDate = datetime.date(int(annee1), int(mois1), int(jour1))
delta = nouvelleDate - datetime.date.today()

print(delta.days)
print(datetime.date.today())


# from datetime import datetime, timedelta

# date1 = datetime(2020, 1, 1)
# date2 = datetime(2026, 2, 15)

# delta = date2 - date1
# print(delta)
