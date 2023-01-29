layout: proof
categories: branches,number-theory
nodeid: bookofproofs$514
orderid: 50
parentid: bookofproofs$508
title: 
description: PROOF OF DIVISIBILITY LAWS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$1272
keywords: divisibility,laws,proof
contributors: bookofproofs

---


---

The divisibility laws follow immediately from the definition of [divisors for integers][bookofproofs$700]:

### Ad 1

* Using the definition of divisibilty, `\(\frac{n}{1}=n\in\mathbb Z\)` and `\(\frac{n}{n}=1\in\mathbb Z\)` for all `\(n\in\mathbb Z\)`.
* Therefore, `\(1\mid n\)` and `\(n\mid n\)` holds for all `\(n\in\mathbb Z\)`.
* Also, for all `$n\in\mathbb Z$`, we have `$0\cdot n=0$`, with `$0\in\mathbb Z.$` Thus, `$n\mid 0.$`

### Ad 2

* By hypothesis, `\(m\mid  n \wedge n\mid  m\)`.
* If `\(m\mid n\)`, then there exists `\(a\in\mathbb Z\)` with `\(a=\frac nm\)`. 
* Correspondingly, if at the same time `\(n\mid m\)`, then there exists `\(b\in\mathbb Z\)` with `\(b=\frac mn\)`. 
* The product of both numbers results in `\(ab=\frac nm\cdot\frac mn=1\)`. 
* Since both, `\(a\)` and `\(b\)`, are natural numbers, their product can only equal 1 if `\(a=b=1\)`. 
* This shows that `\(n=m\)`.

### Ad 3

* By hypothesis, `\(m\mid  n \wedge n\mid  l\)`.
* If `\(m\mid n\)`, then there exists `\(a\in\mathbb Z\)` with `\(a=\frac nm\)`. 
* If `\(n\mid l\)`, then there exists `\(b\in\mathbb Z\)` with `\(b=\frac ln\)`. 
* The [product][bookofproofs$891] of both integers equals `\(ab=\frac nm\cdot\frac ln=\frac lm=:c\)`. 
* Since `\(c\)` is an [integer][bookofproofs$844] (`\(a\)` and `\(b\)` are, so their product is), it follows that `\(m\mid l\)`.

### Ad 4

* By hypothesis, `\(m\mid  n\)`.
* If `\(m\mid n\)`, then there exists `\(a\in\mathbb Z\)` with `\(a=\frac nm\)`. 
* If we [multiply][bookofproofs$891] both sides of the equation by any `\(r\in\mathbb Z\)`, then we get `\(ar=\frac {nr}m\)`. 
* Since `\(ar\)` is an integer, it follows that `\(m\mid (nr)\)` for all `\(r\in\mathbb Z\)`.

### Ad 5

* By hypothesis, `\(m\mid  n \wedge m\mid l \)`.
* If `\(m\mid n\)`, then there exists `\(a\in\mathbb Z\)` with `\(a=\frac nm\)`.  
* Correspondingly, if at the same time `\(m\mid l\)`, then there exists `\(b\in\mathbb Z\)` with `\(b=\frac lm\)`. 
* If we [add][bookofproofs$890] both equations, we get `\(c:=a+b=\frac{n+l}m\)`. 
* Since `\(c\)` is an integer (`\(a\)` and `\(b\)` are, so their sum is), it follows that `\(m\mid (n+l)\)`.
* Note: This holds also for the [subtraction of integers][bookofproofs$1585] `\(m\mid (n-l)\)`, as a special case of addition.

### Ad 6

* By hypothesis, `\(m\mid  n \wedge m\mid  (n+l) \)`.
* If `\(m\mid n\)`, then there exists `\(a\in\mathbb Z\)` with `\(a=\frac nm\)`.  
* Correspondingly, if at the same time `\(m\mid (n+l)\)`, then there exists `\(b\in\mathbb Z\)` with `\(b=\frac {n+l}m\)`. 
* The [difference][bookofproofs$1585] `\(c=b-a=\frac lm\)` is an integer (since `$b$` and `$a$` are.)
* This proves that `\(m\mid l\)`.
* Note: This holds also for the [subtraction of integers][bookofproofs$1585] in the hypothesis `\(m\mid  n \wedge m\mid  (n-l) \)`, as a special case of addition.

### Ad 7

* By hypothesis, `$mr\mid nr.$`
* Since `$mr$` is a [divisor][bookofproofs$700], we have `\(mr\neq 0\)`.
* Thus `\(m\neq 0\)` and `\(r\neq 0\)` by [multiplication of integers][bookofproofs$891]. 
* Furthermore, `\(nr=qmr\)` for some integer `$q.$`
* It follows `\(n=qm\)`, since the [multiplication of integers is cancellative][bookofproofs$1464].
* Thus, `\(m\mid n\)`.

### Ad 8

* By hypothesis, `$m\mid n\wedge r\neq 0.$`
* Since `\(m\neq 0\)`, we have `\(mr\neq 0\)`. 
* Furthermore, `\(n=qm\)` for some integer `$q.$`
* It follows `\(nr=qmr\)`. 
* Therefore, `\(mr\mid nr\)`.

### Ad 9

`\("\Rightarrow"\)` 
* By hypothesis, `$m\mid  n \wedge m\mid  l.$`
* From rule 4 above, we have that `\(m\mid nx\)` and `\(m\mid ly\)` for any integers `$x,y\in\mathbb Z.$`
* From rule 5, it follows that `\(m\mid (nx+ly)\)`  for all integers `$x,y\in\mathbb Z.$`

`\("\Leftarrow"\)` 
* By hypothesis, `\(m\mid (nx+ly)\)`  for all integers `$x,y\in\mathbb Z.$`
* It follows in particular for `\(x=0,y=1\)` and `\(x=1,y=0\)` that `\(m\mid n \wedge m\mid l\)`.
