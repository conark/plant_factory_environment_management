import BlynkLib
from sense_hat import SenseHat
from time import sleep

BLYNK_AUTH = 'TeQOLZwkGYrr_1rAVOywQugDKFvy0cfF'
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

# infinite loop that waits for event
while True:
    blynk.run()
    blynk.virtual_write(1, round(sense.temperature,2))
    blynk.virtual_write(1, round(sense.temperature,2))
    sleep(0.5) # sleep for .5 second