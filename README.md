```bash
my_project/
│
├── main.py # App entry point (initializes FastAPI/Flask/etc.)
├── database.py # Contains your engine, SessionLocal, and get_db()
│
└── modules/
    ├── users/
    │ ├── models.py # Shop owner table schema
    │ ├──schemas.py # validation of the data
    │ ├── services.py # Login, registration, authentication logic
    │ ├──repository.py #
    │ └── router.py # API routes for profile/auth
    │
    ├── products/
    │ ├── models.py # Product info (Name, Price, Stock count)
    │ ├──schemas.py # validation of the data
    │ ├── services.py # Update stock, add new products, check prices
    │ ├──repository.py #
    │ └── router.py # API routes for inventory management
    │
    └── bills/
      ├── models.py # Transaction records (Links customer_id and product_id)
      ├──schemas.py # validation of the data
      ├── services.py # Business logic for checking out, calculating totals
      ├──repository.py #
      └── router.py # API routes to generate invoices and histories
```

---

# Backend Setup

## Deployment

The backend is deployed using **Render**.

## Database

The project uses **Neon PostgreSQL** as the database service.

### Configure Alembic

In `alembic/env.py`, configure the database URL by adding:

```python
context.config.set_main_option("sqlalchemy.url", DB_URL)
```

> Ensure that `DB_URL` is loaded correctly from your environment variables before running migrations.

### Run Database Migrations

Execute the following command to apply all pending migrations:

```bash
alembic upgrade head
```

If the migrations are applied successfully, you should see output similar to:

```text
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade -> 153953f412f7, initial alembic setup
INFO  [alembic.runtime.migration] Running upgrade 153953f412f7 -> 6b7121728426, added login email and password to the users
INFO  [alembic.runtime.migration] Running upgrade 6b7121728426 -> 7d6b346af8e8, added the refresh token table
INFO  [alembic.runtime.migration] Running upgrade 7d6b346af8e8 -> be92e5c44c7b, update models
INFO  [alembic.runtime.migration] Running upgrade be92e5c44c7b -> e33f976efe24, removed the limit for max email length
INFO  [alembic.runtime.migration] Running upgrade e33f976efe24 -> 849bf53bc496, made the email unique
INFO  [alembic.runtime.migration] Running upgrade 849bf53bc496 -> 1e726ef3d8c0, fix user models
```
