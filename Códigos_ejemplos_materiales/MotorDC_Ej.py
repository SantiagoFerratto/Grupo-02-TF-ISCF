import machine
import time

PIN_CONTROL_MOTOR = 18 
TIEMPO_ENCENDIDO = 3.0

motor_control = machine.Pin(PIN_CONTROL_MOTOR, machine.Pin.OUT)

try:
    motor_control.value(1)
    time.sleep(TIEMPO_ENCENDIDO)

    motor_control.value(0)
    time.sleep(1.0)

except KeyboardInterrupt:
    motor_control.value(0)
