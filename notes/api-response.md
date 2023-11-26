# API response idea

```json
{
  "success": true,
  "message": "Request completed",
  "data": {}
}
```

## Simple format sketch

Successful requests should use `success`, `message`, and `data`. Failed requests should use `success`, `message`, and `errors`.
