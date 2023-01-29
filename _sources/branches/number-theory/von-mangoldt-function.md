layout: definition
categories: branches,number-theory
nodeid: bookofproofs$702
orderid: 400
parentid: bookofproofs$8113
title: Von Mangoldt Function
description: VON MANGOLDT FUNCTION &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$1272
keywords: function,mangoldt,von,von mangoldt function
contributors: bookofproofs

---


---

The von Mangoldt `\(\Lambda(n)\)` function `$\Lambda:\mathbb N\to\mathbb N$` is an [arithmetic function][bookofproofs$8112] having the value of the [natural logarithm][bookofproofs$1421] for all `$n\in\mathbb N$` which are [positive powers][bookofproofs$1618] of [prime numbers][bookofproofs$473].
`\[\Lambda(n):=\begin{cases}
\log(p)&\text{for } n=p^e,\; e\ge 1\\
0&\text{for all other }n > 0
\end{cases}.\]`

### Example

As an example, let us calculate the von Mangoldt function for the value `$n=12.$`

`$$\begin{array}{rcl}
\Lambda(12)&=&\cancel{\Lambda(1)}+\Lambda(2)+\Lambda(3)+\Lambda(4)+\Lambda(5)+\cancel{\Lambda(6)}+\Lambda(7)+\Lambda(8)+\Lambda(9)+\cancel{\Lambda(10)}+\Lambda(11)+\cancel{\Lambda(12)}\\
&=&\Lambda(2)+\Lambda(3)+\Lambda(4)+\Lambda(5)+\Lambda(7)+\Lambda(8)+\Lambda(9)+\Lambda(11)\\
&=&\log(2)+\log(3)+\log(2)+\log(5)+\log(7)+\log(2)+\log(3)+\log(11)\\
&=&\log(2\cdot 3\cdot 2\cdot 5\cdot 7\cdot 2\cdot 3\cdot 11)\\
&=&\log(27720)\\
&\approx&10.23\\
\end{array}$$`
