def temp ():
    print('temp high')
    if sense.temperature > 35:
        blynk.logEvent("temp_too_high")  
        sense.clear(255,255,255)  
        print('temp high')
    else:
        sense.clear()    


 
 


#Blynk.notify("Hey, Too humid !!")
#Blynk.notify("Hey, Too Cold !!") 
#Blynk.notify("Hey, Too Hot!!") 