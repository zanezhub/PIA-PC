# PIA (･ัω･ั)

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
<img src="images/hunter_logo.png" width="150" height="150"> 

El **API** que se usa en este script es **[Email Verification](https://hunter.io/verify)**.

### Instrucciones de uso:
```
$ python3 pia.py -d api
```
La bandera **-d** se usa para elegir el programa que quieres usar que en este caso será **api**. 

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
$ python3 pia.py -d cve 
```

Si ejecutas este comando en tu terminal el **output** que te dará será el siguiente:

```
CVE-2021-30583  -  2021-08-03T20:15:00Z
Insufficient policy enforcement in image handling in iOS in Google Chrome
on iOS prior to 92.0.4515.107 allowed a remote attacker to leak cross-origin data via a crafted HTML page.

CVE-2021-30858  -  2021-08-24T19:15:00Z
A use after free issue was addressed with improved memory management. This issue is fixed 
in iOS 14.8 and iPadOS 14.8, macOS Big Sur 11.6. Processing maliciously crafted web content may lead to 
arbitrary code execution. 
Apple is aware of a report that this issue may have been actively exploited.

CVE-2021-30860  -  2021-08-24T19:15:00Z
An integer overflow was addressed with improved input validation. This issue is fixed in 
Security Update 2021-005 Catalina, iOS 14.8 and iPadOS 14.8, macOS Big Sur 11.6, watchOS 7.6.2. Processing a 
maliciously crafted PDF may lead to arbitrary code execution. Apple is aware of a report that this issue may have 
been actively exploited.

CVE-2021-1855  -  2021-09-08T15:15:00Z
A logic issue was addressed with improved state management. This issue is fixed in macOS Big Sur 11.3.
A malicious website may be able to force unnecessary network connections to fetch its favicon.

CVE-2019-15166  -  2019-10-03T17:15:00Z
lmp_print_data_link_subobjs() in print-lmp.c in tcpdump before 4.9.3 lacks certain bounds checks.

CVE-2020-8284  -  2020-12-14T20:15:00Z
A malicious server can use the FTP PASV response to trick curl 7.73.0 and earlier into connecting
back to a given IP address and port, and this way potentially make curl extract information about services 
that are otherwise private and not disclosed, for example doing port scanning and service banner extractions.

CVE-2021-21300  -  2021-03-09T20:15:00Z
Git is an open-source distributed revision control system. In affected versions of Git a specially crafted 
repository that contains symbolic links as well as files using a clean/smudge filter such as Git LFS, 
may cause just-checked out script to be executed while cloning onto a case-insensitive file system such as NTFS, 
HFS+ or APFS (i.e. the default file systems on Windows and macOS). Note that clean/smudge filters have to be 
configured for that. 
Git for Windows configures Git LFS by default, and is therefore vulnerable. The problem has been patched in the 
versions published on Tuesday, March 9th, 2021. As a workaound, if symbolic link support is disabled in Git 
(e.g. via `git config --global core.symlinks false`), the described attack won't work. Likewise, if no
clean/smudge filters such as Git LFS are configured globally (i.e. _before_ cloning), the attack is foiled. 
As always, it is best to avoid cloning repositories from untrusted sources. The earliest impacted version 
is 2.14.2. The fix versions are: 2.30.1, 2.29.3, 2.28.1, 2.27.1, 2.26.3, 2.25.5,
2.24.4, 2.23.4,2.22.5, 2.21.4, 2.20.5, 2.19.6, 2.18.5, 2.17.62.17.6.

CVE-2020-29075  -  2021-02-23T04:15:00Z
Acrobat Reader DC versions 2020.013.20066 (and earlier), 2020.001.30010 (and earlier) and 2017.011.30180 
(and earlier) are affected by an information exposure vulnerability, that could enable an attacker to get a 
DNS interaction and track if the user has opened or closed a PDF file when loaded from the filesystem without 
a prompt.User interaction is required to exploit this vulnerability.

CVE-2017-3099  -  2017-07-17T13:18:00Z
Adobe Flash Player versions 26.0.0.131 and earlier have an exploitable memory corruption vulnerability in 
the Action Script 3 raster data model. Successful exploitation could lead to arbitrary code execution.
```
(output de Apple de la primera página.)

Como puedes ver en el **output** tiene la siguiente forma:
```
CVE-ID  -  Fecha en la que fue publicado
Resumen de la vulnerabilidad
```
Si estas interesado en saber más acerca de esta vulnerabilidad lo único que tienes que hacer es buscar el **CVE-ID** y empezar a investigar todo lo relacionado con ello, siempre habrá blogs acerca de la vulnerabilidad explicando a detalle cómo funciona, qué afecta y cómo se puede recrear.

### Links:
* Github: https://github.com/opencve/opencve
* Página web: https://www.opencve.io/welcome
* Documentación de API: https://docs.opencve.io/api/
