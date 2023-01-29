layout: proof
categories: branches,combinatorics
nodeid: bookofproofs$8429
orderid: 50
parentid: bookofproofs$8428
title: 
description: PROOF OF RECURSIVE FORMULA FOR THE STIRLING NUMBERS OF THE SECOND KIND &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$8404
keywords: recursive formula for the stirling numbers of the second kind,proof
contributors: bookofproofs

---


---

* Let `$n\ge 1$` be a [natural number][bookofproofs$718].
* By definition of the [Stirling numbers of the second kind][bookofproofs$8425] `$$\begin{align}x^{n}&=\sum_{r=1}^n\left\{\begin{array}{c}n\\r\end{array}\right\} x^\underline{r}\tag{1},\\x^{n+1}&=\sum_{r=1}^{n+1}\left\{\begin{array}{c}n+1\\r\end{array}\right\} x^\underline{r}\tag{2}.\end{align}$$` 
* From the [exponentiation law][bookofproofs$676] `$ x^nx=x^{n+1}$` we can conclude 
`$$\begin{align}\sum_{r=1}^{n+1}\left\{\begin{array}{c}n+1\\r\end{array}\right\} x^\underline{r}&=x\sum_{r=1}^n\left\{\begin{array}{c}n\\r\end{array}\right\} x^\underline{r}\tag{3}.\end{align}$$` 
* Moreover, by definition of [falling factorial powers][bookofproofs$1399] `$$\begin{align}x^\underline{q}(x-q)^\underline{p}&=x(x-1)(x-2)\cdots(x-q+1)\cdot\nonumber\\&\quad\cdot (x-q)(x-q-1)\cdots(x-q-(p-q)+1)\nonumber\\&=x(x-1)(x-2)\cdots(x-p+1)\nonumber\\&=x^\underline{p}\tag{4}\end{align}$$` for any [integers][bookofproofs$844] `$p,q\in\mathbb Z.$` 
* For `$p=r+1$` and `$q=r,$` we get `$$\begin{align}x^\underline{r+1}&=x^\underline{r}(x-r)^\underline{1}=xx^\underline{r}-rx^\underline{r}\tag{5}.\end{align}$$`
* Result `$(5)$` allows us to write `$(3)$` as `$$\begin{align}\underbrace{\sum_{r=1}^{n+1}\left\{\begin{array}{c}n+1\\r\end{array}\right\} x^r}_{=:A}&=\underbrace{\sum_{r=1}^n\left\{\begin{array}{c}n\\r\end{array}\right\} x^{r+1}}_{=:B}+\underbrace{r\sum_{r=1}^n\left\{\begin{array}{c}n\\r\end{array}\right\} x^r}_{=:C}.\tag{6}
\end{align}$$` 
* Now, `$$\begin{align}B&=\sum_{r=1}^n\left\{\begin{array}{c}n\\r\end{array}\right\} x^{r+1}=\sum_{k=2}^{n+1}\left\{\begin{array}{c}n\\k-1\end{array}\right\} x^{k}=\sum_{k=2}^n\left\{\begin{array}{c}n\\k-1\end{array}\right\} x^{k} + \left\{\begin{array}{c}n\\n\end{array}\right\} x^{n+1},\tag{7}\\A&=\left\{\begin{array}{c}n+1\\1\end{array}\right\}x+\sum_{k=2}^n\left\{\begin{array}{c}n+1\\k\end{array}\right\} x^{k}+\left\{\begin{array}{c}n+1\\n+1\end{array}\right\} x^{n+1}\tag{8},\\C&=\left\{\begin{array}{c}n\\1\end{array}\right\}x+\sum_{k=2}^nr\left\{\begin{array}{c}n\\k\end{array}\right\} x^{k}.\tag{9}\end{align}$$`
* From `$(6)$` it follows `$0=A-C-B,$` and thus `$$\begin{align}0&=\left(\left\{\begin{array}{c}n+1\\1\end{array}\right\}-\left\{\begin{array}{c}n\\1\end{array}\right\}\right)x\nonumber\\&\quad+\sum_{k=2}^n\left(\left\{\begin{array}{c}n+1\\k\end{array}\right\}-k\left\{\begin{array}{c}n\\k\end{array}\right\}-\left\{\begin{array}{c}n\\k-1\end{array}\right\}\right)x^k\nonumber\\&\quad+\left(\left\{\begin{array}{c}n+1\\k+1\end{array}\right\}-\left\{\begin{array}{c}n\\n\end{array}\right\}\right)x^{n+1}.\tag{10}\end{align}$$`
* Sufficient for `$(10)$` are the conditions `$$\begin{align}0&=\left\{\begin{array}{c}n+1\\1\end{array}\right\}-\left\{\begin{array}{c}n\\1\end{array}\right\},\tag{11}\\0&=\left\{\begin{array}{c}n+1\\k\end{array}\right\}-k\left\{\begin{array}{c}n\\k\end{array}\right\}-\left\{\begin{array}{c}n\\k-1\end{array}\right\},\quad k=2,3,\ldots,n\tag{12}\\0&=\left\{\begin{array}{c}n+1\\k+1\end{array}\right\}-\left\{\begin{array}{c}n\\n\end{array}\right\}\tag{13}.\end{align}$$`
* Given the conventions `$\left\{\begin{array}{c}n\\0\end{array}\right\}:=0$`  and `$\left\{\begin{array}{c}n\\k\end{array}\right\}:=0$` for `$k > n,$` we can re-write those as `$$\begin{align}\left\{\begin{array}{c}n+1\\1\end{array}\right\}&=\left\{\begin{array}{c}n\\0\end{array}\right\}+1\left\{\begin{array}{c}n\\1\end{array}\right\},\tag{14}\\
\left\{\begin{array}{c}n+1\\k\end{array}\right\}&=\left\{\begin{array}{c}n\\k-1\end{array}\right\}+k\left\{\begin{array}{c}n\\k\end{array}\right\},\quad k=2,3,\ldots,n\tag{15}\\\left\{\begin{array}{c}n+1\\k+1\end{array}\right\}&=\left\{\begin{array}{c}n\\n\end{array}\right\}+(n+1)\cdot\left\{\begin{array}{c}n\\n+1\end{array}\right\}.\tag{16}
\end{align}$$`
* `$(14),$` `$(15)$` and `$(16)$` can be written as a single recurrence relation `$$\begin{align}
\left\{\begin{array}{c}n+1\\r\end{array}\right\}&=\left\{\begin{array}{c}n\\r-1\end{array}\right\}+r\cdot \left\{\begin{array}{c}n\\r\end{array}\right\},\nonumber\\
\left\{\begin{array}{c}n\\n\end{array}\right\}&:=1,\quad \text{ for }n\ge 1\nonumber\\
\left\{\begin{array}{c}n\\r\end{array}\right\}&:=0,\quad \text{ for }r=0 < n\text{ or }r > n.\tag{17}
\end{align}$$`
