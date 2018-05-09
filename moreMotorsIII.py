import Adafruit_BBIO.GPIO as GPIO
from time import sleep

EnA = "P9_21"
ln1 = "P9_22"
ln2 = "P9_12"

print "Initialize"

GPIO.setup("P9_21", GPIO.OUT)
GPIO.setup("P9_22", GPIO.OUT)
GPIO.setup("P9_12", GPIO.OUT)

if EnA != HIGH:
    
    EnA = GPIO.output("P9_21", GPIO.LOW)
    ln1 = GPIO.output("P9_22", GPIO.HIGH)
    ln2 = GPIO.output("P9_12", GPIO.LOW)
    sleep(8)

    EnA = GPIO.output("P9_21", GPIO.HIGH)
    ln1 = GPIO.output("P9_22", GPIO.LOW)
    ln2 = GPIO.output("P9_12", GPIO.HIGH)
    sleep(8)

    EnA = GPIO.output("P9_21", GPIO.LOW)
    ln1 = GPIO.output("P9_22", GPIO.LOW)
    ln2 = GPIO.output("P9_12", GPIO.LOW)
    sleep(8)
    print "I am here now!"

    EnA = GPIO.output("P9_21", GPIO.HIGH)
    ln1 = GPIO.output("P9_22", GPIO.HIGH)
    ln2 = GPIO.output("P9_12", GPIO.LOW)
    sleep(8)
    print "Flunk-a-Dunk!"
    
else:

    for i in range(1, 9):
        EnA = GPIO.output("P9_21", GPIO.HIGH)
        ln1 = GPIO.output("P9_22", GPIO.LOW)
        ln2 = GPIO.output("P9_12", GPIO.HIGH)

        EnA = GPIO.output("P9_21", GPIO.HIGH)
        ln1 = GPIO.output("P9_22", GPIO.HIGH)
        ln2 = GPIO.output("P9_12", GPIO.LOW)
        sleep(0.2)

        EnA = GPIO.output("P9_21", GPIO.LOW)
        ln1 = GPIO.output("P9_22", GPIO.HIGH)
        ln2 = GPIO.output("P9_12", GPIO.HIGH)
        sleep(0.2)
        print "I am still almost there!"

try:
    EnA = GPIO.output("P9_21", GPIO.OUT)
    print "Going to sleep now!"

except(KeyboardInterrupt):
        print "I got it over w/!"
        GPIO.cleanup()
        quit()
