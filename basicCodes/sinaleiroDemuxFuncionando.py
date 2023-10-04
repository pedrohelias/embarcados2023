# from time import sleep, perf_counter
# from threading import Thread


# def task():
#     while True:
#         print('Starting a task...')
#         sleep(1)
#         print('done')

# def task2():
#     while True:
#         print("Starting the second task...")
#         sleep(1)
#         print("done 2")


# start_time = perf_counter()

# # create two new threads    
# t1 = Thread(target=task)
# t2 = Thread(target=task2)

# t1.daemon = True
# t2.daemon = True


# t1.start()
# t2.start()

# #while True:

# # start the threads


# # wait for the threads to complete
# t1.join()
# t2.join()

# end_time = perf_counter()

# print(f'It took {end_time- start_time: 0.2f} second(s) to complete.')

from gpiozero import LED, Button
from time import sleep, perf_counter
from threading import Thread

#redLed = LED(17) #utilizando pinagem GPIO(numero), GPIO17
blueLed1 = LED(27)
blueLed2 = LED(22)

redLed1 = LED(5)
redLed2 = LED(6)

button = Button(2)

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
        blueLed2.on()
        print("principal verde")
        sleep(7)
        blueLed1.on()
        blueLed2.off()
        print("principal amarelo")
        sleep(3)
        ##blueLed1.off()
        blueLed2.on()
        print("principal vermelho")
        sleep(10)
        if button.is_pressed:
            print("Botao funcionado")


def task2():
    while True:
        redLed1.on()
        redLed2.on()
        print("auxiliar vermelho")
        sleep(10)
        redLed1.off()
        print("auxiliar verde")
        sleep(7)
        redLed2.off()
        redLed1.on()
        print("auxliar amarelo")
        sleep(3)

#start_time = perf_counter()

# create two new threads    
t1 = Thread(target=task)
t2 = Thread(target=task2)
monitora = Thread(target=monitoraBotao) 
executa = Thread(target=executaFunc)


t1.daemon = True
t2.daemon = True
monitora.daemon = True
executa.daemon = True 

t1.start()
t2.start()
monitora.start()
executa.start()

#while True:

# start the threads


# wait for the threads to complete
t1.join()
t2.join()
monitora.join()
executa.join()

#end_time = perf_counter()

#print(f'It took {end_time- start_time: 0.2f} second(s) to complete.')