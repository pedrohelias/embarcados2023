

from gpiozero import LED, Button
from time import sleep, perf_counter
from threading import Thread

#redLed = LED(17) #utilizando pinagem GPIO(numero), GPIO17
blueLed1 = LED(9)
blueLed2 = LED(11)

redLed1 = LED(5)
redLed2 = LED(6)


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

t1.daemon = True
t2.daemon = True


t1.start()
t2.start()

#while True:

# start the threads


# wait for the threads to complete
t1.join()
t2.join()

#end_time = perf_counter()

#print(f'It took {end_time- start_time: 0.2f} second(s) to complete.')