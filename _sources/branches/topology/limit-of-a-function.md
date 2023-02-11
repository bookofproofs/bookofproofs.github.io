layout: definition
categories: branches,topology
nodeid: bookofproofs$6203
orderid: 600
parentid: bookofproofs$69
title: Limit of a Function
description: LIMIT OF A FUNCTION &#9733; bring your math skills to the graduate level &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$6907
keywords: function,limit
contributors: @Brenner,bookofproofs

---


---

Let `\((X,d)\)` and `\((Y,d)\)` be [metric spaces][bookofproofs$614] and let `\(T\subseteq X\)` be a [subset][bookofproofs$552] with a [boundary point][bookofproofs$1202] `\(b\in X\)`. Furthermore, let `\(f\colon T\longrightarrow Y\,\)` be a [function][bookofproofs$592].
The point `\(a\in Y\)` is called the *limit of `\(f\)` at the point `\(b\)`*, denoted by 
`\[\operatorname {lim} _{x\rightarrow a}\,f(x)=b\]`

if for each `\(\epsilon > 0\)` there exists a `\(\delta > 0\)` such that for each `\(x\)` contained in the [neighborhood][bookofproofs$849] of `\(a\in T\)`, `\(f(x)\)` is contained in the  neighborhood of `\(b\in Y\)`, formally

`\[\forall\,\epsilon > 0\,\exists\delta > 0:\,x\in T\cap B\left(a,\delta \right)\Longrightarrow f(x)\in Y\cap B\left(b,\epsilon \right).\]`
