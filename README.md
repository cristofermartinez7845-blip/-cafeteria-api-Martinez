# Cafetería API

- **Nombre:** Cristopher Tu-Apellido
- **Carné:** 0701922
- **Asignatura:** 102HAD1 - Herramientas Avanzadas para el Desarrollo de Aplicaciones
- **Evaluación:** Parcial práctico, tercera calificación (Ciclo II, 2026)

API del menú de la cafetería de la universidad, hecha con Django REST Framework.

## Cómo ejecutarla

    python -m venv .venv
    .venv\Scripts\activate
    pip install -r requirements.txt
    python manage.py runserver

## Rutas

- GET /api/estado/
- GET /api/platos/
- GET /api/platos/<id>/
- POST /api/platos/