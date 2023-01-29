layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1548
orderid: 50
parentid: bookofproofs$1547
title: 
description:  Proof of COMPARING NATURAL NUMBERS USING THE CONCEPT OF ADDITION &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$1538
keywords: addition,comparing,concept,natural,numbers,using,proof
contributors: bookofproofs

---


---

It is not possible that both cases 

* `\(x=y\)` and 
* there exists a natural number `\(u\neq 0\)` with `\(x=y+u\)`,

are simultaneously true, because it would [contradict][bookofproofs$744] the [cancellation law for adding natural numbers][bookofproofs$1432], according to which `\(x=y\)` implies `\(x+u=y+u\)` for all natural numbers `\(u\)`.

For the same reason, both cases

* `\(x=y\)` and 
* there exists a natural number `\(v\neq 0\)` with `\(y=x+v\)`.

cannot be simultaneously true, because the equality `\(x=y\)` is [symmetric][bookofproofs$1539] and implies `\(y=x\)`.

The cases

* there exists a natural number `\(u\neq 0\)` with `\(x=y+u\)`,
* there exists a natural number `\(v\neq 0\)` with `\(y=x+v\)`. 

can also not be simultaneously true. Otherwise, it would follow from the [associativity of adding natural numbers][bookofproofs$1428] that 

`\[\begin{array}{rcll}
x&=&y+u&\text{assumption case 1}\\
&=&(x+v)+u&\text{assumption case 2}\\
&=&x+(v+u),&\text{associativity of adding natural numbers}
\end{array}\]`

which is a  [contradiction][bookofproofs$744].
