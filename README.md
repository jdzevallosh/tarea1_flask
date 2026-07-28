Tarea 01 - Aplicación Web con Flask

Aplicación web desarrollada con Flask y SQLite que implementa un CRUD completo de usuarios, endpoints API en formato JSON y un buscador en tiempo real utilizando HTMX.

##  Arquitectura del Proyecto
El proyecto sigue una estructura modular simple basada en Flask:
- `app/__init__.py`: Contiene las rutas del CRUD HTML, la API JSON y la vista de HTMX.
- `app/config.py`: Carga la configuración desde las variables de entorno.
- `app/database/`: Contiene el esquema SQL (`schema.sql`) y la base de datos SQLite.
- `app/templates/`: Vistas HTML renderizadas con Jinja2 y el buscador interactivo con HTMX.

## Instalación y Ejecución

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/jdzevallosh/tarea1_flask.git
   cd tarea1_flask
