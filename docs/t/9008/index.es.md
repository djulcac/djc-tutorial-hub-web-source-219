---
type_content: tutorial  
title: Cómo ver las búsquedas internas en tu web usando Google Analytics 4 (GA4)  
description: Cómo ver las búsquedas internas en tu web usando Google Analytics 4 (GA4)
keywords: google, ga4, busqueda
date: 2025-11-20
author: Danny  
---


# Cómo ver las búsquedas internas en tu web usando Google Analytics 4 (GA4)

Saber qué buscan los usuarios dentro de tu sitio web te permite entender sus necesidades, mejorar tu contenido y detectar nuevas oportunidades. En este tutorial aprenderás a visualizar las **búsquedas internas** en **Google Analytics 4 (GA4)**.

---

<iframe width="100%" height="315" src="https://www.youtube.com/embed/nfyUEBlD1eI?si=1u3nBvZGLeDV9baf" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
---

## 1. Verifica si tu web envía el término de búsqueda en la URL

GA4 solo puede registrar las búsquedas internas si el buscador de tu sitio coloca el término en la URL.

Ejemplos correctos:

```
/buscar?q=python
/search?query=javascript
/busqueda?search=html
```

Si tu buscador usa uno de estos parámetros estándar, GA4 lo detecta automáticamente:

* `q`
* `s`
* `search`
* `query`
* `keyword`

Si tu web usa otro parámetro (ej: `texto`, `value`, `q2`), deberás configurarlo manualmente (lo veremos más abajo).

---

## 2. GA4 registra automáticamente el evento “view_search_results”

Cuando GA4 reconoce un parámetro de búsqueda compatible, crea el evento:

```
view_search_results
```

Este evento incluye la dimensión:

```
search_term
```

que contiene el texto buscado por el usuario.

---

## 3. Cómo ver las búsquedas internas en GA4

### Paso 1: Ir a **Explorar**

En el menú izquierdo:

```
Explorar → Exploraciones → Análisis libre
```

### Paso 2: Activar la dimensión

En la sección de **Dimensiones**, busca y activa:

```
Término de búsqueda (search_term)
```

Si no aparece, ve a:

```
Administrar → Eventos → view_search_results
```

y habilita la dimensión personalizada *search_term*.

### Paso 3: Crear la tabla

Arrastra **Término de búsqueda** a *Filas* y cualquier métrica (por ejemplo *Eventos* o *Usuarios*) a *Valores*.

Obtendrás algo como:

| Término de búsqueda | Eventos | Usuarios |
| ------------------- | ------- | -------- |
| python              | 34      | 22       |
| tutorial js         | 12      | 7        |
| html                | 8       | 5        |

---

## 4. Si GA4 no está detectando tus búsquedas

Esto ocurre cuando tu sitio usa un parámetro diferente a los estándar.

### Paso 1: Ir a **Administrar**

```
Administrar → Flujos de datos → Web
```

### Paso 2: Abrir **Configurar etiquetas**

Dentro del flujo de datos selecciona:

```
Más configuraciones → Configuración avanzada de búsqueda en sitio
```

### Paso 3: Agregar tu parámetro de búsqueda

En “Parámetros de consulta” escribe el nombre de tu parámetro.

Ejemplo si tu URL es:

```
/buscar?value=javascript
```

entonces agrega:

```
value
```

Guardar. GA4 empezará a registrar búsquedas desde ese momento.

---

* Revisa las búsquedas internas al menos una vez por semana.
* Usa las búsquedas populares para crear nuevos tutoriales.
* Detecta búsquedas sin resultados para identificar temas faltantes.
* Si usas un buscador en JavaScript o AJAX sin parámetros en la URL, deberás **enviar un evento manual a GA4** (puedo ayudarte a configurarlo).
