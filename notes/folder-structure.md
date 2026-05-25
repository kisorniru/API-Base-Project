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

## Future app structure

Start with `core`, `api`, and `accounts`. Add domain apps only after there is a real feature boundary.
