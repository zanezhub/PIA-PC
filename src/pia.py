#!/usr/bin/env python3

# Se usan más de 3 módulos.
import time
import argparse
import hashlib
import json
import requests
import subprocess

#Se usa para que sea más entendible y corto el nombre.
parser = argparse.ArgumentParser() 
parser.add_argument('-d', nargs=1, type=str, help='elige la función a usar.',
                    choices=['hash', 'hunter', 'encoder', 'decoder', 'cve'])
parser.add_argument('-f', '--file', nargs=1 ,type=str, help='nombre del archivo.')
parser.add_argument('-m', '--mail', nargs=1, type=str, help='nombre del correo que deseas buscar.')
parser.add_argument('-k', '--key', nargs=1, type=str, help='usa tu propia api key para la api de hunter.io')
parser.add_argument('-e', '--empresa', nargs=1, type=str, help='ingresa el nombre de la empresa que quieres investigar')
parser.add_argument('-p', '--page', nargs=1, type=int, help='ingresa el número de la página que quieres obtener')
parser.add_argument('-a', '--auth', nargs=2, type=str, help='ingesa tu usuario y contraseña para poder usar la api')

args = parser.parse_args() # args es igual a una función del módulo. Se usa para que sea más corta.


#manejo de errores por si no elige un programa.
try:
    if args.d[0] == 'hash':
        BUF_SIZE = 65535 # Se usa para leer archivos en 64kb
        md5 = hashlib.md5()
        #manejo de errores.
        try:
            with open(args.file[-1], 'rb') as f:
                while True:
                    data = f.read(BUF_SIZE)

                    # romple el ciclo si no hay más data que leer.
                    if not data:
                        break
                    md5.update(data)

            #GUARDAR TODO EN UN ARCHIVO
            localtime = time.asctime( time.localtime(time.time()) )
            with open("reporte.txt", 'a') as r:
                r.write(localtime+"\n"+args.file[-1]+"\nMD5: {0}".format(md5.hexdigest())+"\n\n")
        except FileNotFoundError:
            print("No se encontró el archivo.")
        except TypeError:
            print("No se eligió la bandera -f.")

    elif args.d[0] == 'hunter':
        try:
            mail = args.mail[0]
            key = args.key[0]
            # bd225a89d94f014d3fb98a7b6c2ecacf5be105dc

            url = f"https://api.hunter.io/v2/email-verifier?email={mail}&api_key={key}"
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
        except TypeError:
            print("No se eligieron banderas correctos o faltan algunos argumentos.")

    elif args.d[0] == 'cve':
        response = requests.get(f"https://www.opencve.io/api/vendors/{args.empresa[0]}/cve?page={args.page[0]}", auth=(args.auth[0], args.auth[1])).text
        data = json.loads(response)

        x = 0
        while True:
            try:
                print(data[x]['id'] + "  -  " + data[x]['created_at'])
                print(data[x]['summary']+"\n")
                x += 1
            except IndexError:
                break

    elif args.d[0] == 'encoder':
        subprocess.run(["bash", "encoder.sh"])

    elif args.d[0] == 'decoder':
        subprocess.run(["bash", "decoder.sh"])

except TypeError:
    print("ERROR. Elige un programa y usa las banderas correctas del mismo.")
