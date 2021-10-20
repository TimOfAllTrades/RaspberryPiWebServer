# External module imports
import RPi.GPIO as GPIO
import time

# Pin Definitons:
pwmPin = 18  # Broadcom pin 18 (P1 pin 12)
ledPin = 23  # Broadcom pin 23 (P1 pin 16)
butPin = 17  # Broadcom pin 17 (P1 pin 11)

RedLED = 18
GreenLED = 23
BlueLED = 24

dc = 95  # duty cycle (0-100) for PWM pin

# Pin Setup:
GPIO.setmode(GPIO.BCM)  # Broadcom pin-numbering scheme
GPIO.setup(RedLED, GPIO.OUT)  # LED pin set as output
GPIO.setup(GreenLED, GPIO.OUT)  # PWM pin set as output
GPIO.setup(BlueLED, GPIO.OUT)  # LED pin set as output

GPIO.output(RedLED, GPIO.LOW)
GPIO.output(GreenLED, GPIO.LOW)
GPIO.output(BlueLED, GPIO.LOW)

GPIO.output(RedLED, GPIO.HIGH)
print(GPIO.input(RedLED))


# pwm = GPIO.PWM(pwmPin, 50)  # Initialize PWM on pwmPin 100Hz frequency
#
# GPIO.setup(butPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up
#
# Initial state for LEDs:
#GPIO.output(ledPin, GPIO.LOW)
# pwm.start(dc)
#
#print("Here we go! Press CTRL+C to exit")
# try:
#    while 1:
#        if GPIO.input(butPin): # button is released
#            pwm.ChangeDutyCycle(dc)
#            GPIO.output(ledPin, GPIO.LOW)
#        else: # button is pressed:
#            print("button pressed!")
#            pwm.ChangeDutyCycle(100-dc)
#            GPIO.output(ledPin, GPIO.HIGH)
#            time.sleep(0.075)
#            GPIO.output(ledPin, GPIO.LOW)
#            time.sleep(0.075)
# except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
#    pwm.stop() # stop PWM
#    GPIO.cleanup() # cleanup all GPIO
