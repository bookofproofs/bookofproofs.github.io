layout: proof
categories: branches,number-theory
nodeid: bookofproofs$3522
orderid: 50
parentid: bookofproofs$8170
title: 
description:  Proof of MULTIPLICATION OF CONGRUENCES WITH A POSITIVE FACTOR &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$1272
keywords: congruences,factor,multiplication,positive,proof
contributors: bookofproofs

---


---

By hypothesis, `$a,b$` are [integers][bookofproofs$844] and `$c > 0, m > 0$` are [positive integers][bookofproofs$1075].
### "`$\Rightarrow$`"

* Since `$c > 0,$` the [divisibility law no. 8][bookofproofs$508] implies `$m\mid (a-b)\Rightarrow mc\mid (a-b)c.$`
* By the [distributivity law of integers][bookofproofs$1466], `$m\mid (a-b)\Rightarrow mc\mid (ac-bc).$` 
* This means, by [definition of congruences][bookofproofs$8154], `$a(m)\equiv b(m)\Rightarrow (ac)(mc)\equiv(bc)(mc).$`

### "`$\Leftarrow$`"

* The [divisibility law no. 7][bookofproofs$508] implies (for all `$c\in\mathbb Z,$` not only `$c > 0$`) that `$mc\mid (a-b)c\Rightarrow m\mid (a-b).$`
* By the [distributivity law of integers][bookofproofs$1466], `$mc\mid (ac-bc)\Rightarrow m\mid (a-b).$` 
* This means, by [definition of congruences][bookofproofs$8154], `$(ac)(mc)\equiv(bc)(mc)\Rightarrow a(m)\equiv b(m).$`
