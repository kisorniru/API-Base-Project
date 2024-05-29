# Auth setup notes

- Keep auth routes under `/api/auth/`
- Validate request data with serializers
- Return tokens through the shared response helper
- Replace example token logic before production

## Serializer list

- `LoginSerializer` validates login payloads
- `RegisterSerializer` validates registration payloads
- `UserSerializer` shapes basic user output
