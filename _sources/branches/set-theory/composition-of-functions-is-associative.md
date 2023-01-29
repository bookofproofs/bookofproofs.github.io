layout: proposition
categories: branches,set-theory
nodeid: bookofproofs$8005
orderid: 100
parentid: bookofproofs$1314
title: Composition of Functions is Associative
description: COMPOSITION OF FUNCTIONS IS ASSOCIATIVE &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$979,bookofproofs$1038
keywords: associative,composition,functions,composition of functions is associative,is composition of functions associative,composition of function is associative,is function composition associative,function composition associative,function composition is associative,associative function,composition of functions associative,associativity of composition of fu
contributors: bookofproofs

---


---

The [composition of functions][bookofproofs$1314] fulfills the [associativity][bookofproofs$668] property, i.e. if `$f:A\mapsto B,$` `$g:B\mapsto C,$` and `$h:C\mapsto D$` are [functions][bookofproofs$592] then `$(h\circ g)\circ f=h\circ (g\circ f).$`



new:branchproof:
* Let `$f:A\mapsto B,$` `$g:B\mapsto C,$` and `$h:C\mapsto D$` be [functions][bookofproofs$592].
* The [lemma defining compositions][bookofproofs$1314] shows that both compositions `$(h\circ g)\circ f$` and `$h\circ (g\circ f)$` are functions.
* Moreover, these functions are identical, since for every `$a\in A$` we have `$$(h\circ g)\circ f(a)=h(g\circ f(a))=h(g(f(a)))=h\circ g(f(a))=h\circ(g\circ f)(a).$$`
