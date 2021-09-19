# PIA.
## El Script.
### Hunter API.
<img src="images/hunter_logo.png" width="150" height="150"> 

El **API** que se usa en este script es **Email Verification**.
#### Intrucciones de uso:
```
python pia.py -d api
```

#### ¿Por qué es importante esta API?
No importa si estás mandando un email relacionado con una campaña o si mandas un correo común y corriente. Lo primero que se debe hacer es revisar la veracidad de los correos.

Usando esta API puedes limpiar toda tu lista de emails, filtrando correos de spam que causan **bounces** (cuando mandas un correo y este nunca llega a la dirección del correo porque se ha cancelado o no pudo ser entregado y el servidor del email lo devuelve al remitente).

* Puedes eliminar emails que no son útiles de tu base de datos.
Lo cual puede incrementar la tasa de entrega, evitando que algunos correos se pierdan o no lleguen a los emails correctos.

* Proteger tu reputación.
Todo correo tiene un puntaje de reputación, el cual es totalmente escencial para entregar correos por el internet.
Si tu puntaje es alto, es muy probable que tu proveedor de Internet ( **ISP** ) va a entregar tus emails a los correos indicados. Existen algunos factores que imapactan tu reputación _( spam complaints, spam traps, sending history, engagement, unsubscribes. )_.

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


## Instrucciones del PIA.
- [ ] Escribe un script que realice al menos 5 tareas de Ciberseguridad y cumpla los siguientes tópicos: 
    - [ ] Cada tarea debe funcionar correctamente y no tener errores de ningún tipo ( 50% - 10% cada tarea ).
    - [X] Manejo de excepciones ( 10% )
    - [ ] Uso de logging, al menos en modo INFO, en el proyecto ( 10% )
    - [X] Uso de argparse
        - [ ] Debe de existir una forma de introducir argumentos para hacer una ejecución "desatendida" del script, a manera opcional tener un menú para complementar o al final de la ejecución. ( **Obligatorio** que se tenga argumentos de entrada )
        - [X] Se debe incluir documentación que proporcione el argumento -h ( 10% )
    - [ ] Uso de socket ( 10% )
    - [X] Consultar una API relacionada con seguridad informática ( **Obligatorio** )
    - [ ] Usar un módulo no nativo de Python ( que requiera instalarse con PIP 5% )
    - [X] Usar al menos un módulo de Python que no hayamos visto en clase y que esté relacionado con Ciberseguridad, desarrollo de una rutina de código que haga alguna función que pueda ayudarnos con seguridad o uso de un módulo que con su aplicación podamos realizar alguna tarea de ciberseguridad ( **Obligatorio** )
    - [ ] Que se genere reportes, en al menos una de las tareas de ciberseguridad, en formato html, xlx(x) o txt. Directamente el uso del logging no cuenta, a menos que además del logging regular implementen otro archivo para generar el reporte ( **Obligatorio** )
    - [X] El script debe estar integrado por al menos 3 módulos ( **Obligatorio** ): 
        - [ ] 2 archivos.py, donde uno debe de tener la función main ( **Obligatorio** )
        - [ ] Un archivo de PS/BASH, que sea invocado desde Python ( **Obligatorio** )
- [ ] Incluye un documento breve ( Word o txt ) con las instrucciones de uso ( 10% )
    - [ ] Documentación en Github ( 15% )
- [ ] Publicar el proyecto en Github - Incluir todos los archivos de código, la documentación y el archivo requirements.txt ( **Obligatorio** )

## Ideas:
### 5 tareas de Ciberseguridad:
- [X] Sacar claves hash de archivos, luego revisar de nuevo las claves hash de un archivo para ver si cambiaron.
    * Puede usar parametros de entrada.
    ```
    pia.py -d hash -f nombre_de_archivo 
    ```
- [ ] Mover eliminar archivos.
- [ ] Copiar archivos
- [ ] Eliminar archivos.
- [X] Usar **Hunter API.**

## Cosas por hacer:
### Hunter API:
- [ ] Agregar banderas para usar una _API key_ propia.
- [ ] Agregar una bandera para su correo.
```
url = "https://api.hunter.io/v2/email-verifier?email=zanez@protonmail.com&api_key=bd225a89d94f014d3fb98a7b6c2ecacf5be105dc"
```
Tal vez agregar manejo de errores y actualizar instrucciones de uso.