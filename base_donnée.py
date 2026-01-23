# Création de la base et insertion de 2 lignes
import duckdb

# Connexion (crée le fichier si inexistant)
con = duckdb.connect("captcha.duckdb")

# Création de la table
con.execute("""
CREATE TABLE IF NOT EXISTS captcha_event (
    id INTEGER,
    image_name VARCHAR,
    action VARCHAR
);
""")

# Insertion de 2 lignes
con.execute("""
INSERT INTO captcha_event (id, image_name, action) VALUES
    (1, 'image1.png', 'shown'),
    (2, 'image2.png', 'selected');
""")

con.close()


#Connexion et lecture de la base de données

import duckdb

# Reconnexion à la base existante
con = duckdb.connect("captcha.duckdb")

# Lecture des données
result = con.execute("SELECT * FROM captcha_event").fetchall()

print("Contenu de la table captcha_event :")
print(result)

con.close()
