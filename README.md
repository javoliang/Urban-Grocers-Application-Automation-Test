# Proyecto 6
Este proyecto tiene como objetivo realizar pruebas automatizadas para verificar la funcionalidad de creación de kits en un servicio en línea. Se utiliza un conjunto de pruebas unitarias para validar diferentes escenarios, como la longitud del nombre del kit, la inclusión de caracteres especiales, espacios y números, entre otros.

Estructura del Proyecto:

data.py: Contiene los datos de ejemplo para los cuerpos de solicitud de usuario y kit.
configuration.py: Almacena la configuración del servicio en línea, incluida la URL base y las rutas para crear usuarios y kits.
sender_stand_request.py: Define funciones para enviar solicitudes con el API Urban Grocers al servicio, incluyendo la creación de usuarios y kits.
create_kit_name_kit_test.py: Contiene las pruebas unitarias para validar la creación de kits en diferentes escenarios.

Ejecución de las Pruebas
Para ejecutar las pruebas, sigue estos pasos:
1. Asegurar de tener Python instalado con lo package en el sistema.
2. Ejecutar el script de sender_stand_request.py y create_kit_name_kit_test.py con el boton Run en cada una.
3. Observar la salida en la consola para verificar el resultado de cada prueba.
