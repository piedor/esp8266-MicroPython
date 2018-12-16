import machine

p5 = machine.Pin(5)
pwm5 = machine.PWM(p5)
pwm5.freq(1000)
# 0-1023 0-5v 512=2.5v
pwm5.duty(512)
