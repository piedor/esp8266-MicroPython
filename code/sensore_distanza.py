import machine
import utime

trig = machine.Pin(5, machine.Pin.OUT)
trig.low()
utime.sleep_us(2)
trig.high()
utime.sleep_us(10)
trig.low()
echo = machine.Pin(4, machine.Pin.IN)
while echo.value() == 0:
    pass
t1 = utime.ticks_us()
while echo.value() == 1:
    pass
t2 = utime.ticks_us()
cm = (t2 - t1) / 58.0
print(cm)
utime.sleep(2)
