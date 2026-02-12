import cv2
import glob
import numpy as np
import random
import utils.bdd as bdd
import os

def choose_images(filepath:str, nb_col:int, nb_row:int, ponderation) -> list:
    """
    A function that create a list of nb_row*nb_col images
    
    :param filepath: file path where images are stored
    :type filepath: str
    
    :param nb_col: number of column in the final grid
    :type nb_col: int
    
    :param nb_row: number of row in the final grid
    :type nb_row: int
    
    :return: a list of nb_row*nb_col images path
    :rtype: list
    """
    nb_images = nb_col * nb_row

    extensions = ["*.png", "*.jpg", "*.jpeg", "*.gif", "*.bmp", "*.webp"]
    # Take all images in the folder
    images = []
    for ext in extensions:
        images.extend(glob.glob(os.path.join(filepath, ext)))
    
    if not images:
        raise ValueError("No images found in the folder")
    if len(images) < nb_images:
        raise ValueError("Not enough images in the folder for the grid")
    
    weights = []
    for img in images:
        count = ponderation.get(img, 0)
        weight = 1 / (1 + count)
        weights.append(weight)

    # Select randomly nb_row*nb_col images
    selected_images = []
    available_images = images.copy()
    available_weights = weights.copy()

    for _ in range(nb_images):
        chosen = random.choices(
            available_images,
            weights=available_weights,
            k=1
        )[0]

        idx = available_images.index(chosen)
        selected_images.append(chosen)

        # Remove chosen image (no replacement)
        available_images.pop(idx)
        available_weights.pop(idx)

    return selected_images

def create_grid(images_list:list, nb_col:int, nb_row:int, img_size:int, images_dict:dict) -> None:
    """
    A function that display a grid with images inside we have to select images of birds
    
    :param images_list: List of images path to build the grid
    :type images_list: list
    """

    nb_images = nb_col * nb_row

    rng = shiny_image(nb_images)
    
    # Read images from images_list
    
    if rng :
        images = []
        for idx, img in enumerate(images_list):
            if idx == rng :
                image_shiny = cv2.resize(cv2.imread(img), dsize=[img_size, img_size])
                b, r, g = cv2.split((image_shiny))
                images.append(cv2.merge((r, g, b)))
            else :
                images.append(cv2.resize(cv2.imread(img), dsize=[img_size, img_size]))
    else :
        images = [cv2.resize(cv2.imread(img), dsize=[img_size, img_size]) for img in images_list]

    

    # Build the grid
    row_list = []
    for i in range(0, len(images), nb_col):
        row = np.hstack(images[i:i + nb_col])
        row_list.append(row)

    grid = np.vstack(row_list)

    coord_dict = create_coord_dict(images_list, nb_col, nb_row, img_size)
    params = {"grid": grid, "coord_dict":coord_dict, "images_dict":images_dict}
    # display grid
    cv2.namedWindow('CAPTCHA')
    cv2.setMouseCallback('CAPTCHA',clic_event, params)
    for coord in coord_dict:
        cv2.rectangle(grid, (coord[0][0] + 3 ,coord[0][1] + 3), (coord[1][0] - 3,coord[1][1] - 3), (255,255,255), 7)
    cv2.imshow("CAPTCHA", grid)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def create_coord_dict(images_list:list, nb_col:int, nb_row:int, img_size:int):
    coord_dict = {}
    for i in range(nb_row):
        for j in range(nb_col):
            coord_dict[((j*img_size, i*img_size),((j+1)*img_size,(i+1)*img_size))] = images_list[i*3+j]
    return coord_dict

def clic_event(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONUP:
        for coord in param["coord_dict"]:
            if coord[0][0] < x < coord[1][0] and coord[0][1] < y < coord[1][1]:
                if param["images_dict"][param["coord_dict"][coord]] == 0:
                    cv2.rectangle(param["grid"], (coord[0][0] + 5 ,coord[0][1] + 5), (coord[1][0] - 5,coord[1][1] - 5), (255,147,116), 5)
                    param["images_dict"][param["coord_dict"][coord]] = 1
                    cv2.imshow("CAPTCHA", param["grid"])
                    break
                elif param["images_dict"][param["coord_dict"][coord]] == 1:
                    cv2.rectangle(param["grid"], (coord[0][0] + 5 ,coord[0][1] + 5), (coord[1][0] - 5,coord[1][1] - 5), (255,255,255), 5)
                    param["images_dict"][param["coord_dict"][coord]] = 0
                    cv2.imshow("CAPTCHA", param["grid"])
                    break

def shiny_image(nb_max):
    rng = random.randint(0,nb_max*3)
    if rng <= nb_max :
        return rng
    return None


def captcha(filepath, nb_col, nb_row, img_size, ponderation):
    images_list = choose_images(filepath, nb_col, nb_row, ponderation)
    images_dict = {image:0 for image in images_list}
    create_grid(images_list, nb_col, nb_row, img_size, images_dict)
    bdd.insert_events(images_dict)

