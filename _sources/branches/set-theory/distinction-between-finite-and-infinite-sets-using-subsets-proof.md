layout: proof
categories: branches,set-theory
nodeid: bookofproofs$3475
orderid: 50
parentid: bookofproofs$8304
title: 
description: Proof of DISTINCTION BETWEEN FINITE AND INFINITE SETS USING SUBSETS ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$8297
keywords: distinction between finite and infinite,proof
contributors: bookofproofs


---


---

* By hypothesis, `$X$` is a [non-empty set][bookofproofs$550] with a [proper subset][bookofproofs$552] `$S\subset X.$`

### Finite case "`$\Rightarrow$`"

* Let `$X$` be [finite][bookofproofs$985].
* By [subsets of finite sets][bookofproofs$986], `$S$` is finite with `$|S| \le |X|.$`
* Since `$S$` is a proper subset, we have even `$|S| \neq |X|.$` 
* Therefore, `$|S| < |X|.$` 
* By [characterization of finite sets][bookofproofs$8053] (no. `$3$`), there is no [injective function][bookofproofs$769]n `$f:X\to S.$`

### Infinite case "`$\Rightarrow$`"

* Assume, `$X$` is [infinite][bookofproofs$985].
* Choose `$x_1\in X,$` `$x_2\in X\setminus\{x_1\},$` `$x_3\in X\setminus\{x_1,x_2\},$` etc.  
* Since `$X$` is infinite, we can continue this process for all indices `$i\in\mathbb N$` be [mapping][bookofproofs$592] `$f:\mathbb N\to X,$` `$f(i):=x_i.$`
* By construction, this is an [injective function][bookofproofs$769] `$f:\mathbb N\to X.$`
* Now, define the function `$g:X\to S$` ($S$ being a proper subset of `$X$`) as follows:
`$$g(x):=\begin{cases}x&\text{if }x\in X\setminus \{x_i\mid i\in\mathbb N\}\\x_{i+1}&\text{if }x=x_i\end{cases}$$`
* By construction, the function `$g$` is injective as well.

### Infinite case "`$\Leftarrow$`"

* By [contraposition][bookofproofs$1330] to finite case `$"\Rightarrow",$` if there _is_ an injective function `$f:X\to S,$` then `$X$` is not finite, therefore `$X$` is infinite.

### Finite case "`$\Leftarrow$`"

* By [contraposition][bookofproofs$1330] to the infinite case `$"\Rightarrow",$` if there _is no_ injective function `$g:X\to S,$` then `$X$` is not infinite, therefore `$X$` is finite.
