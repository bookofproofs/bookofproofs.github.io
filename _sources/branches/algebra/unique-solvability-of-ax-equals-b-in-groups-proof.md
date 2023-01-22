layout: proof
categories: branches,algebra
nodeid: bookofproofs$8656
orderid: 0
parentid: bookofproofs$8655
title: 
description: PROOF OF UNIQUE SOLVABILITY OF $A\AST X=B$ IN GROUPS ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$581
keywords: unique solvability of a*x=b in groups,proof
contributors: bookofproofs

---


---

* By hypothesis, `$(G,\ast)$` is a [group][bookofproofs$671]
* We first show that `$a^{-1}\ast b$` _is_ the solution of the equation `$a\ast x=b.$`
   * Replacing `\(x\)` by `\((a^{-1}\ast b)\)` in the equation leads to `$a\ast (a^{-1}\ast b)=b.$`
   *  Since `$[\ast"$` is "associative][bookofproofs$668], we get `$(a\ast a^{-1})\ast b=b.$`
   * Since the [inverse element][bookofproofs$670] `$a^{-1}$` is [unique][bookofproofs$359], it follows `$e\ast b=b,$` where `$e$` is a [neutral element][bookofproofs$661] in `$G$` (even "the" neutral element in `$G,$` since it is also [unique][bookofproofs$669] in `$G.$`)
   * It follows `$b=b$` which shows that `$a^{-1}\ast b$` is a solution.
* Now, we show, the solution `$a^{-1}\ast b$` is _unique_. 
   * Assume, `$c\in G$` is a solution of the equation `$a\ast x=b,$` i.e. `$a\ast c=b.$`  
   * Then `$a^{-1}\ast (a\ast c)=a^{-1}\ast b.$`
   * Since  `$[\ast"$` is "associative][bookofproofs$668], we get `$(a\ast a^{-1})\ast c=a^{-1}\ast b.$` 
   * Thus, `$e\ast c=a^{-1}\ast b.$`
   * Thus, `$c=a^{-1}\ast b.$`
