layout: proof
categories: branches,analysis
nodeid: bookofproofs$1762
orderid: 50
parentid: bookofproofs$1761
title: 
description:  Proof of RIEMANN UPPER AND RIEMANN LOWER INTEGRALS FOR BOUNDED REAL FUNCTIONS &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$581
keywords: bounded,functions,integrals,lower,real,riemann,riemann lower integral,riemann upper integral,upper,proof
contributors: bookofproofs

---


---

Let `\([a,b]\)` be a [closed real interval][bookofproofs$1153] and let `\(f\)` be [bounded][bookofproofs$302] on `\([a,b]\)` and let `\(\psi\)` be a [step function][bookofproofs$1751] defined on that interval.

The proof goes in two steps:

### We will show that the upper Riemann integral is well-defined.

Obviously, if by hypothesis 

`\[\phi(x)\ge f(x)\text{ for all }x\in[a,b]\]`

then `\(\phi\)` is bounded from below by `\(f\)`. The set `\(D\)` of all [Riemann integrals of such functions][bookofproofs$1752]:

`\[D:=\left\{\int_{a}^b\phi(x)dx:~~\phi(x)\ge f(x)\text{ for all }x\in[a,b]\text{ and }\phi\text{ is a step function over }[a,b]\right\}\]`

is therefore a subset of real numbers, which is [bounded from below][bookofproofs$584]. From the [infimum property of real numbers][bookofproofs$1756], it follows that the following infimum exists:

`\[\inf D:=\inf\left\{\int_{a}^b\phi(x)dx:~~\phi(x)\ge f(x)\text{ for all }x\in[a,b]\text{ and }\phi\text{ is a step function over }[a,b]\right\}.\]`

The [definition of infimum][bookofproofs$1755] shows that it is unique. Therefore, we the upper Riemann integral of the bounded function `\(f\)` is well-defined:

`\[\int_{a}^{b~*}f(x)dx:=\inf D.\]`


### We will show that the lower Riemann integral is well-defined.

Similarly, if by hypothesis 

`\[\phi(x)\le f(x)\text{ for all }x\in[a,b]\]`

then `\(\phi\)` is bounded from above by `\(f\)`. The set `\(D\)` of all [Riemann integrals of such functions][bookofproofs$1752]:

`\[D':=\left\{\int_{a}^b\phi(x)dx:~~\phi(x)\le f(x)\text{ for all }x\in[a,b]\text{ and }\phi\text{ is a step function over }[a,b]\right\}\]`

is therefore a subset of real numbers, which is [bounded from above][bookofproofs$584]. From the [supremum property of real numbers][bookofproofs$1756], it follows that the following supremum exists:

`\[\inf D':=\inf\left\{\int_{a}^b\phi(x)dx:~~\phi(x)\le f(x)\text{ for all }x\in[a,b]\text{ and }\phi\text{ is a step function over }[a,b]\right\}.\]`

The [definition of supremum][bookofproofs$1754] shows that it is unique. Therefore, we the lower Riemann integral of the bounded function `\(f\)` is well-defined:

`\[\int_{a~*}^{b}f(x)dx:=\sup D'.\]`
