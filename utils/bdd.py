import duckdb
from datetime import datetime

def insert_events(images_dict, db_path="./captcha.duckdb"):
    # Connexion à la base (crée le fichier si inexistant)
    con = duckdb.connect(db_path)

    # --- Créer la table si elle n'existe pas ---
    con.execute("""
    CREATE TABLE IF NOT EXISTS captcha_event (
        image_name VARCHAR PRIMARY KEY,
        display_count INT,
        selected_count INT,
    );
    """)

    # --- Insertion des images affichées ---
    for img, state in images_dict.items():
        select = con.execute("SELECT display_count, selected_count FROM captcha_event WHERE image_name = ?", [img]).fetchone()
        if select is None:
            con.execute("""
                INSERT INTO captcha_event (image_name, display_count, selected_count) VALUES (?, ?, ?)
                """, (img, 1, state)
            )
        else :
            display_count = select[0] + 1
            selected_count = select[1] + state
            con.execute(
                "UPDATE captcha_event SET display_count = ?, selected_count = ? WHERE image_name = ?",
                [display_count, selected_count, img]
            )

    con.close()
    print("Insertion dans la DB terminée.")

def get_display_count(db_path="./captcha.duckdb"):
    con = duckdb.connect(db_path)

    # --- Créer la table si elle n'existe pas ---
    con.execute("""
    CREATE TABLE IF NOT EXISTS captcha_event (
        image_name VARCHAR PRIMARY KEY,
        display_count INT,
        selected_count INT,
    );
    """)

    select = con.execute("SELECT image_name, display_count FROM captcha_event").fetchall()

    return(select)

