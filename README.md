<p align="center">
<a href='https://coveralls.io/github/jalvaradosegura/changelog-pre-commit?branch=main'>
  <img src='https://coveralls.io/repos/github/jalvaradosegura/changelog-pre-commit/badge.svg?branch=main' alt='Coverage Status' />
</a>
<a href="https://github.com/psf/black" target="_blank">
  <img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="black">
</a>
<a href="https://pycqa.github.io/isort/" target="_blank">
  <img src="https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336" alt="isort">
</a>
<a href="https://github.com/jalvaradosegura/changelog-pre-commit/blob/main/LICENSE">
  <img alt="GitHub license" src="https://img.shields.io/github/license/jalvaradosegura/changelog-pre-commit">
</a>
<a href="https://github.com/jalvaradosegura/changelog-pre-commit/actions/workflows/code_quality.yml" target="_blank">
    <img src="https://github.com/jalvaradosegura/changelog-pre-commit/actions/workflows/code_quality.yml/badge.svg" alt="Test">
</a>
</p>


# 🪝 changelog-pre-commit
A pre-commit hook so you don't ever again forget to update your changelog file, when doing push/commits

# Usage
1) You need to have pre-commit installed in your project, if you don't, you can install it like this:
```sh
pip install pre-commit
```
2) Create a `.pre-commit-config.yaml` file (the dot is very important)

>💡 In the .pre-commit-config.yaml we will define which hooks we want to run and when to run it (before a commit, before a push, etc)


## .pre-commit-config.yaml examples
3) These are some examples on how you can fill the file:

### Run before a commit
```yaml
repos:
- repo: https://github.com/jalvaradosegura/changelog-pre-commit
  rev: v0.1.0-alpha
  hooks:
  - id: changelog_pre_commit

```

### Run before a push
```yaml
repos:
- repo: https://github.com/jalvaradosegura/changelog-pre-commit
  rev: v0.1.0-alpha
  hooks:
  - id: changelog_pre_commit
    stages: [push]

```

4) Run:
```
pre-commit install
```
And you should be ready to go, now whenever you are about to do a commit/push, this hook will check if you updated the changelog file.

> ⚠️ If you are using it before a push you may need to install it like this:
> ```pre-commit install --hook-type pre-push```

## .pre-commit-config.yaml structure
* repos: a list with the repositories you want to use, each of them should contain git hooks (in the examples we only use changelog-pre-commit).
* repo: the url to repository that contains the hooks.
* rev: the code of a commit or a tag.
* hooks: a list of the hooks from the current repository that you want to use (yes, a repository may have more than 1 hook).
