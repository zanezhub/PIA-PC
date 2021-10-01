#!/bin/bash
read -p "Introduce el nombre del archivo: " archivo
base64 "$archivo" > "$archivo"_encoded.b64
