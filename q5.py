import numpy
import cv2
import glob

test = glob.glob('./Images/oiseau/*.png')

for i, image in enumerate(test) :
    img = cv2.imread(image)
    sortie = cv2.resize(img, dsize = [150,150])
    cv2.imwrite(f"./Images/oiseau/resize/fichier_{i:03}_resize.png", sortie)
    