# API response idea

```json
{
  "success": true,
  "message": "Request completed",
  "data": {}
}
```

## Simple format sketch

Successful requests should use `success`, `message`, and `data`. Failed requests should keep the same top-level feel and return `errors` instead of `data`.

## Reusable response note

The response format should be reusable enough that views do not build JSON by hand every time.

## Error response thought

Errors should carry a readable message plus a stable code when the client needs to branch on the result.
