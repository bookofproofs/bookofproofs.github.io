layout: theorem
categories: branches,number-theory
nodeid: bookofproofs$8182
orderid: 400
parentid: bookofproofs$90
title: Chinese Remainder Theorem
description: CHINESE REMAINDER THEOREM &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$1272,bookofproofs$8152
keywords: chinese,remainder,theorem,proof of chinese remainder theorem
contributors: bookofproofs


---
The following theorem is known as the _Chinese remainder theorem_ because it was discovered by [Qin Jiushao](https://mathshistory.st-andrews.ac.uk/Biographies/Qin_Jiushao/) (1202 - 1261).

---

Let `$m_1,m_2,\ldots,m_r$` be [positive integers][bookofproofs$1075] and let `$a_1,\ldots,a_r$` be any [integers][bookofproofs$844]. The simultaneous [congruences][bookofproofs$8154] `$$\begin{array}{rcl}
x(m_1)&\equiv&a_1(m_1)\\ 
x(m_2)&\equiv&a_2(m_2)\\
&\vdots&\\
x(m_r)&\equiv& a_r(m_r)\\
\end{array}\label{eq:E18594}\tag{*}$$`
have a solution if and only if for all pairs of numbers `$a_i,a_j$` with `$i\neq j$` the [greatest common divisor][bookofproofs$1280] `$d:=\gcd(a_i,a_j)$` is a [divisor][bookofproofs$700] of `$a_i-a_j$` (equivalently `$a_i\equiv a_j\mod \gcd(a_i,a_j)$` whenever `$i\neq j$`).

In this case, the solution consists of all integers belonging to a single [congruence class][bookofproofs$8154] modulo `$m=\operatorname{lcm}(m_1,m_2,\cdots, m_r),$` where `$m$` is the [least common multiple of the `$r$` numbers][bookofproofs$8124] `$m_1,\ldots,m_r.$`

In particular, `$(\ref{eq:E18594})$` is always solvable if `$m_i\perp m_j$` are [co-prime][bookofproofs$8093], whenever `$i\neq j.$`
