#!/usr/bin/env python3

# Se usan más de 3 módulos.
import argparse
import hashlib
import requests
import json

#Se usa para que sea más entendible y corto el nombre.
parser = argparse.ArgumentParser() 
parser.add_argument('-d', nargs=1, type=str, help='elige la función a usar.',
                    choices=['hash', 'api'])
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

def ApiSec():
    url = "https://api.hunter.io/v2/email-verifier?email=zanez@protonmail.com&api_key=bd225a89d94f014d3fb98a7b6c2ecacf5be105dc"
    response = requests.get(url).text
    data = json.loads(response)

    print("Email: " + data['data']['email']\
        + "\nWebmail: " + str(data['data']['webmail']) + "\n"\
         + "\nResultado: " + data['data']['result']\
              + "\nPuntuación: " + str(data['data']['score'])\
                   + "\nCorreo basura: " + str(data['data']['gibberish'])\
                        + "\nCorreo desechable: " + str(data['data']['disposable'])\
                             + "\nMX Records: " + str(data['data']['mx_records'])\
                                  + "\nPresencia de SMTP Server: " + str(data['data']['smtp_server'])\
                                       + "\nSMTP Check: " + str(data['data']['smtp_check'])\
                                            + "\nAccept All: " + str(data['data']['accept_all']) )

args = parser.parse_args() # args es igual a una función del módulo. Se usa para que sea más corta.

#manejo de errores por si no elige un programa.
try:
    if args.d[0] == 'hash':
        Hash()
    elif args.d[0] == 'api':
        ApiSec()
except TypeError:
    print("ERROR. \nElige un programa y usa las banderas correctas del mismo.")