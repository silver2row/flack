import Adafruit_BBIO.GPIO as GPIO
from time import sleep
 
EnA = "P9_21"
In1 = "P9_22"
In2 = "P9_12"
 
for pin in EnA, In1, In2:
    GPIO.setup(pin, GPIO.OUT)
 
def disable(): GPIO.output(EnA, GPIO.LOW)
def enable(): GPIO.output(EnA, GPIO.HIGH)
 
def drive(level1, level2):
    GPIO.output(In1, level1)
    GPIO.output(In2, level2)
    enable()
 
def stop():    drive(GPIO.LOW,  GPIO.LOW)
def forward(): drive(GPIO.HIGH, GPIO.LOW)
def reverse(): drive(GPIO.LOW,  GPIO.HIGH)
 
forward(5)
sleep(2)
stop(6)
sleep(2)
reverse(5)
sleep(2)
 
stop()
sleep(1)
disable()