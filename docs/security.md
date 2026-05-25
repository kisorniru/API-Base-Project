# Security notes

## Rate limits

Add throttling for login, registration, and public write endpoints before production.

## CORS

Use a small allowlist for browser clients. Avoid wildcard origins on authenticated APIs.

## Checklist

- Use strong `DJANGO_SECRET_KEY` values
- Disable debug in production
- Keep allowed hosts explicit
- Use HTTPS for token traffic

## Token security

Treat access tokens as credentials. Keep lifetimes short and rotate refresh tokens when the authentication package supports it.

## Last reminder

Do not ship the example secret key, example token strings, or debug settings to production.
