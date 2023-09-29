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

def demux(): #a transição funciona de acordo com a paridade. Led2, Led1 = 1, 1; 1,0; 0,1...
    blueLed2.on()
    blueLed1.on()
    print("verde")
    sleep(5)
    blueLed1.off()
    print("amarelo")
    sleep(3)
    blueLed2.off()
    blueLed1.on()
    print("vermelho")
    sleep(10)

while True:
    demux()









