# External module imports
import RPi.GPIO as GPIO
import time

# Pin Definitons:
RedLED = 18
GreenLED = 23
BlueLED = 24
Buttonpin = 12


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(Buttonpin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(RedLED, GPIO.OUT)
GPIO.setup(GreenLED, GPIO.OUT)
GPIO.setup(BlueLED, GPIO.OUT)

print(str(GPIO.input(RedLED)) + str(GPIO.input(GreenLED)) +
      str(GPIO.input(BlueLED)) + str(GPIO.input(Buttonpin)))
