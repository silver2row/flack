import Adafruit_BBIO.GPIO as GPIO
import time

Master_Pin1 =  "P8_13"
ln1a =         "P8_14"
ln1b =         "P8_15"

Master_Pin2 =  "P8_16"
ln2a =         "P8_17"
ln2b =         "P8_18"

if __name__=="__main__":

    GPIO.setup(Master_Pin1, GPIO.OUT)
    GPIO.setup(Master_Pin2, GPIO.OUT)
    GPIO.output(Master_Pin1, GPIO.LOW)
    GPIO.output(Master_Pin2, GPIO.LOW)

    GPIO.output(Master_Pin1, GPIO.HIGH)
    GPIO.output(Master_Pin2, GPIO.HIGH)

    GPIO.setup(ln1a, GPIO.OUT)
    GPIO.setup(ln1b, GPIO.OUT)

    GPIO.setup(ln2a, GPIO.OUT)
    GPIO.setup(ln2b, GPIO.OUT)

    GPIO.output(ln1a, GPIO.HIGH)
    GPIO.output(ln1b, GPIO.LOW)
    GPIO.output(ln2a, GPIO.HIGH)
    GPIO.output(ln2b, GPIO.LOW)
    time.sleep(2)

    GPIO.output(ln1a, GPIO.HIGH)
    GPIO.output(ln1b, GPIO.HIGH)
    GPIO.output(ln2a, GPIO.HIGH)
    GPIO.output(ln2b, GPIO.HIGH)
    time.sleep(2)

    GPIO.output(ln1a, GPIO.LOW)
    GPIO.output(ln1b, GPIO.HIGH)
    GPIO.output(ln2a, GPIO.LOW)
    GPIO.output(ln2b, GPIO.HIGH)
    print ("I love your body Larry!")

    GPIO.output(ln1a, GPIO.LOW)
    GPIO.output(ln1b, GPIO.LOW)
    GPIO.output(ln2a, GPIO.LOW)
    GPIO.output(ln2b, GPIO.LOW)
    print ("Waka, Waka, Waka!")

    GPIO.output(Master_Pin1, GPIO.LOW)
    GPIO.output(Master_Pin2, GPIO.LOW)

    GPIO.cleanup()
