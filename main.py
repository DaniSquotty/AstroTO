import numpy as np
from picamera import PiCamera, Color
from time import sleep
from datetime import datetime, timedelta
from orbit import ISS, ephemeris
from skyfield.api import load
from sense_hat import SenseHat
from pathlib import Path





# Camera settings
camera = PiCamera()
camera.resolution = (2592, 1944)
camera.iso = 300
sleep(3)
camera.image_effect = 'none'
camera.exposure_mode = 'auto'
sleep(2)
camera.start_preview(alpha=150)

# Destination file
base_folder = Path(__file__).parent.resolve()

counter = 1
start_time = datetime.now()
now_time = datetime.now()
while (now_time < start_time + timedelta(minutes=175)):
        sleep(5)
        
        #In order to avoid night images, we have included this condition which allows to verify that the ISS is in sunlit 
        timescale = load.timescale()
        t = timescale.now()
        if ISS.at(t).is_sunlit(ephemeris):
            print("In sunlight")
            #Take color value in order to decide if taking the image or not
            sense = SenseHat()
            sense.clear()
            sense.color.gain = 60
            sense.color.integration_cycles = 64
            sleep(3)
            red, green, blue, clear = sense.colour.colour
            print(f"R: {red}, G: {green}, B: {blue}, C: {clear}")
            sleep(2)
            #To obtain the necessary images we have created this condition in order to discard images that are too dark.
            if clear > 35:
                #We would like to discard photos with the ocean or clouds, because they are not the photos we need for our experiment.
                #So we manually calculated ranges for RED, GREEN and BLUE to be discarded and created these two conditions (the first for the ocean and the second for clouds).
                if (red < 150 or red > 160) and (green < 130 or green > 140) and (blue < 200 or blue > 210):
                    if (red > 210 or red < 200) and (green > 240 or green < 205) and (blue > 240 or blue < 185):
                        #Take location data
                        location = ISS.coordinates()
                        #Add text (coordinates) to the image, setting text color
                        camera.annotate_background = Color('blue')
                        camera.annotate_foreground = Color('yellow')
                        camera.annotate_text_size = 55
                        camera.annotate_text = f'Latitude: {location.latitude} \n Longitude: {location.longitude} \n Elevation: {location.elevation.km}'
                        camera.capture(f'{base_folder}/image_{counter:03d}.jpg')
                        #Update counter and now_time
                        counter += 1
        now_time = datetime.now()


#Close the camera and stop the program
camera.stop_preview()
camera.close()

exit()