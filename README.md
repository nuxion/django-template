# changeme

[![PyPI - Version](https://img.shields.io/pypi/v/changeme.svg)](https://pypi.org/project/changeme)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/changeme.svg)](https://pypi.org/project/changeme)

-----

## Description

This is a template used to start django projects. 

At the starts it's opinated about folder structure. 

`changeme`: where configurations and servers lives
`apps/<name_app>`: Where apps should live. 

## Using this template

It can be used as if clonning the git repository, or using degit:

```console
degit https://github.com/nuxion/django-template <your-project-name>
```

After that run `rename.sh` script to refactor folders and names to the new one:

```console
./rename.sh <your-project-name>
```

## Features

- Makefile for common tasks
- Sphinx 
- pytest
- `.gitignore` for python + nodejs projects + emacs + vim + vscode (using topal gitignore generation tool)
- jupyter as optional dependency + jupytext
- linting tools
- By default use a custom user from the BaseUser.   
- DRF implemented
- Dockerfile


## Creating apps

You can use the command defined in `Makefile`:

```
make create-app NAME=<your app>
```

When you create an app, you should check that "name" property in `apps.py` match with the doted path. See: https://code.djangoproject.com/ticket/24801

Also you can check `accounts` app as example. 

## Using settings

Settings are splited into environments. 

- `base.py`: common settings 
- `local.py`: never commited, you can rename `local.example.py` to start 
- `dev.py`, `test.py` and `prod.py`

## References

- https://waylonwalker.com/hatch-version/
- https://fly.io/django-beats/deploying-django-to-production/
- if ERROR: Could not build wheels for backports-zoneinfo, which is required to install pyproject.toml-based projects, check https://stackoverflow.com/questions/71712258/error-could-not-build-wheels-for-backports-zoneinfo-which-is-required-to-insta

## License

`changeme` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
