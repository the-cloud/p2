import microbit
import time

# obrazek do wyświetlenie gry program się uruchomi
cloud = microbit.Image("00000:00000:00000:00000:00000")  # matryca LED
microbit.display.show(cloud)

# Quiz początek
score = 0  # zmienna zapisująca punkty

# początek pytania
print()  # pusta funkcja print() po to by zrobić linię przerwy
print(" ... ?")
# odpowiedzi
print("A) ... ")
print("B) ... ")
print("C) ... ")
while True:
    # która odpowiedź jest poprawna? zmień odpowiednio numery pin'ów
    # wedle tego schematu: pin0 - A, pin1 - B, pin2 - C
    if microbit.pin0.is_touched():  # odpowiedź poprawna
      score +=1
      print("Brawo! Dobra odpowiedź")
      print("Otrzymałeś: ", score)
      microbit.display.show(score)
      break
    # odpowiedzi niepoprawne
    if microbit.pin1.is_touched():
        print("Zła odpowiedź")
        microbit.display.show(score)
        break
    if microbit.pin2.is_touched():
        print("Zła odpowiedź")
        microbit.display.show(score)
        break
print()
time.sleep(1) # mały odstęp czasu pomiędzy pytaniami
# koniec pytania

# skopiuj powyższy kod by utworzyć więcej pytań

time.sleep(1)  # dodatkowa chwila pauzy
# wiadomość na koniec
if score == 0:
    print("Koniec quizu. Niestety nie otrzymałeś żadnych punktów")
else:
    print("Brawo! Dobra odpowiedź")
    print("Otrzymałeś: ", score)

# Quiz koniec
