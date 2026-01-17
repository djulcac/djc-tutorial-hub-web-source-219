---
type_content: tutorial  
title: Instalar Python en Windows (PASO A PASO)  
description: Instalar Python en Windows (PASO A PASO)
keywords: python, windows
date: 2026-01-17  
author: Erickson
---
# Instalar Python en Windows (PASO A PASO)

## Paso 1: Descargar Python

1. Abre tu navegador
2. Ve a **[https://www.python.org](https://www.python.org)**
3. Haz clic en **Downloads**
4. Presiona **Download Python 3.x.x** (el botón amarillo)

>  Descarga siempre la **versión más reciente estable**

---

## Paso 2: Instalar Python (MUY IMPORTANTE)

1. Abre el archivo descargado (`python-3.x.x-amd64.exe`)
2. **MARCA ESTA CASILLA OBLIGATORIA** 
    **Add Python to PATH**
3. Luego haz clic en:
    **Install Now**

 Si no marcas *Add Python to PATH*, Python no funcionará en la terminal.

---

## Paso 3: Verificar instalación

Abre **PowerShell** o **CMD** y escribe:

```bash
python --version
```

O también:

```bash
py --version
```

Si ves algo como:

```
Python 3.12.x
```

 ¡Python está instalado correctamente!

---

## Paso 4: Instalar pip (normalmente ya viene)

Verifica:

```bash
pip --version
```

Si aparece una versión →  listo

---

## Paso 5: Crear un entorno virtual (recomendado)

Dentro de tu proyecto:

```bash
python -m venv venv
```

Activar el entorno:

### PowerShell

```powershell
.\venv\Scripts\activate
```

### CMD

```cmd
venv\Scripts\activate
```

Cuando veas:

```
(venv)
```

El entorno está activo

---

## Paso 6: Instalar dependencias

Ejemplo:

```bash
pip install django
```

---

## Problemas comunes y soluciones

### `python no se reconoce como comando`

 No marcaste **Add Python to PATH**
 Solución: reinstala Python y marca la casilla

---

###  Error al activar venv en PowerShell

 Política de scripts bloqueada
 Solución:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

---

## Recomendaciones finales

* Usa **Python 3.10+**
* Usa **entornos virtuales** siempre
* Usa **VS Code** para programar

---

