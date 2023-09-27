from gpiozero import LED, Button
from time import sleep

redLed = LED(17) #utilizando pinagem GPIO(numero), GPIO17
blueLed1 = LED(27)
blueLed2 = LED(22)


def sinaleiro():
    redLed.on()
    sleep(10) #segundos sinal vermelho
    redLed.off()
    blueLed2.on() #sinal verde
    sleep(7)
    blueLed2.off()
    blueLed1.on() #sinal amarelo
    sleep(2)
    blueLed1.off()



while True:
    sinaleiro()