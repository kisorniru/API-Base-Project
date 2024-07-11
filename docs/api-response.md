# API responses

Response helpers live in `apps.core.responses` and should be used instead of hand-built dictionaries in views.

## Error codes

- `not_found` for missing resources
- `unauthorized` for missing credentials
- `forbidden` for blocked actions
- `validation_error` for invalid request payloads
