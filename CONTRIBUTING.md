# Contributing to RPI Computer Club Server

Thanks for helping improve the RPI Computer Club backend! This repository ships the REST API that powers authentication, member profiles, events, notices, squads, and payments for the club’s web/mobile surfaces. Follow this guide to keep contributions smooth, predictable, and secure.

## 1. Contribution Workflow

1. **Fork & branch** – Fork from `main` (or the team’s canonical branch) and create a feature branch named like `feature/<description>` or `fix/<ticket>`.
2. **Sync regularly** – Rebase or merge `main` often so your branch reflects the latest migrations, settings, and dependency changes.
3. **Small, focused PRs** – Prefer one concern per pull request so reviews stay fast and tests stay targeted.
4. **Describe the change** – In your PR description, explain why the change exists, reference the relevant issue, and summarize testing steps.

## 2. Testing & Quality

- Run the Django test suite before opening a PR: `python manage.py test`.
- If the change touches database models or serializers, include regression tests that cover validation, serialization, and permissions.
- For authentication or permission fixes, test both authenticated and anonymous flows.
- Keep migrations tidy: one migration per model change, and do not re-generate existing ones without necessity.

## 3. Code Standards

- **Formatting**: Follow [PEP 8](https://peps.python.org/pep-0008/) and use consistent indentation (spaces, 4 columns).
- **Imports**: Group standard library, third-party, and local imports separately.
- **Documentation**: Add docstrings to public functions/classes. Mention any new API behavior in `README.md` or relevant docs.
- **Security**: Never commit secrets (JWT signing keys, DB credentials). Prefer environment variables defined in `.env.example` or the deployment docs.
- **Type hints**: Include type hints for new utilities where feasible.

## 4. Pull Request Process

1. Push your branch to GitHub and open a PR targeting `main`.
2. Link the PR to the issue or describe the motivation.
3. Ensure CI passes: formatting checks (if added), linting (when applicable), and Django tests.
4. Tag reviewers (core maintainers: @coder-black-mamba) and wait for approvals before merging.
5. Squash/merge once the PR is green, and delete the branch after merging.

## 5. Communication

- Use club communication channels (Discord/GitHub discussions) for architecture debates.
- Mention any breaking changes or migration steps in the PR summary.
- Flag any security-sensitive changes for urgent review by maintainers.

## 6. Resources

- [Django documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/)
