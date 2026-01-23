import cv2
import glob
import numpy as np
import random
from base_donnée_captcha import insert_events 

filepath = "./out2"
nb_col = 3
nb_row = 3
img_size = 150

# Listes pour stocker les images affichées et cliquées
images_affichées = []
images_sélectionnées = []

def choose_images(filepath:str, nb_col:int, nb_row:int) -> list:
    nb_images = nb_col * nb_row
    images = glob.glob(filepath + "/*.png")
    
    if not images:
        raise ValueError("No images found in the folder")
    if len(images) < nb_images:
        raise ValueError("Not enough images in the folder for the grid")
    
    selected_images = random.sample(images, nb_images)
    return selected_images

def create_coord_dict(images_list:list, nb_col:int, nb_row:int, img_size:int):
    coord_dict = {}
    for i in range(nb_row):
        for j in range(nb_col):
            coord_dict[((j*img_size, i*img_size),((j+1)*img_size,(i+1)*img_size))] = images_list[i*nb_col+j]
    return coord_dict

def clic_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONUP:
        for coord in param["dict"]:
            if coord[0][0] < x < coord[1][0] and coord[0][1] < y < coord[1][1]:
                # Dessine le rectangle bleu sur l'image
                cv2.rectangle(param["grid"], (coord[0][0], coord[0][1]),
                              (coord[1][0], coord[1][1]), (255,0,0), 5)
                clicked_image = param["dict"][coord]
                print("Image cliquée :", clicked_image)
                # Ajouter à la liste des clics
                param["clicked"].append(clicked_image)
                cv2.imshow("CAPTCHA", param["grid"])
                break

def create_grid(images_list:list, nb_col:int, nb_row:int, img_size:int):
    # Stocker les images affichées
    images_affichées.extend(images_list)

    images = [cv2.imread(img) for img in images_list]

    # Construire la grille
    row_list = []
    for i in range(0, len(images), nb_col):
        row = np.hstack(images[i:i + nb_col])
        row_list.append(row)
    grid = np.vstack(row_list)

    coord_dict = create_coord_dict(images_list, nb_col, nb_row, img_size)
    params = {"grid": grid, "dict": coord_dict, "clicked": images_sélectionnées}

    # Afficher la grille et gérer les clics
    cv2.namedWindow('CAPTCHA')
    cv2.setMouseCallback('CAPTCHA', clic_event, params)
    cv2.imshow("CAPTCHA", grid)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# --- Exécution ---
images_list = choose_images(filepath, nb_col, nb_row)
create_grid(images_list, nb_col, nb_row, img_size)

# --- Insérer dans DuckDB ---
insert_events(images_affichées, images_sélectionnées)
