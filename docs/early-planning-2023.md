# Early planning notes from 2023

This project exists because I keep starting API projects with the same loose questions: response shape, auth routes, validation, and where shared helpers should live.

## Rough feature list

- Shared JSON response format
- Auth endpoint examples
- Request validation pattern
- Pagination shape
- Health check endpoint
- Testing checklist

## Project goal

Start with plain notes, then slowly turn the useful pieces into a Django REST Framework base project that can be copied into real work.

## Wording cleanup

Use API consistently instead of mixing API, backend, and service language too early.

## Simple folder plan

```text
config/
apps/
docs/
tests/
```

## Serializer note

Serializers should probably handle both input validation and simple output shaping once DRF enters the project.

## Rough authentication checklist

- Decide token package later
- Keep example views simple
- Document protected route behavior
- Avoid storing token examples as real secrets

## Pagination note

Paginated endpoints should return items and metadata together so clients do not guess total counts or next page state.
