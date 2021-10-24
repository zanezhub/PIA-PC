#!/usr/bin/env python3
import argparse
from json       import loads
from requests   import get

#Se usa para que sea más entendible y corto el nombre.
parser = argparse.ArgumentParser() 
parser.add_argument('-d', nargs=1, type=str, help='elige la función a usar.',
                    choices=['hash', 'hunter', 'encoder', 'decoder', 'cve', 'bw'])
parser.add_argument('-f', '--file', nargs=1 ,type=str, help='nombre del archivo.')
parser.add_argument('-m', '--mail', nargs=1, type=str, help='nombre del correo que deseas buscar.')
parser.add_argument('-k', '--key', nargs=1, type=str, help='usa tu propia api key para la api de hunter.io.')
parser.add_argument('-e', '--empresa', nargs=1, type=str, help='ingresa el nombre de la empresa que quieres investigar.')
parser.add_argument('-p', '--page', nargs=1, type=int, help='ingresa el número de la página que quieres obtener.')
parser.add_argument('-a', '--auth', nargs=2, type=str, help='ingesa tu usuario y contraseña para poder usar la api.')
parser.add_argument('-w', '--web', nargs=1, type=str, help='ingresa la página web que quieres investigar.')

args = parser.parse_args() # args es igual a una función del módulo. Se usa para que sea más corta.

try:  #manejo de errores por si no elige un programa.
    if args.d[0] == 'hash':
        import logging
        from time       import asctime, localtime, time
        import hashlib  # Módulo no visto en clase.

        logging.basicConfig(filename='hash.log', format='%(levelname)s | %(asctime)s - %(message)s', level=logging.DEBUG)

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
            localtime = asctime( localtime(time()) )
            with open("hashes.txt", 'a') as r:
                r.write(localtime+"\n"+args.file[-1]+"\nMD5: {0}".format(md5.hexdigest())+"\n\n")
            logging.info('El script se utilizó correctamente')

        except FileNotFoundError:
            logging.critical('No se encontró el archivo.')
        except TypeError:
            logging.critical('No se usaron las banderas necesarias.')

    elif args.d[0] == 'hunter':
        try:
            mail = args.mail[0]
            key = args.key[0]
            #  bd225a89d94f014d3fb98a7b6c2ecacf5be105dc

            url = f"https://api.hunter.io/v2/email-verifier?email={mail}&api_key={key}"
            response = get(url).text
            data = loads(response)
            print("Email: " + data['data']['email']+ "\nWebmail: " + str(data['data']['webmail']) + "\n" + "\nResultado: " + data['data']['result'] + "\nPuntuación: " + str(data['data']['score']) + "\nCorreo basura: " + str(data['data']['gibberish']) + "\nCorreo desechable: " + str(data['data']['disposable']) + "\nMX Records: " + str(data['data']['mx_records']) + "\nPresencia de SMTP Server: " + str(data['data']['smtp_server']) + "\nSMTP Check: " + str(data['data']['smtp_check']) + "\nAccept All: " + str(data['data']['accept_all']) )
        except TypeError:
            print("No se eligieron banderas correctos o faltan algunos argumentos.")

    elif args.d[0] == 'cve':
        from time       import asctime, localtime, time
        response = get(f"https://www.opencve.io/api/vendors/{args.empresa[0]}/cve?page={args.page[0]}", auth=(args.auth[0], args.auth[1])).text
        data = loads(response)
        localtime = asctime( localtime(time()) )
        x = 0
        while True:
            try:
                with open(f'CVE - {localtime}.txt', 'a') as f:
                    f.write(data[x]['id']+"\n")
                    f.write("Publicado en: " + data[x]['created_at'] + "  -  "  + "Actualizado en: " + data[x]['updated_at']+"\n")
                    f.write(data[x]['summary']+"\n\n")
                x += 1
            except IndexError:
                break

    elif args.d[0] == 'bw':
        from builtwith import parse # Modulo no nativo de python

        info = parse(args.web[0]) #dict
        for key,value in info.items():
            print(key, "->",value)

    elif args.d[0] == 'encoder':
        from subprocess import run
        run(["bash", "encoder.sh"])

    elif args.d[0] == 'decoder':
        from subprocess import run
        run(["bash", "decoder.sh"])
    
except TypeError:
    print("ERROR. Elige un programa y usa las banderas correctas del mismo.")
