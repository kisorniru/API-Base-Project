# Small auth flow

- Client sends login payload
- API validates credentials
- API returns token response shape
- Protected endpoints read authenticated user from request

## Endpoint ideas

- `POST /auth/login`
- `POST /auth/logout`
- `GET /auth/me`
- `POST /auth/refresh`

## Token auth update

Token examples should be labeled clearly as placeholders so nobody mistakes them for a finished authentication system.
