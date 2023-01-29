layout: proof
categories: branches,analysis
nodeid: bookofproofs$1617
orderid: 50
parentid: bookofproofs$1616
title: By Induction
description: PROOF BY INDUCTION Proof of EXPONENTIAL FUNCTION OF GENERAL BASE WITH NATURAL EXPONENTS &#9733; master graduate maths &#10004; visit BookOfProofs now!
references: bookofproofs$581
keywords: base,exponential,exponents,function,general,natural,proof
contributors: bookofproofs

---


---

We will [prove by induction][bookofproofs$657] that the [exponential function of general base][bookofproofs$1603] `\(a > 0\)`  is identical with the [n-th power function][bookofproofs$1618], formally `\(\exp_a(n)=a^n\)` for all [positive real numbers][bookofproofs$1107] `\(a > 0\)` and all [natural numbers][bookofproofs$718]  `\(n\ge 0\)`.

### Special case `\(n=0\)` 

Using the [corresponding proposition][bookofproofs$1423] due to which `\(\exp(0)=1\)`, we get from the definition of the [exponential function of general base][bookofproofs$1603], and the definition of the [n-th power function][bookofproofs$46]: `\[\exp_a(0) =\exp(0\cdot \ln(a))=\exp(0)=1=a^0.\]`

### Base case `\(n=1\)`

For `\(n=1\)`, we get (because the [logarithm is the inverse function of the exponential function][bookofproofs$1421])

`\[\exp_a(1) =\exp(1\cdot \ln(x))=a=a^1.\]`

### Induction step `\(n\to n+1\)`

Assume `\(\exp_a(m)=a^m\)` is correct for all `\(m\le n\)` for a given `\(n\ge 0\)`.  By virtue of the [functional equation of the exponential function of general base][bookofproofs$1612], we get

`\[\begin{array}{rcll}
\exp_a(n+1)&=&\exp_a(1)\cdot \exp_a(n)&\text{by functional equation}\\
&=&a\cdot a^n&\text{by base case}\\
&=&a^{n+1}&\text{by definition of the n-th power function}.\end{array}\]`
