import cv2
import numpy as np
import glob


image_path = glob.glob('/home/astropapalia/Desktop/Fase 4 analisi/immagini/Nuova estensione/*.jpg')
image = []

cutted_directory = '/home/astropapalia/Desktop/Fase 4 analisi/immagini/Cutted images'
counter = 1

for image in image_path:
    #'/home/astropapalia/Desktop/Fase 4 analisi/immagini/image_013.jpg'
    img = cv2.imread(image)
    rows, cols, _ = img.shape
    print('Base:', cols)
    print('Height:', rows)
   
   
    # How do we want to resize images?
    # Insert the numbers of pixels for height (rows) and base (columns) we want to delete
    Height_cut = 199
    Base_cut = 182
   
    result_Base = cols - Base_cut
    result_Height = rows - Height_cut
    result_Total = result_Base, 'x', result_Height
   
    # Cut of image and saving
    cut_image = img[Height_cut: rows, Base_cut: cols]
    cv2.imwrite(f'{cutted_directory}/Cutted_image_{counter:03d}.jpg', cut_image)
    print('Done! Image cutted from ', cols, 'x', rows, ' to ', result_Total, ' and saved.')
    counter += 1



exit()
