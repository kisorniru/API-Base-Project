# Validation thoughts

- Prefer serializer validation for request payloads
- Return field errors in a stable object
- Keep validation messages simple

## Request validation update

Validation errors should return field names, not just one flat message. That will make frontend handling easier later.
