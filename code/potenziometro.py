import machine

adc = machine.ADC(0)
value = adc.read()
print("adc value: ", value)
print("voltage: ", value * 5 / 1024)
