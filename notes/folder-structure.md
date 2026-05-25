# Folder structure idea

```text
config/
apps/
  core/
  api/
docs/
tests/
```

## Controller thought

Reusable controllers should stay thin. They can call serializers, services, and response helpers, but should avoid business rules.
