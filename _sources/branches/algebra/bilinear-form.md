layout: definition
categories: branches,algebra
nodeid: bookofproofs$6229
orderid: 14
parentid: bookofproofs$194
title: Bilinear Form
description: BILINEAR FORM &#9733; bring your math skills to the graduate level &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$6907
keywords: bilinear,form
contributors: 

---


---

Let `\(F\)` be a [field][bookofproofs$557] and `\(V\)` be a [vector space][bookofproofs$560] over `\(F\)`. A [function][bookofproofs$592]

`\[B:\cases{V\times V\longrightarrow F,\cr(v,w)\longmapsto \left\langle v,w\right\rangle,}\]`

(i.e. a function mapping all pairs of vectors `\((v,w)\)` to their respective [dot products][bookofproofs$1049]) `\(\langle v,w\rangle\)`) is called a **bilinear form**, if it is [linear][bookofproofs$403] over `\(F\)` in each argument separately, i.e.:


> `\(\langle u + v, w\rangle = \langle u, w) + \langle v, w\rangle\)`
`\(\langle su, v\rangle = s\langle u, v\rangle\)`
`\(\langle u, v + w\rangle = \langle u, v\rangle + \langle u, w\rangle\)`
`\(\langle u, sv\rangle = s\langle u, v\rangle\)`

for all `\(u,v,w\in V\)` and `\(s\in F\)`.
