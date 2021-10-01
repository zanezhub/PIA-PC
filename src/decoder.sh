#!/usr/bin/env bash

read -p "Introduce el nombre del archivo: " archivo
base64 -d "$archivo" > "$archivo"_decoded.b64