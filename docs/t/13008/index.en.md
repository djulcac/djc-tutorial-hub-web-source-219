---
type_content: tutorial  
title: How to Use Virtual Environments (venv) in Python with Visual Studio Code on Windows  
description: How to Use Virtual Environments (venv) in Python with Visual Studio Code on Windows  
keywords: python, venv, windows, powershell  
date: 2026-01-17  
author: Erickson
---

# How to Use Virtual Environments (venv) in Python with Visual Studio Code on Windows

## Create the Virtual Environment

Open your project in VS Code and then the integrated terminal:

> **Terminal → New Terminal**

Run:

```bash
python -m venv venv
```

This will create a folder called `venv/`.

---

## Activate the venv (Windows)

In the VS Code terminal:

### Recommended option (PowerShell):

```powershell
.\venv\Scripts\Activate.ps1
```

If you get a permission error, run this once:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

Then activate the environment again.

---

### CMD option:

```bat
venv\Scripts\activate
```

---

When it is active, you will see something like:

```text
(venv) C:\Users\Danny\project>
```

---

## Select the Interpreter in VS Code

Press:

```
Ctrl + Shift + P
```

Type:

```
Python: Select Interpreter
```

And choose the one that looks like:

```
.\venv\Scripts\python.exe
```

This makes VS Code use your virtual environment automatically.

---

## Install Packages Inside the venv

With the environment active:

```bash
pip install requests flask django
```

Check:

```bash
pip list
```

---

## Run Your Script

```bash
python main.py
```

---

## (Optional) .gitignore

To avoid uploading the virtual environment to Git:

```gitignore
venv/
```

---

## Common Problems

### "python is not recognized"

Install Python and make sure to check:

```
Add Python to PATH
```

---

### The venv does not activate in VS Code

Close and reopen VS Code.
Then make sure the selected interpreter is the one from the venv.
