def est_bissextile(annee):
    if annee%400==0 or annee%4==0 and annee%100!=0:
        bissextile=True
    else:
        bissextile=False
    return bissextile
annee=int(input("entrez une annee: "))
print(est_bissextile(annee))