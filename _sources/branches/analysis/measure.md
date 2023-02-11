layout: definition
categories: branches,analysis
nodeid: bookofproofs$6232
orderid: 200
parentid: bookofproofs$6212
title: Measure
description: MEASURE &#9733; bring your math skills to the graduate level &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$6907
keywords: measure
contributors: @Brenner,bookofproofs

---


---

Let `\((M, {\mathcal {A}})\)` be a [measurable set][bookofproofs$6230] with the [`\(\sigma\)`-algebra][bookofproofs$6212] `\(\mathcal{A}\,\)`. 
A [function][bookofproofs$592] mapping `\(\mathcal {A}\)` to the set of [positive real numbers][bookofproofs$1107] `\[\mu \colon \cases{{\mathcal {A}}\longrightarrow {\mathbb {R}}_{+},\cr T\longmapsto \mu (T)},\]` is called a *measure on `\(M\)`*, if `\(\mu (\emptyset)=0\)` and if for every [countable][bookofproofs$772] [family][bookofproofs$6198] of [mutually disjoint][bookofproofs$6227] [subsets][bookofproofs$552] `\(T_{i}\subseteq {\mathcal {A}}\)`, `\(i\in I\)`, the measure of the [union of these subsets][bookofproofs$552] equals the sum of the measures of each subset, formally: 
`\[\mu \left(\bigcup _{i\in I}T_{i}\right)=\sum _{i\in I}\mu (T_{i}).\]`
The second property is called **`\(\sigma\)`-additivity**.

Please note that the only difference between a [measure][bookofproofs$6232] and a [pre-measure][bookofproofs$6236] is that a measure is defined on a [`\(\sigma\)`-algebra][bookofproofs$6212] while a pre-measure is defined on a [ring of sets][bookofproofs$6216].