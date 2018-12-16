import time

import machine
led = machine.Pin(5, machine.Pin.OUT)
while True:
    led.high()
    time.sleep(.2)
    led.low()
    time.sleep(.2)
