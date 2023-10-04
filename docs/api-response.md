# API responses

Response helpers live in `apps.core.responses` and should be used instead of hand-built dictionaries in views. Keep examples short so they are easy to copy into real endpoints.

## Error codes

- `not_found` for missing resources
- `unauthorized` for missing credentials
- `forbidden` for blocked actions
- `validation_error` for invalid request payloads

## Basic payload example

```json
{
  "success": true,
  "message": "Request completed",
  "data": {
    "id": 1
  }
}
```
