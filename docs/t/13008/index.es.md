---
type_content: tutorial  
title: Cómo usar entornos virtuales (venv) en Python con Visual Studio Code en Windows  
description: Cómo usar entornos virtuales (venv) en Python con Visual Studio Code en Windows
keywords: python, venv, windows, powershell
date: 2026-01-17  
author: Erickson
---

# Cómo usar entornos virtuales (venv) en Python con Visual Studio Code en Windows

## Crear el entorno virtual

Abre tu proyecto en VS Code y luego la terminal integrada:

> **Terminal → New Terminal**

Ejecuta:

```bash
python -m venv venv
```

Esto creará una carpeta llamada `venv/`.

---

## Activar el venv (Windows)

En la terminal de VS Code:

### Opción recomendada (PowerShell):

```powershell
.\venv\Scripts\Activate.ps1
```

Si te sale error de permisos, ejecuta una sola vez:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

Luego vuelve a activar el entorno.

---

### Opción CMD:

```bat
venv\Scripts\activate
```

---

Cuando esté activo verás algo así:

```text
(venv) C:\Users\Danny\proyecto>
```

---

## Seleccionar el intérprete en VS Code

Presiona:

```
Ctrl + Shift + P
```

Escribe:

```
Python: Select Interpreter
```

Y elige el que diga algo como:

```
.\venv\Scripts\python.exe
```

Esto hace que VS Code use tu entorno virtual automáticamente.

---

## Instalar paquetes dentro del venv

Con el entorno activo:

```bash
pip install requests flask django
```

Verifica:

```bash
pip list
```

---

## Ejecutar tu script

```bash
python main.py
```

---

## (Opcional) .gitignore

Para no subir el entorno virtual a Git:

```gitignore
venv/
```

---

## Problemas comunes

### python no se reconoce

Instala Python y marca la opción:

```
Add Python to PATH
```

---

### El venv no se activa en VS Code

Cierra y vuelve a abrir VS Code
Luego revisa que el intérprete seleccionado sea el del venv.
