layout: proof
categories: branches,combinatorics
nodeid: bookofproofs$8433
orderid: 50
parentid: bookofproofs$8432
title: 
description: PROOF OF STIRLING NUMBERS AND RISING FACTORIAL POWERS ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$1112
keywords: stirling numbers and rising factorial powers,proof
contributors: bookofproofs

---


---

* Let `$n\ge 1$` be a [natural number][bookofproofs$718].
* By definition of the [Stirling numbers of the first kind][bookofproofs$8425], that involves [falling factorial powers][bookofproofs$1399] `$$x^\underline{n}= \sum_{r=1}^n\left[\begin{array}{c}n\\r\end{array}\right](-1)^{n-r}x^r.$$`
* By virtue of the [reciprocity law for factorial powers][bookofproofs$1412], we can transform this into a formula involving [rising factorial powers][bookofproofs$1399] as follows `$$\begin{align}
(-1)^n(-x)^\overline{n}&= \sum_{r=1}^n\left[\begin{array}{c}n\\r\end{array}\right](-1)^{n-r}x^r\quad\Longleftrightarrow\nonumber\\
(-1)^nx^\overline{n}&= \sum_{r=1}^n\left[\begin{array}{c}n\\r\end{array}\right](-1)^{n-r}(-x)^r\quad\Longleftrightarrow\nonumber\\
(-1)^nx^\overline{n}&= \sum_{r=1}^n\left[\begin{array}{c}n\\r\end{array}\right](-1)^{n-r}(-1)^rx^r\quad\Longleftrightarrow\nonumber\\
(-1)^nx^\overline{n}&= (-1)^{n}\sum_{r=1}^n\left[\begin{array}{c}n\\r\end{array}\right]x^r\nonumber\\
x^\overline{n}&= \sum_{r=1}^n\left[\begin{array}{c}n\\r\end{array}\right]x^r.\nonumber\\
\end{align}$$`
* By definition of the [Stirling numbers of the second kind][bookofproofs$8425], that involves [falling factorial powers][bookofproofs$1399].
`$$x^{n}= \sum_{r=1}^n\left\{\begin{array}{c}n\\r\end{array}\right\}x^\underline{r}.$$`
* By virtue of the [reciprocity law for factorial powers][bookofproofs$1412], we can transform this into a formula involving [rising factorial powers][bookofproofs$1399] as follows `$$\begin{align}
x^{n}&= \sum_{r=1}^n\left\{\begin{array}{c}n\\r\end{array}\right\}(-1)^r(-x)^\overline{r}\quad\Longleftrightarrow\nonumber\\
(-x)^{n}&= \sum_{r=1}^n\left\{\begin{array}{c}n\\r\end{array}\right\}(-1)^rx^\overline{r}\quad\Longleftrightarrow\nonumber\\
(-1)^nx^{n}&= \sum_{r=1}^n\left\{\begin{array}{c}n\\r\end{array}\right\}(-1)^rx^\overline{r}\quad\Longleftrightarrow\nonumber\\
x^{n}&= \sum_{r=1}^n\left\{\begin{array}{c}n\\r\end{array}\right\}(-1)^{r-n}x^\overline{r}\quad\Longleftrightarrow\nonumber\\
x^{n}&= \sum_{r=1}^n\left\{\begin{array}{c}n\\r\end{array}\right\}(-1)^{n-r}x^\overline{r}.\nonumber\\
\end{align}$$`
