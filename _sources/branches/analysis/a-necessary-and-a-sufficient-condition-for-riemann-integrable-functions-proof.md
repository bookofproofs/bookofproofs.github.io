layout: proof
categories: branches,analysis
nodeid: bookofproofs$1765
orderid: 50
parentid: bookofproofs$1764
title: 
description:  Proof of A NECESSARY AND A SUFFICIENT CONDITION FOR RIEMANN INTEGRABLE FUNCTIONS &#9733; master graduate maths &#10004; visit BookOfProofs now!
references: bookofproofs$581
keywords: condition,functions,integrable,necessary,riemann,sufficient,proof
contributors: bookofproofs

---


---

We prove both implications:

### "`\(\Rightarrow\)`"

* Assume, `\(f\)` is [Riemann integrable][bookofproofs$1763].
* Then, by definition, its [Riemann upper and lower integrals][bookofproofs$1761] exist and are equal. 
* Therefore, `\(f\)` is [bounded][bookofproofs$302] by some [step functions][bookofproofs$1751] `\(\phi:[a,b]\mapsto\mathbb R\)` and `\(\psi:[a,b]\mapsto\mathbb R\)` with `\[\phi\le f\le \psi.\]`
* From the [definition of supremum][bookofproofs$1754] and [infimum][bookofproofs$1755] it follows for every `\(\epsilon > 0\)`: `\[\int_a^b\psi(x)dx-\int_a^b\phi(x)dx\le \epsilon.\]`

### "`\(\Leftarrow\)`"

* Now, assume that `\(f\)` is [bounded][bookofproofs$302] and that for every `\(\epsilon > 0\)` there exist some [step functions][bookofproofs$1751] `\(\phi:[a,b]\mapsto\mathbb R\)` and `\(\psi:[a,b]\mapsto\mathbb R\)` with `\[\phi\le f\le \psi\quad\quad( * )\]` and `\[\int_a^b\psi(x)dx-\int_a^b\phi(x)dx\le \epsilon.\]`
* This means that, as `\(\epsilon\)` tends to `\(0\)`, the [Riemann lower integral][bookofproofs$1761] of the step function `\(\phi\)` and the [Riemann upper integral][bookofproofs$1761] of the step function `\(\psi\)` tend to each other:
`\[\lim_{\epsilon\to 0}\int_{a~*}^{b}\phi(x)dx=\lim_{\epsilon\to 0}\int_{a}^{b~*}\psi(x)dx.\quad\quad ( * * )\]`
* On the other hand, from `\(( * )\)`, from the [monotony of Riemann integrals for step functions][bookofproofs$1759], and from the [fact that convergence preserves lower and upper bounds, it follows][bookofproofs$1145].
`\[\lim_{\epsilon\to 0}\int_{a~*}^{b}\phi(x)dx\le \int_{a~*}^{b}f(x)dx \le \int_{a}^{b}f(x)dx\le \int_{a}^{b~*}f(x)dx \le \lim_{\epsilon\to 0}\int_{a}^{b~*}\psi(x)dx.\]`
* Together with `\(( * * )\)`, this means that `\(f\)` is [Riemann integrable][bookofproofs$1763], because in fact, 
`\[ \int_{a~*}^{b}f(x)dx = \int_{a}^{b}f(x)dx= \int_{a}^{b~*}f(x)dx.\]`
