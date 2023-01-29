layout: proof
categories: branches,analysis
nodeid: bookofproofs$1771
orderid: 50
parentid: bookofproofs$1769
title: 
description:  Proof of LINEARITY AND MONOTONY OF THE RIEMANN INTEGRAL &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$581
keywords: linearity of the integral,monotony of the integral,proof
contributors: bookofproofs

---


---

### Proof of Linearity Rules

It follows from the [definition of Riemann integrable functions][bookofproofs$1763] that they are [bounded][bookofproofs$302]. By applying the [rules of adding Riemann upper and lower integrals of bounded functions][bookofproofs$1770] we get the 
 of inequations
`\[\int_{a~*}^{b}f(x)dx + \int_{a~*}^{b}g(x)dx \le \int_{a~*}^{b}(f+g)(x)dx \le \int_{a}^{b~*}(f+g)(x)dx \le \int_{a}^{b~*}f(x)dx + \int_{a}^{b~*}g(x)dx.\]`
Because, by hypothesis
`\[\int_{a~*}^{b}f(x)dx =\int_{a}^{b~*}f(x)dx = \int_{a}^{b}f(x)dx\quad\quad\text{and}\quad\quad\int_{a~*}^{b}g(x)dx =\int_{a}^{b~*}g(x)dx = \int_{a}^{b}g(x)dx\]`
we get the result that the function `\(f+g:[a,b]\mapsto\mathbb R\)` is Riemann integrable and that
`\[\int_{a~*}^{b}(f+g)(x)dx = \int_{a}^{b~*}(f+g)(x)dx = \int_{a}^{b}(f+g)(x)dx=\int_{a}^{b}f(x)dx+\int_{a}^{b}g(x)dx.\]`
Similarly, by applying the [rules of scalar multiplication of Riemann upper and lower integrals][bookofproofs$1770], we get the equation chain
`\[\int_a^{b~*}(\lambda\cdot f)(x)dx=\lambda\cdot\int_a^{b~*}f(x)dx =\lambda\cdot\int_a^{b}f(x)dx=\lambda\cdot\int_{a~*}^{b}f(x)dx=\int_{a~*}^{b}(\lambda\cdot f)(x)dx.\]`
This means that the function `\(\lambda\cdot f:[a,b]\mapsto\mathbb R\)` is Riemann integrable and that
`\[\int_a^{b}(\lambda\cdot f)(x)dx =\lambda\cdot\int_a^{b}f(x)dx.\]`

### Proof of Monotony

If `\(f(x)\le g(x)\)` for all `\(x\in[a,b]\)`, then we have `\(f(x)-g(x)\le 0\)`  for all `\(x\in[a,b]\)`. It follows from the linearity rules that

`\[\int_a^{b}(f-g)(x)dx=\int_a^{b}f(x)dx-\int_a^{b}g(x)dx\ge \int_a^{b}0dx=0.\]`
It follows
`\[\int_a^{b}f(x)dx\le\int_a^{b}g(x)dx.\]`
