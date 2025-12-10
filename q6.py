import cv2
import glob
import numpy as np
import random

# Charger toutes les images disponibles
all_images = glob.glob("./Images/oiseau/resize/*.png")

# Séparer les images contenant "oiseau" à la fin du nom
oiseau_images = [img for img in all_images if img.endswith("oiseau.png")]
other_images = [img for img in all_images if img not in oiseau_images]

if not oiseau_images:
    raise ValueError("Aucune image avec 'oiseau' à la fin trouvée !")

# Sélectionner 8 images aléatoires parmi les autres
selected_images = random.sample(other_images, 8)

# Ajouter au moins 1 image avec "oiseau" à la fin
selected_images.append(random.choice(oiseau_images))

# Mélanger pour ne pas avoir l'image 'oiseau' toujours à la même position
random.shuffle(selected_images)

# Charger les images
images = [cv2.imread(img) for img in selected_images]

# Construire la grille (3 lignes, 3 colonnes)
row1 = np.hstack(images[0:3])
row2 = np.hstack(images[3:6])
row3 = np.hstack(images[6:9])

grid = np.vstack([row1, row2, row3])

# Affichage
cv2.imshow("CAPTCHA Grid", grid)
cv2.waitKey(0)
cv2.destroyAllWindows()
