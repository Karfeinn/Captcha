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

dict_img = {
    ((0,0),(150,150)):"img 1",((151,0),(300,150)):"img 2",((301,0),(450,150)):"img 3",
    ((0,151),(150,300)):"img 4",((151,151),(300,300)):"img 5",((301,151),(450,300)):"img 6",
    ((0,301),(150,450)):"img 7",((151,301),(300,450)):"img 8",((301,301),(450,450)):"img 9"
    }

def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONUP:
        print(x,y)
        for coord in dict_img:
            if coord[0][0] < x < coord[1][0] and coord[0][1] < y < coord[1][1]:
                print(dict_img[coord])

cv2.namedWindow('CAPTCHA Grid')
cv2.setMouseCallback('CAPTCHA Grid',draw_circle)
cv2.imshow("CAPTCHA Grid", grid)
cv2.waitKey(0)
cv2.destroyAllWindows()
