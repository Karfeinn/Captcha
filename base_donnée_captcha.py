import duckdb
from datetime import datetime

def insert_events(images_affichées, images_sélectionnées, db_path="captcha.duckdb"):
    # Connexion à la base (crée le fichier si inexistant)
    con = duckdb.connect(db_path)

    # --- Créer la séquence si elle n'existe pas ---
    # Cette séquence permet d'obtenir un autoincrement non disponible sur duckdb
    con.execute("""
    CREATE SEQUENCE IF NOT EXISTS seq_captcha_event START 1;
    """)

    # --- Créer la table si elle n'existe pas ---
    con.execute("""
    CREATE TABLE IF NOT EXISTS captcha_event (
        id INTEGER PRIMARY KEY DEFAULT nextval('seq_captcha_event'),
        image_name VARCHAR,
        action VARCHAR,
        event_time TIMESTAMP
    );
    """)

    # --- Insertion des images affichées ---
    for img in images_affichées:
        con.execute("""
        INSERT INTO captcha_event (image_name, action, event_time) VALUES (?, ?, ?)
        """, (img, "affichée", datetime.now()))

    # --- Insertion des images cliquées ---
    for img in images_sélectionnées:
        con.execute("""
        INSERT INTO captcha_event (image_name, action, event_time) VALUES (?, ?, ?)
        """, (img, "sélectionnée", datetime.now()))

    con.close()
    print("Insertion dans la DB terminée.")
