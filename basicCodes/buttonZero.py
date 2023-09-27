
from signal import pause
from gpiozero import LED, Button

button = Button(21)
button2 = Button(19)
led = LED(26)


try:
    button.when_pressed = led.on
    button2.when_pressed = led.off

    
    pause()
finally:
    pass









