import microbit

while True:
    # buzzer/brzęczyk jest domyślnie na pin0
    if microbit.button_a.is_pressed():
    microbit.pin0.write_digital(0)
    # jeżeli chcemy się trochę pobawić brzemieniem
    # microbit.pin0.write_analog(10)
    if microbit.button_a.is_pressed() == False:
        microbit.pin0.write_digital(1)