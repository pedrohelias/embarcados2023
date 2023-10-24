import termios
import os
from time import sleep
import serial


def abrirUart():
    uarto_filestream = os.open("/dev/serial0", os.O_RDWR | os.O_NOCTTY | os.O_NDELAY)
    return uarto_filestream



def main():
    uart = abrirUart()

