from machine import I2C, Pin
from ina219 import INA219
import time

# Ejemplo con bus I2C
i2c = I2C(0, scl=Pin(22), sda=Pin(21))
ina = INA219(shunt_ohms=0.1, i2c=i2c)
ina.configure()

while True:
    print("Tensión bus: %.3f V" % ina.voltage())
    print("Corriente: %.3f mA" % ina.current())
    time.sleep(2)
