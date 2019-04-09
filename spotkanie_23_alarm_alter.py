import microbit
from time import sleep

while True:
    czujnik = microbit.pin1.read_digital() # czujnik ruchu
    microbit.display.show(czujnik)
    if czujnik == 1:
        microbit.pin0.write_digital(0)  # sygnał domyślnie wysyłany na pin0
        sleep(1)  # czas trwania dźwięku
    microbit.pin0.write_digital(1)
    sleep(1)  # czas trwania przerwy
