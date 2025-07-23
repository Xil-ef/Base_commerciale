import sqlite3
from faker import Faker
import random
from datetime import datetime, timedelta

# Initialisation
fake = Faker()
conn = sqlite3.connect("base_commerciale.db")
cur = conn.cursor()

# Création des tables
cur.execute("""
CREATE TABLE IF NOT EXISTS Clients (
    client_id INTEGER PRIMARY KEY,
    nom TEXT,
    pays TEXT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS Produits (
    produit_id INTEGER PRIMARY KEY,
    nom_produit TEXT,
    categorie TEXT,
    prix_unitaire REAL
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS Commandes (
    commande_id INTEGER PRIMARY KEY,
    client_id INTEGER,
    date_commande DATE,
    total REAL
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS DetailsCommande (
    detail_id INTEGER PRIMARY KEY,
    commande_id INTEGER,
    produit_id INTEGER,
    quantite INTEGER,
    prix_vente_unitaire REAL
)
""")

# Insertion Clients
clients = []
for _ in range(50):
    nom = fake.name()
    pays = fake.country()
    cur.execute("INSERT INTO Clients (nom, pays) VALUES (?, ?)", (nom, pays))
    clients.append(cur.lastrowid)

# Insertion Produits
categories = ["Électronique", "Maison", "Sport", "Vêtements", "Jouets"]
produits = []
for _ in range(50):
    nom = fake.word().capitalize() + " " + fake.word().capitalize()
    categorie = random.choice(categories)
    prix = round(random.uniform(5, 500), 2)
    cur.execute("INSERT INTO Produits (nom_produit, categorie, prix_unitaire) VALUES (?, ?, ?)", (nom, categorie, prix))
    produits.append((cur.lastrowid, prix))

# Insertion Commandes
commandes = []
for _ in range(50):
    client_id = random.choice(clients)
    date_cmd = fake.date_between(start_date='-1y', end_date='today')
    total = 0  # Calculé plus tard avec les détails
    cur.execute("INSERT INTO Commandes (client_id, date_commande, total) VALUES (?, ?, ?)", (client_id, date_cmd, total))
    commandes.append(cur.lastrowid)

# Insertion DetailsCommande + mise à jour des totaux
for commande_id in commandes:
    total_commande = 0
    nb_lignes = random.randint(1, 5)
    produits_choisis = random.sample(produits, nb_lignes)
    for produit_id, prix_unitaire in produits_choisis:
        quantite = random.randint(1, 10)
        prix_vente_unitaire = round(prix_unitaire * random.uniform(0.9, 1.2), 2)
        total_ligne = quantite * prix_vente_unitaire
        total_commande += total_ligne
        cur.execute("""
            INSERT INTO DetailsCommande (commande_id, produit_id, quantite, prix_vente_unitaire)
            VALUES (?, ?, ?, ?)
        """, (commande_id, produit_id, quantite, prix_vente_unitaire))
    
    # Mise à jour du total dans la commande
    cur.execute("UPDATE Commandes SET total = ? WHERE commande_id = ?", (round(total_commande, 2), commande_id))

# Sauvegarde et fermeture
conn.commit()
conn.close()

print("Base de données créée avec succès avec 50 insertions par table.")
