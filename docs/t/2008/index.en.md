---
title: How to Use HTML Templates in Django (Templates and Contexts)
---

# How to Use HTML Templates in Django (Templates and Contexts)

[DJC](https://www.djc.pe/) >  
[Tutorials](../../index.md)

| [Django](../../c/django/index.md) |

---

**Templates** in Django allow you to separate the server-side logic from the visual design of your web application. Thanks to them, you can reuse HTML code, pass data from views, and keep your project organized.

In this guide, you’ll learn **what templates are in Django**, **how to use them**, and **how to pass data through contexts**. You’ll also see how to apply **template inheritance** to create reusable layouts.

---

## What is a Template in Django?

A **template** is an HTML file that can contain special tags and variables that Django processes to generate dynamic content.

For example, a template can display a list of users, personalized messages, or information from a database.

**Basic structure of a template:**

```html
<!DOCTYPE html>
<html>
<head>
  <title>{{ title }}</title>
</head>
<body>
  <h1>Hello, {{ user_name }}!</h1>
  <p>Welcome to my website.</p>
</body>
</html>
````

The variables between `{{ }}` are replaced with the values Django sends from the view.

---

## How to Create and Use Templates in Django

By convention, templates are stored inside a folder called **templates**.

### 1. Create the Templates Folder

Inside your app, create a folder:

```
my_project/
│
├── my_app/
│   ├── templates/
│   │   └── my_app/
│   │       └── index.html
```

> It’s recommended to include the app name inside the `templates` folder to avoid conflicts when you have multiple apps.

### 2. Configure Templates in `settings.py`

Make sure Django knows where to look for your templates:

```python
# settings.py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # global directory
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

With `APP_DIRS: True`, Django will automatically search for templates inside each app.

### 3. Create a View That Uses the Template

```python
# views.py
from django.shortcuts import render

def home(request):
    context = {
        'title': 'Home',
        'user_name': 'Danny',
    }
    return render(request, 'my_app/index.html', context)
```

### 4. Link the View in `urls.py`

```python
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```

Now, when you visit `http://localhost:8000/`, Django will render the template with the provided data.

---

## What is Context in Django?

A **context** is a dictionary containing the data that is passed from the view to the template.

In the previous example:

```python
context = {
    'title': 'Home',
    'user_name': 'Danny',
}
```

The template can access these values using `{{ title }}` or `{{ user_name }}`.

---

## Template Inheritance in Django

**Template inheritance** allows you to define a base structure (such as the header, menu, and footer) and reuse it across multiple pages.

### Example:

#### base.html

```html
<!DOCTYPE html>
<html>
<head>
  <title>{% block title %}My Site{% endblock %}</title>
</head>
<body>
  <header>
    <h1>My Website</h1>
  </header>

  <main>
    {% block content %}{% endblock %}
  </main>

  <footer>
    <p>© 2025 My Site</p>
  </footer>
</body>
</html>
```

#### index.html

```html
{% extends "my_app/base.html" %}

{% block title %}Home{% endblock %}

{% block content %}
  <h2>Welcome, {{ user_name }}</h2>
  <p>This is the main content area.</p>
{% endblock %}
```

This way, all pages can share the same base layout without repeating code.

---

## Common Template Tags and Filters

Django includes template tags and filters that let you manipulate data inside your HTML:

| Type        | Example                          | Description                      |                            |
| ----------- | -------------------------------- | -------------------------------- | -------------------------- |
| Variable    | `{{ name }}`                     | Displays the value of a variable |                            |
| Filter      | `{{ name                         | upper }}`                        | Converts text to uppercase |
| Loop        | `{% for item in list %}`         | Iterates over a list of elements |                            |
| Conditional | `{% if user.is_authenticated %}` | Evaluates conditions             |                            |
| Extension   | `{% extends "base.html" %}`      | Inherits a base template         |                            |
| Block       | `{% block content %}`            | Defines editable sections        |                            |

---

Using **HTML templates in Django** is essential for separating server logic from visual design.
With **contexts**, you can send dynamic data to your views, and with **template inheritance**, you can keep your code clean and reusable.

Mastering this part of the framework will allow you to build professional, scalable, and easy-to-maintain web applications.

---

[DJC](https://www.djc.pe/) >
[Tutorials](../../index.md)
