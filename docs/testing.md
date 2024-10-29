# Testing notes

SQLite is enough for the starter test setup. Projects can swap to PostgreSQL when feature behavior depends on database-specific behavior.

## Test env

Use `.env.test` locally if a project needs isolated settings. Keep secrets out of committed files.

## Final testing checklist

- Run `python manage.py test`
- Run helper tests after response changes
- Add feature tests with each new endpoint
