from signal import pause
from gpiozero import LED, Button

button = Button(21)
button2 = Button(19)
led = LED(26)


while True:
    if button.is_pressed:
        print("Botao pressionado")
        led.on
    else:
        print("Botao nao pressionado")
        led.off

    pause()


