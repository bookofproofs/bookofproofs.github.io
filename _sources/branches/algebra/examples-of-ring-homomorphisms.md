layout: example
categories: branches,algebra
nodeid: bookofproofs$8654
orderid: 5
parentid: bookofproofs$192
title: Examples of Ring Homomorphisms
description: EXAMPLES OF RING HOMOMORPHISMS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$8311
keywords: examples of ring homomorphisms
contributors: bookofproofs

---


---

### Example 1

We look for all [endomorphisms][bookofproofs$6235] (i.e. self-homomorphisms) of the ring `$(\mathbb Z,+,\cdot)$` of all integers with addition and multiplication. Let `$f:\mathbb Z\to\mathbb Z$` be a [ring homomorphism][bookofproofs$885] This means that it has to fulfill the properties `$$\begin{array}{rcl}
f(x + y)&=&f(x) + f(y),\\
f(x \cdot y)&=&f(x)\cdot f(y)\\
f(1)&=&1.
\end{array}$$`
Then for the special case `$n\ge 1$` we get `$$f(n)=f(\underbrace{1+\ldots+1}_{n\text{ times}})=\underbrace{f(1)+\ldots+f(1)}_{n\text{ times}}=\underbrace{1+\ldots+1}_{n\text{ times}}=n.$$` This implies `$$f(0)=f(0\cdot 1)=f(0)\cdot f(1)=0\cdot 1=0.$$` Thus `$f(n)+f(-n)=0$`, or `$$f(-n)=-f(n)=-n.$$`
It follows that `$f:\mathbb Z\to\mathbb Z$` be a [ring homomorphism][bookofproofs$885] if and only if `$f$` is the [identity function][bookofproofs$371] `$f(n)=n$` for all `$n\in\mathbb Z.$`

### Example 2

The [complex conjugation][bookofproofs$1245] `$f:\mathbb C\to\mathbb C$` is a ring homomorphism, since `$$\begin{array}{rcl}
(z_1+z_2)^*&=&z_1^*+z_2^*\\
(z_1\cdot z_2)^*&=&z_1^*\cdot z_2^*\\
(1)^*&=&1^*
\end{array}$$`

### Example 3

For any integer `$m\ge 2,$` the function `$f:\mathbb Z\to \mathbb Z_m$` sith `$f(a)=a(m)$` of the [commutative ring of integers][bookofproofs$892] `$(\mathbb Z,+,\cdot)$` to the commutative ring of congruences `$\mathbb Z_m$` is a ring homomorphism which is partially [shown here][bookofproofs$8156] It remains to note that `$$1\equiv 1(m)$$` for all `$m\ge 2.$`
