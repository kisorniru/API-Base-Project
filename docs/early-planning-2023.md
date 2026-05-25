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

## API example cleanup

Keep example paths short until there is a real domain feature to organize.

## Settings structure idea

Keep one settings module at first. Split settings only when local, test, and production behavior actually diverge.

## Env example note

An `.env.example` file should document secret key, debug mode, and allowed hosts before any deployment notes are added.

## DRF dependency note

The requirements file should eventually pin Django and Django REST Framework ranges instead of relying on whatever is newest.

## Planning cleanup

Removed an older wording note after the README settled on the API language.

## Small security checklist

- Never commit real secrets
- Keep debug disabled outside local development
- Document token handling before adding auth examples

## Local development todo

- Add install commands
- Add migrate and runserver notes
- Add test command notes
- Keep setup short enough to follow quickly

## CI later

A simple GitHub Actions workflow can run tests once the project has a real Django structure and requirements files.

## Year-end polish

The notes now point toward a small DRF starter instead of a vague API idea, which is enough direction for a proper rebuild.

## Initial planning wrap-up

The planning phase is complete enough to move into Django project setup, response helpers, auth examples, and tests next.
