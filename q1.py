import numpy
import cv2
import glob
import os
import re

test = glob.glob('./images_animaux/**/*', recursive=True)

for i, image in enumerate(test) :
    img = cv2.imread(image)
    print(f'Traitement du fichier {image}')
    if img is None :
        print('lecture impossible')
    else :
        # récupération du nom de l'animal ou décor 
        nom_fichier = os.path.basename(image)                     
        nom_sans_ext = os.path.splitext(nom_fichier)[0]           
        animal = re.sub(r'^\d+', '', nom_sans_ext)                

        # on met le nom de l'animal ou décor en nom de sortie
        fichier_sortie = f"./out/{animal}/image_{i:03}_{animal}.png"


        valeur_sortie = cv2.imwrite(fichier_sortie, img)
        print(f'sauvegarde dans {fichier_sortie} : {valeur_sortie}')
