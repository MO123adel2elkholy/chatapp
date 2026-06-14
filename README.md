# mvec (chatapp) — Django eCommerce demo

Brief eCommerce demo built with Django (app: `mvec`). Features: product listing, product details, categories, CKEditor content, simple coupon model, and cart operations using `django-carton`.

---

## Tech stack
- Python + Django 4.2
- SQLite (default)
- django-ckeditor
- django-carton
- Pillow

See `requirements.txt` for full dependency list.

---

## Quick start (Windows)

1. Open PowerShell / CMD and go to repo root:
2. Create and activate venv:
   - `python -m venv venv`
   - PowerShell: `.\venv\Scripts\Activate.ps1`
   - CMD: `.\venv\Scripts\activate`
3. Install deps:
   - `pip install -r requirements.txt`
4. Change into Django source folder and run migrations:
   - `cd src`
   - `python manage.py migrate`
5. Create superuser:
   - `python manage.py createsuperuser`
6. Run server:
   - `python manage.py runserver`
7. Access:
   - Site: `http://127.0.0.1:8000/`
   - Admin: `http://127.0.0.1:8000/admin/`

---

## Project layout (important files)
- `src/project/settings.py` — Django settings (STATIC, MEDIA, CKEditor, CART_SESSION_ID)
- `src/mvec/` — main app (models, views, urls, templates)
- `requirements.txt` — Python dependencies
- `README.md` — this file

---

## Environment & config notes
- `DEBUG = True` and `SECRET_KEY` are in settings for development. Replace with env vars for production.
- Email credentials are set in `settings.py` — move to env for security.
- CKEditor uploads: `CKEDITOR_UPLOAD_PATH = 'media/ckeditor/'`. Ensure `MEDIA_ROOT` is writable.

---

## Database & media
- Default DB: SQLite (`db.sqlite3` in `src`).
- Static files: `STATICFILES_DIRS = [BASE_DIR / "static"]`
- Media files: `MEDIA_ROOT = <project>/media`, served in development via `project.urls` static helper.

---

## Main models (summary)
- Slider — homepage sliders.
- BannerArea — banner items.
- Main_Category, Category, Sub_Category — category hierarchy.
- Section — product sections (e.g., "Top Deals Of The Day").
- Product — main product model (price, tax, packing_cost, category, section, etc.).
- Codon_copon — coupon code and discount.
- Product_Image, Addtional_Iformation, Accessories — product related models.

(See `src/mvec/models.py` for full fields.)

---

## Key URLs (from `src/mvec/urls.py`)
- `/` -> home (name: `home`)
- `/product/<pk>` -> product details (name: `product`)
- `/product` -> product listing (name: `product`)
- `/product/filter-data` -> AJAX filter (name: `filter-data`)
- Auth:
  - `/register` -> register (name: `use_register`)
  - `/login` -> custom login (name: `user_login`)
  - `/logout` -> logout (name: `user_logout`)
- Cart:
  - `/cart/add/<id>/` (name: `cart_add`)
  - `/cart/item_clear/<id>/` (name: `item_clear`)
  - `/cart/item_increment/<id>/` (name: `item_increment`)
  - `/cart/item_decrement/<id>/` (name: `item_decrement`)
  - `/cart/cart_clear/` (name: `cart_clear`)
  - `/cart/cart-detail/` (name: `cart_detail`)
  - `/cart/checkout/` (name: `checkout`)

CKEditor URLs are included at `/ckeditor/`.

---

## Cart
- Uses `django-carton`. Session key set as `CART_SESSION_ID = 'cart'` in settings.
- Views in `views.py` call `Cart(request)` for add/remove operations.

---



---

## Tests
- No automated tests included. Add tests under `src/mvec/tests.py` and run `python manage.py test`.

---

## Contributing
- Fork, create a feature branch, open a PR.
- Keep changes focused and add tests for behavioral changes.

---

## License
MIT — see LICENSE (add if desired).

---