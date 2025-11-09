from machine import ADC, Pin
import time

adc = ADC(0)  # Si estás en ESP8266; en ESP32 usar ADC(Pin(34))
# Ejemplo ESP32:
# adc = ADC(Pin(34))
# adc.atten(ADC.ATTN_11DB)  # hasta 3.3 V

while True:
    valor = adc.read()
    print("Lectura ADC:", valor)
    time.sleep(1)
