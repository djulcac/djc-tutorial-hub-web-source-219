---
type_content: tutorial
keywords: django login, django logout, django registro, autenticación en django, crear login en django, usuarios en django, tutorial django autenticación
---

# Cómo autenticar usuarios en Django (Login, logout y registro)

Django incluye un potente sistema de **autenticación de usuarios** que facilita la gestión de inicios de sesión, cierres de sesión y registro de nuevos usuarios.  
En este tutorial aprenderás cómo implementar **login, logout y registro** de usuarios paso a paso usando las herramientas que Django proporciona por defecto.

---

## ¿Qué incluye el sistema de autenticación de Django?

El sistema de autenticación de Django maneja:

- Creación y gestión de usuarios.
- Contraseñas seguras (encriptadas).
- Sesiones para mantener a los usuarios autenticados.
- Formularios listos para login y registro.
- Permisos y grupos de usuarios.

Todo esto está disponible a través del módulo `django.contrib.auth`.

---

## 1. Configurar el proyecto

Asegúrate de tener un proyecto Django creado. Si aún no lo tienes:

```bash
django-admin startproject mi_proyecto
cd mi_proyecto
python manage.py startapp cuentas
```

Agrega la app en tu archivo `settings.py`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cuentas',  # nuestra app de usuarios
]
```

---

## 2. Crear el modelo de usuario (opcional)

Django incluye un modelo de usuario por defecto (`User`), pero si quieres personalizarlo puedes extenderlo:

```python
from django.contrib.auth.models import AbstractUser

class UsuarioPersonalizado(AbstractUser):
    pass
```

Si usas este modelo, recuerda configurarlo en `settings.py`:

```python
AUTH_USER_MODEL = 'cuentas.UsuarioPersonalizado'
```

---

## 3. Crear el formulario de registro

En `cuentas/forms.py`:

```python
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
```

---

## 4. Crear vistas para registro, login y logout

En `cuentas/views.py`:

```python
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegistroForm

def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'cuentas/registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('inicio')
        else:
            return render(request, 'cuentas/login.html', {'error': 'Credenciales incorrectas'})
    return render(request, 'cuentas/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')
```

---

## 5. Crear las plantillas HTML

### `templates/cuentas/registro.html`

```html
<h2>Registro</h2>
<form method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Registrarse</button>
</form>
<a href="{% url 'login' %}">¿Ya tienes cuenta? Inicia sesión</a>
```

### `templates/cuentas/login.html`

```html
<h2>Iniciar sesión</h2>
{% if error %}
<p style="color:red;">{{ error }}</p>
{% endif %}
<form method="POST">
    {% csrf_token %}
    <input type="text" name="username" placeholder="Usuario" required>
    <input type="password" name="password" placeholder="Contraseña" required>
    <button type="submit">Entrar</button>
</form>
<a href="{% url 'registro' %}">Crear cuenta nueva</a>
```

---

## 6. Definir las rutas (urls.py)

En `cuentas/urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro_view, name='registro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
```

Y en el `urls.py` principal del proyecto:

```python
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cuentas/', include('cuentas.urls')),
]
```

---

## 7. Proteger vistas con login requerido

Puedes restringir el acceso a ciertas páginas usando el decorador `login_required`:

```python
from django.contrib.auth.decorators import login_required

@login_required
def perfil_view(request):
    return render(request, 'cuentas/perfil.html')
```

Y asegúrate de definir a dónde redirigir si un usuario no ha iniciado sesión:

```python
LOGIN_URL = '/cuentas/login/'
LOGIN_REDIRECT_URL = '/inicio/'
LOGOUT_REDIRECT_URL = '/cuentas/login/'
```

---

## 8. Probar el sistema

1. Ejecuta el servidor:

   ```bash
   python manage.py runserver
   ```
2. Ve a:

   * `/cuentas/registro/` → para registrarte
   * `/cuentas/login/` → para iniciar sesión
   * `/cuentas/logout/` → para cerrar sesión

Django gestionará automáticamente las sesiones de usuario.

---

Con muy poco código, Django te ofrece un sistema completo de autenticación listo para usar.
Ya puedes registrar usuarios, iniciar sesión, cerrar sesión y proteger rutas fácilmente.

A partir de aquí puedes extender el sistema con **recuperación de contraseñas**, **confirmación por correo electrónico** o **perfiles personalizados**.

