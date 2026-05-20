Proyecto Automatización de App Urban Routes v2

Proyecto de bootcamp para automatizar pruebas basadas en la lista de comprobacion descrita en este archivo
para la App de Urban Routes que es una app de solicitudes de taxis o autos para transportar pasajeros (similar a Uber).
Lo que se hace es simular una solicitud personalizada por un usuario para pedir un taxi de un punto A a un punto B con
detalles como numero telefónico, método de pago, tipo de viaje y algunos requisitos especificos del pedido.

Estructura:
Data.py - Contiene los datos que se utilizan en las pruebas, principalmente para escribir texto en formularios y validar textos en algunos elementos de la página.
Pages.py - Contiene los localizadores y métodos que se utilizan en las pruebas.
utilities.py - Contiene un script complejo que se utiliza para obtener el código de confirmación del formulario "Rellenar número telefónico".
main.py - Contiene todas las suite de pruebas.

Aqui esta la lista de casos de prueba:

### 📋 Matriz de Casos de Prueba - Urban Routes

| Número | Nombre | Pre-condiciones | Pasos | Resultado Esperado |
| :---: | :--- | :--- | :--- | :--- |
| **1** | Configurar la dirección. | Inicializar el servidor | 1. Ingresar 'East 2nd Street, 601' en campo "Desde".<br>2. Ingresar '1300 1st St' en campo "Hasta".<br>3. Validar el texto del campo "Desde"<br>4. Validar el texto del campo "Hasta" | 3. El texto debe coincidir con el que se acaba de escribir en el campo.<br>4. El texto debe coincidir con el que se acaba de escribir en el campo. |
| **2** | Seleccionar la tarifa Comfort. | Inicializar el servidor<br>Configurar la dirección. | 1. Click en botón "Pedir un taxi".<br>2. Seleccionar la tarifa "Comfort".<br>3. Validar la selección. | 3. La selección debe retornar un estado "True" |
| **3** | Rellenar el número de teléfono. | Inicializar el servidor<br>Configurar la dirección.<br>Seleccionar la tarifa "Comfort" | 1. Click en campo "Número de teléfono".<br>2. Ingresar '+1 123 123 12 12' en el campo.<br>3. Validar dicho número previamente ingresado.<br>4. Click en "Siguiente".<br>5. Ingresar el código otorgado por el servidor.<br>6. Validar dicho código previamente ingresado.<br>7. Click en "confirmar". | 3. El texto debe coincidir con el que se acaba de escribir en el campo.<br>6. El texto debe coincidir con el que se acaba de escribir en el campo. |
| **4** | Agregar una tarjeta de crédito. | Inicializar el servidor<br>Configurar la dirección.<br>Seleccionar la tarifa "Comfort" | 1. Click en "Método de pago".<br>2. Click en "Agregar tarjeta".<br>3. Ingresar '1234 5678 9100' en el campo del número.<br>4. Ingresar '111' en el campo del código.<br>5. Click fuera de los campos.<br>6. Validar texto en campo "Número de tarjeta".<br>7. Validar texto en campo "Código".<br>8. Click en "Agregar"<br>9. Click en "Cerrar". | 6. El texto debe coincidir con el que se acaba de escribir en el campo.<br>7. El texto debe coincidir con el que se acaba de escribir en el campo. |
| **5** | Escribir un mensaje para el conductor. | Inicializar el servidor<br>Configurar la dirección.<br>Seleccionar la tarifa "Comfort" | 1. Ingresar 'Muéstrame el camino al museo' en el campo "Mensaje para el conductor".<br>2. Validar texto en el campo. | 2. El texto debe coincidir con el que se acaba de escribir en el campo. |
| **6** | Pedir una manta y pañuelos. | Inicializar el servidor<br>Configurar la dirección.<br>Seleccionar la tarifa "Comfort" | 1. Click en "Requisitos del pedido".<br>2. Click en "Manta y pañuelos".<br>3. Validar la selección del switch. | 3. La selección debe retornar un estado "True" |
| **7** | Pedir 2 helados. | Inicializar el servidor<br>Configurar la dirección.<br>Seleccionar la tarifa "Comfort" | 1. Click 2 veces en el botón "+" de Helado.<br>2. Validar la cantidad del contador. | 2. El contador debe contener "2". |
| **8** | Aparece el modal para buscar un taxi. | Inicializar el servidor<br>Configurar la dirección.<br>Seleccionar la tarifa "Comfort".<br>Rellenar todos los campos requeridos. | 1. Validar que aparezca "Pedir un taxi" en el botón principal de la orden.<br>2. Click en el botón.<br>3. Validar que aparezca el popup. | 1. El texto debe coincidir después de completar todos los campos requeridos.<br>3. Debe aparecer un popup que diga "Buscando automóvil..." |
| **9** | Esperar a que aparezca la información del conductor. | Inicializar el servidor<br>Configurar la dirección.<br>Seleccionar la tarifa "Comfort".<br>Rellenar todos los campos requeridos.<br>Pedir un taxi. | 1. Esperar a que se complete el tiempo de espera al buscar el automóvil.<br>2. Validar la información del conductor. | 2. Los elementos deben estar visibles en la ventana después de completarse el timer. |l.

Pre-condiciones para correr el proyecto.
1. Hay que tener previamente configurada el interprete en Pycharm e instalado pytest y selenium para poder utilizar las librerías.
Estas son las versiones que se necesitan para este proyecto:
PyTest 7.4.4 (o posterior)
Selenium 4.11.2 (o posterior)

2. Hay que actualizar la ruta del servidor en el archivo "data.py" en la variable "urban_routes_url" ya que el proyecto funciona con un servidor temporal.

PARA EJECUTARLO:
Una vez instalado todo lo requerido, simplemente vaya al archivo "main.py" y haga click en simbolo de "flecha verde"
que aparece en "class TestUrbanRoutes" para ejecutar todas las pruebas.
Si se quiere ejecutar pruebas en especifico, hay que seguir las precondiciones de la tabla descrita previamente.

La URL con la que se trabajo fue: https://cnt-43fafe03-ef9a-41ae-ad3f-851fc792d8c8.containerhub.tripleten-services.com/?lng=es

Este proyecto se desarrollo con PyTest y Selnium con conceptos básicos de DOM, OOP y otros conceptos básicos de python.
El IDE necesario para ejecutar el proyecto es PyCharm 2026.1.
También se utilizaron comandos básicos de Git Bash para clonar y empujar (push) el proyecto desde y hacia GitHub.