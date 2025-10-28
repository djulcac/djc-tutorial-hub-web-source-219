---
title: Migrar y restaurar datos en Django
---

# Migrar y restaurar datos en Django

[DJC](https://www.djc.pe/es/) >
[Tutoriales](https://tutorial-hub.djc.pe/es/)

| [Django](../../c/django/index.md) |
[Python](../../c/python/index.md) |
[SQL](../../c/sql/index.md) |

Este tutorial explica, en español y con ejemplos para PowerShell en Windows, cómo manejar migraciones (crear/aplicar) y cómo hacer backups y restores de los datos de un proyecto Django. Incluye opciones con fixtures (`dumpdata` / `loaddata`) y dumps a nivel de base de datos (SQLite, PostgreSQL, MySQL).

### Contrato rápido
- Entrada: un proyecto Django con `manage.py` y el entorno virtual activado.
- Salida: migraciones aplicadas o revertidas, y datos restaurados desde un backup.
- Errores comunes: migraciones desalineadas entre código y base de datos, permisos en PostgreSQL/MySQL, políticas de ejecución de PowerShell.

### Requisitos previos
- Python y Django instalados en el entorno virtual.
- Acceso a la base de datos (archivo SQLite, credenciales PostgreSQL/MySQL).
- En PowerShell, activa tu entorno virtual (ejemplo común):

```powershell
# Windows PowerShell
.\venv\Scripts\Activate.ps1
# Si no puedes ejecutar el script por política de ejecución, usa:
# Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Nota: también puedes usar `pipenv`, `poetry` u otro gestor; adapta los comandos según corresponda.

### 1) Migraciones: crear y aplicar

1. Crear archivos de migración a partir de cambios en modelos:

```powershell
python manage.py makemigrations
```

2. Revisar el plan de migración (opcional, útil antes de aplicar):

```powershell
python manage.py migrate --plan
```

3. Aplicar migraciones a la base de datos:

```powershell
python manage.py migrate
```

4. Ver el estado de las migraciones por app:

```powershell
python manage.py showmigrations
```

5. Forzar (fake) una migración si la estructura ya existe en la BD pero la migración no está marcada como aplicada:

```powershell
python manage.py migrate <app_name> --fake
```

Usa `--fake-initial` cuando estés probando una migración inicial en una base con tablas ya creadas por otro proceso.

### Notas sobre rollback
- Django no genera automáticamente migraciones inversas para todo; muchas migraciones sí (crear/eliminar campo), pero para revertir a una versión anterior normalmente se aplica `migrate <app> <migration_name>`.

Ejemplo: volver a la migración `0003_auto` de la app `blog`:

```powershell
python manage.py migrate blog 0003_auto
```

### 2) Backup y restore de datos en Django

Existen dos métodos principales:
- Backups a nivel de aplicación (fixtures) con `dumpdata` / `loaddata`.
- Backups a nivel de base de datos (pg_dump/pg_restore, mysqldump, copia del archivo SQLite).

Elige el método según el tamaño de tus datos y si necesitas preservar esquemas/índices/procedimientos.

#### A) Uso de fixtures: dumpdata / loaddata

1. Hacer un volcado JSON de toda la base (útil para proyectos pequeños o despliegues entre entornos Django):

```powershell
python manage.py dumpdata --natural-foreign --natural-primary --indent 2 > backup_all.json
```

2. Para volcar solo una app específica:

```powershell
python manage.py dumpdata myapp --indent 2 > myapp_backup.json
```

3. Restaurar desde una fixture:

```powershell
python manage.py loaddata myapp_backup.json
```

Notas:
- `dumpdata` escribe datos en formato JSON (o XML/ YAML si instalas soporte). No incluye archivos de media.
- Para datos sensibles, cifra o protege el archivo resultante.

#### B) Backups a nivel de base de datos

- SQLite: copia del archivo `db.sqlite3` (asegúrate de que Django no esté escribiendo durante la copia).

```powershell
# Detener proceso que use la DB (si aplica) y luego copiar:
Copy-Item .\db.sqlite3 .\backups\db_$(Get-Date -Format "yyyyMMdd_HHmmss").sqlite3
```

- PostgreSQL: `pg_dump` / `pg_restore` (recomendado para bases grandes o producción).

```powershell
# Dump (formato personalizado, comprimido)
pg_dump -U dbuser -h dbhost -Fc dbname -f backup_db.dump

# Restaurar (ejemplo con base recién creada)
pg_restore -U dbuser -h dbhost -d dbname --clean --no-owner backup_db.dump
```

Si `pg_restore` no está disponible en el PATH en Windows, instala PostgreSQL o usa las utilidades desde el binario.

- MySQL / MariaDB: `mysqldump` y `mysql` para restaurar:

```powershell
mysqldump -u dbuser -p dbname > backup_db.sql

# Restaurar
mysql -u dbuser -p dbname < backup_db.sql
```

#### Recomendaciones prácticas
- Para desarrollo o migraciones rápidas, `dumpdata` + `loaddata` funciona bien.
- Para entornos de producción con mucha data, usa pg_dump/pg_restore o mysqldump para preservar índices y rendimiento.
- Antes de restaurar en producción, prueba el restore en una copia de staging.

### 3) Flujo típico de migración + backup antes de cambios destructivos

1. Crear backup completo de la base (pg_dump o copia de SQLite).
2. Crear migrations: `makemigrations`.
3. Revisar plan: `migrate --plan`.
4. Aplicar migraciones en staging y probar.
5. Aplicar migraciones en producción en ventana de mantenimiento.

### 4) Restaurar en caso de problemas (ejemplos)

- Si usaste `dumpdata`:

```powershell
# Borrar tablas o vaciar DB según sea necesario (con cuidado)
python manage.py flush  # ADVERTENCIA: elimina todo, deja superuser? No.

python manage.py loaddata backup_all.json
```

- Si usaste `pg_dump` o `mysqldump`, usa los comandos de restore correspondientes (ver sección anterior). Asegúrate de recrear usuarios/privilegios si es necesario.

### 5) Archivos media y static
- Los archivos `MEDIA` no se incluyen en fixtures. Haz copia de la carpeta `MEDIA_ROOT` (por ejemplo `media/`) y restaura copiando los archivos al mismo lugar.

```powershell
# Ejemplo simple de copia
 robocopy .\media .\backups\media_backup /E
```

### 6) Problemas frecuentes y soluciones
- Error: "table does not exist" después de `loaddata` -> ejecuta `migrate` antes de crear las tablas.
- Migraciones desalineadas entre ramas -> usa `python manage.py showmigrations` y considera `--fake` si has creado manualmente la estructura.
- Errores de codificación JSON -> comprueba que `dumpdata` y `loaddata` usan la misma versión de Django/serializadores.
- Permisos en PostgreSQL -> asegúrate de que el usuario de la DB tenga privilegios necesarios para crear tablas/índices al restaurar.

### 7) Comprobaciones rápidas de verificación
- Comprobar migraciones aplicadas:

```powershell
python manage.py showmigrations
```

- Comprobar que la app arranca:

```powershell
python manage.py runserver
```

- Verificar que los datos esperados existen (Django shell):

```powershell
python manage.py shell
>>> from myapp.models import MyModel
>>> MyModel.objects.count()
```

### 8) Buenas prácticas resumidas
- Siempre hacer backup antes de cambios destructivos.
- Probar migraciones en staging antes de producción.
- Mantener las migraciones en el control de versiones.
- Mantener scripts o procedimientos documentados para restore y verificación.

### Recursos y referencias
- Documentación oficial Django sobre migraciones: https://docs.djangoproject.com/en/stable/topics/migrations/
- Dumpdata/Loaddata: https://docs.djangoproject.com/en/stable/ref/django-admin/#dumpdata

---

[DJC](https://www.djc.pe/es/) >
[Tutoriales](https://tutorial-hub.djc.pe/es/)
