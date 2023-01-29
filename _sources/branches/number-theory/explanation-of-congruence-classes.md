layout: explanation
categories: branches,number-theory
nodeid: bookofproofs$585
orderid: 200
parentid: bookofproofs$8153
title: Explanation of Congruence Classes
description: EXPLANATION OF CONGRUENCE CLASSES &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$8152
keywords: classes,congruence,explanation,congruence classes,congruence class
contributors: bookofproofs

---


---

In the proposition about [congruence classes][bookofproofs$8154], we have seen that the relation "`$\equiv$`" is an [equivalence relation][bookofproofs$574].
For each [integer][bookofproofs$844] `$a\in\mathbb Z$` and each [positive integer][bookofproofs$1075] `$m > 0$` there is a unique [congruence class][bookofproofs$8154] `$a(m)$`  
`$$\begin{array}{rcl}a(m)&=&\{x\in\mathbb Z\mid x(m)\equiv a(m)\}\\
&=&\{\ldots,a-2m,a-m,a,a+m,a+2m,\ldots\}.
\end{array}$$`

If another integer `$a'$` can be written as `$a'=a+km$` then its congruence class is
`$$\begin{array}{rcl}a'(m)&=&\{\ldots,(a+km)-2m,(a+km)-m,(a+km),(a+km)+m,(a+km)+2m,\ldots\},\\
\end{array}$$`
and it is easy to see that both sets are equal: `$a(m)=a'(m).$` This is because both sets have infinitely many elements and those of `$a'(m)$` correspond to those of `$a(m)$` shifted by `$k$` positions.

So, we now know what a congruence class is. But what is the [quotient set][bookofproofs$7991] `$\mathbb Z_m,$` then? It is a [set][bookofproofs$550] containing the sets like `$a(m)$` as elements. The proposition about the relationship between [congruences and division with quotient and remainder][bookofproofs$8155] shows that this set is finite. If we write any given integer `$a\in\mathbb Z$` in the form `$$a=qm+r,\quad 0\le r < m,$$` then we will always arrive at exactly one of the values `$r=0,1,2,\ldots,m-1.$` Therefore, these values can be taken as _representatives_ of their congruence classes

`$$0(m),1(m),2(m),\ldots,(m-1)(m).$$`

Below, we will learn some calculation rules with congruence classes. We will see that we can add, subtract, multiply, and sometimes even divide them. And we will also see that the results of these calculations will be compatible with the same arithmetical operations done with "normal" integers, modulo the multiples of `$m.$`
