import Adafruit_BBIO.GPIO as GPIO
from time import sleep

EnA = "P8_13"
EnB = "P8_16"
ln1 = "P8_14"
ln2 = "P8_15"
ln3 = "P8_17"
ln4 = "P8_18"

print "Initialize"

GPIO.setup(EnA, GPIO.OUT)
GPIO.setup(EnB, GPIO.OUT)
GPIO.setup(ln1, GPIO.OUT)
GPIO.setup(ln2, GPIO.OUT)
GPIO.setup(ln3, GPIO.OUT)
GPIO.setup(ln4, GPIO.OUT)

while True:

    GPIO.output(EnA, GPIO.LOW)
    GPIO.output(ln1, GPIO.LOW)
    GPIO.output(ln2, GPIO.LOW)
    GPIO.output(EnB, GPIO.LOW)
    GPIO.output(ln3, GPIO.LOW)
    GPIO.output(ln4, GPIO.LOW)
    sleep(8)
    print "I like bacon!"

    GPIO.output(EnA, GPIO.HIGH)
    GPIO.output(EnB, GPIO.HIGH)

    GPIO.output(ln1, GPIO.LOW)
    GPIO.output(ln2, GPIO.HIGH)

    GPIO.output(ln3, GPIO.LOW)
    GPIO.output(ln4, GPIO.HIGH)
    sleep(8)
    print "I am not a cohort!"

    GPIO.output(EnA, GPIO.HIGH)
    GPIO.output(EnB, GPIO.HIGH)

    GPIO.output(ln1, GPIO.LOW)
    GPIO.output(ln2, GPIO.LOW)

    GPIO.output(ln3, GPIO.LOW)
    GPIO.output(ln4, GPIO.LOW)
    sleep(8)
    print "Heh?"
	
    GPIO.output(EnA, GPIO.HIGH)
    GPIO.output(EnB, GPIO.HIGH)

    GPIO.output(ln1, GPIO.HIGH)
    GPIO.output(ln2, GPIO.LOW)

    GPIO.output(ln3, GPIO.HIGH)
    GPIO.output(ln4, GPIO.LOW)
    sleep(8)
    print "I am here now!"

    GPIO.output(EnA, GPIO.LOW)
    GPIO.output(EnB, GPIO.LOW)
    GPIO.cleanup()
    quit()
