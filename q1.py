import numpy
import cv2
import glob

test = glob.glob('../../../Téléchargements/images/**/*')

for i, image in enumerate(test) :
    img = cv2.imread(image)
    print(f'Traitement du fichier {image}')
    if img is None :
        print('lecture impossible')
    else :
        fichier_sortie = f"./Images/oiseau/fichier_{i:03}.png"
        valeur_sortie = cv2.imwrite(fichier_sortie, img)
        print(f'sauvegarde dans {fichier_sortie} : {valeur_sortie}')
