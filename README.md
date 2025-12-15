<div align="center">

<img src="https://raw.githubusercontent.com/RPI-Computer-Club-rpicc/RPI-Computer-Club-rpicc/refs/heads/main/logo-final-3.0.png" alt="RPI Computer Club" width="200" height="200" />

# RPI Computer Club

**Backend for the Rajshahi Polytechnic Institute Computer Club ecosystem.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Django](https://img.shields.io/badge/Django-092E20?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/Django_REST_Framework-ff1709?logo=django&logoColor=white)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?logo=postgresql&logoColor=white)](https://www.postgresql.org/)

Empowering students through technology, innovation, and community at  
**Rajshahi Polytechnic Institute.**

---


[![GitHub](https://img.icons8.com/ios-filled/30/ffffff/github.png)](https://github.com/RPI-Computer-Club-rpicc)
[![LinkedIn](https://img.icons8.com/ios-filled/30/0077B5/linkedin.png)](https://www.linkedin.com/company/rpi-computer-club/)
[![Facebook](https://img.icons8.com/ios-filled/30/1877F2/facebook-new.png)](https://www.facebook.com/people/Computer-Club-Rpi/61581226467108/)
[![Instagram](https://img.icons8.com/ios-filled/30/E4405F/instagram-new.png)](https://www.instagram.com/rpi.cc)
[![YouTube](https://img.icons8.com/ios-filled/30/FF0000/youtube-play.png)](https://www.youtube.com/@rpicomputerclub)
[![Discord](https://img.icons8.com/ios-filled/30/5865F2/discord-logo.png)](https://discord.gg/4RDVuuJW)

</div>



# RPI Computer Club Server

Backend for the Rajshahi Polytechnic Institute Computer Club ecosystem. This Django 5.2 API handles authentication, member profiles, squad management, notices, events, and payments while syncing with Supabase PostgreSQL and serving JWT-protected endpoints for React/Vite clients.

## 🧱 Architecture

- **Framework**: Django 5.2 with Django REST Framework powering RESTful JSON endpoints  
- **Authentication**: `rest_framework_simplejwt` with short-lived access tokens and rotating refresh tokens  
- **Database**: PostgreSQL (Supabase) configured via environment variables  
- **Apps**: `my_auth`, `users_details`, `squads`, `notices`, `events`, `payments`  
- **Deployment Target**: Cloud hosting (Heroku/Vercel/Render) with environment secrets and migrations

## 🚀 Features

- JWT login/refresh flows and automatic role-based group assignment  
- Rich `UserDetails` model storing contact info, quotes, bio, social links, and join history  
- APIs for notices, events, squads, and payment records to keep the club digital-first  
- Secure settings via environment configuration (no credentials committed)  
- Ready for client consumption with browsable DRF schema plus CORS-friendly responses

## 🛠️ Tech Stack

| Layer | Tool |
| ----- | ---- |
| Backend | Python 3.12, Django 5.2.5 |
| API | Django REST Framework, Simple JWT |
| Database | Supabase PostgreSQL (via `psycopg2`) |
| DevOps | Pip, pip-tools, `manage.py`, optional Docker |

## 🏁 Getting Started

```bash
# Clone the repo
git clone https://github.com/<your-org>/rpicc-server.git
cd rpicc-server

# Create virtual environment & install
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` (or use your secrets manager) with the following keys:

```env
DJANGO_SECRET_KEY=your-secret
DB_NAME=<supabase-db-name>
DB_USER=<supabase-user>
DB_PASSWORD=<supabase-password>
DB_HOST=<supabase-host>
DB_PORT=<supabase-port>
```

Apply migrations and create a superuser:

```bash
python manage.py migrate
python manage.py createsuperuser
```

Run the development server:

```bash
python manage.py runserver
```

The API will be reachable at `http://localhost:8000/`. JWT auth lives under `/auth/`.

## 📦 Usage

- Hit `/auth/login/` to obtain an access/refresh pair.  
- Use the access token in the `Authorization: Bearer <token>` header for protected endpoints.  
- Explore `/api/` endpoints (notice, events, payments) via the DRF browsable API.  
- Hook into the `users_details` to sync club member profiles with the frontend roster.

## 🧪 Testing

```bash
python manage.py test
```

Extend tests for each app as features expand.

## 🧭 Deployment

1. Provision a PostgreSQL database (Supabase, Render Postgres, etc.).  
2. Set the required env vars in the hosting platform.  
3. Run `python manage.py collectstatic` if serving static files (or let the frontend handle it).  
4. Keep `DEBUG=False` and rotate JWT signing keys as needed.

## 🤝 Contributing

1. Fork the repository and create feature branches.  
2. Keep migrations isolated per feature/app.  
3. Run linters/tests before submitting a PR.  
4. Describe API contract or schema changes clearly in PR descriptions.

## 📚 Resources

- Django docs: https://docs.djangoproject.com/  
- Django REST Framework: https://www.django-rest-framework.org/  
- Simple JWT: https://django-rest-framework-simplejwt.readthedocs.io/

## 📝 License

MIT © Abu Sayed (coder-black-mamba)

## 📬 Maintainers

Abu Sayed — General Secretary, RPI Computer Club  
Website: https://absyd.xyz  
GitHub: https://github.com/coder-black-mamba