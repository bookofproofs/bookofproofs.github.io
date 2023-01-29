layout: solution
categories: branches,number-theory
nodeid: bookofproofs$8219
orderid: 50
parentid: bookofproofs$8218
title: 
description: Solution of APPLICATIONS OF THE JACOBI SYMBOL &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$1272
keywords: applications,jacobi,symbol solution
contributors: bookofproofs

---


---

### Ad 1

* `$443$` is a [prime number][bookofproofs$473], and the solvability of the quadratic [congruence][bookofproofs$8153] can be decided by the calculating the [Legendre symbol][bookofproofs$8198] `$\left(\frac{383}{443}\right).$`
* In order to do this, we can use the [properties of the Jacobi symbol][bookofproofs$8216]:
`$$\begin{array}{rcll}
\left(\frac{383}{443}\right)&=&-\left(\frac{443}{383}\right)&\text{reciprocity law}\\
&=&-\left(\frac{60}{383}\right)&\text{equal residues}\\
&=&-\left(\frac{2}{383}\right)^2\left(\frac{15}{383}\right)&\text{definition of the Jacobi symbol}\\
&=&-\left(\frac{15}{383}\right)&\text{second supplementary law}\\
&=&\left(\frac{383}{15}\right)&\text{reciprocity law}\\
&=&\left(\frac{8}{15}\right)&\text{equal residues}\\
&=&\left(\frac{2}{15}\right)^3&\text{definition of the Jacobi symbol}\\
&=&1&\text{second supplementary law}\\
\end{array}$$`
* It follows that the quadratic [congruence][bookofproofs$8153] `$x^2\equiv 383\mod 443$` is solvable.

### Ad 2

* `$87$` is not a prime number, however, `$35$` and `$87$` are [co-prime][bookofproofs$8093].
* We use again the [properties of the Jacobi symbol][bookofproofs$8216]:
`$$\begin{array}{rcll}
\left(\frac{35}{87}\right)&=&-\left(\frac{87}{35}\right)&\text{reciprocity law}\\
&=&-\left(\frac{17}{35}\right)&\text{equal residues}\\
&=&-\left(\frac{35}{17}\right)&\text{reciprocity law}\\
&=&-\left(\frac{1}{17}\right)&\text{equal residues}\\
&=&-1\\
\end{array}$$`
