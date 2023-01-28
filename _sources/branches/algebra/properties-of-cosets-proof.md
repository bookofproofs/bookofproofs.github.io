layout: proof
categories: branches,algebra
nodeid: bookofproofs$830
orderid: 50
parentid: bookofproofs$829
title: 
description:  Proof of PROPERTIES OF COSETS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$828
keywords: cosets,properties,properties of cosets,coset properties,proof
contributors: bookofproofs

---


---

In the following let `\((G,\ast)\)` be a [group][bookofproofs$671] and `\(H\subseteq G\)` its [subgroup][bookofproofs$554] 

#### Proof of (1)

If `\(|H|=n\)`, then `\(|Ha|\le n\)`, which follows from the [definition of a coset][bookofproofs$827] But `\(|Ha| \not <  n\)`. For if `\(|Ha| <  n\)`, then there would be at least two different elements `\(g,h\in H\)`, `\(g\neq h\)` and `\(g\ast a=h\ast a\)`. This is equivalent to `\(g=h\)`, which is a [contradiction][bookofproofs$744] to `\(g\neq h\)`. Thus it must be `\(|Ha|=|H|\)`. Analogously, we can prove `\(|aH|=|H|\)`.

#### Proof of (2)

We have to prove that `\(a\sim_l b:=a\in bH\)` (respectively `\(a\sim_r b:=a\in Hb\)`) define [equivalence relations][bookofproofs$574], by proving their reflexivity, symmetry and transitivity.

### Reflexivity

Because `\(H\subset G\)` is a [subgroup][bookofproofs$554] of `\(G\)`, the neutral element of `\(G\)` is also the neutral element of `\(H\)`. Therefore, following the [definition of cosets][bookofproofs$827], `\(a\in aH\)` and `\(a\in Ha\)`. So `\(a\sim_l a\)` (respectively `\(a\sim_r a\)`) are reflexive. 

### Symmetry

Assume `\(a\sim_l b\)`. From `\(a\in bH\)` it follows that there exists `\(x\in H\)` with `\(a=b\ast x\)`, which is equivalent to `\(a\ast x^{-1}=b\)`. Because also `\(x^{-1}\in H\)`, it follows that `\(b\in aH\)`, so `\(b\sim_l a\)` is symmetric. Respectively, assume `\(a\sim_r b\)`. From `\(a\in Hb\)` it follows that there exists `\(x\in H\)` with `\(a=x\ast b\)`, which is equivalent to `\(x^{-1}a=b\)`. Because also `\(x^{-1}\in H\)`, it follows that `\(b\in Ha\)`, so `\(b\sim_r a\)` is symmetric.

### Transitivity

Assume `\(a\sim_l b\)` and `\(b\sim_l c\)`. From `\(a\in bH\)` it follows that there exists `\(x\in H\)` with `\(a=b\ast x\)`, which is equivalent to `\(a\ast x^{-1}=b\)`. From `\(b\in cH\)` it follows that there exists `\(y\in H\)` with `\(b=c\ast y\)`. From both results, it follows that `\(a\ast x^{-1}=c\ast y\)`, which is equivalent to `\(a=c\ast y\ast x\)`. Because `\(H\)` is closed under `\(\ast\)`, `\(y\ast x\in H\)`. Therefore, `\(a\sim_l c\)` is transitive.
Respectively, assume `\(a\sim_r b\)` and `\(b\sim_r c\)`. From `\(a\in Hb\)` it follows that there exists `\(x\in H\)` with `\(a=x\ast b\)`, which is equivalent to `\(x^{-1}\ast a=b\)`. From `\(b\in Hc\)` it follows that there exists `\(y\in H\)` with `\(b=y\ast c\)`. From both results, it follows that `\(x^{-1}\ast a=y\ast c\)`, which is equivalent to `\(a=x\ast y\ast c\)`. Because `\(H\)` is closed under `\(\ast\)`, `\(x\ast y\in H\)`. Therefore, `\(a\sim_r c\)` is transitive.
