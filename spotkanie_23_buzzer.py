import music, microbit

while True:
    if microbit.button_a.is_pressed():
        music.pitch(1024)
    if microbit.button_a.is_pressed() == False:
        music.pitch(0)