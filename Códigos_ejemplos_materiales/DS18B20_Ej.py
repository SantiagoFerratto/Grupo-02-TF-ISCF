import onewire, ds18x20, time
from machine import Pin

pin = Pin(14)  # D5 en Wemos D1 mini, por ejemplo
sensor = ds18x20.DS18X20(onewire.OneWire(pin))
roms = sensor.scan()

while True:
    sensor.convert_temp()
    time.sleep_ms(750)
    for rom in roms:
        print("Temperatura:", sensor.read_temp(rom), "°C")
    time.sleep(2)
