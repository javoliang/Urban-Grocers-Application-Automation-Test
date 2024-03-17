Proyecto 6: Pruebas Automatizadas para Creación de Kits

Acerca del Proyecto:

Este proyecto tiene como objetivo realizar pruebas automatizadas para verificar la funcionalidad de creación de kits en un servicio en línea. Se utiliza un conjunto de pruebas unitarias para validar diferentes escenarios, como la longitud del nombre del kit, la inclusión de caracteres especiales, espacios y números, entre otros.

Tecnologías Utilizadas:

PyCharm
PyTest

Estructura del Proyecto:

1. data.py: Contiene los datos de ejemplo para los cuerpos de solicitud de usuario y kit.
2. configuration.py: Almacena la configuración del servicio en línea, incluida la URL base y las rutas para crear usuarios y kits.
3. sender_stand_request.py: Define funciones para enviar solicitudes con el API Urban Grocers al servicio, incluyendo la creación de usuarios y kits.
4. create_kit_name_kit_test.py: Contiene las pruebas unitarias para validar la creación de kits en diferentes escenarios.

Instalación y Uso de las Librerías:

1. Asegúrate de tener Python instalado en tu sistema.
2. Instala la librería pytest si aún no lo has hecho:
pip version 24.0
requests 2.31.0
configuration 0.8.3
pytest 8.1.1
4. Ejecuta los scripts sender_stand_request.py y create_kit_name_kit_test.py con PyCharm.

Ejecución de las Pruebas en la Terminal:
Para ejecutar las pruebas, utiliza el comando siguiente en la terminal:
pytest /create_kit_name_kit_test.py

Nombre del Autor y Sprint del Proyecto
Autor: Liang Yung Hsin
Sprint del Proyecto: Proyecto 6
