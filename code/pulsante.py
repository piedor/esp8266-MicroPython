import time
import machine

pul = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_UP)
led = machine.Pin(5, machine.Pin.OUT)
while True:
    led.value(1 - pul.value())
    time.sleep(0.1)
