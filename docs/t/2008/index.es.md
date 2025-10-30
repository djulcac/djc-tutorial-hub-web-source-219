---
title: Cómo usar plantillas HTML en Django (Templates y contextos)
---

# Cómo usar plantillas HTML en Django (Templates y contextos)

[DJC](https://www.djc.pe/es/) >  
[Tutoriales](../../index.md)

| [Django](../../c/django/index.md) |

---

Las **plantillas (templates)** en Django permiten separar la lógica del servidor del diseño visual de tu aplicación web. Gracias a ellas, puedes reutilizar código HTML, enviar datos desde las vistas y mantener tu proyecto organizado.

En esta guía aprenderás **qué son las plantillas en Django**, **cómo usarlas** y **cómo pasar datos mediante contextos**. Además, verás cómo aplicar **herencia de plantillas** para crear diseños reutilizables.

---

## Qué es una plantilla en Django

Una **plantilla** (template) es un archivo HTML que puede contener etiquetas y variables especiales que Django procesa para generar contenido dinámico.

Por ejemplo, una plantilla puede mostrar una lista de usuarios, mensajes personalizados o información proveniente de una base de datos.

**Estructura básica de un template:**

```html
<!DOCTYPE html>
<html>
<head>
  <title>{{ title }}</title>
</head>
<body>
  <h1>Hola, {{ nombre_usuario }}!</h1>
  <p>Bienvenido a mi sitio web.</p>
</body>
</html>
```

Las variables entre `{{ }}` son sustituidas por los valores que Django envía desde la vista.

---

## Cómo crear y usar plantillas en Django

Por convención, las plantillas se guardan dentro de una carpeta llamada **templates**.

### 1. Crear la carpeta de plantillas

Dentro de tu aplicación, crea una carpeta:

```
mi_proyecto/
│
├── mi_app/
│   ├── templates/
│   │   └── mi_app/
│   │       └── index.html
```

> Es recomendable incluir el nombre de la app dentro de la carpeta `templates` para evitar conflictos cuando tengas varias aplicaciones.

### 2. Configurar las plantillas en `settings.py`

Asegúrate de que Django sepa dónde buscar las plantillas:

```python
# settings.py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # directorio global
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

Con `APP_DIRS: True`, Django buscará automáticamente las plantillas dentro de cada aplicación.

### 3. Crear una vista que use la plantilla

```python
# views.py
from django.shortcuts import render

def inicio(request):
    contexto = {
        'title': 'Inicio',
        'nombre_usuario': 'Danny',
    }
    return render(request, 'mi_app/index.html', contexto)
```

### 4. Enlazar la vista en `urls.py`

```python
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
]
```

Ahora, al ingresar a `http://localhost:8000/`, Django renderizará el template con los datos enviados.

---

## Qué es el contexto en Django

El **contexto** es un diccionario que contiene los datos que se pasan desde la vista al template.

En el ejemplo anterior:

```python
contexto = {
    'title': 'Inicio',
    'nombre_usuario': 'Danny',
}
```

El template puede acceder a estos valores usando `{{ title }}` o `{{ nombre_usuario }}`.

---

## Herencia de plantillas en Django

La **herencia de plantillas** te permite definir una estructura base (como el encabezado, el menú y el pie de página) y reutilizarla en otras páginas.

### Ejemplo:

#### base.html

```html
<!DOCTYPE html>
<html>
<head>
  <title>{% block title %}Mi sitio{% endblock %}</title>
</head>
<body>
  <header>
    <h1>Mi sitio web</h1>
  </header>

  <main>
    {% block content %}{% endblock %}
  </main>

  <footer>
    <p>© 2025 Mi sitio</p>
  </footer>
</body>
</html>
```

#### index.html

```html
{% extends "mi_app/base.html" %}

{% block title %}Inicio{% endblock %}

{% block content %}
  <h2>Bienvenido, {{ nombre_usuario }}</h2>
  <p>Este es el contenido principal.</p>
{% endblock %}
```

De esta forma, todas las páginas pueden compartir el mismo diseño base sin repetir código.

---

## Etiquetas y filtros comunes de templates

Django incluye etiquetas y filtros que permiten manipular datos dentro del HTML:

| Tipo        | Ejemplo                             | Descripción                      |                                 |
| ----------- | ----------------------------------- | -------------------------------- | ------------------------------- |
| Variable    | `{{ nombre }}`                      | Muestra el valor de una variable |                                 |
| Filtro      | `{{ nombre                          | upper }}`                        | Convierte el texto a mayúsculas |
| Bucle       | `{% for item in lista %}`           | Recorre una lista de elementos   |                                 |
| Condicional | `{% if usuario.is_authenticated %}` | Evalúa condiciones               |                                 |
| Extensión   | `{% extends "base.html" %}`         | Hereda una plantilla base        |                                 |
| Bloques     | `{% block content %}`               | Define zonas personalizables     |                                 |

---

Usar **plantillas HTML en Django** es esencial para separar la lógica del servidor del diseño visual.
Con los **contextos** puedes enviar información dinámica a las vistas, y con la **herencia de plantillas** puedes mantener tu código limpio y reutilizable.

Dominar esta parte del framework te permitirá crear sitios web profesionales, escalables y fáciles de mantener.

---

[DJC](https://www.djc.pe/es/) >  
[Tutoriales](../../index.md)
