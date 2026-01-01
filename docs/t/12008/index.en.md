---
title: Contest 1111 - Codeforces - DJC
keywords: Codeforces, contest, python
date: 2026-01-01
author: Danny
---

## A. Superhero Transformation

**Time limit per test:** 1 second
**Memory limit per test:** 256 megabytes

We all know that a superhero can transform into certain other superheroes. However, not all superheroes can transform into any other superhero. A superhero with name **s** can transform into another superhero with name **t** if **s** can be made equal to **t** by changing any vowel in **s** to any other vowel and any consonant in **s** to any other consonant. Multiple changes can be made.

In this problem, the letters **'a'**, **'e'**, **'i'**, **'o'**, and **'u'** are considered vowels, and all other letters are considered consonants.

Given the names of two superheroes, determine whether the superhero with name **s** can be transformed into the superhero with name **t**.

---

### Input

The first line contains the string **s**, with length between **1** and **1000**, inclusive.

The second line contains the string **t**, with length between **1** and **1000**, inclusive.

Both strings **s** and **t** are guaranteed to be different and consist only of lowercase English letters.

---

### Output

Print **"Yes"** (without quotes) if the superhero with name **s** can be transformed into the superhero with name **t**, or **"No"** (without quotes) otherwise.

You may print each letter in any case (uppercase or lowercase).

---

### Examples

**Input**

```
a
u
```

**Output**

```
Yes
```

**Input**

```
abc
ukm
```

**Output**

```
Yes
```

**Input**

```
akm
ua
```

**Output**

```
No
```

---

### Note

In the first sample, since both **'a'** and **'u'** are vowels, it is possible to convert string **s** into **t**.

In the third sample, **'k'** is a consonant, whereas **'a'** is a vowel, so it is not possible to convert string **s** into **t**.
