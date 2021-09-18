#!/usr/bin/env python3

import argparse
import hashlib

def Hash():
    #Se usa para que sea más entendible y corto el nombre.
    parser = argparse.ArgumentParser() 
    parser.add_argument('-f', '--file', nargs=1 ,type=str, help='nombre del archivo.')

    args = parser.parse_args() # args es igual a una función del módulo. Se usa para que sea más corta.
    
    BUF_SIZE = 65536
    md5 = hashlib.md5()
    with open(args.file[0], 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            md5.update(data)
    print("MD5: {0}".format(md5.hexdigest()))

Hash()

