import machine
from machine import Pin, ADC
import time

V_REF = 3.3
MAX_ADC = 1023
M = -0.002
T_CAL = 25
V_CAL = 0.6

entradaAnalogica = machine.ADC(0)
ledD4  =  Pin(2, Pin.OUT)
estadoLed = True

while True:
    if(estadoLed):
        ledD4.on()
        estadoLed = False
    else:
        ledD4.off()
        estadoLed = True
    sensado = entradaAnalogica.read()
    V_D = sensado * (V_REF / MAX_ADC)
    temperatura = T_CAL + (V_D - V_CAL) / M
    print(f'Lectura Diodo: {sensado} | Voltaje diodo: {V_D} | Temperatura: {temperatura} \n')
    time.sleep(2)
