from hcsr04 import HCSR04
from time import sleep
import time
from machine import Pin

sensor = HCSR04(trigger_pin=5, echo_pin=18, echo_timeout_us=10000)
buzzer = Pin(19, Pin.OUT)

while True:
    distance = sensor.distance_cm()
    if 0 <= distance <= 10:
        buzzer.value(1)
    else:
        buzzer.value(0)
