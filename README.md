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
    ├── customers/
    │ ├── models.py # Customer demographics (Name, Phone, Email)
    │ ├──schemas.py # validation of the data
    │ ├── services.py # Check if customer exists, create new customer
    │ ├──repository.py # 
    │ └── router.py # API routes to view/manage customers
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

## ⚠️ Database Migration Guidelines (Alembic)

Before merging any code changes into the `main` branch, ensure that the database schema is synchronized with the latest model changes.

### 1. Generate a Migration Script

If you have modified any SQLAlchemy models, create a new migration revision:

```bash
alembic revision --autogenerate -m "Detailed description of your changes"
```

### 2. Review the Generated Migration

Carefully inspect the generated migration file inside the `alembic/versions/` directory before committing.

> **Important:** `--autogenerate` may not detect every schema change correctly. Always verify the generated operations.

### 3. Apply the Migration

Update your local database to the latest schema:

#### Single Database Setup

```bash
alembic upgrade head
```

#### Multi-Database / Split-History Setup

```bash
alembic upgrade heads
```

### 4. Commit Migration Files

When submitting a pull request, ensure that:

- Model changes are committed.
- Corresponding Alembic migration files are committed.
- Migration scripts have been tested locally.
- The database successfully upgrades to the latest revision.

### Pre-Merge Checklist

- [ ] Models updated
- [ ] Migration generated
- [ ] Migration reviewed
- [ ] Database upgraded successfully
- [ ] Migration file committed
- [ ] Application tested against updated schema

---

**Reminder:** Never merge model changes without the corresponding migration files.
