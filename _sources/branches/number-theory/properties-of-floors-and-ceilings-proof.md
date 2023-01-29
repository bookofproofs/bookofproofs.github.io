layout: proof
categories: branches,number-theory
nodeid: bookofproofs$8110
orderid: 50
parentid: bookofproofs$8109
title: 
description:  Proof of PROPERTIES OF FLOORS AND CEILINGS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$1112,bookofproofs$1272
keywords: ceilings,floors,properties,floors and ceilings,properties of floor and ceiling functions,properties of ceiling function,ceiling function properties,floor and ceiling proofs,properties of floor,floor properties,proof
contributors: bookofproofs

---


---

In the following, et `$x\in\mathbb R$` be a [real number][bookofproofs$1105].
#### Ad `$1,2,3$`

* These propositions follow immediately from the definitions of the [floor and ceiling functions][bookofproofs$280].
#### Ad `$4$`

* For every [integer][bookofproofs$844] `$n\in\mathbb Z$`, `$n\le n < n + 1.$`
* By definition, `$\lfloor x\rfloor\le x < \lfloor x\rfloor+1.$`
* Adding both inequations results in `$\lfloor x\rfloor+n\le x+n < \lfloor x \rfloor+n + 1.$`
* On the other hand, we have `$\lfloor x+n\rfloor\le x+n< \lfloor x+n\rfloor+1.$`
* This is equivalent to `$\lfloor x+n \rfloor = \lfloor x \rfloor+n.$`

#### Ad `$5$`

* For example, take `$n=2$` and `$x=\frac 12.$`
* Then `$\lfloor 2\cdot\frac 12\rfloor=1$` but `$2\cdot\lfloor \frac 12\rfloor=2\cdot 0=0.$`

#### Ad `$6$`

* Ad `$(6a)$` If `$x < n$` then since `$\lfloor x\rfloor\le x$` we have `$\lfloor x \rfloor < n.$` Conversely, if `$\lfloor x \rfloor < n$` then since `$x < \lfloor x \rfloor + 1\le n$` we have `$x < n.$`
* Ad `$(6b)$` If `$n < x$` then since `$x \le \lceil x\rceil$` we have `$n < \lceil x\rceil.$` Conversely, if `$n < \lceil x\rceil$` then because of `$(3)$` we have `$n < x.$`
* Ad `$(6c)$` If `$x \le n$` then because of `$(2)$` and `$(3)$` and `$(6a)$` we have `$\lceil x\rceil\le n,$` and vice versa.
* Ad `$(6d)$` If `$n\le x$` then because of `$(2)$` and `$(3)$` and `$(6b)$` we have  `$n\le \lfloor x \rfloor,$` and vice versa.

#### Ad `$7$`

* If `$g\le \frac xn < g+1$` then `$ng\le x < n(g+1).$`
* It follows `$ng\le \lfloor x\rfloor < n(g+1),$`
* and finally `$g\le \frac {\lfloor x\rfloor}n < g+1.$`
