## Estructura del proyecto

- `configuration.py`: URL del servidor y endpoints.
- `data.py`: datos utilizados en las pruebas.
- `sender_stand_request.py`: funciones para enviar solicitudes HTTP.
- `create_kit_name_kit_test.py`: casos de prueba automatizados.

## Ejecución

1. Instalar Python y las dependencias:

   pip install pytest requests

2. Configurar una URL válida del servidor Urban Grocers en `configuration.py`.

3. Ejecutar las pruebas:

   pytest create_kit_name_kit_test.py -v

La ejecución requiere acceso a un entorno funcional de Urban Grocers.

## Validaciones realizadas

- Códigos de respuesta HTTP.
- Valores límite.
- Campos obligatorios.
- Tipos de datos.
- Caracteres especiales.
- Autenticación mediante Bearer Token.
- Datos devueltos en respuestas exitosas.

## Resultados

El proyecto contiene 9 pruebas automatizadas.

Los resultados de ejecución se incorporarán cuando se verifiquen en un entorno disponible.

## Contexto

Proyecto académico realizado durante el programa de QA Engineering de TripleTen.
