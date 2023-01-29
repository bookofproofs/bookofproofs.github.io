layout: proof
categories: branches,analysis
nodeid: bookofproofs$2934
orderid: 50
parentid: bookofproofs$6807
title: 
description: PROOF OF FUNDAMENTAL THEOREM OF CALCULUS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$581
keywords: fundamental theorem of calculus,fundamental,proof
contributors: bookofproofs

---


---

* By hypothesis, `$[a,b]$` is a [real interval][bookofproofs$1153] `$f:[a,b]\to\mathbb R$` is a [continuous function][bookofproofs$1260].
* Let `$x\in [a,b].$`
* Assume, `$F_0:[a,b]\to\mathbb R$` is an [antiderivative][bookofproofs$1768] of `$f$`, i.e. by definition `$$F_0(x)=\int_a^xf(t)dt.$$`
* It follows from the definition of the [Riemann integral][bookofproofs$1763] that `$$F_0(a)=0,\quad F_0(b)=\int_a^bf(t)dt.$$`
* For an arbitrary antiderivative `$F$` of `$f$` it follows from the fact that [antiderivatives are unique up to a constant][bookofproofs$6806] that `$$F(b)-F(a)=F_0(b)-F_0(a)=F_0(b)=\int_a^bf(t)dt.$$`
