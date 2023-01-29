layout: proof
categories: branches,analysis
nodeid: bookofproofs$1753
orderid: 50
parentid: bookofproofs$1752
title: 
description:  Proof of RIEMANN INTEGRAL FOR STEP FUNCTIONS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$581
keywords: functions,integral,riemann,riemann integral of the step function,proof
contributors: bookofproofs

---


---

Let `\(\phi\in T[a,b]\)` be a [step function][bookofproofs$6796] with respect to the partition `\(a=x_0 < x_1 < \ldots < x_{n-1} < x_n=b\)`. We want to show that the definition of the Riemann integral
`\[\int_a^b\phi(x)dx:=\sum_{i=1}^nc_i(x_i-x_{i-1})\]`
does not depend on the specific choice of the partition `\(a=x_0 < x_1 < \ldots < x_{n-1} < x_n=b\)`, i.e. for any such partition, the above [sum][bookofproofs$261] takes the same value.

### Case 1

Assume 

`\[\begin{array}{rcl}
S&:=&a=x_0 < x_1 < \ldots < x_{n-1} < x_n=b\\
T&:=&a=t_0 < t_1 < \ldots < t_{m-1} < x_m=b\\
\end{array}
\]`

are two different partitions of the closed interval  `\([a,b]\)` such that 


`\[\begin{array}{rcl}
\phi (x)=c_i\quad&\quad&\text{for all } x\in(x_{i-1},x_i),\quad i=1,\ldots,n,\\
\phi (x)=d_j\quad&\quad&\text{for all } x\in(t_{j-1},t_j),\quad j=1,\ldots,m.\\
\end{array}
\]`

and assume that `\(S\subset T\)`. This means that for each `\(i\)` there is an index `\(j_i\)` such that `\(x_i=t_{j_i}\)`. Then we have 

`\[x_{i-1}=t_{j_{i-1}} < t_{j_{i-1}+ 1}  < t_{j_{i-1}+ 2}  < \ldots <  t_{j_i}=x_i\quad\quad\text{for }1\le i\le n.\]`
and
`\[c_i=d_j\quad\quad\text{for }j_{i-1} < i \le j_i,\quad 1\le i\le n.\]`
It follows
`\[\sum_{i=1}^{n}c_i(x_i-x_{i-1})=\sum_{i=1}^n\sum_{k=j_{i-1}+1}^{j_i}d_k(t_k-t_{k-1}).\]`

In other words, the Riemann integrals with respect to the partitions `\(S\)` and `\(T\)` equal each other. 

### Case 2

Now assume arbitrary partitions `\(S\)` and `\(T\)` and that `\(U=S\cup T\)`. Then we have `\(S\subset U\)` and `\(T\subset U\)`. According to case 1, the Riemann integrals with respect to the partitions `\(S\)` and `\(U\)` equal each other, as well as the Riemann integrals with respect to the partitions `\(T\)` and `\(U\)` equal each other. Thus, the Riemann integrals with respect to the partitions `\(S\)` and `\(T\)` also equal each other. In other words, the Riemann integral of the step function does not depend on the specific choice of the partition.
