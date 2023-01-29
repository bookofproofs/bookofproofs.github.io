layout: definition
categories: branches,set-theory
nodeid: bookofproofs$592
orderid: 50
parentid: bookofproofs$64
title: Partial and Total Maps (Functions)
description: PARTIAL AND TOTAL MAPS, FUNCTION, FIBER, DOMAIN AND CODOMAIN, MAPPINGS  ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$577,bookofproofs$979,bookofproofs$6823,bookofproofs$6907
keywords: function,functions,image,images,map,maps,range,ranges,mapping,mappings,partial map,partial and total functions,domain,domains,fiber,fibers,partial mapping,undefined,inverse image,inverse images
contributors: bookofproofs

---


---

Let `\(A\)` and `\(B\)` be two (not necessarily different) [sets][bookofproofs$550] and let `\(f \subseteq A \times B\)` be a binary [relation][bookofproofs$571].
* a  **total**) **function** (or a **map**), if it is [left-total][bookofproofs$1308] and [right-unique][bookofproofs$1308]. This is equivalant to saying that for every element `\(x\in A\)` there is exactly one element `\(y\in B\)` with `\((x,y)\in f\)`. To express this, we write `$f(x)=y$` for functions instead of writing `$(x,y)\in f$` as we wrote for general relations.
* a  **partial**) **function** (or a **map**), if it is [right-unique][bookofproofs$1308], but not left-total.

The following terms are strongly related to functions:
* `$A$` is called the **domain** of `$f$`.
* `$B$` is called the **codomain** of `$f$`. 
* The element `\(f(x)=y\)` for some `$x\in A$` and `$b\in B$` is called the *value of `$f$` at the point `$x$`*.
* The set `\(f[A]:=\{y\in B:f(x)=y\;\text{ for all }x\in A\}\)` is called the *range:* (or **image**) of `$f$`.
* For some `$y\in B$`, the set `$f^{-1}(y):=\{x\in A:f(x)=y\}$` is called the *fiber of `$y$` under `$f$`*.
* The set `$f^{-1}[B]:=\{x\in A:f(x)=y\text{ for all }y\in B\}$` is called the **inverse image** of `$f$`.
* If a partial function `$f$` is **undefined** for an `$a\in A$`, i.e. `$\not\exists b\in B:f(a)=b,$` then we write `$f(a)=\perp.$`
