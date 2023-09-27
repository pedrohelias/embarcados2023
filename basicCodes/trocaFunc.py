from gpiozero import LED, Button
from time import sleep

redLed = LED(17) #utilizando pinagem GPIO(numero), GPIO17
blueLed1 = LED(27)
blueLed2 = LED(22)
botao = Button(2)

def blink1():
    redLed.on()
    sleep(1) #segundos
    redLed.off()
    sleep(1)
    blueLed1.on()
    sleep(1)
    blueLed1.off()
    sleep(1)
    blueLed2.on()
    sleep(1)
    blueLed2.off()
    sleep(1)

def blink2():
    redLed.on()
    sleep(2)
    redLed.off()
    sleep(2)
    blueLed1.on()
    sleep(2)
    blueLed1.off()
    sleep(2)
    blueLed2.on()
    sleep(2)
    blueLed2.off()
    sleep(2)
while True:
    botao.when_pressed = blink1()
    botao.when_released = blink2()