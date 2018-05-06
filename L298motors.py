import Adafruit_BBIO.GPIO as GPIO
import time

Master_Pin =  "P9_21"
ln1 =         "P9_22"
ln2 =         "P9_12"

if __name__=="__main__":

    GPIO.setup(Master_Pin, GPIO.OUT)
    GPIO.output(Master_Pin, GPIO.LOW)

    GPIO.setup(ln1, GPIO.OUT)
    GPIO.setup(ln2, GPIO.OUT)

    GPIO.output(Master_Pin, GPIO.HIGH)
    GPIO.output(ln1, GPIO.HIGH)
    GPIO.output(ln2, GPIO.LOW)
    time.sleep(5)

    GPIO.output(Master_Pin, GPIO.HIGH)
    GPIO.output(ln1, GPIO.LOW)
    GPIO.output(ln2, GPIO.HIGH)
    time.sleep(5)
    print "I love your body Larry!"

    GPIO.output(Master_Pin, GPIO.LOW)

    GPIO.output(Master_Pin, GPIO.LOW)
    GPIO.cleanup()
