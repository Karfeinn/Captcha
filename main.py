import utils.bdd as bdd
import utils.captcha as captcha

filepath = "./images"
nb_col = 3
nb_row = 3
img_size = 150

ponderation = dict(bdd.get_display_count())
captcha.captcha(filepath, nb_col, nb_row, img_size, ponderation)