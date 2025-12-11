import cv2
import glob
import numpy as np

images = [cv2.imread(f"./Images/oiseau/resize/fichier_00{i}_resize.png") for i in range(9)]

# Vérification
images = [img for img in images if img is not None]
if len(images) != 9:
    raise ValueError("9 images doivent être chargées !")

# Construire la grille (3 lignes, 3 colonnes)
row1 = np.hstack(images[0:3])
row2 = np.hstack(images[3:6])
row3 = np.hstack(images[6:9])

grid = np.vstack([row1, row2, row3])

def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONUP:
        print(x,y)

cv2.namedWindow('CAPTCHA Grid')
cv2.setMouseCallback('CAPTCHA Grid',draw_circle)
cv2.imshow("CAPTCHA Grid", grid)
cv2.waitKey(0)
cv2.destroyAllWindows()
