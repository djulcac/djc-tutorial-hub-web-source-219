---
type_content: tutorial  
title: How to View Internal Searches on Your Website Using Google Analytics 4 (GA4)  
description: How to view internal searches on your website using Google Analytics 4 (GA4)
keywords: google, ga4, search
date: 2025-11-20
author: Danny  
---

# How to View Internal Searches on Your Website Using Google Analytics 4 (GA4)

Knowing what users search for inside your website helps you understand their needs, improve your content, and discover new opportunities. In this tutorial, you will learn how to view **internal searches** in **Google Analytics 4 (GA4)**.

---

<iframe width="100%" height="315" src="https://www.youtube.com/embed/nfyUEBlD1eI?si=1u3nBvZGLeDV9baf" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---

## 1. Check if your website sends the search term in the URL

GA4 can only track internal searches if your site’s search engine places the search term in the URL.

Correct examples:

```
/buscar?q=python
/search?query=javascript
/busqueda?search=html
```

If your search engine uses one of these standard parameters, GA4 detects it automatically:

* `q`
* `s`
* `search`
* `query`
* `keyword`

If your site uses another parameter (e.g., `texto`, `value`, `q2`), you’ll need to configure it manually (explained later).

---

## 2. GA4 automatically registers the “view_search_results” event

When GA4 identifies a compatible search parameter, it creates the following event:

```
view_search_results
```

This event includes the dimension:

```
search_term
```

which contains the text entered by the user.

---

## 3. How to view internal searches in GA4

### Step 1: Go to **Explore**

In the left-hand menu:

```
Explore → Explorations → Free Form
```

### Step 2: Enable the dimension

In the **Dimensions** section, find and enable:

```
Search term (search_term)
```

If it doesn’t appear, go to:

```
Admin → Events → view_search_results
```

and enable the custom dimension *search_term*.

### Step 3: Create the table

Drag **Search term** into *Rows* and any metric (such as *Events* or *Users*) into *Values*.

You will get something like:

| Search term | Events | Users |
| ----------- | ------ | ----- |
| python      | 34     | 22    |
| tutorial js | 12     | 7     |
| html        | 8      | 5     |

---

## 4. If GA4 is not detecting your searches

This happens when your site uses a non-standard search parameter.

### Step 1: Go to **Admin**

```
Admin → Data Streams → Web
```

### Step 2: Open **Configure tag settings**

Inside the data stream, select:

```
More tagging settings → Site search settings
```

### Step 3: Add your search parameter

In “Query parameters”, enter your parameter name.

Example: if your URL is:

```
/buscar?value=javascript
```

then add:

```
value
```

Save. GA4 will begin tracking searches from that moment on.

---

* Review internal searches at least once per week.
* Use popular searches to create new tutorials.
* Identify missing content by checking searches with no results.
* If your search engine uses JavaScript or AJAX without URL parameters, you’ll need to **send a manual event to GA4** (I can help you set this up).
