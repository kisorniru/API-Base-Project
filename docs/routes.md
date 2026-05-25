# Route examples

- `GET /api/health/` checks app status
- `POST /api/echo/` demonstrates request validation
- `POST /api/auth/login/` demonstrates token response shape
- `GET /api/auth/me/` demonstrates current user output

## Early route ideas

- `/api/health/`
- `/api/auth/login/`
- `/api/auth/me/`
- `/api/echo/`

## Versioning idea

Start without explicit versioning, but leave room for `/api/v1/` if the first real client needs a stable contract.

## Health check

A health endpoint should return a tiny response and avoid touching the database unless a deeper readiness check is needed.
