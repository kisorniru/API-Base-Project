# Naming guide

## Requests

Request serializers should describe the payload, for example `LoginSerializer` or `CreatePostSerializer`.

## Controllers

Views should read like API actions: `login`, `logout`, `current_user`, `health_check`. Keep controller names short and route-focused.

## Serializers

Use `Serializer` suffixes for request and response shapes. Prefer feature-local serializers before adding shared ones.
