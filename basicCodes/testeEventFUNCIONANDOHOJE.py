from gpiozero import LED, Button
from threading import Thread, Event
from time import sleep


blueLed1 = LED(2)
blueLed2 = LED(3)

button = Button(4)

# Evento para sinalizar a interrupção das threads
interromper_event = Event()

def task1():
    while not interromper_event.is_set():
        blueLed1.off()
        print("principal verde")
        #event.wait(1)
        sleep(1)
        blueLed1.on()
        print("principal amarelo")
        #event.wait(1)
        sleep(1)

def task2():
    while not interromper_event.is_set():
        blueLed2.on()
        print("auxiliar vermelho")
        #event.wait(1)
        sleep(1)
        blueLed2.off()
        print("auxiliar verde")
        #event.wait(1)#espera ate um evento ou ate o tempo finalzar 
        sleep(1)

def nova_task():
    while not interromper_event.is_set():
        print("Nova thread em execução...")
        sleep(1)

def task3():
    print("entrou aqui!")
    blueLed1.on()
    blueLed2.on()
    sleep(1)
    blueLed1.off()
    blueLed2.off()
    sleep(1)
    blueLed1.on()
    blueLed2.on()
    sleep(1)
    blueLed1.off()
    blueLed2.off()
    sleep(1)

# Cria as threads
t1 = Thread(target=task1)
t2 = Thread(target=task2)


t1.daemon = True
t2.daemon = True

# Inicia as threads
t1.start()
t2.start()

# Aguarda até que o botão seja pressionado
button.wait_for_press()

# Sinaliza o evento para interromper as threads task1 e task2
interromper_event.set()

# Aguarda até que as threads task1 e task2 terminem
t1.join()
t2.join()
print("chegou aqui!")

# Inicia a nova thread

nova_thread = Thread(target=task3)
nova_thread.start()

print("chegou dps do inicio")

nova_thread.join()


#daqui pra baixo chama outra thread

interromper_event.clear()

t1 = Thread(target=task1)
t2 = Thread(target=task2)

t1.start()
t2.start()

t1.join()
t2.join()
# print("finalizou")