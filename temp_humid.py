import BlynkLib
from sense_hat import SenseHat
from time import sleep
import requests
import os
from dotenv import load_dotenv

# load .env　file
load_dotenv()

BLYNK_AUTH = os.getenv ('BLYNK_AUTH')

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
    # 温度が30度以上の場合# HTTP メソッドでblynkに通知
    if sense.temperature >= 30:
        print ('temp hot')
        requests.get("https://blynk.cloud/external/api/logEvent?token=fFBWjj108jcqQ7XmRXeDQ4MCMHJ3os6_&code=temp_too_high")
    elif sense.temperature <= 25:
        print ('temp low')
        requests.get("https://blynk.cloud/external/api/logEvent?token=fFBWjj108jcqQ7XmRXeDQ4MCMHJ3os6_&code=temp_too_low")
    else:
        print ('temp fine')
    
    if sense.humidity >= 40:
        print ('humid high')
        requests.get("https://blynk.cloud/external/api/logEvent?token=fFBWjj108jcqQ7XmRXeDQ4MCMHJ3os6_&code=humidity_too_high")
    elif sense.humidity <= 20:
        print ('humid low')
        requests.get("https://blynk.cloud/external/api/logEvent?token=fFBWjj108jcqQ7XmRXeDQ4MCMHJ3os6_&code=humidity_too_low")
    else:
        print ('humid fine')


