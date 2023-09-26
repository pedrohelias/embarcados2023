import RPi.GPIO as GPIO
import time 

BOTAO = 14 ##GPIO21
LED = 18 #GPIO18

GPIO.setwarnings(False) #desativar avisos
GPIO.setMode(GPIO.BCM) #formatacao dos pinos
GPIO.setup(LED, GPIO.OUT) #setando o led como saida
GPIO.setup(BOTAO, GPIO.IN) #setando o botao como entrada

try:
    while True: #loop infinito
        GPIO.output(LED, GPIO.input(BOTAO)) #setar o led com o que se ler no botao
        time.sleep(0.1)

except KeyboardInterrupt: #ctrl-c
    GPIO.cleanup() #desativa a pinagem