from gpiozero import LED, Button
from time import sleep, perf_counter
from threading import Thread
import threading

blueLed1 = LED(2)
blueLed2 = LED(3)
button = Button(4)

event = threading.Event()


def minha_funcao():
    while not event.is_set():
        print("Thread em execução...")
        sleep(1)  # Faça alguma coisa aqui
    print("thread encerrada")
    

def monitoraBotao():
    global botaoPressionado
    while True:
        if button.is_pressed:
            botaoPressionado = True
        else:
            botaoPressionado = False 
        sleep(0.1)

def executaFunc():
    while True:
        if botaoPressionado:
            print("botao pressionado")
            botaoPressionado = False
        sleep(0.1)


def task():
    while True:
        blueLed1.off()
        print("principal verde")
        event.wait(1)
        #sleep(1)
        blueLed1.on()
        print("principal amarelo")
        event.wait(1)
        #sleep(1)


def task2():
    while True:
        blueLed2.on()
        print("auxiliar vermelho")
        event.wait(1)
        #sleep(3)
        blueLed2.off()
        print("auxiliar verde")
        event.wait(1)#espera ate um evento ou ate o tempo finalzar 
        #sleep(3)
def task3():
    while True:
        print("entrou aqui!")
        blueLed1.on()
        blueLed2.on()
        #event.wait(1)
        sleep(2)
        blueLed1.off()
        blueLed2.off()
        #event.wait(1)
        sleep(2)

sair = threading.Event()

thread = threading.Thread(target=minha_funcao)
t1 = Thread(target=task)
t2 = Thread(target=task2)

thread.daemon = True
t1.daemon = True
t2.daemon = True

thread.start()
t1.start()
t2.start()


sleep(7)
event.set()


# sleep(10)
# event.set()

t1.join()
t2.join()
thread.join()
#t3.join()


t3 = Thread(target=task3)
t3.start()
t3.daemon=True
t3.join()