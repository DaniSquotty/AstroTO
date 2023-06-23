# This code is correct and calculate the numer of pixel of any image
# in given intensity ranges. For the calculation the image is converted in a grey scale 
# and considering the intensity of white color.

import numpy as np
import cv2

import glob
import os
from csv import writer

def count_pixels_in_range(image_path, lower_range, upper_range):
    # Load image in grey scale
    grayscale_image = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
   
    # Obtain image dimension
    height, width = grayscale_image.shape
   
    # Initialize pixel counter
    pixel_count = 0
   
    # Check all image pixels
    for y in range(height):
        for x in range(width):
            # Obtain number of pixels
            pixel_value = grayscale_image[y, x]
           
            # Check if the number of pixels respect the range
            if lower_range <= pixel_value <= upper_range:
                pixel_count += 1
   
    return pixel_count




def count_pixels_in_range_nero(image_path, lower_range_nero, upper_range_nero):
    # Load image in grey scale
    grayscale_image = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
   
    # Obtain image dimension
    height, width = grayscale_image.shape
   
    # Initialize pixel counter
    pixel_count_nero = 0
   
    # Check all image pixels
    for y in range(height):
        for x in range(width):
            # Obtain number of pixels
            pixel_value = grayscale_image[y, x]
           
            # Check if the number of pixels respect the range
            if lower_range_nero <= pixel_value <= upper_range_nero:
                pixel_count_nero += 1
   
    return pixel_count_nero




image_path = sorted(glob.glob('/home/astropapalia/Desktop/Fase 4 analisi/immagini/Stitching Images/EXACTLY/*.jpg'), key=os.path.getmtime)
images = []

lower_range = 200  # min white
upper_range = 255  # max white

lower_range_nero = 0  # min black
upper_range_nero = 5  # max black




with open('Number of pixel_result.csv', 'w', newline='') as f:
    data_writer = writer(f)
    data_writer.writerow(['total_pixel', 'region_pixel', 'black_pixel', 'white_pixel', 'glacier %', 'glacier km2'])
   
   
    for image in image_path:
       
        img = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
        height, width = img.shape
        total_pixel = height * width
       
        result_nero = count_pixels_in_range_nero(image_path, lower_range_nero, upper_range_nero)
        result = count_pixels_in_range(image_path, lower_range, upper_range)
       
        # Calcolo dei valori %
        pixel_area_geografica = total_pixel - result_nero
        percentuale_ghiaccio = (result / (pixel_area_geografica / 100))
       
        # Calcolo del valori in km2 del ghiacciaio
        area_geografica_km2_singola_foto = 142630
        pixel_area_geografica_singola_foto = 718584
       
       
        n_km2_each_pixel = area_geografica_km2_singola_foto / pixel_area_geografica_singola_foto
        km2_ghiacciaio = result * n_km2_each_pixel
       
       
       
        data = total_pixel, pixel_area_geografica, result_nero, result, percentuale_ghiaccio, km2_ghiacciaio
        data_writer.writerow(data)
       
        print(f"Il numero totale di pixel della foto è: {total_pixel}")
       
        print(f"Il numero totale di pixel dell'area geografica è: {pixel_area_geografica}")
       
        print(f"Il numero di pixel di colore nero è: {result_nero}")
       
        print(f"Il numero di pixel nell'intervallo BGR stabilito è: {result}")
       
        print(f"La % di ghiaccio (pixel bianchi) rispetto all'area geografica è {percentuale_ghiaccio} %")
       
        print(f"La superficie di ghiaccio in km2 ammonta a {km2_ghiacciaio}")




exit()
