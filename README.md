# Grille d’images type CAPTCHA

Ce projet permet d’afficher une grille d’images semblable à un CAPTCHA, générée automatiquement à partir d’un dossier d’images.

Dans cette grille l'objectif est de séléctionné les images d'oiseaux

Le script principal est main.py.

## Fonctionnement

Le fichier main.py :

charge des images depuis un dossier

sélectionne un ensemble d’images

les affiche sous forme de grille (type CAPTCHA)

## Personnalisation de la grille

La personnalisation se fait directement dans main.py grâce aux variables suivantes :

```python
filepath = "./images"  # Chemin vers le dossier contenant les images
nb_col = 3             # Nombre de colonnes de la grille
nb_row = 3             # Nombre de lignes de la grille
img_size = 150         # Taille des images (en pixels)
```

Détails des paramètres

filepath
Chemin vers le dossier contenant les images à afficher.

nb_col
Nombre de colonnes dans la grille.

nb_row
Nombre de lignes dans la grille.

img_size
Taille (largeur et hauteur) de chaque image en pixels.

Le nombre total d’images affichées est :

nb_col × nb_row

## Structure attendue

Exemple :

```
project/
├── main.py
├── images/
│   ├── img1.png
│   ├── img2.png
│   ├── img3.png
│   └── ...
```

## Exécution

```bash
python main.py
```

## Remarque

Assurez-vous que le dossier d’images contient au moins nb_col × nb_row images, sinon l’exécution échouera.