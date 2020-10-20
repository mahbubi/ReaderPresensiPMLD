# importing the requests library
import requests
import time
import RPi.GPIO as GPIO
import lcddriver
from time import sleep
from mfrc522 import SimpleMFRC522
from gpiozero import Buzzer
# defining the api-endpoint
API_ENDPOINT = "http://10.33.109.90:9090/api/kehadiran"
# your source code here
# buzzer 23 =pin 16 physical
reader = SimpleMFRC522()
display = lcddriver.lcd()
buzzer = Buzzer(23)
try:
 while True:
    print("Tap Your card")
    display.lcd_display_string("Tap Your card",1)
    id, text = reader.read()
    display.lcd_display_string("Absensi Berhasil",1)
    buzzer.on()
    time.sleep(0.5)
    buzzer.off()
    time.sleep(1)
    print("CARD ID   : ",id)
    print("Credential: ",text)
    # data to be sent to api
    data = {'rfid_uid': id,'nama': text,}
    # sending post request and saving response as response object
    r = requests.post(url = API_ENDPOINT, data = data)
    display.lcd_clear()
    time.sleep(2)
finally:
  GPIO.cleanup()
