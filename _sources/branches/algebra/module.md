layout: definition
categories: branches,algebra
nodeid: bookofproofs$6233
orderid: 50
parentid: bookofproofs$263
title: Module
description: MODULE ★ bring your math skills to the graduate level ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$6907
keywords: left module,module,right module,left modules,modules,right modules
contributors: @Brenner,bookofproofs

---


---

Let `\((R, + ,\cdot)\)` be a [ring with identity][bookofproofs$683] `\(1_R\)` and let `\(M=(M,+)\)` be a [commutative group][bookofproofs$553].
We call `\(_RM\)` a **left module**, if there is a [binary operation][bookofproofs$6188].
`\[\odot:\cases{R\times M\longrightarrow M,\cr(r,v)\longmapsto r\odot v,}\]`

with the following properties:
* `\(r\odot (u+v)=(r\odot u)+(r\odot v)\)`,
* `\((r+s)\odot u=(r\odot u)+(s\odot u)\)`,
* `\((rs)\odot u =r\odot (s\odot u)\)`,
* `\(1\odot u=u\)`.

for all `\(r,s\in R\)` and all `\(u,v\in M\)`.

Analogously, we call `\(M_R\)` a **right module**, if there is a [binary operation][bookofproofs$6188].
`\[\odot:\cases{M\times R\longrightarrow M,\cr(v,r)\longmapsto v\odot r,}\]`

with the following properties:
* `\((u+v)\odot r=(u\odot r)+(v\odot r)\)`,
* `\(u \odot (r+s)=(u\odot r)+(u\odot s)\)`,
* `\(u \odot (rs) =u\odot (r\odot s)\)`,
* `\(u\odot 1=u\)`.

If `\(R\)` is a [commutative unit ring][bookofproofs$880], then both definitions are equivalent and `\(M\)` is called an **module**.
