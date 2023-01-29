layout: proof
categories: branches,combinatorics
nodeid: bookofproofs$8427
orderid: 50
parentid: bookofproofs$8426
title: 
description: PROOF OF RECURSIVE FORMULA FOR THE STIRLING NUMBER OF THE FIRST KIND ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$8404
keywords: recursive formula for the stirling numbers of the first kind,proof
contributors: bookofproofs

---


---

* Let `$n\ge 1$` be a [natural number][bookofproofs$718].
* By the [Stirling numbers of the first kind and rising factorial powers][bookofproofs$8432] `$$\begin{align}x^\overline{n}&=\sum_{r=1}^n\left[\begin{array}{c}n\\r\end{array}\right] x^r\tag{1},\\x^\overline{n+1}&=\sum_{r=1}^{n+1}\left[\begin{array}{c}n+1\\r\end{array}\right] x^r\tag{2}.\end{align}$$` 
* Moreover, by definition of [rising factorial powers][bookofproofs$1399] `$$\begin{align}x^\overline{q}(x+q)^\overline{p}&=x(x+1)(x+2)\cdots(x+q-1)\cdot\nonumber\\&\quad\cdot (x+q)(x+q+1)\cdots(x+q+(p-q)-1)\nonumber\\&=x(x+1)(x+2)\cdots(x+p-1)\nonumber\\&=x^\overline{p}\tag{3}\end{align}$$` for any [integers][bookofproofs$844] `$p,q\in\mathbb Z.$` 
* For `$p=n+1$` and `$q=n,$` we get `$$\begin{align}x^\overline{n+1}&=x^\overline{n}(x+n)^\overline{1}=xx^\overline{n}+nx^\overline{n}\tag{4}.\end{align}$$`
* Result `$(4)$` allows us to write `$(2)$` in terms of `$(1)$` as `$$\begin{align}\underbrace{\sum_{r=1}^{n+1}\left[\begin{array}{c}n+1\\r\end{array}\right] x^r}_{=:A}&=\underbrace{x\sum_{r=1}^n\left[\begin{array}{c}n\\r\end{array}\right] x^r}_{=:B}+\underbrace{n\sum_{r=1}^n\left[\begin{array}{c}n\\r\end{array}\right] x^r}_{=:C}.\tag{5}\end{align}$$` 
* Now, `$$\begin{align}B&=\sum_{r=1}^n\left[\begin{array}{c}n\\r\end{array}\right] x^{r+1}=\sum_{k=2}^{n+1}\left[\begin{array}{c}n\\k-1\end{array}\right] x^{k}=\sum_{k=2}^n\left[\begin{array}{c}n\\k-1\end{array}\right] x^{k} + \left[\begin{array}{c}n\\n\end{array}\right] x^{n+1},\tag{6}\\A&=\left[\begin{array}{c}n+1\\1\end{array}\right]x+\sum_{k=2}^n\left[\begin{array}{c}n+1\\k\end{array}\right] x^{k}+\left[\begin{array}{c}n+1\\n+1\end{array}\right] x^{n+1}\tag{7},\\C&=n\left[\begin{array}{c}n\\1\end{array}\right]x+\sum_{k=2}^nn\left[\begin{array}{c}n\\k\end{array}\right] x^{k}.\tag{8}\end{align}$$`
* From `$(5)$` it follows `$0=A-C-B,$` and thus `$$\begin{align}0&=\left(\left[\begin{array}{c}n+1\\1\end{array}\right]-n\left[\begin{array}{c}n\\1\end{array}\right]\right)x\nonumber\\&\quad+\sum_{k=2}^n\left(\left[\begin{array}{c}n+1\\k\end{array}\right]-n\left[\begin{array}{c}n\\k\end{array}\right]-\left[\begin{array}{c}n\\k-1\end{array}\right]\right)x^k\nonumber\\&\quad+\left(\left[\begin{array}{c}n+1\\k+1\end{array}\right]-\left[\begin{array}{c}n\\n\end{array}\right]\right)x^{n+1}.\tag{9}\end{align}$$`
* Sufficient for `$(9)$` are the conditions `$$\begin{align}0&=\left[\begin{array}{c}n+1\\1\end{array}\right]-n\left[\begin{array}{c}n\\1\end{array}\right],\tag{10}\\0&=\left[\begin{array}{c}n+1\\k\end{array}\right]-n\left[\begin{array}{c}n\\k\end{array}\right]-\left[\begin{array}{c}n\\k-1\end{array}\right],\quad k=2,3,\ldots,n\tag{11}\\0&=\left[\begin{array}{c}n+1\\k+1\end{array}\right]-\left[\begin{array}{c}n\\n\end{array}\right]\tag{12}.\end{align}$$`
* Given the conventions `$\left[\begin{array}{c}n\\0\end{array}\right]:=0$`  and `$\left[\begin{array}{c}n\\k\end{array}\right]:=0$` for `$k > n,$` we can re-write those as `$$\begin{align}\left[\begin{array}{c}n+1\\1\end{array}\right]&=\left[\begin{array}{c}n\\0\end{array}\right]+n\left[\begin{array}{c}n\\1\end{array}\right],\tag{13}\\
\left[\begin{array}{c}n+1\\k\end{array}\right]&=\left[\begin{array}{c}n\\k-1\end{array}\right]+n\left[\begin{array}{c}n\\k\end{array}\right],\quad k=2,3,\ldots,n\tag{14}\\\left[\begin{array}{c}n+1\\k+1\end{array}\right]&=\left[\begin{array}{c}n\\n\end{array}\right]+n\cdot\left[\begin{array}{c}n\\n+1\end{array}\right].\tag{15}
\end{align}$$`
* `$(13),$` `$(14)$` and `$(15)$` can be written as a single recurrence relation `$$\begin{align}
\left[\begin{array}{c}n+1\\r\end{array}\right]&=\left[\begin{array}{c}n\\r-1\end{array}\right]+n\cdot \left[\begin{array}{c}n\\r\end{array}\right],\nonumber\\
\left[\begin{array}{c}n\\n\end{array}\right]&:=1,\quad \text{ for }n\ge 1\nonumber\\
\left[\begin{array}{c}n\\r\end{array}\right]&:=0,\quad \text{ for }r=0 < n\text{ or }r > n.\tag{16}
\end{align}$$`
