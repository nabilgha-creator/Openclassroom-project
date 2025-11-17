import requests

from bs4 import BeautifulSoup

url=(r"https://books.toscrape.com/")
response = requests.get(url)
page = response.text

soup= BeautifulSoup(page,"html.parser")
title = soup.title.string

data=[]

livres= soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3") 

for livre in livres: 
    titre_livre= livre.h3.a["title"]
    prix_livre= livre.find("p", class_="price_color").text
    prix_livre=prix_livre.replace("£", "").replace("Â", "")
    prix_livre=float(prix_livre)
    note= livre.find("p", class_="star-rating")["class"][1]
    dispo= livre.find("p", class_="instock availability").text.strip()
    dico={"titre": titre_livre , "prix": prix_livre, "note": note , "disponibilite": dispo}
    data.append(dico)

import csv
fieldnames=["titre", "prix" , "note" , "disponibilite"]
with open(r"C:\Users\Nabil\Desktop\Bootcamp python\test.csv", "w", newline="", encoding="utf-8") as test:
    writer=csv.DictWriter(test, fieldnames=fieldnames)

    writer.writeheader()
    for ligne in data:
        writer.writerow(ligne)





    