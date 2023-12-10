# Testing notes

SQLite is enough for the starter test setup. Projects can swap to PostgreSQL when feature behavior depends on database-specific behavior.

## Test env

Use `.env.test` locally if a project needs isolated settings. Keep secrets out of committed files.

## Final testing checklist

- Run `python manage.py test`
- Run helper tests after response changes
- Add feature tests with each new endpoint

## Early testing plan

- Test response helpers first
- Add one route test for health checks
- Add serializer validation tests when request examples exist

## Local SQLite note

SQLite is the easiest local default for this starter. Projects can switch databases when their real feature set demands it.

## Testing checklist draft

- Run the Django test command
- Check response helper behavior
- Check serializer validation behavior
- Add route tests for public endpoints
