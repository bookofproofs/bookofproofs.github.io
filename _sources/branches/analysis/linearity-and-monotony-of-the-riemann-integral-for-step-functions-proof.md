layout: proof
categories: branches,analysis
nodeid: bookofproofs$1760
orderid: 50
parentid: bookofproofs$1759
title: 
description:  Proof of LINEARITY AND MONOTONY OF THE RIEMANN INTEGRAL FOR STEP FUNCTIONS &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$581
keywords: functions,integral,riemann,riemann integral of the step function,proof,proof
contributors: bookofproofs

---


---

Let`\(\phi,\psi\in T[a,b]\)` be [step functions][bookofproofs$6796]. According to the [definition of the Riemann integral for step functions][bookofproofs$1752], both integrals
`\[\int_a^b\phi(x)dx=\sum_{i=1}^n\phi(x_i)(x_i-x_{i-1})\quad\quad\text{and}\quad\quad\int_a^b\psi(x)dx=\sum_{i=1}^n\psi(x_i)(x_i-x_{i-1})\]`
can be calculated without loss of generality using the same partition `\(a=x_0 < x_1 < \ldots < x_{n-1} < x_n=b\)`. Therefore, the stated 

*linearity rules*:

`\[\int_a^b(\phi+\psi)(x)dx=\int_a^b\phi(x)dx+\int_a^b\psi(x)dx\]`
`\[\int_a^b(\lambda\cdot \phi)(x)dx=\lambda\cdot\int_a^b\phi(x)dx\quad\quad(\text{for all }\lambda\in\mathbb R)\]`

and the **monotony rule**:

`\[\phi\le \psi\Rightarrow \int_a^b\phi(x)dx\le \int_a^b\psi(x)dx\]`

are trivial. In the monotony rule, "`\(\phi\le \psi\)`" means the [order relation for step functions][bookofproofs$1758].