---
type_content: tutorial
title: Install Python on Windows (STEP BY STEP)
description: Install Python on Windows (STEP BY STEP)
keywords: python, windows
date: 2026-01-17
author: Erickson
---
# Tutorial: Install Python on Windows (STEP BY STEP)

## Step 1: Download Python

1. Open your web browser
2. Go to **[https://www.python.org](https://www.python.org)**
3. Click on **Downloads**
4. Click **Download Python 3.x.x** (the yellow button)

> Always download the **latest stable version**

---

## Step 2: Install Python (VERY IMPORTANT)

1. Open the downloaded file (`python-3.x.x-amd64.exe`)
2. **CHECK THIS REQUIRED BOX**
   **Add Python to PATH**
3. Then click:
   **Install Now**

If you do not check *Add Python to PATH*, Python will not work in the terminal.

---

## Step 3: Verify the installation

Open **PowerShell** or **CMD** and type:

```bash
python --version
```

Or also:

```bash
py --version
```

If you see something like:

```
Python 3.12.x
```

Python is installed correctly!

---

## Step 4: Install pip (it usually comes preinstalled)

Verify with:

```bash
pip --version
```

If a version appears → ready

---

## Step 5: Create a virtual environment (recommended)

Inside your project folder:

```bash
python -m venv venv
```

Activate the environment:

### PowerShell

```powershell
.\venv\Scripts\activate
```

### CMD

```cmd
venv\Scripts\activate
```

When you see:

```
(venv)
```

The environment is active.

---

## Step 6: Install dependencies

Example:

```bash
pip install django
```

---
