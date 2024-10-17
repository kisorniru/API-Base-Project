# Security notes

## Rate limits

Add throttling for login, registration, and public write endpoints before production.

## CORS

Use a small allowlist for browser clients. Avoid wildcard origins on authenticated APIs.
