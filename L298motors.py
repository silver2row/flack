import Adafruit_BBIO.GPIO as GPIO
import time

EnA = "P9_21"
ln1 = "P9_22"
ln2 = "P9_12"

print "Initialize"

GPIO.setup("P9_21", GPIO.OUT)
GPIO.setup("P9_22", GPIO.OUT)
GPIO.setup("P9_12", GPIO.OUT)

while True:

    for i in range(10):
        EnA = GPIO.output("P9_21", GPIO.LOW)
    for i in range(3):
        ln1 = GPIO.output("P9_22", GPIO.HIGH)
    for i in range(5):
        ln2 = GPIO.output("P9_12", GPIO.HIGH)
    for i in range(4):
        ln1 = GPIO.output("P9_22", GPIO.LOW)
    for i in range(10):
        EnA = GPIO.output("P9_21", GPIO.LOW)
        print "Go, Go Bananas!"

        try:
		
		except KeyboardInterrupt:
		    print "I got it over w/!"
			GPIO.cleanup()
			quit()
