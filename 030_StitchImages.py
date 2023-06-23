# This code is correct and able to stitching correctly two images considering keypoints.


import numpy as np
import cv2
import glob


image_paths = glob.glob('/home/astropapalia/Desktop/Fase 4 analisi/immagini/Cutted images/*.jpg')
images = []



for image in image_paths:
    img = cv2.imread(image)
    images.append(img)
    #cv2.imshow("Image", img)
    #cv2.waiKey(0)


imageStitcher = cv2.Stitcher_create()
error, stitched_img = imageStitcher.stitch(images)



if not error:
    cv2.imwrite('/home/astropapalia/Desktop/Fase 4 analisi/immagini/Stitching Images/Stitching_images_result_code.jpg', stitched_img)
    #cv2.imshow("Result", stitched_img)
    #cv2.waitKey(0)
    print("Well done! The Stitched Images has been save")

exit()
