"""
link do tutoriala, dokumentacji:
https://tinyurl.com/y2k5kl94
poniżej jest mój przykład, wąż który sunie przez dwie pierwsze linijki
DM me if you have any questions
"""
import microbit

# klatki animacji
# pusta klatka, do kopiowania
kropka0 = microbit.Image('00000:''00000:''00000:''00000:''00000:')
# faktyczna animacja
kropka1 = microbit.Image('30000:''00000:''00000:''00000:''00000:')
kropka2 = microbit.Image('36000:''00000:''00000:''00000:''00000:')
kropka3 = microbit.Image('36900:''00000:''00000:''00000:''00000:')
kropka4 = microbit.Image('03690:''00000:''00000:''00000:''00000:')
kropka5 = microbit.Image('00369:''00000:''00000:''00000:''00000:')
kropka6 = microbit.Image('00036:''90000:''00000:''00000:''00000:')
kropka7 = microbit.Image('00003:''69000:''00000:''00000:''00000:')
kropka8 = microbit.Image('00000:''36900:''00000:''00000:''00000:')
kropka9 = microbit.Image('00000:''03690:''00000:''00000:''00000:')
kropka10 = microbit.Image('00000:''00369:''00000:''00000:''00000:')
kropka11 = microbit.Image('00000:''00000:''00000:''00000:''00000:')

# lista klatek
kropka_animacja = [
    kropka0, kropka1, kropka2, kropka3, kropka4, kropka5, kropka6, 
    kropka7, kropka8, kropka9, kropka10, kropka11
    ]   
    
# Wyświetlenie animacji
#microbit.display.show(kropka_animacja)
# dodatkowe przydatne argumenty: delay, loop, clear
microbit.display.show(kropka_animacja, delay = 200, loop = True, clear = True)
