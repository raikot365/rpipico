from machine import Pin
from time import sleep

led_board = Pin("LED", Pin.OUT)
sleep(1)    #le damos tiempo a vREPL
print("\nLED esta destellando...")
while True:
    #se puede utilizar sin try-except pero muestra el mensaje de que no se manejo la excepcion
    try:
        led_board.toggle() #solo para raspberry pi pico
        # led_board.value(not led_board.value()) # para esp32, lee el estado y lo invierte
        sleep(1) # sleep 1sec
    except KeyboardInterrupt:
        break
led_board.off()
print("Listo")
