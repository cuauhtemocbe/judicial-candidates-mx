# Candidatos al Poder Judicial - Proyecto Flask

Este proyecto es una herramienta informativa para comparar y analizar candidaturas al Poder Judicial de la Federación en México, con base en análisis públicos de especialistas como Viridiana Ríos, Fabrizio Mejía y Manuel Pedrero. El sitio permite consultar propuestas, perfiles y recomendaciones para la elección judicial de 2025.

## Requisitos

- Python 3.12+
- [Flask](https://flask.palletsprojects.com/)
- [gunicorn](https://gunicorn.org/)
- [Poetry](https://python-poetry.org/) (para gestión de dependencias)
- Git (para la fecha de actualización)
- Docker y Docker Compose (opcional, recomendado para desarrollo)
- (Opcional) Dev Containers para Visual Studio Code

## Instalación

### Opción 1: Entorno local

1. Clona el repositorio:

   ```sh
   git clone https://github.com/cuauhtemocbe/judicial-candidates-mx.git
   cd judicial-candidates-mx
   ```

2. Instala las dependencias con Poetry:

   ```sh
   pip install poetry
   poetry install
   ```

3. (Opcional) Genera la fecha de última actualización:

   ```sh
   python app/generate_last_updated.py
   ```

### Opción 2: Usando Docker y Docker Compose

1. Construye e inicia el contenedor de desarrollo:

   ```sh
   docker compose -f docker-compose.dev.yml up --build
   ```

2. Accede al contenedor:

   ```sh
   docker exec -it judicial-candidates-mx bash
   ```

3. (Opcional) Genera la fecha de última actualización dentro del contenedor:

   ```sh
   python app/generate_last_updated.py
   ```

## Correr en local

Puedes iniciar el servidor con Gunicorn:

```sh
gunicorn main:app --bind 0.0.0.0:5000
```

O usando el servidor de desarrollo de Flask:

```sh
export FLASK_APP=main:create_app
flask run
```

## Estructura del proyecto

- `app/` - Código fuente principal (rutas, datos, plantillas)
- `app/data/` - Datos de candidaturas y scripts de generación
- `app/templates/` - Plantillas HTML (Jinja2)
- `app/static/` - Archivos estáticos (CSS)
- `Readme.md` - Este archivo
- `pyproject.toml` - Configuración de dependencias y herramientas (Poetry)
- `docker-compose.dev.yml` - Configuración de Docker Compose para desarrollo
- `Dockerfile.dev` - Dockerfile para entorno de desarrollo

## Uso

Abre [http://localhost:5000](http://localhost:5000) en tu navegador para ver la aplicación.

## Créditos y licencia

- Proyecto sin fines de lucro, para fines educativos y de transparencia.
- Código fuente disponible en [GitHub](https://github.com/cuauhtemocbe/judicial-candidates-mx).

---