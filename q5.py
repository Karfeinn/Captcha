import numpy
import cv2
import glob
import os
import re

test = glob.glob('./out/*.png')

for i, image in enumerate(test) :
    img = cv2.imread(image)
    sortie = cv2.resize(img, dsize = [150,150])

    # extraction du nom de l'animal et ou decor 
    nom_fichier = os.path.basename(image)                
    nom_sans_ext = os.path.splitext(nom_fichier)[0]      
    # recupere l'animal d'après le nom du fichier
    animal = nom_sans_ext.split("_")[-1]

    
    fichier_sortie = f"./out2/image_{i:03}_{animal}.png"

    cv2.imwrite(fichier_sortie, sortie)
