layout: proof
categories: branches,number-theory
nodeid: bookofproofs$3531
orderid: 50
parentid: bookofproofs$8182
title: By Induction
description:  Proof of CHINESE REMAINDER THEOREM &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$1272
keywords: chinese,remainder,theorem,proof of chinese remainder theorem,proof
contributors: bookofproofs

---


---

By hypothesis, `$m_1,m_2,\ldots,m_r$` are [positive integers][bookofproofs$1075] and `$a_1,\ldots,a_r$` are any [integers][bookofproofs$844]. We will first prove the theorem for `$r=2$` and then the general case by induction. We can assume all `$a_i$` are distinct, otherwise, we could replace two congruences of the system by just one and reduce the number of simultaneous congruences. For the case `$r=1,$` the Chinese remainder theorem is trivial.

### Base Case `$r=2$`

We will first show that both congruences are solvable simultaneously if and only if the [greatest common divisor][bookofproofs$1280] `$d:=\gcd(m_1,m_2)$` is a [divisor][bookofproofs$700] of `$a_1-a_2.$`

### "`$\Rightarrow$`"

* Assume, `$x(m_1)\equiv a_1(m_1)$` and `$x(m_2)\equiv a_1(m_2).$` 
* From the [congruence modulo a divisor][bookofproofs$8171], it follows that `$x(d)\equiv a_1(d)$` and `$x(d)\equiv a_1(d).$`
* Thus, `$a_1(d)=a_2(d).$`
* By definition of [congruence][bookofproofs$8154], it follows `$d\mid (a_1-a_2).$`

### "`$\Leftarrow$`"

* Assume, `$d\mid (a_1-a_2).$` 
* It follows, `$d\mid (a_2-a_1).$`
* According to [existence and number of solutions of an LDE with one variable][bookofproofs$8178], the congruence `$(m_1y)(m_2)\equiv (a_2-a_1)(m_2)\label{eq:E18592a}\tag{1}$` is solvable if and only if `$\gcd(m_1,m_2)=d\mid (a_2-a_1),$` and it has exactly `$d$` solutions.
* By setting `$x:=m_1y$` we have `$(x+a_1)(m_2)\equiv a_2(m_2).$`
* On the other side, the congruence class `$x(m_1)\equiv a_1(m_1)\label{eq:E18592b}\tag{2}$` is equivalent to `$x=a_1+m_1h$` for all `$h\in\mathbb Z.$`
* Now we can chose `$h$` such that `$x(m_2)\equiv(hm_1+a_1)(m_2)\equiv a_2(m_2).$`
* Comparing both results, we have `$y=h$` and `$x(m_2)\equiv(x+a_1)(m_2)\equiv a_2(m_2).\label{eq:E18592c}\tag{3}$`
* It follows from `$(\ref{eq:E18592b})$` and `$(\ref{eq:E18592c})$` that `$x(m_1)\equiv a_1(m_1)$` and `$x(m_2)\equiv a_1(m_2).$` 

Now, we will show that all simultaneous solutions belong to a single congruence class modulo the [least common multiple][bookofproofs$1276] `$\operatorname{lcm}(m_1,m_2).$`

* In particular, the congruence `$(\ref{eq:E18592a})$` is solvable for an `$y_0$` with `$$\frac{m_1}{d}y_0\equiv\frac{a_2-a_1}{d}\mod \frac{m_2}{d},$$` which has exactly one solution according to the [existence and number of solutions of an LDE with one variable][bookofproofs$8178].
* All `$x$` solving the simultaneous congruences `$x(m_1)\equiv a_1(m_1)$` and `$x(m_2)\equiv a_1(m_2)$` can be written (for `$h\in\mathbb Z$`) as `$$\begin{array}{rcl}x&=&a_1+\left(y_0+h\frac{m_2}{d}\right)m_1\\
&=&a_1+y_0m_1+h\frac{m_1m_2}{d}\\
&=&a_1+y_0m_1+h\operatorname{lcm}(m_1,m_2),
\end{array}$$` 
because of the [relationship between the greatest vommon divisor and the least common multiple][bookofproofs$1281].
* For `$h\in\mathbb Z,$` the last equation consists exactly of the congruence class modulo `$\operatorname{lcm}(m_1,m_2).$`

### Induction step `$r > 2.$`

* Let `$r > 2$` and let the claim be proven for `$r-1.$` 
* This means that there is an `$a\in\mathbb Z$` with `$x\equiv a\mod \operatorname{lcm}(m_1,\ldots,m_{r-1})$` being a solution of the simultaneous `$r-1$` congruence classes
`$$\begin{array}{rcl}
x(m_1)&\equiv&a_1(m_1)\\
x(m_2)&\equiv&a_2(m_2)\\
&\vdots&\\
x(m_{r-1})&\equiv& a_{r-1}(m_{r-1}).\\
\end{array}\label{eq:E18598d}\tag{4}$$`
* The step `$r-1\to r$` follows from the base case applied to the congruence system
`$$\begin{array}{rcl}
x(\operatorname{lcm}(m_1,\ldots,m_{r-1}))&\equiv&a(\operatorname{lcm}(m_1,\ldots,m_{r-1}))\\
x(m_r)&\equiv&a_r(m_r),\\
\end{array}$$`
and the definition of the [least common multiple with more than two variables][bookofproofs$8124] `$\operatorname{lcm}(m_1,\ldots,m_{r})=\operatorname{lcm}(\operatorname{lcm}(m_1,\ldots,m_{r-1}), m_r).$`
