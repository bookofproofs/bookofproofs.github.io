layout: definition
categories: branches,logic
nodeid: bookofproofs$7877
orderid: 100
parentid: bookofproofs$7875
title: Rules of Inference
description: RULES OF INFERENCE ★ bring your math skills to the graduate level ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$656
keywords: rules of inference,rule of inference
contributors: bookofproofs

---


---

Let `$U$` be the [domain of discourse][bookofproofs$6219], whose elements or (any kind of mathematical objects) we want to study, and let `$L\subset (\Sigma^*,\cdot)$` be a [formal language][bookofproofs$94] over an alphabet `$\Sigma$` with a [syntax][bookofproofs$709] appropriate to generate strings that are [interpretable][bookofproofs$7874] under the interpretation `$I$`, and let the corresponding [truth function][bookofproofs$7874] `$[[]]_I:L\to \mathbb B$` be given. 

The **rules of inference** is a non-empty, [finite][bookofproofs$985] set of rules of the form


`$$\begin{array}{rcl}Rule_{(1)}&:=&\frac{f^{(1)}_1,\ldots,f^{(1)}_{m_{(1)}}}{f_1},\\&\vdots\\
Rule_{(r)}&:=&\frac{f^{(r)}_1,\ldots,f^{(r)}_{m_{(r)}}}{f_r}\end{array}$$`

meaning for the `$j$`-th rule, `$j=1,\ldots,r$` that if `$f^{(j)}_1,\ldots,f^{(j)}_{m_{(j)}}\in L$` are strings interpreted as true, then also the string `$f_j\in L$` can be taken for granted, in other words, from `$[[f^{(j)}_1]]_I=1,\ldots,[[f^{(j)}_{m_{(j)}}]]_I=1$` it follows that `$[[f_j]]_I=1$` for `$j=1,\ldots,r$`.

We also say that `$f_j$` are (logically) **derivable** from the `$f^{(j)}_1,\ldots,f^{(j)}_{m_{(j)}},$` `$j=1,\ldots,r$` and write this using the symbol "$\vdash$", i.e. 

`$$\begin{array}{rcl}f^{(1)}_1,\ldots,f^{(1)}_{m_{(1)}},&\vdash& f_1,\\
&\vdots\\
f^{(r)}_1,\ldots,f^{(r)}_{m_{(r)}},&\vdash& f_r.\end{array}$$`
