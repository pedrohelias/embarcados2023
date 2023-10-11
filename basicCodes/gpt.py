from gpiozero import LED, Button
from time import sleep
from threading import Thread, Event

blueLed1 = LED(2)
blueLed2 = LED(3)
button = Button(4)

event = Event()

def minha_funcao():
    while not event.is_set():
        print("Thread em execução...")
        sleep(1)

    print("thread encerrada")

def task():
    while not event.is_set():
        blueLed1.off()
        print("principal verde")
        event.wait(1)
        blueLed1.on()
        print("principal amarelo")
        event.wait(1)

def task2():
    while not event.is_set():
        blueLed2.on()
        print("auxiliar vermelho")
        event.wait(1)
        blueLed2.off()
        print("auxiliar verde")
        event.wait(1)

def task3():
    while event.is_set():
        print("entrou aqui!")
        blueLed1.on()
        blueLed2.on()
        sleep(1)
        blueLed1.off()
        blueLed2.off()
        sleep(1)
        #not event.is_set
    #not event.is_set()

event.clear()

thread = Thread(target=minha_funcao)
t1 = Thread(target=task)
t2 = Thread(target=task2)

thread.start()
t1.start()
t2.start()

sleep(7)
event.set()

t1.join()
t2.join()
thread.join()

t3 = Thread(target=task3)
t3.start()
t3.join()
