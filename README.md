# API Base Project

A practical base for Django REST Framework APIs.

A small Django and Django REST Framework base project for starting JSON APIs with predictable settings, routes, responses, validation, authentication examples, and tests.

## Response shape

```json
{
  "success": true,
  "message": "Request completed",
  "data": {}
}
```

## Pagination

Paginated responses should return `items` with a `meta` object containing page and total count details.

## Testing

Install development requirements and run `pytest`. The starter uses SQLite for local tests.

## Local development checklist

- Create a virtual environment
- Install requirements
- Copy `.env.example` to `.env`
- Run migrations
- Start the development server

## Pip commands

```bash
python -m pip install -r requirements.txt
python -m pip install -r requirements-dev.txt
```

## Manage.py commands

```bash
python manage.py migrate
python manage.py runserver
python manage.py test
```

## API routes

- `GET /api/health/`
- `POST /api/echo/`
- `POST /api/auth/login/`
- `POST /api/auth/logout/`
- `GET /api/auth/me/`

## Folder structure

```text
config/              Django project settings and URLs
apps/core/           Shared API helpers
apps/api/            Public example endpoints
apps/accounts/       Auth example endpoints
docs/                Project notes and conventions
tests/               Starter test examples
```

## Project summary

This starter gives a new API project a practical starting shape: Django settings, DRF routes, response helpers, auth examples, architecture notes, and test examples.

## Response helpers

Use `success_response`, `error_response`, and `validation_error_response` from `apps.core.responses` so endpoints return the same top-level keys.

## Stable version note

The first stable version is still intentionally small. It is ready to clone, install, inspect, and extend into a real API service.
