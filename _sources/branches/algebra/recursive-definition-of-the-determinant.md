layout: definition
categories: branches,algebra
nodeid: bookofproofs$6252
orderid: 50
parentid: bookofproofs$298
title: Recursive Definition of the Determinant
description: RECURSIVE DEFINITION OF THE DETERMINANT &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$6907
keywords: definition,determinant,recursive,recursive definition of determinant,recursive determinant,recursive definition
contributors: 

---


---

Let `\(F\)` be a [field][bookofproofs$557] and let `\(A\in M_{n\times n}(F)\)` be a [square matrix][bookofproofs$1056] For `\(i\in \{1,\ldots ,n\}\)` let `\(A_{i}\in M_{(n-1)\times (n-1)}(F)\)` be a square matrix gained by deleting the first column and the `\(i\)`-th row of `\(A\)`. 

The **determinant** `\(|A|\)` is defined recursively by 
`\[|M|={\begin{cases}a_{11}\,,&{\text{if }}n=1\,,\\\sum _{i=1}^{n}(-1)^{i+1}a_{i1}|A_{i}|&{\text{ for }}n\geq 2\,.\end{cases}}\]`


### Example - Calculating the Determinant of a (4x4)-Matrix

`\[\begin{array}{rcl}
\left|\begin{array}{cccc}a&b&c&d\\e&f&g&h\\i&j&k&l\\m&n&o&p\end{array}\right|&=&a\left|\begin{array}{ccc}f&g&h\\j&k&l\\n&o&p\end{array}\right|-e\left|\begin{array}{ccc}b&c&d\\j&k&l\\n&o&p\end{array}\right|+i\left|\begin{array}{ccc}b&c&d\\f&g&h\\n&o&p\end{array}\right|-m\left|\begin{array}{ccc}b&c&d\\f&g&h\\j&k&l\end{array}\right|\\
&=&af\left|\begin{array}{cc}k&l\\o&p\end{array}\right|-aj\left|\begin{array}{cc}g&h\\o&p\end{array}\right|+an\left|\begin{array}{cc}g&h\\k&l\end{array}\right|- eb\left|\begin{array}{cc}k&l\\o&p\end{array}\right|+ej\left|\begin{array}{cc}c&d\\o&p\end{array}\right|-en\left|\begin{array}{cc}c&d\\k&l\end{array}\right|+\\
&&ib\left|\begin{array}{cc}g&h\\o&p\end{array}\right|-if\left|\begin{array}{cc}c&d\\o&p\end{array}\right|+in\left|\begin{array}{cc}c&d\\g&h\end{array}\right|- mb\left|\begin{array}{cc}g&h\\k&l\end{array}\right|+mf\left|\begin{array}{cc}c&d\\k&l\end{array}\right|-mj\left|\begin{array}{cc}c&d\\g&h\end{array}\right|\\
&=&afkp-afol-ajgp+ajoh+angl-ankh-ebkp+ebol+ejcp-ejod-encl+enkd+\\
&&ibgp-iboh-ifcp+ifod+inch-ingd-mbgl+mbkh+mfcl-mfkd-mjch+mjgd
\end{array}\]`
