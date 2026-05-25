# Troubleshooting

## Django cannot import settings

Check that `DJANGO_SETTINGS_MODULE=config.settings` is set and commands run from the repository root.

## Requirements fail to install

Upgrade pip first, then reinstall the development requirements. If a package fails on Python version support, use the version from the workflow file.

## Common API issues

- `401` means the request needs authentication
- `403` means the user is known but blocked
- `422` means the request payload did not pass validation
