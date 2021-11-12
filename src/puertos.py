#!/usr/bin/env python3
import socket
from socket import *

def ip():
    ip = input("Agrega la ip: ")
    begin = input("Agrega el puerto en el que quieres empezar a escanear: ")
    end = input("Agrega el puerto en el que quieres terminar: ")

    try:
        print('comenzando el escaneo en la ip: ', ip)
        for puertos in range(int(begin), int(end)+1):
            cliente = socket(AF_INET, SOCK_STREAM)
            resultado = cliente.connect_ex((ip, puertos))
            if (resultado == 0):
                print(('puerto %d: Abierto') %(puertos))
            else:
                print(('puerto %d: Cerrado') %(puertos))
            #se cierra la conexion para que se analice el siguiente puerto
            cliente.close()
    except Exception as error:
        print("Ocurrió un error")
