layout: proof
categories: branches,theoretical-computer-science, computability
nodeid: bookofproofs$1198
orderid: 50
parentid: bookofproofs$1196
title: 
description:  Proof of THE SET OF WHILE-COMPUTABLE FUNCTIONS IS INCLUDED IN THE SET OF PARTIALLY WHILE-COMPUTABLE FUNCTIONS &#9733; master maths &#10004; visit BookOfProofs!
references: bookofproofs$1086
keywords: computable,functions,included,note,partially,set,while,proof
contributors: bookofproofs

---


---

It is sufficient to find a function `\(f : \mathbb N^k \to \mathbb N\)`, which is [partially WHILE-computable][bookofproofs$1184], but is not [WHILE-computable][bookofproofs$1184]. This is the case for the [partial function][bookofproofs$592] `\(f : \mathbb N \to \mathbb N\)`

`\[f(n):=\cases{0&\text{if }n=0\\
undefined&\text{if }n\neq 0}\]`

which is computed by the following `\(W H I L E\)` program:

`\[\mathtt{WHILE~r_i\neq 0~DO~r_i:=r_i+1~END;}\]`
