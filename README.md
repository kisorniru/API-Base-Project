# API Base Project

A small Django and Django REST Framework base project for starting JSON APIs with a predictable response shape.

The project began as loose notes and is slowly becoming a reusable API starter. The goal is not to hide Django, but to keep the first few decisions clear: settings, routes, responses, validation, authentication examples, and tests.

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
pip install -r requirements.txt
pip install -r requirements-dev.txt
```
