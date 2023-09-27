from gpiozero import LED, Button
from time import sleep

redLed = LED(17) #utilizando pinagem GPIO(numero), GPIO17
blueLed1 = LED(27)
blueLed2 = LED(22)
botao = Button(2)

def blink0():
    redLed.on()
    sleep(0.5)
    redLed.off()
    sleep(0.5)
    blueLed1.on()
    sleep(0.5)
    blueLed1.off()
    sleep(0.5)
    blueLed2.on()
    sleep(0.5)
    blueLed2.off()
    sleep(0.5)


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

##selecao = input("selecione a entrada ")

while True:
    # if(selecao == "blink1"):
    #     blink1()
    # elif (selecao == "blink2"):
    #     blink0()
    # else:
    #     blink2()
    

    # selecao = input("selecione a entrada ")

    if botao.is_pressed: #altera a funçaõ de blink
        blink1()
    else:
        blink2()
