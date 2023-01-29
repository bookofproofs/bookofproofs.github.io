layout: proof
categories: branches,analysis
nodeid: bookofproofs$1773
orderid: 50
parentid: bookofproofs$1772
title: 
description:  Proof of MEAN VALUE THEOREM FOR RIEMANN INTEGRALS &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$581
keywords: mean value theorem for riemann integrals,proof
contributors: bookofproofs

---


---

Let `\(m\)` and `\(M\)` be the values of the [infimum][bookofproofs$1755] and the [supremum][bookofproofs$1754] of all values, which the function `\(f\)` takes on the [closed real interval][bookofproofs$1153] `\([a,b]\)`, formally:
`\[\begin{array}{rcll}
m&:=&\inf&\{f(x):x\in[a,b]\}\\
M&:=&\sup&\{f(x):x\in[a,b]\}
\end{array}\]`

By hypothesis, `\(\phi(x)\ge 0\)` for all `\(x\in[a,b]\)`. Thus, we get `\[m\cdot \phi(x)\le f(x)\cdot\phi(x)\le M\cdot\phi(x)\quad\quad\text{for all }x\in[a,b].\]`
It follows from the [linearity and monotony of the Riemann integral][bookofproofs$1769].
`\[m\cdot \int_a^b\phi(x)dx\le \int_a^bf(x)\cdot\phi(x)dx\le M\cdot \int_a^b\phi(x)dx.\]`

Therefore, there exists `\(\mu\in[m,M]\)` with

`\[\int_a^bf(x)\cdot\phi(x)dx= \mu\cdot \int_a^b\phi(x)dx.\]`

By hypothesis, `\(f:[a,b]\mapsto\mathbb R\)` is a [continuous functions][bookofproofs$1260]. By virtue of the [intermediate value theorem][bookofproofs$1259], `\(f\)` takes any value between `\(f(a)\)` and `\(f(b)\)`, in particular the value `\(\mu\)`. Thus, there exist `\(\xi\in[a,b]\)` with `\(f(\xi)=\mu\)` and

`\[\int_a^bf(x)\cdot\phi(x)dx= f(\xi)\cdot \int_a^b\phi(x)dx.\]`
