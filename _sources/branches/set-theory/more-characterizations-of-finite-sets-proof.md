layout: proof
categories: branches,set-theory
nodeid: bookofproofs$8054
orderid: 50
parentid: bookofproofs$8053
title: 
description: Proof of MORE CHARACTERIZATIONS OF FINITE SETS ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$577
keywords: characterization of finite sets,properties of finite sets,proof
contributors: bookofproofs

---


---

By hypothesis, `$X,Y$` are [finite sets][bookofproofs$985] equal [cardinalities][bookofproofs$980] `$|X|=|Y|  < \infty.$`

### Ad `$(1)$`

* Let `$f:X\to Y$` be [surjective][bookofproofs$770].
* Assume `$f$` wasn't injective. Then there would exist some `$v_1,v_2\in X$` with `$x_1\neq x_1$` but `$f(x_1)=f(x_2).$`
* Since, in this case, at least `$2$` elements `$x_1,x_2$` of `$X$` were mapped to a single element `$f(x_1)=f(x_2)$` and because `$X,Y$` are finite, this would mean that there is an `$y\in Y$` such that no `$x\in X$` are left with `$f(x)=y$`. But this would [contradict][bookofproofs$744] the surjectivity of `$f$`.
* Therefore, `$f$` is [injective][bookofproofs$769].
###  `$(2)$`

* Let `$f:X\to Y$` be [injective][bookofproofs$769].
* This means that `$f(x_1)\neq f(x_2)$` if `$x_1\neq x_2.$`
* It follows that `$f$` maps different elements of `$X$` on different elements of `$Y.$`
* Since `$X$` has the same number of elements as `$Y$`, every element of `$x\in X$` will be mapped to a distinct value `$y\in Y.$`
* It follows that `$f$` is [surjective][bookofproofs$770].
Now, `$X,Y$` are [finite sets][bookofproofs$985] with unequal [cardinalities][bookofproofs$980].

###  `$(3)$` By Induction

* By hypothesis, the cardinalities `$|Y|=n$` and `$|X|=m$` and `$n < m.$`
* For the sake of transparency in the notation, we write `$Y_n$` for `$Y$` with `$|Y|=n$` and `$X_m$` for `$X$` with `$|X|=m.$`
* We will prove this lemma [by induction][bookofproofs$657] of `$m.$`
* Base case: `$m=1$`. 
   * Assume for the sake of [contradiction][bookofproofs$744] that there is an [injective function][bookofproofs$769] `$f:X_1\to Y_n$` and `$n > 1.$` 
   * This assumption means that there are some `$a,b\in X_1$` with `$a\neq b$` and `$f(a)=f(b).$`
   * But this is impossible, since `$X_1$` has only one element. 
   * Therefore, there is no injective function, and the lemma is true.
* Induction step: `$m\to m+1$`
   * Assume, there is no injective function `$f:X_m\to Y_n$` for some `$m < n.$`
   * By [contraposition][bookofproofs$1330], this is equivalent to saying that if `$n > m$` for some `$m\in\mathbb N$` then there _is_ an injective function `$f:X_m\to Y_n.$`
   * Holding `$n$` fixed and using this injective function `$f$`, we will now construct another injective function `$f':X_{m+1}\to Y_n.$` as follows:
      * Without loss of generality, let `$X_m=\{x_1,\ldots,x_m\}$` and `$X_{m+1}:=X_m\cup \{x_{m+1}\}.$`
      * Since `$n > m,$` and `$f$` is injective, there is an element `$y\in Y_n$` with `$y\neq f(x_k)$` for all `$k=1,\ldots,m.$` 
      * Define the function `$f':X_{m+1}\to Y_n$` by 
 `$$f'(x_k):=\begin{cases}f(x_k)\in Y_n&\text{if }k\le m\\y&\text{if }k=m+1.\end{cases}$$`
      * By construction `$f'$` is injective.

###  `$(4)$`

* Another proof:
   * From `$(3)$` it follows that if `$f:X\to Y$` is injective than `$|X|\le |Y|$`.
   * Vice versa, if `$g:Y\to X$` is injective than `$|Y| \le |X|$`
   * By the [Schroeder-Bernstein Theorem][bookofproofs$8051], it follows `$|X|=|Y|.$`
   * By the definition of [equipotent][bookofproofs$978] sets, this is the case if an only if `$f$` and `$g$` are bijective.
