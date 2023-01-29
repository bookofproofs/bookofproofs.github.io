layout: definition
categories: branches,number-theory
nodeid: bookofproofs$804
orderid: 500
parentid: bookofproofs$8104
title: Canonical Representation of Positive Rational Numbers
description: CANONICAL REPRESENTATION OF POSITIVE RATIONAL NUMBERS &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: 
keywords: canonical,canonical representation,numbers,positive,rational,representation
contributors: bookofproofs

---
The [canonical representation of natural numbers][bookofproofs$803] can be extended to [positive rational numbers][bookofproofs$1076], i.e. numbers of the form
`\[\frac ab,~~~~~ a,b\text{ both being positive integers.}\]`
This can be done by allowing the exponents to be negative integers as follows:

---

Let `$a,b$` be [natural numbers][bookofproofs$718], both `$\ge 1$`, and let `$a=\prod_{i=1}^\infty p_i^{e_i}\text { and }b=\prod_{i=1}^\infty p_i^{f_i}$`
be their [canonical representations][bookofproofs$803] of `\(a\)` and `\(b\)`. By setting `\(\alpha_i:=e_i - f_i\)` we get 
 `\[\frac ab=\prod_{i=1}^\infty p_i^{\alpha_i}\]`
as the unique **canonical representation**  of the [positive rational number][bookofproofs$1076] `\(\frac ab > 0\)`.

### Example

Please note that with each rational number `\(\frac ab > 0\)` we can associate a unique series of the integer exponents `\(\alpha_i\in\mathbb Z\)` of is canonical representation. For instance, we have

`\[\begin{array}{ccrrrrrrrr}
10=2^1\cdot 5^1&\text{ can be associated with the series }&1,&0,&1,&0,&0,&0,&0,&\ldots\\
\frac1{10}=\frac1{2^1\cdot 5^1}&\text{ can be associated with the series }&-1,&0,&-1,&0,&0,&0,&0,&\ldots\\
\frac{25}{1188}=\frac{5^2}{2^2\cdot 3^3\cdot 11^1}&\text{ can be associated with the series }&-2,&-3,&2,&0,&-1,&0,&0,&\ldots\\
\end{array}\]`

Please also note that the multiplication of any two positive rational numbers results in the addition of their associated series of exponents in their canonical representations.
