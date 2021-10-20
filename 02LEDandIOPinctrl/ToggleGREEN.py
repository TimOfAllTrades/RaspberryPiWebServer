# External module imports
import RPi.GPIO as GPIO
import time

# Pin Definitons:
RedLED = 18
GreenLED = 23
BlueLED = 24

dc = 95  # duty cycle (0-100) for PWM pin

# Pin Setup:
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)  # Broadcom pin-numbering scheme
GPIO.setup(GreenLED, GPIO.OUT)

if GPIO.input(GreenLED) == 1:
    GPIO.output(GreenLED, GPIO.LOW)
else:
    GPIO.output(GreenLED, GPIO.HIGH)
#GPIO.output(GreenLED, GPIO.LOW)

# GPIO.cleanup()

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
