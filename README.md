# PIA

Ingresa el siguiente comando en tu terminal si tienes alguna duda acerca de las --flags que usa el script y para qué sirve cada una:
```
$ python3 pia.py -h
```

## Tabla de contenidos:
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
Vamos a sacar el hash del archivo [pia.py](https://github.com/zanezhub/PIA-PC/blob/0196c59c88353e11926853e6f9463932f4864f97/pia.py) del commit **0196c59...**
```
$ python3 pia.py -d hash -f pia.py
$ MD5: 7275e5ed4acfe4b1f3f861874dc251a9
```
El hash del archivo [pia.py](https://github.com/zanezhub/PIA-PC/blob/0196c59c88353e11926853e6f9463932f4864f97/pia.py) es **7275e5ed4acfe4b1f3f861874dc251a9**. Si ejecutas el algoritmo en el mismo archivo del commit que se indicó anteriormente el hash siempre será el mismo. En commits más recientes el hash será diferente ya que el script probablemente ya ha sido modificado múltiples veces.

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

#### 3. Encoder:
```
$ python3 pia.py -d encoder
```
Este comando va a ejecutar un script de bash que realizará todo el algoritmo.
```
$ python3 pia.py -d encoder
Introduce el nombre del archivo: <nombre_del_archivo>
```
Esto va a generar un archivo llamado: **archivo_encoded.64**.

#### 4. Decoder:
```
$ python3 pia.py -d decoder
```
Este comando va a ejecutar un script de bash que realizará todo el algoritmo.
```
$ python3 pia.py -d decoder
Introduce el nombre del archivo: <nombre_del_archivo>
```
Esto va a generar un archivo llamado: **archivo_decoded.64**.

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

CVE-2021-40702
Publicado en: 2021-09-27T16:15:00Z  -  Actualizado en: 2021-10-04T13:57:00Z
Adobe Premiere Elements version 2021.2235820 (and earlier) is affected by a memory 
corruption vulnerability due to insecure handling of a malicious psd file, potentially 
resulting in arbitrary code execution in the context of the current user. 
User interaction is required to exploit this vulnerability.

CVE-2021-40703
Publicado en: 2021-09-27T16:15:00Z  -  Actualizado en: 2021-10-04T13:53:00Z
Adobe Premiere Elements version 2021.2235820 (and earlier) is affected by a memory corruption
vulnerability due to insecure handling of a malicious m4a file, potentially resulting in arbitrary
code execution in the context of the current user. User interaction is required to exploit this vulnerability.

CVE-2021-40701
Publicado en: 2021-09-27T16:15:00Z  -  Actualizado en: 2021-10-04T13:51:00Z
Adobe Premiere Elements version 2021.2235820 (and earlier) is affected by a memory 
corruption vulnerability due to insecure handling of a malicious m4a file, potentially
resulting in arbitrary code execution in the context of the current user. 
User interaction is required to exploit this vulnerability.

CVE-2021-40700
Publicado en: 2021-09-27T16:15:00Z  -  Actualizado en: 2021-10-04T13:51:00Z
Adobe Premiere Elements version 2021.2235820 (and earlier) is affected by a 
memory corruption vulnerability due to insecure handling of a malicious TIFF file, 
potentially resulting in arbitrary code execution in the context of the current user. 
User interaction is required to exploit this vulnerability.

CVE-2021-30858
Publicado en: 2021-08-24T19:15:00Z  -  Actualizado en: 2021-10-04T03:15:00Z
A use after free issue was addressed with improved memory management. 
This issue is fixed in iOS 14.8 and iPadOS 14.8, macOS Big Sur 11.6. 
Processing maliciously crafted web content may lead to arbitrary code execution. 
Apple is aware of a report that this issue may have been actively exploited.

CVE-2021-39821
Publicado en: 2021-09-29T16:15:00Z  -  Actualizado en: 2021-10-03T00:10:00Z
Adobe InDesign versions 16.3 (and earlier), and 16.3.1 (and earlier) are affected 
by an out-of-bounds write vulnerability that could result in arbitrary code execution 
in the context of the current user. Exploitation of this issue requires user interaction 
in that a victim must open a malicious TIF file.

CVE-2021-28547
Publicado en: 2021-09-29T16:15:00Z  -  Actualizado en: 2021-10-03T00:07:00Z
Adobe Creative Cloud Desktop Application for macOS version 5.3 (and earlier) is 
affected by a privilege escalation vulnerability that could allow a normal user to 
delete the OOBE directory and get permissions of any directory under the administrator authority.

CVE-2021-39246
Publicado en: 2021-09-24T19:15:00Z  -  Actualizado en: 2021-10-01T13:00:00Z
Tor Browser through 10.5.6 and 11.x through 11.0a4 allows a correlation attack 
that can compromise the privacy of visits to v2 onion addresses. 
Exact timestamps of these onion-service visits are logged locally, and an attacker might be able 
to compare them to timestamp data collected by the destination server 
(or collected by a rogue site within the Tor network).

CVE-2021-40709
Publicado en: 2021-09-27T16:15:00Z  -  Actualizado en: 2021-10-01T12:50:00Z
Adobe Photoshop versions 21.2.11 (and earlier) and 22.5 (and earlier) are affected by a 
Buffer Overflow vulnerability when parsing a specially crafted SVG file. 
An unauthenticated attacker could leverage this vulnerability to achieve 
arbitrary code execution in the context of the current user. Exploitation of this issue requires 
user interaction in that a victim must open a malicious file.

CVE-2021-39828
Publicado en: 2021-09-27T16:15:00Z  -  Actualizado en: 2021-10-01T12:39:00Z
Adobe Digital Editions 4.5.11.187646 (and earlier) are affected by a privilege escalation 
vulnerability in the Digital Editions installer. An authenticated attacker could leverage 
this vulnerability to escalate privileges. User interaction is required before product 
installation to abuse this vulnerability.

CVE-2021-39827
Publicado en: 2021-09-27T16:15:00Z  -  Actualizado en: 2021-10-01T12:36:00Z
Adobe Digital Editions 4.5.11.187646 (and earlier) are affected by an arbitrary
file write vulnerability in the Digital Editions installer. 
An authenticated attacker could leverage this vulnerability to write an a
rbitrary file to the system. User interaction is required before product installation to abuse this vulnerability.

CVE-2021-39826
Publicado en: 2021-09-27T16:15:00Z  -  Actualizado en: 2021-10-01T11:59:00Z
Adobe Digital Editions 4.5.11.187646 (and earlier) are affected by an arbitrary 
command execution vulnerability. An authenticated attacker could leverage this 
vulnerability to execute arbitrary commands. User interaction is required to abuse this
vulnerability in that a user must open a maliciously crafted .epub file.

CVE-2021-30583
Publicado en: 2021-08-03T20:15:00Z  -  Actualizado en: 2021-09-24T23:15:00Z
Insufficient policy enforcement in image handling in iOS in Google Chrome on iOS 
prior to 92.0.4515.107 allowed a remote attacker to leak cross-origin data via a crafted HTML page.

CVE-2021-30860
Publicado en: 2021-08-24T19:15:00Z  -  Actualizado en: 2021-09-24T16:15:00Z
An integer overflow was addressed with improved input validation. 
This issue is fixed in Security Update 2021-005 Catalina, iOS 14.8 and 
iPadOS 14.8, macOS Big Sur 11.6, watchOS 7.6.2. Processing a maliciously 
crafted PDF may lead to arbitrary code execution. Apple is aware of a report that this issue
may have been actively exploited.

CVE-2021-1855
Publicado en: 2021-09-08T15:15:00Z  -  Actualizado en: 2021-09-23T20:35:00Z
A logic issue was addressed with improved state management. This issue is fixed in 
macOS Big Sur 11.3. A malicious website may be able to force unnecessary network connections to fetch its favicon.

CVE-2019-15166
Publicado en: 2019-10-03T17:15:00Z  -  Actualizado en: 2021-09-23T20:15:00Z
lmp_print_data_link_subobjs() in print-lmp.c in tcpdump before 4.9.3 lacks certain bounds checks.

CVE-2020-8284
Publicado en: 2020-12-14T20:15:00Z  -  Actualizado en: 2021-09-23T13:56:00Z
A malicious server can use the FTP PASV response to trick curl 7.73.0 and 
earlier into connecting back to a given IP address and port, and this way potentially 
make curl extract information about services that are otherwise private and not disclosed, 
for example doing port scanning and service banner extractions.
```
(output de Apple de la primera página.)

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

<img alt="OpenCVE" src="img/da-dog.jpg" width="100" height="125">