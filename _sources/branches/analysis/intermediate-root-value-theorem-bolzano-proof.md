layout: proof
categories: branches,analysis
nodeid: bookofproofs$6695
orderid: 50
parentid: bookofproofs$6692
title: By Induction
description:  Proof of INTERMEDIATE ROOT VALUE THEOREM &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$581
keywords: bolzano,intermediate,root,theorem,value,proof
contributors: bookofproofs

---


---

* Let `\([a,b]\)` be a [closed real interval][bookofproofs$1153].
* Let `\(f:[a,b]\to\mathbb R\)` be a [continuous real function][bookofproofs$1260] with `$f(a) < 0$` and `$f(b) > 0$` (or `$f(a) > 0$` and `$f(b) < 0$`). Without loss of generality, assume `$f(a) < 0 < f(b)$`.
* We will prove [by induction][bookofproofs$657] that there exists a sequence `\((I_n)_{n\in\mathbb N}\)` of [closed real intervals][bookofproofs$1153] `\(I_n:=[a_n,b_n]\)` with the following properties:
   * Case `\((i)\)` `\([a_n,a_n]\subset [a_{n-1},b_{n-1}]\)` for `\(n\ge 1\)`.
   *  Case `\((ii)\)`  `\(b_n - a_n = 2^{-n}(b-a)\)`.
   * Case `\((iii)\)`  `\(f(a_n) \le 0\)` and `\(f(b_n)\ge 0\)` for all `\(n\in\mathbb N\)`.
* Base case `\(n=0\)`
   * For `\([a_0,b_0]:=[a,b]\)` the properties  `\((i)\)` to `\((iii)\)` are obviously fulfilled.
* Induction step `\(n\rightarrow n + 1\)`.
   * Let `\([a_n,b_n]\)` be an interval, for which the properties are fulfilled. Set `\(m:=(a_n + b_n)/2\)`. `\(m\)` is the "middle" of the interval  `\([a_n,b_n]\)`. 
   * We set now `\[[a_{n+1},b_{n+1}]:=\begin{cases}
[a_n,m]&\text{if }f(m)\ge 0,\\
[m,b_n]&\text{else.}
\end{cases}\]`
   * Obviously, the properties `\((i)\)` to `\((iii)\)` are fulfilled.  
   * It follows that the sequence  `\((a_{n})_{n\in\mathbb N}\)` is [monotonically increasing][bookofproofs$1155] and [bounded][bookofproofs$1136] and the sequence `\((b_{n})_{n\in\mathbb N}\)` is [monotonically decreasing][bookofproofs$1155] and [bounded][bookofproofs$1136].
   * Therefore, because of the [monotone convergence theorem][bookofproofs$197], both sequences are convergent and we have 
`\[\lim_{n\to\infty}a_n=\lim_{n\to\infty}b_n=c\]`
for some `\(c\in [a,b]\)`. 
   * Because `\(f\)` is [continuous on the interval][bookofproofs$1260] `\([a,b]\)`, we have
`\[\lim_{n\to\infty}f(a_n)=\lim_{n\to\infty}f(b_n)=f( c).\]`
   * Because [convergence preserves upper and lower bounds for sequence members][bookofproofs$1145] and because of `\((iii)\)`, we have 
`\[f( c) \le 0\text{ and } f( c)\ge 0,\]`
which means that `\(f( c)=0\)`. 
   * Thus we have found a [root value][bookofproofs$6736] of the function `\(f\)`.
