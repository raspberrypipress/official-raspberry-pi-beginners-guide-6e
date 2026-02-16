from gpiozero import LED, Button
from time import sleep
from random import uniform

left_name = input("Der Spieler links heißt ")
right_name = input("Der Spieler rechts heißt ")
led = LED(4)
right_button = Button(15)
left_button = Button(14)

led.on()
sleep(uniform(5, 10))
led.off()

def pressed(button):
    right_button.when_pressed = None
    left_button.when_pressed = None
    if button == left_button:
        print(left_name + " hat gewonnen")
    else:
        print(right_name + " hat gewonnen")

right_button.when_pressed = pressed
left_button.when_pressed = pressed