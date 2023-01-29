layout: proof
categories: branches,set-theory
nodeid: bookofproofs$8086
orderid: 50
parentid: bookofproofs$8085
title: 
description: PROOF OF MOSTOWSKI'S THEOREM &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$8055
keywords: mostowskis,theorem,proof
contributors: bookofproofs

---


---

* Let `$U$` be a [universal set][bookofproofs$7984] and `$(V,\prec)$` with a [well-founded][bookofproofs$8058] relation "`$\prec$`" and with the corresponding [Mostowski function][bookofproofs$8079] `$\pi:V\to U$` with `$\pi(x):=\{\pi(y)\mid y\in V\wedge y\prec x\},$` and `$\pi[V]\subseteq U$` is the [Mostowski collapse][bookofproofs$8079].
* Assume that `$x\in y$` and `$y\in \pi[V].$` 
   * Since `$y\in \pi[V]$`, there is an `$u\in V$` with `$y=\pi(u).$`
   * By definition of the Mostowski function, `$y=\pi(u)=\{\pi(v)\mid v\in V\wedge v\prec u\}$` for an `$u\in V.$`
   * By assumption, `$x\in y.$` Therefore `$x=\pi(v)$` for some `$v\in V$` with `$v\prec u.$`
   * By definition of the Mostowski function, from `$v\prec u$` it follows that `$\pi(v)\in \pi[V].$`
   * Therefore, `$x\in \pi[V]$`. 
   * Altogether, we have shown that if `$x\in y$` and `$y\in \pi[V]$` then `$x\in\pi[V]$` which means that the Mostowski collapse `$\pi[V]$` is a [transitive set][bookofproofs$720].
* Now, assume that "`$\prec$`" is well-founded and, in addition, [extensional][bookofproofs$8059]. We want to show that `$\pi$` is an [order embedding][bookofproofs$8083], i.e. fulfills the property `$v_1\prec v_2\Longleftrightarrow \pi(v_1)\in\pi(v_2)$` for `$v_1,v_2\in V.$` It suffices to show that `$\pi$` is [injective][bookofproofs$769]. We will assume that `$\pi$` is not injective and conclude a [contradiction][bookofproofs$744].
   * If `$\pi$` is not injective, then the values `$\pi(v_1)=\pi(v_2)$` are equal for some two different elements `$v_1,v_2\in V$` with `$v_1\neq v_2.$` 
   * Since "`$\prec$`" is [well-founded][bookofproofs$8058], every non-empty subset `$S\subseteq V$` contains a [minimal][bookofproofs$7995] element. 
   * In particular, the subset `$S:=\{v_1,v_2\}$` contains a minimal element. 
   * Without loss of generalization, assume `$v_1$` is minimal, which means that there is no `$x\in S$` with `$x\prec v_1.$`
   * Since `$v_2\neq v_1$` and `$v_1$` is minimal in `$S$`, we must have `$v_1\prec v_2.$` 
   * Since "`$\prec$`" is [extensional][bookofproofs$8059], and since `$v_1\neq v_2,$` we have  `$V_1\neq V_2$` with `$V_1:=\{z\in V\mid z\prec v_1\}$` and `$V_2:=\{z\in V\mid z\prec v_2\}.$`
   * In particular, since `$v_1\prec v_2$` we must have `$V_1\subset V_2,$` `$u\not\in V_1,$` `$u\in V_2.$` 
   * Thus, `$v_1\preceq u\prec v_2.$` 
   * If `$u\prec v_2,$` then `$\pi(u)\in\{\pi(z)\mid z\prec v_2\},$` which by definition of the [Mostowski function][bookofproofs$8079] means `$\pi(u)\in\pi(v_2).$`
   * By assumption, `$\pi(v_2)=\pi(v_1),$` thus `$\pi(u)\in \pi(v_1).$`
   * If `$v_1=u$`, then `$\pi(u)\in \pi(u)$`, in contradiction to the [axiom of foundation][bookofproofs$717].
   * But then `$v_1\prec u$` and we have both, `$\pi(u)\in \pi(v_1)$` and `$\pi(v_1)\in \pi(u)$`, which is again a contradiction.
   * Altogether, we have shown that `$\pi$` is injective.
   * By definition, `$\pi$` is an [order embedding][bookofproofs$8083]. 

The following calculation is not needed for the proof, but we want to verify that, indeed, the property `$v_1\prec v_2\Longleftrightarrow \pi(x)\in\pi(y)$` is fulfilled in the case "`$\prec$`" is well-founded and, in addition, [extensional][bookofproofs$8059]:

### "`$\Rightarrow$`"

* If `$v_1\prec v_2,$` then `$\pi(v_1)\in\{\pi(z)\mid z\prec v_2\}.$` 
* This means `$\pi(v_1)\in\pi(v_2)$` by the definition of the [Mostowski function][bookofproofs$8079]. 

### "`$\Leftarrow$`"

* If `$\pi(v_1)\in\pi(v_2),$` then by the definition of the [Mostowski function][bookofproofs$8079] `$\pi(v_1)\in\{\pi(z)\mid z\prec v_2\}.$`
* This means `$\pi(v_1)=\pi(z)$` for some `$z\in V$` with `$z\prec u_2.$` 
* Since `$\pi$` is [injective][bookofproofs$769], this means  `$v_1=z$` for some `$z\in V$` with `$z\prec u_2.$` 
* This means `$v_1\prec u_2.$`
