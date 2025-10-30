---
type_content: tutorial
keywords: django login, django logout, django register, authentication in django, create login in django, django users, django authentication tutorial
---

# How to Authenticate Users in Django (Login, Logout, and Registration)

Django includes a powerful **user authentication system** that makes it easy to handle user logins, logouts, and registration.  
In this tutorial, you’ll learn how to implement **login, logout, and user registration** step by step using Django’s built-in tools.

---

## What Does Django’s Authentication System Include?

Django’s authentication system manages:

- User creation and management  
- Secure (encrypted) passwords  
- Sessions to keep users logged in  
- Ready-to-use login and registration forms  
- User permissions and groups  

All of this is available through the `django.contrib.auth` module.

---

## 1. Set Up the Project

Make sure you already have a Django project created. If not, create one with:

```bash
django-admin startproject my_project
cd my_project
python manage.py startapp accounts
```

Then, add the app to your `settings.py` file:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',  # our user app
]
```

---

## 2. Create the User Model (Optional)

Django includes a default `User` model, but if you need customization, you can extend it:

```python
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass
```

If you use this model, remember to configure it in your `settings.py`:

```python
AUTH_USER_MODEL = 'accounts.CustomUser'
```

---

## 3. Create the Registration Form

In `accounts/forms.py`:

```python
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
```

---

## 4. Create Views for Registration, Login, and Logout

In `accounts/views.py`:

```python
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid credentials'})
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')
```

---

## 5. Create the HTML Templates

### `templates/accounts/register.html`

```html
<h2>Register</h2>
<form method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Sign up</button>
</form>
<a href="{% url 'login' %}">Already have an account? Log in</a>
```

### `templates/accounts/login.html`

```html
<h2>Login</h2>
{% if error %}
<p style="color:red;">{{ error }}</p>
{% endif %}
<form method="POST">
    {% csrf_token %}
    <input type="text" name="username" placeholder="Username" required>
    <input type="password" name="password" placeholder="Password" required>
    <button type="submit">Log in</button>
</form>
<a href="{% url 'register' %}">Create a new account</a>
```

---

## 6. Define the Routes (urls.py)

In `accounts/urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
```

And in the project’s main `urls.py`:

```python
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
]
```

---

## 7. Protect Views with Login Required

You can restrict access to certain pages using the `login_required` decorator:

```python
from django.contrib.auth.decorators import login_required

@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html')
```

Make sure to define where users are redirected if they’re not logged in:

```python
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/home/'
LOGOUT_REDIRECT_URL = '/accounts/login/'
```

---

## 8. Test the System

1. Run the development server:

   ```bash
   python manage.py runserver
   ```

2. Visit:

   * `/accounts/register/` → to register
   * `/accounts/login/` → to log in
   * `/accounts/logout/` → to log out

Django will automatically handle user sessions.

---

With very little code, Django gives you a **fully functional authentication system** out of the box.
You can now register users, log in, log out, and protect views easily.

From here, you can extend the system with **password recovery**, **email verification**, or **custom user profiles**.
