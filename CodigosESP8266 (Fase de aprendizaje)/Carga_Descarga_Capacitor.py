import machine
from machine import Pin
import time
import array

salidaD6 = Pin(12, Pin.OUT)  
entradaAnalogica = machine.ADC(0)
ledD4  =  Pin(2, Pin.OUT)

contadorCiclos = 0
estadoArchivo = 0
ledD4.off()

lecturas_adc = array.array('i')
Muestreo_CSV = "datos_rc.csv"

def guardar_csv():
    try:
        with open(Muestreo_CSV, 'a') as archivo:
            
            print(f"Escribiendo {len(lecturas_adc)} muestras en {Muestreo_CSV}...")
            for indice, valor in enumerate(lecturas_adc):
                linea_csv = f"{indice},{valor}\n"
                archivo.write(linea_csv)
        
        print(f"Datos guardados exitosamente. Tamanno del archivo: {os.stat(Muestreo_CSV)[6]} bytes.")
        estadoArchivo=1
    except Exception as e:
        print(f"ERROR al guardar el archivo: {e}")
        estadoArchivo=1
        
while True:
    if contadorCiclos==10:
        ledD4.on()
        time.sleep(2)
        ledD4.off()
        contadorCiclos=0
        if estadoArchivo == 0:
            guardar_csv()
            
    salidaD6.on()
    for i in range(10):
        valor_adc = entradaAnalogica.read()
        lecturas_adc.append(valor_adc)
        time.sleep_us(8)
    time.sleep_us(1155)
    salidaD6.off()
    for i in range(10):
        valor_adc = entradaAnalogica.read()
        lecturas_adc.append(valor_adc)
        time.sleep_us(8)
    time.sleep_us(1155)
    contadorCiclos+=1
    print (f"Realizado {contadorCiclos} ciclos de carga y descarga")
