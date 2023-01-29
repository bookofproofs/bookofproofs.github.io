layout: proof
categories: branches,theoretical-computer-science, semi-numerical-algorithms
nodeid: bookofproofs$2879
orderid: 50
parentid: bookofproofs$8217
title: 
description: PROOF OF JACOBI SYMBOL PYTHON &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$1357,bookofproofs$8187
keywords: jacobi,python,symbol,jacobi symbol python,jacobi symbol,jacobi python,proof
contributors: bookofproofs

---


---

* The correctness of the algorithm follows from the [properties of the Jacobi symbol][bookofproofs$8216].
* Referring to these properties, the first (5) and second (6) supplementary laws are implemented as static methods of the class JacobiSymbol and their runtime is `$\mathcal O(1).$`
* The recursive method _calculate_ removes for [even][bookofproofs$8130] numbers `$a$` the factor `$2$` and for [odd][bookofproofs$8130] numbers `$a,$` the [greatest common divisor (Python)][bookofproofs$503] algorithm is used.
* Since both operations need the runtime `$\mathcal O(\log(b)),$` the recursive method _calculate_ requires the runtime `$\mathcal O(\log^2(b)),$` which corresponds to `$\mathcal O(\log^3(b))$` bit operations.
