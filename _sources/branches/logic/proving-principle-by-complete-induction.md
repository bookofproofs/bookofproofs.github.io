layout: lemma
categories: branches,logic
nodeid: bookofproofs$657
orderid: 800
parentid: bookofproofs$7917
title: The Proving Principle by Complete Induction
description: PROVING PRINCIPLE BY COMPLETE INDUCTION ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: 
keywords: proving principle by induction,complete induction,proof by induction,inductive proof,proving principle by complete induction
contributors: bookofproofs

---


---

The **proving principle by complete induction** is a [valid logical argument][bookofproofs$7915] in [first order predicate][bookofproofs$186] logic[^1]. It consists of:

* the **base case premise**: `$p(m)$` for some [natural number][bookofproofs$664] `$m\in\mathbb N.$`
* the **induction step premise**:  prove that `$p(n+1)$` is true assuming that `$p(m)$` is true for all `$m \le n,$`
* the **conclusion**: `$p(n)$` is true for all `$n\in\mathbb N$` [greater than or equal][bookofproofs$697] the base case `$n\ge m.$` 

### Example

We can write the logical argument also as follows:

 `$$\begin{array}{rll}
p(m)&\text{base case premise}&\text{e.g. } 1 = 1^2.\quad (m=1)\\
p(n)\Rightarrow p(n+1)&\text{induction step premise}&\text{e.g. if } 1 + 3 + \ldots + (2n-1)= n^2\text{ for some }n\ge 1\\&&\text {then }1 + 3 + \ldots + 2((n+1)-1)=(n+1)^2.\\
\hline
\forall n\ge m: p(n)&\text{conclusion}&1 + 3 + \ldots + (2n-1)= n^2\text{ for all }n\ge 1.\\ 
\end{array} $$`

This logical argument is called "complete" since it includes __all__ (infinitely many) premises for the values `$n=m, n+1, n+2\ldots, $` and it is called "induction" since it derives the conclusion from the __special cases__ `$n=m, n+1, n+2\ldots, $` to the __general case__ `$n\ge m.$`


[^1]: This is because it requires the [quantifier][bookofproofs$186] "for all: `$\forall$`."
