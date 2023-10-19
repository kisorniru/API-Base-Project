

# Architecture notes

Repositories are optional, but they are useful when a feature starts mixing query logic with business rules.

## DTO note

Small dataclasses can make service return values clearer when a plain dictionary starts hiding intent.

## Thin views

Views should coordinate request parsing, validation, service calls, and response helpers. They should not become the place where business rules collect.
