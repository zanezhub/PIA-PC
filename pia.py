#!/usr/bin/env python3
import argparse
import hashlib

#Se usa para que sea más entendible y corto el nombre.
parser = argparse.ArgumentParser() 
parser.add_argument('-d', nargs=1, type=str, help='elige la función a usar.',
                    choices=['hash', 'mover'])
parser.add_argument('-f', '--file', nargs=1 ,type=str, help='nombre del archivo.')

def Hash():    
    BUF_SIZE = 65536 # Se usa para leer archivos en 64kb
    md5 = hashlib.md5()
    #manejo de errores.
    try: 
        with open(args.file[0], 'rb') as f:
            while True:
                data = f.read(BUF_SIZE)
                
                # romple el ciclo si no hay más data que leer.
                if not data:
                    break
                md5.update(data)
        print("MD5: {0}".format(md5.hexdigest()))

    except FileNotFoundError:
        print("No se encontró el archivo.")
    except TypeError:
        print("No se eligió la bandera (-f).")

args = parser.parse_args() # args es igual a una función del módulo. Se usa para que sea más corta.

#manejo de errores por si no elige un programa.
try:
    if args.d[0] == 'hash':
        Hash()
except TypeError:
    print("ERROR. \nElige un programa y usa las banderas correctas del mismo.")