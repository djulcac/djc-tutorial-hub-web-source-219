---
title: Migrate and Restore Data in Django
---

# Migrate and Restore Data in Django

[DJC](https://www.djc.pe/) >
[Tutorials](https://tutorial-hub.djc.pe/)

| [Django](../../c/django/index.md) |
[Python](../../c/python/index.md) |
[SQL](../../c/sql/index.md) |

This tutorial explains, with examples for PowerShell on Windows, how to handle migrations (create/apply) and how to backup and restore data in a Django project. It includes options with fixtures (`dumpdata` / `loaddata`) and database-level dumps (SQLite, PostgreSQL, MySQL).

### Quick Contract
- Input: a Django project with `manage.py` and activated virtual environment.
- Output: migrations applied or reverted, and data restored from backup.
- Common errors: misaligned migrations between code and database, PostgreSQL/MySQL permissions, PowerShell execution policies.

### Prerequisites
- Python and Django installed in the virtual environment.
- Database access (SQLite file, PostgreSQL/MySQL credentials).
- In PowerShell, activate your virtual environment (common example):

```powershell
# Windows PowerShell
.\venv\Scripts\Activate.ps1
# If you can't run the script due to execution policy, use:
# Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Note: you can also use `pipenv`, `poetry`, or another package manager; adapt the commands accordingly.

### 1) Migrations: Create and Apply

1. Create migration files from model changes:

```powershell
python manage.py makemigrations
```

2. Review migration plan (optional, useful before applying):

```powershell
python manage.py migrate --plan
```

3. Apply migrations to the database:

```powershell
python manage.py migrate
```

4. View migrations status by app:

```powershell
python manage.py showmigrations
```

5. Force (fake) a migration if the structure already exists in the DB but the migration is not marked as applied:

```powershell
python manage.py migrate <app_name> --fake
```

Use `--fake-initial` when testing an initial migration on a database with tables already created by another process.

### Notes on Rollback
- Django doesn't automatically generate reverse migrations for everything; many migrations do (create/delete field), but to revert to a previous version, you typically apply `migrate <app> <migration_name>`.

Example: go back to migration `0003_auto` of the `blog` app:

```powershell
python manage.py migrate blog 0003_auto
```

### 2) Backup and Restore Data in Django

There are two main methods:
- Application-level backups (fixtures) with `dumpdata` / `loaddata`.
- Database-level backups (pg_dump/pg_restore, mysqldump, SQLite file copy).

Choose the method based on your data size and whether you need to preserve schemas/indexes/procedures.

#### A) Using Fixtures: dumpdata / loaddata

1. Make a JSON dump of the entire database (useful for small projects or deployments between Django environments):

```powershell
python manage.py dumpdata --natural-foreign --natural-primary --indent 2 > backup_all.json
```

2. To dump a specific app only:

```powershell
python manage.py dumpdata myapp --indent 2 > myapp_backup.json
```

3. Restore from a fixture:

```powershell
python manage.py loaddata myapp_backup.json
```

Notes:
- `dumpdata` writes data in JSON format (or XML/YAML if you install support). Does not include media files.
- For sensitive data, encrypt or protect the resulting file.

#### B) Database-Level Backups

- SQLite: copy the `db.sqlite3` file (ensure Django isn't writing during the copy).

```powershell
# Stop process using DB (if applicable) then copy:
Copy-Item .\db.sqlite3 .\backups\db_$(Get-Date -Format "yyyyMMdd_HHmmss").sqlite3
```

- PostgreSQL: `pg_dump` / `pg_restore` (recommended for large databases or production).

```powershell
# Dump (custom format, compressed)
pg_dump -U dbuser -h dbhost -Fc dbname -f backup_db.dump

# Restore (example with newly created database)
pg_restore -U dbuser -h dbhost -d dbname --clean --no-owner backup_db.dump
```

If `pg_restore` is not available in the PATH on Windows, install PostgreSQL or use the utilities from the binary.

- MySQL / MariaDB: `mysqldump` and `mysql` to restore:

```powershell
mysqldump -u dbuser -p dbname > backup_db.sql

# Restore
mysql -u dbuser -p dbname < backup_db.sql
```

#### Practical Recommendations
- For development or quick migrations, `dumpdata` + `loaddata` works well.
- For production environments with lots of data, use pg_dump/pg_restore or mysqldump to preserve indexes and performance.
- Before restoring in production, test the restore on a staging copy.

### 3) Typical Migration + Backup Flow Before Destructive Changes

1. Create complete database backup (pg_dump or SQLite copy).
2. Create migrations: `makemigrations`.
3. Review plan: `migrate --plan`.
4. Apply migrations in staging and test.
5. Apply migrations in production during maintenance window.

### 4) Restore in Case of Problems (Examples)

- If you used `dumpdata`:

```powershell
# Delete tables or empty DB as needed (carefully)
python manage.py flush  # WARNING: deletes everything, keeps superuser? No.

python manage.py loaddata backup_all.json
```

- If you used `pg_dump` or `mysqldump`, use the corresponding restore commands (see previous section). Make sure to recreate users/privileges if necessary.

### 5) Media and Static Files
- `MEDIA` files are not included in fixtures. Make a copy of the `MEDIA_ROOT` folder (e.g., `media/`) and restore by copying the files to the same location.

```powershell
# Simple copy example
robocopy .\media .\backups\media_backup /E
```

### 6) Common Problems and Solutions
- Error: "table does not exist" after `loaddata` -> run `migrate` before creating tables.
- Misaligned migrations between branches -> use `python manage.py showmigrations` and consider `--fake` if you've manually created the structure.
- JSON encoding errors -> check that `dumpdata` and `loaddata` use the same Django/serializer version.
- PostgreSQL permissions -> ensure the DB user has necessary privileges to create tables/indexes when restoring.

### 7) Quick Verification Checks
- Check applied migrations:

```powershell
python manage.py showmigrations
```

- Check that the app starts:

```powershell
python manage.py runserver
```

- Verify expected data exists (Django shell):

```powershell
python manage.py shell
>>> from myapp.models import MyModel
>>> MyModel.objects.count()
```

### 8) Summarized Best Practices
- Always backup before destructive changes.
- Test migrations in staging before production.
- Keep migrations in version control.
- Maintain documented scripts or procedures for restore and verification.

### Resources and References
- Official Django documentation on migrations: https://docs.djangoproject.com/en/stable/topics/migrations/
- Dumpdata/Loaddata: https://docs.djangoproject.com/en/stable/ref/django-admin/#dumpdata

---

[DJC](https://www.djc.pe/) >
[Tutorials](https://tutorial-hub.djc.pe/)