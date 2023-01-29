layout: proof
categories: branches,analysis
nodeid: bookofproofs$1263
orderid: 50
parentid: bookofproofs$1259
title: 
description:  Proof of INTERMEDIATE VALUE THEOREM &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$581
keywords: intermediate,theorem,value,proof
contributors: bookofproofs

---


---

* Let `\([a,b]\)` be a [closed real interval][bookofproofs$1153].
* Let `\(f:[a,b]\to\mathbb R\)` be a [continuous real function][bookofproofs$1260].
* We want to shot that `\(f\)` takes any value between `\(f(a)\)` and `\(f(b)\)`, i.e. for each `\(u\in [f(a),f(b)]\)` there is at least one `\(c\in[a,b]\)` with `\(f( c)=u\)`.
* This is trivial for `$u=f(a)$` or `$u=f(b)$`. Therefor let `$f(a) < u < f(b).$`
* Set the function `$g:[a,b]\to\mathbb R$` with `$g(x):=f(x)-u$`.
* Since `$f$` is continuous by hypothesis and the [identity function is continuous][bookofproofs$6685], `$g$` is also continuous, because the arithmetic operation "`$-$`" [preserves the continuity][bookofproofs$1604].
* Thus we all prerequisites for the [intermediate root value theorem][bookofproofs$6692] are fulfilled and there is a `$c\in[a,b]$` with `$g(c )=0.$` 
* It follows that `$f(c )=u.$`
