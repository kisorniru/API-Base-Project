

# Architecture notes

Repositories are optional, but they are useful when a feature starts mixing query logic with business rules.

## DTO note

Small dataclasses can make service return values clearer when a plain dictionary starts hiding intent.

## Thin views

Views should coordinate request parsing, validation, service calls, and response helpers. They should not become the place where business rules collect.

## Service layer planning

Services can hold use-case level behavior once a feature has more than one step. Until then, a clear view and serializer are enough.
