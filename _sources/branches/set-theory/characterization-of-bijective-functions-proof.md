layout: proof
categories: branches,set-theory
nodeid: bookofproofs$8546
orderid: 50
parentid: bookofproofs$8545
title: 
description: PROOF OF CHARACTERISATION OF BIJECTIVE FUNCTIONS ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$8311
keywords: characterization of bijective functions,proof
contributors: bookofproofs

---


---

### "`$\Rightarrow$`"

* Assume, the [function][bookofproofs$592] `$f:A\to B$` be [bijective][bookofproofs$771].
* By definition, `$f$` is [surjective][bookofproofs$770] and [injective][bookofproofs$769].
* Since `$f$` is [surjective][bookofproofs$770], for every `$b\in B$` there is exactly one `$a\in A$` with `$b=f(a).$`
* Set `$g:B\to A$` be the function defined by `$g(b)=a$`
* Obviously, the required [compositions][bookofproofs$1314] are `$g(f(a))=g(b)=a$` and `$f(g(b))=f(a)=b.$`

### "`$\Leftarrow$`"

* Let `$g:B\to A$` be a function with the required compositions `$g(f(a))=g(b)=a$` and `$f(g(b))=f(a)=b$` for all `$a\in A$` and `$b\in B.$`
* By definition, `$f\circ g=id_A$` is the [identity function][bookofproofs$371] on `$A.$` Thus, `$f$` is surjective.
* For any `$a_1,a_2\in A$` with `$f(a_1)=f(a_2)$` we have `$a_1=g(f(a_1))=g(f(a_2))=a_2$`. Thus, `$f$` is injective.
* Since `$f$` is injective and surjective, it follows that `$f$` is objective.

### Uniqueness of `$g$` 

* If `$g$` and `$h$` are two functions with the required properties, then because the [composition of functions is associative][bookofproofs$8005], `$$g=g\circ id_B=g\circ (f\circ h)=(g\circ f)\circ h=id_A\circ h=h.$$`
