layout: solution
categories: branches,combinatorics
nodeid: bookofproofs$8491
orderid: 50
parentid: bookofproofs$8490
title: 
description: SOLUTION OF INTERPOLATING NUMBERS WITH A POLYNOMIAL &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$8404
keywords: interpolating numbers with a polynomial,solution
contributors: bookofproofs

---


---

Surprisingly, we can find a combinatorial solution to this problem using the [discrete difference calculus methods][bookofproofs$8407].
* By "Taylor's formula for the difference operator", we have for any [factorial polynomial][bookofproofs$8418] `$$f(x)=\frac{\Delta^n f(0)}{n !} x^{\underline{n}}+\frac{\Delta^n f(0)}{(n-1) !} x^{\underline{n-1}}+ \ldots + \frac{\Delta^2 f(0)}{2 !} x^{\underline{2}} + \Delta f(0) x^{\underline{1}}+ f(0).$$`
* Because [factorial polynomials and usual polynomials equal each other][bookofproofs$8419], the only difference are their different coeffecients.
* Since we want to find the coefficients of the of a "usual" [polynomial][bookofproofs$199], and not a factorial polynomial, we can, nevertheless use the above Taylor's formula as a starting point.
* Writing the data in tabular form and computing the successive differences until all become `$0$` yields
`$$\begin{array}{rrrrrrr}
x&f(x)&\Delta f(x)&\Delta^2 f(x)&\Delta^3 f(x)&\Delta^4 f(x)&\Delta^7 f(x)\\
\hline
0&0&15&50&60&24&0\\
1&15&65&110&84&24&0\\
2&80&175&194&108&24&0\\
3&255&369&302&132&24\\
4&624&671&434&156\\
5&1295&1105&590\\
6&2400&1695\\
7&4095
\end{array}$$`
* It follows that the factorial polynomial representation of `$f(x)$` is `$$\begin{align}f(x)&=0+15x^{\underline 1}+\frac{50}{2!}^{\underline 2}+\frac{60}{3!}^{\underline 3}+\frac{24}{4!}^{\underline 4}\nonumber\\
&=0+15x+\frac{50}{2!}x(x-1)+\frac{60}{3!}x(x-1)(x-2)+\frac{24}{4!}x(x-1)(x-2)(x-3)\nonumber\\
&=x^4+4x^3+6x^2+4x\nonumber\\
&=(x+1)^4-1
\end{align}$$`
which is the required usual representation of the polynomial.
