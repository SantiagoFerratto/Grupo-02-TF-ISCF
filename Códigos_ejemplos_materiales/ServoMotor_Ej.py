import machine
import time

PIN_SERVO = 14
FRECUENCIA_PWM = 50
PAUSA = 1.0

servo_pin = machine.Pin(PIN_SERVO, machine.Pin.OUT)
servo_pwm = machine.PWM(servo_pin, freq=FRECUENCIA_PWM)

def set_angle(angle):
    min_duty = 25
    max_duty = 125
    duty = min_duty + (angle * (max_duty - min_duty) // 180)
    servo_pwm.duty(duty)

try:
    set_angle(90)
    time.sleep(PAUSA)

    set_angle(0)
    time.sleep(PAUSA)

    set_angle(180)
    time.sleep(PAUSA)

    set_angle(90)

except KeyboardInterrupt:
    servo_pwm.deinit()
