# mvec (chatapp) — Django eCommerce demo

Brief eCommerce demo built with Django (app: `mvec`). Features: product listing, product details, categories, CKEditor content, coupon model, and cart operations using `django-carton`.

---

## Tech stack
- Python + Django 4.2
- SQLite (default)
- django-ckeditor
- django-carton
- Pillow
- Docker + Docker Compose (added)

See `requirements.txt` for full dependency list.

---

## Quick start (local, Windows)
1. Open PowerShell / CMD at repo root:
   - cd "c:\Users\HP\Desktop\تجميعة\New folder\chatapp"
2. Create & activate venv:
   - python -m venv venv
   - PowerShell: .\venv\Scripts\Activate.ps1
   - CMD: .\venv\Scripts\activate
3. Install deps:
   - pip install -r requirements.txt
4. Run migrations, create superuser, run server:
   - cd src
   - python manage.py migrate
   - python manage.py createsuperuser
   - python manage.py runserver

---

## Docker (recommended for repeatable env)
Files added: `Dockerfile`, `docker-compose.yml`, `.dockerignore`.

.env (example)
```
SECRET_KEY=changeme
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

Build & run:
- docker compose up --build -d

Run management commands:
- docker compose exec web python manage.py migrate
- docker compose exec web python manage.py createsuperuser
- docker compose exec web python manage.py collectstatic --noinput
- docker compose logs -f web

Ports:
- Host 8000 -> container 8000

Volumes:
- static and media persisted via named volumes (see docker-compose.yml)

---

## Project layout (important files)
- `src/project/settings.py` — settings (STATIC, MEDIA, CKEditor, CART_SESSION_ID)
- `src/mvec/` — app (models, views, urls, templates)
- `Dockerfile`, `docker-compose.yml`, `.dockerignore`
- `requirements.txt`

---

## Environment & config notes
- Provide a `.env` with SECRET_KEY, DEBUG, ALLOWED_HOSTS.
- For production set DEBUG=False, use a proper DB (Postgres), configure static/media hosting, secure SECRET_KEY and allowed hosts.
- CKEditor uploads: `CKEDITOR_UPLOAD_PATH = 'media/ckeditor/'`.


## Contributing
- Fork, feature branch, PR. Add tests for behavior changes.

--- 

## License
MIT 