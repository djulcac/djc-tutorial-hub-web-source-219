---
title: Contest 1111 - Codeforces - DJC
keywords: Codeforces, contest, python
date: 2026-01-01
author: Danny
---

## A. Transformación de Superhéroes

**Límite de tiempo por prueba:** 1 segundo
**Límite de memoria por prueba:** 256 megabytes

Todos sabemos que un superhéroe puede transformarse en ciertos otros superhéroes. Pero no todos los superhéroes pueden transformarse en cualquier otro superhéroe. Un superhéroe con nombre **s** puede transformarse en otro superhéroe con nombre **t** si **s** puede hacerse igual a **t** cambiando cualquier vocal en **s** por cualquier otra vocal y cualquier consonante en **s** por cualquier otra consonante. Se pueden realizar múltiples cambios.

En este problema, consideramos que las letras **'a'**, **'e'**, **'i'**, **'o'** y **'u'** son vocales, y todas las demás letras son consonantes.

Dado el nombre de dos superhéroes, determina si el superhéroe con nombre **s** puede transformarse en el superhéroe con nombre **t**.

---

### Entrada

La primera línea contiene la cadena **s**, con una longitud entre **1** y **1000**, inclusive.

La segunda línea contiene la cadena **t**, con una longitud entre **1** y **1000**, inclusive.

Ambas cadenas **s** y **t** están garantizadas como diferentes y consisten únicamente en letras minúsculas del alfabeto inglés.

---

### Salida

Imprime **"Yes"** (sin comillas) si el superhéroe con nombre **s** puede transformarse en el superhéroe con nombre **t**, o **"No"** (sin comillas) en caso contrario.

Puedes imprimir cada letra en mayúscula o minúscula.

---

### Ejemplos

**Entrada**

```
a
u
```

**Salida**

```
Yes
```

**Entrada**

```
abc
ukm
```

**Salida**

```
Yes
```

**Entrada**

```
akm
ua
```

**Salida**

```
No
```

---

### Nota

En el primer ejemplo, dado que tanto **'a'** como **'u'** son vocales, es posible convertir la cadena **s** en **t**.

En el tercer ejemplo, **'k'** es una consonante, mientras que **'a'** es una vocal, por lo que no es posible convertir la cadena **s** en **t**.
