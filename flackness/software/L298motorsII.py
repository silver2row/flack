import Adafruit_BBIO.GPIO as GPIO
from time import sleep
import time

EnA = "P9_13"
In1 = "P9_14"
In2 = "P9_15"

for fill in EnA, In1, In2:
    GPIO.setup(fill, GPIO.OUT)

def disable():
    GPIO.output(EnA, GPIO.LOW)
def enable():
    GPIO.output(EnA, GPIO.HIGH)

def drive(level1, level2):
    GPIO.output(In1, level1)
    GPIO.output(In2,level2)
    enable()

def stop():
    drive(GPIO.LOW,  GPIO.LOW)
    sleep(2)
def forward(geaux):
    drive(GPIO.HIGH, GPIO.LOW)
    sleep(9)
def reverse(II):
    drive(GPIO.LOW,  GPIO.HIGH)
    sleep(18)

stop()
forward(10)
reverse(10)
enable()
disable()
drive(1, 2)
sleep(7)
