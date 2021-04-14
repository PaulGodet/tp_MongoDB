from sqlite3 import Date
from pymongo import MongoClient

if __name__ == '__main__':
    client = MongoClient('mongodb://127.0.0.1:27017/')

tpDB = client['hypermarche']
Produit = tpDB['Produit']
Commande = tpDB['Commande']
InventaireProduit = tpDB['InventaireProduit']
Caisse = tpDB['Caisse']


inventaireProduit1 = {"_id": "1", "nom": "oeuf", "nbr_stock": 14}
inventaireProduit2 = {"_id": "2", "nom": "fromage", "nbr_stock": 2}
inventaireProduit3 = {"_id": "3", "nom": "saumon", "nbr_stock": 4}
inventaireProduit4 = {"_id": "4", "nom": "lait", "nbr_stock": 0}
inventaireProduit5 = {"_id": "5", "nom": "baguette", "nbr_stock": 21}
inventaireProduit6 = {"_id": "6", "nom": "beurre", "nbr_stock": 3}
inventaireProduit7 = {"_id": "7", "nom": "confiture", "nbr_stock": 5}

produit1 = {"_id": "1", "nom": "oeuf", "description": "produitfrais", "quantite": inventaireProduit1}
produit2 = {"_id": "2", "nom": "fromage", "description": "produitlaitier", "quantite": inventaireProduit2}
produit3 = {"_id": "3", "nom": "saumon", "description": "produitmarin", "quantite": inventaireProduit3}
produit4 = {"_id": "4", "nom": "lait", "description": "produitlaitier", "quantite": inventaireProduit4}
produit5 = {"_id": "5", "nom": "baguette", "description": "produitfrais", "quantite": inventaireProduit5}
produit6 = {"_id": "6", "nom": "beurre", "description": "produitlaitier", "quantite": inventaireProduit6}
produit7 = {"_id": "7", "nom": "confiture", "description": "produitconserve", "quantite": inventaireProduit7}

commande1 = {"_id": "1", "contenu": [produit1, produit2], "date": "13/04/2021"}
commande2 = {"_id": "2", "contenu": [produit4, produit7], "date": "13/04/2021"}
commande3 = {"_id": "3", "contenu": [produit5, produit5], "date": "13/04/2021"}
commande4 = {"_id": "4", "contenu": [produit2, produit4], "date": "14/04/2021"}

caisse1 = {"_id": "1", "commande": [commande1, commande4]}
caisse2 = {"_id": "2", "commande": [commande2, commande3]}


"""x1=InventaireProduit.insert_one(inventaireProduit1)
x2=InventaireProduit.insert_one(inventaireProduit2)
x3=InventaireProduit.insert_one(inventaireProduit3)
x4=InventaireProduit.insert_one(inventaireProduit4)
x5=InventaireProduit.insert_one(inventaireProduit5)
x6=InventaireProduit.insert_one(inventaireProduit6)
x7=InventaireProduit.insert_one(inventaireProduit7)
print(x1)
print(x2)
print(x3)
print(x4)
print(x5)
print(x6)
print(x7)"""

""""#x=produit.insert_one(produit1)
x1=Produit.insert_one(produit1)
x2=Produit.insert_one(produit2)
x3=Produit.insert_one(produit3)
x4=Produit.insert_one(produit4)
x5=Produit.insert_one(produit5)
x6=Produit.insert_one(produit6)
x7=Produit.insert_one(produit7)
print(x1)
print(x2)
print(x3)
print(x4)
print(x5)
print(x6)
print(x7)"""

"""x1=Commande.insert_one(commande1)
x2=Commande.insert_one(commande2)
x3=Commande.insert_one(commande3)
x4=Commande.insert_one(commande4)
print(x1)
print(x2)
print(x3)
print(x4)"""

"""x1 = Caisse.insert_one(caisse1)
x2 = Caisse.insert_one(caisse2)
print(x1)
print(x2)"""







