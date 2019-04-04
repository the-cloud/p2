import microbit

while True:
    # czujnik wysyła 0 lub 1, w zależności czy jest ruch
    czujnik_ruchu = microbit.pin1.read_digital()
    if czujnik_ruchu == 1:
        microbit.display.show(1)
    if czujnik_ruchu == 0:
        microbit.display.show(0)