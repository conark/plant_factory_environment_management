# Import necessary libraries
from sense_hat import SenseHat
from picamera import PiCamera
from time import sleep
import time

# Initialize the camera and sensehat
sense = SenseHat()
camera = PiCamera()

# Set camera settings
camera.resolution = (1280, 720)  # Set resolution
camera.framerate = 30  # Set frame rate


while True:
  # flash green light, currentry 12 seconds
  sense.clear(0, 255, 0)
  #time.sleep(12 * 60)
  time.sleep(12)
  
  # flash red light, currentry 12 seconds
  sense.clear(255, 0, 0)
  #time.sleep(12 * 60)
  time.sleep(12)
  
  # turn off light for 5 seconds and take a picture
  sense.clear()
  camera.capture('image/image.jpg')
  time.sleep(5)
