import music, microbit
from time import sleep

while True:
    czujnik = microbit.pin1.read_digital() # czujnik ruchu
    microbit.display.show(czujnik)
    if czujnik == 1:
        music.pitch(1024)  # sygnał domyślnie wysyłany na pin0
        sleep(1)  # czas trwania dźwięku
    music.pitch(0)
    sleep(1)  # czas trwania przerwy