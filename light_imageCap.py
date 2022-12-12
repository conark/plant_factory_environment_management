# Import necessary libraries
from sense_hat import SenseHat
from picamera import PiCamera
from time import sleep
import time
import datetime
import schedule

# Initialize the camera and sensehat
sense = SenseHat()
camera = PiCamera()

# Set camera settings
camera.resolution = (1280, 720)  # Set resolution
camera.framerate = 30  # Set frame rate
camera.start_preview()
frame = 1


def green_light():
  sense.clear(0, 255, 0)
  time.sleep(12)

def red_light():
  sense.clear(255, 0, 0)
  #time.sleep(12 * 60) #12 min
  time.sleep(12)

def imageCap():
  # turn off light and take a picture
  sense.clear()
  # sense.clear(255,255,255) #for white light
  # set the location of image file and current time
  currentTime = datetime.datetime.now()
  image = f'/home/pi/plant_management/plant_factory_environment_management/image/{currentTime}.jpg'
  camera.capture(image)
  #camera.capture('image/image.jpg')
  print(f'pic taken at {currentTime}') # print frame number to console
  time.sleep(5)


#####################################################
# schedule everyday at 7:55am take pic, 8am and 8pm lights turn on

# schedule.every().day.at("7:55").do(imageCap)
# schedule.every().day.at("8:00").do(red_light)
# schedule.every().day.at("20:00").do(green_light)
######################################################
# test schedule
# schedule.every().day.at("16:28").do(red_light)
# schedule.every().day.at("16:29").do(green_light)
# schedule.every().day.at("16:30").do(imageCap)



while True:
  red_light()
  green_light()
  imageCap()

  ####################################
  # When use schedule
  #schedule.run_pending()
  #time.sleep(1)
  #sense.clear()
  ####################################



