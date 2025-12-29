# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Django template project for starting new Django applications. Uses email-based authentication with a custom user model.

## Common Commands

```bash
# Development
make run                    # Run dev server at 127.0.0.1:8000
make setup                  # Install all dependencies via uv

# Testing & Quality
make test                   # Run pytest with coverage
make lint                   # Run ruff linter
make format                 # Auto-fix linting issues
make check                  # Run mypy type checking

# Django Operations
make create-app NAME=<name> # Create new app in apps/ directory
make admin                  # Create superuser
make static                 # Collect static files
make secret-key             # Generate new SECRET_KEY

# Documentation
make docs-serve             # Sphinx docs at localhost:9292
```

**Running a single test:**
```bash
pytest tests/path/to/test_file.py::test_function_name -v
```

## Architecture

### Directory Structure
- `changeme/` - Main Django project config (rename for your project via `./rename.sh <name>`)
- `apps/` - All Django applications live here
- `dj_tools/` - Shared Django utilities (not a Django app)
- `static/` - Project-wide static files

### Settings Pattern
Settings use inheritance: `base.py` + environment-specific file + optional `local.py`

- `changeme/settings/base.py` - Common settings, SECRET_KEY from env var
- `changeme/settings/dev.py` - Development (DEBUG=True, SQLite, browser-reload)
- `changeme/settings/prod.py` - Production (DEBUG=False)
- `changeme/settings/local.py` - Local overrides, never committed (copy from `local.example.py`)

Default: `DJANGO_SETTINGS_MODULE=changeme.settings` imports base then tries local.

### Custom User Model
Uses `apps.accounts.Emailuser` with email as USERNAME_FIELD instead of username.

### HTMX Integration
The `@for_htmx` decorator in `dj_tools/htmx.py` enables partial template rendering:

```python
from dj_tools.htmx import for_htmx

@for_htmx(if_hx_target="content", use_block="content")
def my_view(request):
    return TemplateResponse(request, "template.html", context)
```

Requires `render-block` library. Renders only specified block when request has matching `hx-target` header.

### Creating New Apps
```bash
make create-app NAME=myapp
```
Then update `apps/myapp/apps.py` to set `name = "apps.myapp"` and add `"apps.myapp"` to INSTALLED_APPS.

## Key Dependencies
- Django 5.x with WhiteNoise for static files
- uv for dependency management
- Ruff for linting/formatting, mypy for type checking
- pytest-django for testing
