# PIA
Ingresa el siguiente comando en tu terminal si tienes alguna duda acerca de las --flags que usa el script y para qué sirve cada una:
```
$ python3 pia.py -h
```
## Tabla de contenidos:
| Temas |
|-------|
| [Hash con MD5](#1-hash-con-md5)|
| [Hunter API](#2-hunter-api)  |
| [Base64](#base64)  |
| [OpenCVE API](#5-opencve-api)  |

## Tabla de archivos:
| Archivos | Descripción |
|----------|-------------|
| [main.py](src/main.py) | Este archivo se usará para ejecutar todas las funciones del script que desees, aunque puedes usar el archivo [pia.py](src/pia.py) para usar todas las funciones del script como se muestra en la documentación, solo tendrás que sustituir: ```$ python3 pia.py -d hash -f nombre_archivo``` por: ```$ python3 main.py -d hash -f nombre_archivo``` |
| [pia.py](src/pia.py)  | Este archivo contiene todos las funcione del script.  |
| [decoder.sh](src/decoder.sh) | Este script está hecho con Bash y se usará para obtener la información de un archivo que tenga esté cifrado con el algoritmo de Base64. |
| [encoder.sh](src/encoder.sh) | Este script igualmente está hecho con Bash y se utilizará para encodear cualquier archivo que desees con el algoritmo de Base64. |
| [CVE_TEST4.mp4](docs/vids/CVE_TEST4.mp4)  | Este en un archivo mp4, en el video está una demostración del funcionamiento correcto del API de [**OpenCVE**](https://github.com/zanezhub/PIA-PC#5-opencve-api), la demostración usa los comandos de ejemplo.  |

## 1. Hash con MD5.
### Importancia de los Hash.
Los hash (algunas veces llamado checksum) MD5 se utilizan mucho en el mundo del software para dar seguridad a algunos archivos descargados por Internet para comprobar que este no haya sido alterado. 

Puedes verificar que la información de un archivo no haya sido modificada, no importa cuántas veces ejecutes el algoritmo en un archivo, si el archivo no ha sido modificado el hash siempre será el mismo. 

### Instrucciones de uso:
```
$ python3 pia.py -d hash -f nombre_archivo
```
La bandera **-d** se usa para elegir el programa que quieres usar que en este caso será **hash**, luego la bandera **-f** se usa para elegir el archivo del que quieres saber el hash.

### Ejemplo:
```
$ python3 pia.py -d hash -f pia.py
```
Vamos a sacar el hash del archivo [**pia.py**](https://github.com/zanezhub/PIA-PC/blob/0196c59c88353e11926853e6f9463932f4864f97/pia.py) del commit **0196c59...**
```
$ python3 pia.py -d hash -f pia.py
$ MD5: 7275e5ed4acfe4b1f3f861874dc251a9
```
El hash del archivo [**pia.py**](https://github.com/zanezhub/PIA-PC/blob/0196c59c88353e11926853e6f9463932f4864f97/pia.py) es **7275e5ed4acfe4b1f3f861874dc251a9**. Si ejecutas el algoritmo en el mismo archivo del commit que se indicó anteriormente el hash siempre será el mismo. En commits más recientes el hash será diferente ya que el script probablemente ya ha sido modificado múltiples veces.

Todo esto te va a generar los siguientes archivos:
* [**hash.log**](docs/reportes/hash/hash.log) Aquí se van a guardar todas las cosas relacionadas con el programa, si tuvo un fallo, si se ejecutó correctamente y la fecha en que se ejecutó tal fallo.
* [**hashes.txt**](docs/reportes/hashes.txt) Aquí se guardarán los hashes de los archivos con el siguiente formato:
```
fecha en la que se ejecutó el script
nombre del archivo
hash del archivo
```

## 2. [Hunter API](https://hunter.io/)
<img src="img/hunter_logo.png" width="150" height="150"> 

El **API** que se usa en este script es **[Email Verification](https://hunter.io/verify)**.

### Instrucciones de uso:
```
$ python3 pia.py -d hunter -m <email@example.com> -k <api-key>
```
La bandera **-d** se usa para elegir el programa que quieres usar que en este caso será **api**, **-m** se usará para elegir el email y **-k** se usará para elegir el API key que quieres utilizar. 

#### API KEY:
Si deseas utilizar el script ten en cuenta que necesitas poseer una API Key de la página, podrás obtener una si te registrar en la misma.

### ¿Por qué es importante esta API?
No importa si estás mandando un email relacionado con una campaña o si mandas un correo común y corriente. Lo primero que se debe hacer es revisar la veracidad de los correos.

Usando esta API puedes limpiar toda tu lista de emails, filtrando correos de spam que causan **bounces** (cuando mandas un correo y este nunca llega a la dirección del correo porque se ha cancelado o no pudo ser entregado y el servidor del email lo devuelve al remitente).

* Puedes eliminar emails que no son útiles de tu base de datos.
Lo cual puede incrementar la tasa de entrega, evitando que algunos correos se pierdan o no lleguen a los emails correctos.

* Proteger tu reputación.
Todo correo tiene un puntaje de reputación, el cual es totalmente escencial para entregar correos por el internet.
Si tu puntaje es alto, es muy probable que tu proveedor de Internet ( **ISP** ) va a entregar tus emails a los correos indicados. Existen algunos factores que imapactan tu reputación _(spam complaints, spam traps, sending history, engagement, unsubscribes.)_.

### Pruebas usadas en la API:
* **Formato válido:** Primero, se verifica que el formato de correo sea correcto ( email@provider.com )
* **Correo basura:** Nos aseguramos que la dirección de correo no sea algo aleatorio. Por ejemplo 123sdh7l0sj@compañía.com no pasa la prueba.
* **Correo desechable:** Verificamos si la dirección del correo tiene un nombre del dominio que se usa para direcciones de correo temporales.
* **Dirección _Webmail_:** Verificamos si el email usa un webmail como *Gmail* o *Yahoo*.
* **Presencia de los MX Records:** Revisamos si existen intercambios de correos (Mail Exchange) (MX) records en el dominio. Basicamente un MX record apunta al SMTP mail server usado para recibir emails. Si no hay MX records, los emails enviados a ese dominio no pueden ser entregados.
* **Presencia del SMTP Server:** Esta prueba se pasa si somos capaces de conectarnos al **SMTP server** (indicado en MX records).
* **SMTP Check:** Se prueba si la dirección email para saber si esta existe. En caso de que el **SMTP server** no nos permita realizar esta acción, marcaremos el email como "Blocked".
* **Accept-All Domain:** Se revisa si el servicio de email tiene algo conocido como *catch-all policy* que acepta todos los emails que son recibidos.

### Links:
* https://hunter.io/
* https://hunter.io/blog/how-to-verify-email-address/
* https://help.hunter.io/en/articles1935168-what-checks-are-performed-on-an-email-with-the-email-verifier

## Base64
La codificación **Base64** es una forma de tomar datos binarios y convertirlos en texto para que se transmitan más fácilmente en cosas como correo electrónico y datos de formularios HTML.

### 3. Encoder:
#### Instrucciones:
```
$ python3 pia.py -d encoder
Introduce el nombre del archivo: <nombre_del_archivo>
```
Ingresas el nombre del archivo que deseas y todo el algoritmo se realizará por sí mismo. Dando como resultado un archivo llamado: **<nombre_del_archivo>_encoded.64**

#### Ejemplo:
```
$ python3 pia.py -d encoder
Introduce el nombre del archivo: pia.py
```
Esto va a generar el archivo [**pia.py_encoded.b64**](docs/reportes/base64/pia.py_encoded.b64) y este tendrá el siguiente output:
```
IyEvdXNyL2Jpbi9lbnYgcHl0aG9uMwoKIyBTZSB1c2FuIG3DoXMgZGUgMyBtw7NkdWxvcy4KaW1w
b3J0IGFyZ3BhcnNlCmltcG9ydCBoYXNobGliICMgTcOzZHVsbyBubyB2aXN0byBlbiBjbGFzZS4K
ZnJvbSBqc29uIGltcG9ydCBsb2Fkcwpmcm9tIHJlcXVlc3RzIGltcG9ydCBnZXQKZnJvbSB0aW1l
IGltcG9ydCBhc2N0aW1lLCBsb2NhbHRpbWUsIHRpbWUKZnJvbSBzdWJwcm9jZXNzIGltcG9ydCBy
dW4KCiNTZSB1c2EgcGFyYSBxdWUgc2VhIG3DoXMgZW50ZW5kaWJsZSB5IGNvcnRvIGVsIG5vbWJy
ZS4KcGFyc2VyID0gYXJncGFyc2UuQXJndW1lbnRQYXJzZXIoKSAKcGFyc2VyLmFkZF9hcmd1bWVu
dCgnLWQnLCBuYXJncz0xLCB0eXBlPXN0ciwgaGVscD0nZWxpZ2UgbGEgZnVuY2nDs24gYSB1c2Fy
LicsCiAgICAgICAgICAgICAgICAgICAgY2hvaWNlcz1bJ2hhc2gnLCAnaHVudGVyJywgJ2VuY29k
ZXInLCAnZGVjb2RlcicsICdjdmUnXSkKcGFyc2VyLmFkZF9hcmd1bWVudCgnLWYnLCAnLS1maWxl
JywgbmFyZ3M9MSAsdHlwZT1zdHIsIGhlbHA9J25vbWJyZSBkZWwgYXJjaGl2by4nKQpwYXJzZXIu
YWRkX2FyZ3VtZW50KCctbScsICctLW1haWwnLCBuYXJncz0xLCB0eXBlPXN0ciwgaGVscD0nbm9t
YnJlIGRlbCBjb3JyZW8gcXVlIGRlc2VhcyBidXNjYXIuJykKcGFyc2VyLmFkZF9hcmd1bWVudCgn
LWsnLCAnLS1rZXknLCBuYXJncz0xLCB0eXBlPXN0ciwgaGVscD0ndXNhIHR1IHByb3BpYSBhcGkg
a2V5IHBhcmEgbGEgYXBpIGRlIGh1bnRlci5pbycpCnBhcnNlci5hZGRfYXJndW1lbnQoJy1lJywg
Jy0tZW1wcmVzYScsIG5hcmdzPTEsIHR5cGU9c3RyLCBoZWxwPSdpbmdyZXNhIGVsIG5vbWJyZSBk
ZSBsYSBlbXByZXNhIHF1ZSBxdWllcmVzIGludmVzdGlnYXInKQpwYXJzZXIuYWRkX2FyZ3VtZW50
KCctcCcsICctLXBhZ2UnLCBuYXJncz0xLCB0eXBlPWludCwgaGVscD0naW5ncmVzYSBlbCBuw7pt
ZXJvIGRlIGxhIHDDoWdpbmEgcXVlIHF1aWVyZXMgb2J0ZW5lcicpCnBhcnNlci5hZGRfYXJndW1l
bnQoJy1hJywgJy0tYXV0aCcsIG5hcmdzPTIsIHR5cGU9c3RyLCBoZWxwPSdpbmdlc2EgdHUgdXN1
YXJpbyB5IGNvbnRyYXNlw7FhIHBhcmEgcG9kZXIgdXNhciBsYSBhcGknKQoKYXJncyA9IHBhcnNl
ci5wYXJzZV9hcmdzKCkgIyBhcmdzIGVzIGlndWFsIGEgdW5hIGZ1bmNpw7NuIGRlbCBtw7NkdWxv
LiBTZSB1c2EgcGFyYSBxdWUgc2VhIG3DoXMgY29ydGEuCgoKI21hbmVqbyBkZSBlcnJvcmVzIHBv
ciBzaSBubyBlbGlnZSB1biBwcm9ncmFtYS4KdHJ5OgogICAgaWYgYXJncy5kWzBdID09ICdoYXNo
JzoKICAgICAgICBCVUZfU0laRSA9IDY1NTM1ICMgU2UgdXNhIHBhcmEgbGVlciBhcmNoaXZvcyBl
biA2NGtiCiAgICAgICAgbWQ1ID0gaGFzaGxpYi5tZDUoKQogICAgICAgICNtYW5lam8gZGUgZXJy
b3Jlcy4KICAgICAgICB0cnk6CiAgICAgICAgICAgIHdpdGggb3BlbihhcmdzLmZpbGVbLTFdLCAn
cmInKSBhcyBmOgogICAgICAgICAgICAgICAgd2hpbGUgVHJ1ZToKICAgICAgICAgICAgICAgICAg
ICBkYXRhID0gZi5yZWFkKEJVRl9TSVpFKQoKICAgICAgICAgICAgICAgICAgICAjIHJvbXBsZSBl
bCBjaWNsbyBzaSBubyBoYXkgbcOhcyBkYXRhIHF1ZSBsZWVyLgogICAgICAgICAgICAgICAgICAg
IGlmIG5vdCBkYXRhOgogICAgICAgICAgICAgICAgICAgICAgICBicmVhawogICAgICAgICAgICAg
ICAgICAgIG1kNS51cGRhdGUoZGF0YSkKCiAgICAgICAgICAgICNHVUFSREFSIFRPRE8gRU4gVU4g
QVJDSElWTwogICAgICAgICAgICBsb2NhbHRpbWUgPSBhc2N0aW1lKCBsb2NhbHRpbWUodGltZSgp
KSApCiAgICAgICAgICAgIHdpdGggb3BlbigicmVwb3J0ZS50eHQiLCAnYScpIGFzIHI6CiAgICAg
ICAgICAgICAgICByLndyaXRlKGxvY2FsdGltZSsiXG4iK2FyZ3MuZmlsZVstMV0rIlxuTUQ1OiB7
MH0iLmZvcm1hdChtZDUuaGV4ZGlnZXN0KCkpKyJcblxuIikKICAgICAgICBleGNlcHQgRmlsZU5v
dEZvdW5kRXJyb3I6CiAgICAgICAgICAgIHByaW50KCJObyBzZSBlbmNvbnRyw7MgZWwgYXJjaGl2
by4iKQogICAgICAgIGV4Y2VwdCBUeXBlRXJyb3I6CiAgICAgICAgICAgIHByaW50KCJObyBzZSBl
bGlnacOzIGxhIGJhbmRlcmEgLWYuIikKCiAgICBlbGlmIGFyZ3MuZFswXSA9PSAnaHVudGVyJzoK
ICAgICAgICB0cnk6CiAgICAgICAgICAgIG1haWwgPSBhcmdzLm1haWxbMF0KICAgICAgICAgICAg
a2V5ID0gYXJncy5rZXlbMF0KICAgICAgICAgICAgIyBiZDIyNWE4OWQ5NGYwMTRkM2ZiOThhN2I2
YzJlY2FjZjViZTEwNWRjCiAgICAgICAgICAgIHVybCA9IGYiaHR0cHM6Ly9hcGkuaHVudGVyLmlv
L3YyL2VtYWlsLXZlcmlmaWVyP2VtYWlsPXttYWlsfSZhcGlfa2V5PXtrZXl9IgogICAgICAgICAg
ICByZXNwb25zZSA9IGdldCh1cmwpLnRleHQKICAgICAgICAgICAgZGF0YSA9IGxvYWRzKHJlc3Bv
bnNlKQogICAgICAgICAgICBwcmludCgiRW1haWw6ICIgKyBkYXRhWydkYXRhJ11bJ2VtYWlsJ11c
CiAgICAgICAgICAgICAgICArICJcbldlYm1haWw6ICIgKyBzdHIoZGF0YVsnZGF0YSddWyd3ZWJt
YWlsJ10pICsgIlxuIlwKICAgICAgICAgICAgICAgICsgIlxuUmVzdWx0YWRvOiAiICsgZGF0YVsn
ZGF0YSddWydyZXN1bHQnXVwKICAgICAgICAgICAgICAgICsgIlxuUHVudHVhY2nDs246ICIgKyBz
dHIoZGF0YVsnZGF0YSddWydzY29yZSddKVwKICAgICAgICAgICAgICAgICsgIlxuQ29ycmVvIGJh
c3VyYTogIiArIHN0cihkYXRhWydkYXRhJ11bJ2dpYmJlcmlzaCddKVwKICAgICAgICAgICAgICAg
ICsgIlxuQ29ycmVvIGRlc2VjaGFibGU6ICIgKyBzdHIoZGF0YVsnZGF0YSddWydkaXNwb3NhYmxl
J10pXAogICAgICAgICAgICAgICAgKyAiXG5NWCBSZWNvcmRzOiAiICsgc3RyKGRhdGFbJ2RhdGEn
XVsnbXhfcmVjb3JkcyddKVwKICAgICAgICAgICAgICAgICsgIlxuUHJlc2VuY2lhIGRlIFNNVFAg
U2VydmVyOiAiICsgc3RyKGRhdGFbJ2RhdGEnXVsnc210cF9zZXJ2ZXInXSlcCiAgICAgICAgICAg
ICAgICArICJcblNNVFAgQ2hlY2s6ICIgKyBzdHIoZGF0YVsnZGF0YSddWydzbXRwX2NoZWNrJ10p
XAogICAgICAgICAgICAgICAgKyAiXG5BY2NlcHQgQWxsOiAiICsgc3RyKGRhdGFbJ2RhdGEnXVsn
YWNjZXB0X2FsbCddKSApCgogICAgICAgIGV4Y2VwdCBUeXBlRXJyb3I6CiAgICAgICAgICAgIHBy
aW50KCJObyBzZSBlbGlnaWVyb24gYmFuZGVyYXMgY29ycmVjdG9zIG8gZmFsdGFuIGFsZ3Vub3Mg
YXJndW1lbnRvcy4iKQoKICAgIGVsaWYgYXJncy5kWzBdID09ICdjdmUnOgogICAgICAgIHJlc3Bv
bnNlID0gZ2V0KGYiaHR0cHM6Ly93d3cub3BlbmN2ZS5pby9hcGkvdmVuZG9ycy97YXJncy5lbXBy
ZXNhWzBdfS9jdmU/cGFnZT17YXJncy5wYWdlWzBdfSIsIGF1dGg9KGFyZ3MuYXV0aFswXSwgYXJn
cy5hdXRoWzFdKSkudGV4dAogICAgICAgIGRhdGEgPSBsb2FkcyhyZXNwb25zZSkKICAgICAgICB4
ID0gMAogICAgICAgIHdoaWxlIFRydWU6CiAgICAgICAgICAgIHRyeToKICAgICAgICAgICAgICAg
IHByaW50KGRhdGFbeF1bJ2lkJ10pCiAgICAgICAgICAgICAgICBwcmludCgiUHVibGljYWRvIGVu
OiAiICsgZGF0YVt4XVsnY3JlYXRlZF9hdCddICsgIiAgLSAgIiAgKyAiQWN0dWFsaXphZG8gZW46
ICIgKyBkYXRhW3hdWyd1cGRhdGVkX2F0J10pCiAgICAgICAgICAgICAgICBwcmludChkYXRhW3hd
WydzdW1tYXJ5J10rIlxuIikKICAgICAgICAgICAgICAgIHggKz0gMQogICAgICAgICAgICBleGNl
cHQgSW5kZXhFcnJvcjoKICAgICAgICAgICAgICAgIGJyZWFrCgogICAgZWxpZiBhcmdzLmRbMF0g
PT0gJ2VuY29kZXInOgogICAgICAgIHJ1bihbImJhc2giLCAiZW5jb2Rlci5zaCJdKQoKICAgIGVs
aWYgYXJncy5kWzBdID09ICdkZWNvZGVyJzoKICAgICAgICBydW4oWyJiYXNoIiwgImRlY29kZXIu
c2giXSkKCmV4Y2VwdCBUeXBlRXJyb3I6CiAgICBwcmludCgiRVJST1IuIEVsaWdlIHVuIHByb2dy
YW1hIHkgdXNhIGxhcyBiYW5kZXJhcyBjb3JyZWN0YXMgZGVsIG1pc21vLiIpCg==
```

### 4. Decoder:
#### Instrucciones:
```
$ python3 pia.py -d decoder
Introduce el nombre del archivo: <nombre_del_archivo>
```
Ingresas el nombre del archivo que deseas y todo el algoritmo se realizará por sí mismo. Dando como resultado un archivo llamado: **<nombre_del_archivo>_decoded.64**

#### Ejemplo:
Tomando todo el output del ejemplo anterior ([**pia.py_encoded.b64**](docs/reportes/base64/pia.py_encoded.b64)) y ejecutando el siguiente comando sobre él:
```
$ python3 pia.py -d decoder
Introduce el nombre del archivo: pia.py_encoded.b64
```
Te va a generar el archivo [**pia.py_encoded.b64_decoded.b64**](docs/reportes/base64/pia.py_encoded.b64_decoded.b64) y podrás ver que todo esto te va a dar como resultado un archivo .py que fue encodeado previamente.

## 5. OpenCVE API:
<p align="center">
  <img alt="OpenCVE" src="https://raw.githubusercontent.com/opencve/opencve/master/logo.png">
</p>

### ¿Qué es?
[**OpenCVE**](https://github.com/opencve/opencve) se utiliza para almacenar todos los **CVE** (Common Vulnerabilities and Exposures) de manera local, también se puede hostear en una página web si es necesario.

### ¿Por qué es importante?
Es necesario estar al tanto de las vulnerabilidades en software y hardware, para aprender de todas estas vulnerabilidades, para protegerse y para estar informado sobre todo lo que está pasando en este campo laboral. Una persona que conoce acerca de esto y está al día con todo lo que está pasando tiene un mayor conocimiento, mayor experiencia y mayor práctica en los temas de seguridad informática.

Las CVE tienen descripción de la vulnerabilidad, qué versiones del software están afectadas, posible solución al fallo (si existe) o como configurar para mitigar la vulnerabilidad y referencias a publicaciones o entradas de foros o blog donde se ha hecho pública la vulnerabilidad o se demuestra su explotación. Además suele también mostrarse un enlace directo a la información de la base de datos de vulnerabilidades del NIST (NVD), en la que pueden conseguirse más detalles de la vulnerabilidad y su valoración.

### Instrucciones de uso:
```
$ python3 pia.py -d cve -e <empresa> -p <pagina> -a <usuario> <contraseña>
```
* **-a**: La autentificación sirve para que la API te pueda dar los permisos adecuados para acceder al REST API que proporciona, en este caso tendrás que registrarse en la página e ingresar en el script tu usuario y contraseña.

### Ejemplo:
```
$ python3 pia.py -d cve -e apple -p 1 -a <usuario> <contraseña>
```
[**Video de demostración.**](docs/vids/CVE_TEST4.mp4)

Si ejecutas este comando en tu terminal el **output** que te dará será el siguiente:
```
CVE-2021-1810
Publicado en: 2021-09-08T15:15:00Z  -  Actualizado en: 2021-10-04T18:15:00Z
A logic issue was addressed with improved state management. 
This issue is fixed in macOS Big Sur 11.3, Security Update 2021-002 Catalina. 
A malicious application may bypass Gatekeeper checks.

CVE-2021-3747
Publicado en: 2021-10-01T03:15:00Z  -  Actualizado en: 2021-10-04T17:59:00Z
The MacOS version of Multipass, version 1.7.0, fixed in 1.7.2, accidentally 
installed the application directory with incorrect owner.

CVE-2021-40708
Publicado en: 2021-09-29T16:15:00Z  -  Actualizado en: 2021-10-04T16:02:00Z
Adobe Genuine Service versions 7.3 (and earlier) are affected by a privilege 
escalation vulnerability in the AGSService installer. An authenticated attacker could 
leverage this vulnerability to achieve read / write privileges to execute arbitrary code.
User interaction is required to abuse this vulnerability.

....
```

[**CVE de Apple de la primera página.**](docs/reportes/cve/CVE_TEST4_PAG1.txt)

Como puedes ver en el **output** tiene la siguiente forma:
```
CVE-ID
Publicado en: Fecha en la que la vulnerabilidad fue publicada  -  Actualizado en: Fecha en la que se actualizó
Resumen de la vulnerabilidad
```
Si estas interesado en saber más acerca de esta vulnerabilidad lo único que tienes que hacer es buscar el **CVE-ID** y empezar a investigar todo lo relacionado con ello, siempre habrá blogs acerca de la vulnerabilidad explicando a detalle cómo funciona, qué afecta y cómo se puede recrear.

La fecha en la que una vulnerabilidad fue actualizada generalmente tiene que ver con los patches para las vulnerabilidades que fueron descubiertas, los patches se aplican en el software para corregir todos los errores/vulenrabilidades del mismo.

La descripción te dirá una descripción de la vulnerabilidad, si tiene una solución, cuándo se arregló si es que ya se ha solucionado, lo que se puede hacer con la vulnerabilidad (si es que se puede ejecutar código remoto) y si es necesario que un usuario interactue para que se pueda usar. No siempre se muestra esta información, pero lo de que puedes estar seguro es que siempre habrá un resumen para cada vulnerabilidad.

### Links:
* Github: https://github.com/opencve/opencve
* Página web: https://www.opencve.io/welcome
* Documentación de API: https://docs.opencve.io/api/

<img src="img/walter.jpg" width="300" height="300">