layout: definition
categories: branches,analysis
nodeid: bookofproofs$1754
orderid: 200
parentid: bookofproofs$117
title: Supremum, Least Upper Bound
description: SUPREMUM, LEAST UPPER BOUND ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$586
keywords: supremum,least upper bound
contributors: bookofproofs

---
> applicability: `$\mathbb {R}$`

---

Let `\(D\)` be a [non-empty subset][bookofproofs$552] of [real numbers][bookofproofs$1105]. The real number `\(\sup(D)\)` is called the [supremum][bookofproofs$7995] (or the [least upper bound][bookofproofs$7995]) of `\(D\)`, if  

1. `\(\sup(D)\)` is an [upper bound][bookofproofs$584] of `\(D\)` and 
1. it is [less than or equal to][bookofproofs$1107] every upper bound of `\(D\)`, i.e. if `$B$` is any upper bound of `$D$` then `$\sup(D)\le B$`.

Equivalently, for every `\(\epsilon > 0\)` there exists an `\(y\in D\)` with `\(y  > \sup(D) - \epsilon\)`.

### Notes

* Not all sets have the property that their non-empty subsets have a supremum. In fact, this definition is valid only for [complete ordered fields][bookofproofs$6193], since in them, the existence of a supremum is ensured.
* For instance, the set of all rational numbers `$0 \le x \le \sqrt{2}$` does not have a supremum since we cannot identify the least _rational_ upper bound that is still `$\le \sqrt{2},$` however, the set of all real numbers `$0 \le x \le \sqrt{2}$` has the supremum `$\sqrt{2},$` since it is the least _real_ upper bound `$\le \sqrt{2}.$`

### Examples

* The real number `$b$` in the semi-open interval `$[a,b)$` is the supremum of this interval because for every `$\epsilon > 0$` (no matter how small) there is an `$y\in[a,b)$` lying between the numbers `$b-\epsilon$` and `$b.$` 
* `$\sqrt{2}\not\in\mathbb Q$` is the supremum of the set or real numbers whose square is less or equal `$2$`, i.e. the set `$A:=\{x\in\mathbb Q\mid x^2\le 2\}$`, because for every `$\epsilon > 0$` there is a real number `$d\in A$` with `$d > \sqrt{2}-\epsilon.$`
* Please note that the `$\sup(D)$` does not have to be an element of `$D$`, like `$b\not\in[a,b).$` However, `$\sup(D)$` must be in the same domain as `$D$`, like `$\sqrt{2}$` is not a supremum of `$D=\{x\in\mathbb Q\mid x < \sqrt{2}\},$` but it is a supremum of  `$D=\{x\in\mathbb R\mid x < \sqrt{2}\}.$`
