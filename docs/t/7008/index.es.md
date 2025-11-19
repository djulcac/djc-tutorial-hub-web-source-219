---
type_content: tutorial  
title: Cómo usar UUID v5 en JavaScript (HTML + Web Crypto API)  
description: Usar uuid v5 en javascript y pruebas  
keywords: javascript, uuid, v5, crypto, api  
date: 2025-11-19  
author: Danny
---

# Cómo usar UUID v5 en JavaScript (HTML + Web Crypto API)

En este tutorial aprenderás a generar **UUID versión 5 (UUID v5)** usando únicamente **HTML y JavaScript**, sin librerías externas. Usaremos la API nativa `crypto.subtle.digest`, disponible en todos los navegadores modernos.

UUID v5 es ideal cuando necesitas **identificadores únicos pero determinísticos**, es decir, que siempre generen el mismo resultado para el mismo texto + namespace.

---

## 1. ¿Qué es un UUID v5?

Un **UUID v5** se genera aplicando:

* Un **namespace UUID** (puede ser uno estándar o uno personalizado)
* Un **nombre** (string)
* Un **hash SHA‑1**

Es determinístico: si pasas siempre el mismo namespace + texto, obtendrás el mismo UUID.

---

## 2. Namespaces estándar

RFC 4122 define estos namespaces:

| Tipo | UUID                                   |
| ---- | -------------------------------------- |
| DNS  | `6ba7b810-9dad-11d1-80b4-00c04fd430c8` |
| URL  | `6ba7b811-9dad-11d1-80b4-00c04fd430c8` |
| OID  | `6ba7b812-9dad-11d1-80b4-00c04fd430c8` |
| X500 | `6ba7b814-9dad-11d1-80b4-00c04fd430c8` |

También puedes usar un **namespace personalizado**, generado con UUID v4.

---

## 3. Función JavaScript para generar UUID v5

Aquí tienes la función completa que genera UUID v5 desde cero:

```javascript
async function uuidv5(name, namespace) {
    const textEncoder = new TextEncoder();
    const nameBytes = textEncoder.encode(name);

    const ns = namespace.replace(/-/g, "");
    const nsBytes = new Uint8Array(ns.match(/.{1,2}/g).map(byte => parseInt(byte, 16)));

    const combined = new Uint8Array(nsBytes.length + nameBytes.length);
    combined.set(nsBytes);
    combined.set(nameBytes, nsBytes.length);

    const hashBuffer = await crypto.subtle.digest("SHA-1", combined);
    const hash = new Uint8Array(hashBuffer);

    hash[6] = (hash[6] & 0x0f) | 0x50;
    hash[8] = (hash[8] & 0x3f) | 0x80;

    const hex = [...hash].map(b => b.toString(16).padStart(2, "0")).join("");

    return [
        hex.substring(0, 8),
        hex.substring(8, 12),
        hex.substring(12, 16),
        hex.substring(16, 20),
        hex.substring(20, 32)
    ].join("-");
}
```

---

## 4. Ejemplo completo en HTML

Copia y pega este archivo `.html` y pruébalo en cualquier navegador:

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>UUID v5 Example</title>
</head>
<body>
  <h2>Generar UUID v5</h2>

  <input id="name" placeholder="Texto para generar UUID" />
  <button onclick="generateUUIDv5()">Generar</button>

  <p><strong>UUID v5:</strong> <span id="result"></span></p>

<script>
async function uuidv5(name, namespace) {
    const textEncoder = new TextEncoder();
    const nameBytes = textEncoder.encode(name);

    const ns = namespace.replace(/-/g, "");
    const nsBytes = new Uint8Array(ns.match(/.{1,2}/g).map(byte => parseInt(byte, 16)));

    const combined = new Uint8Array(nsBytes.length + nameBytes.length);
    combined.set(nsBytes);
    combined.set(nameBytes, nsBytes.length);

    const hashBuffer = await crypto.subtle.digest("SHA-1", combined);
    const hash = new Uint8Array(hashBuffer);

    hash[6] = (hash[6] & 0x0f) | 0x50;
    hash[8] = (hash[8] & 0x3f) | 0x80;

    const hex = [...hash].map(b => b.toString(16).padStart(2, "0")).join("");

    return [
        hex.substring(0, 8),
        hex.substring(8, 12),
        hex.substring(12, 16),
        hex.substring(16, 20),
        hex.substring(20, 32)
    ].join("-");
}

async function generateUUIDv5() {
  const name = document.getElementById("name").value;
  const DNS_NAMESPACE = "6ba7b810-9dad-11d1-80b4-00c04fd430c8";

  const uuid = await uuidv5(name, DNS_NAMESPACE);
  document.getElementById("result").innerText = uuid;
}
</script>
</body>
</html>
```

---

## 5. ¿Cómo probarlo?

1. Ingresa un texto en el cuadro (por ejemplo: `example.com`).
2. Presiona **Generar**.
3. Obtendrás un UUID v5 siempre igual.

Ejemplo:

```
9073926b-929f-31c2-abc9-fad77ae3e8eb
```

---

## 6. Usar tu propio Namespace personalizado

Si quieres un namespace propio:

1. Genera en Python o JS un UUID v4.
2. Guárdalo (archivo, variable, config).
3. Úsalo así:

```javascript
const MY_NAMESPACE = "3f52c084-2c22-4c62-bec7-53d704d6e02b";
const id = await uuidv5("usuario123", MY_NAMESPACE);
```

Siempre obtendrás el mismo resultado para ese nombre.

---

Con esta función puedes generar UUID v5:

* Sin librerías
* En cualquier navegador moderno
* De forma determinística
* Compatible con Python, Node.js, Go, Java y más

Si quieres puedo agregar:

* Ejemplo en módulos ES6
* Versión optimizada
* Cómo validar UUID v5
* Cómo crear un WebComponent para generar UUID v5
