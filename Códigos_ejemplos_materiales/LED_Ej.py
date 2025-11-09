import machine
import time

PIN_LED = 2 
DELAY_SEGUNDOS = 0.5 

led = machine.Pin(PIN_LED, machine.Pin.OUT)

try:
    while True:
        led.value(1)
        time.sleep(DELAY_SEGUNDOS)

        led.value(0)
        time.sleep(DELAY_SEGUNDOS)

except KeyboardInterrupt:
    led.value(0)
