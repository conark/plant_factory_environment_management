import BlynkLib
from sense_hat import SenseHat
from time import sleep

BLYNK_AUTH = 'fFBWjj108jcqQ7XmRXeDQ4MCMHJ3os6_'
# initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)

#initialise SenseHAT
sense = SenseHat()
sense.clear()

# register handler for virtual pin V0 write event
@blynk.on("V0")
def v3_write_handler(value):
    buttonValue=value[0]
    print(f'Current button value: {buttonValue}')
    if buttonValue=="1":
        sense.clear(255,255,255)
    else:
        sense.clear()

# infinite loop that waits for event for temp and humidity
while True:
    blynk.run()
    blynk.virtual_write(1, round(sense.temperature,2))
    blynk.virtual_write(2, round(sense.humidity,2))
    sleep(0.5) # sleep for .5 second

