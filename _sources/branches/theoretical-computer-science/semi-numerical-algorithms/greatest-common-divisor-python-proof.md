layout: proof
categories: branches,theoretical-computer-science, semi-numerical-algorithms
nodeid: bookofproofs$1286
orderid: 50
parentid: bookofproofs$503
title: 
description:  Proof of GREATEST COMMON DIVISOR PYTHON &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$701,bookofproofs$1272
keywords: common,divisor,greatest,python,proof
contributors: bookofproofs

---


---

We want to show that if `\(a\)`, `\(b\)` are [integers][bookofproofs$844], with `\(a\neq 0\)` or `\(b\neq \)`. The algorithm calculates correctly the greatest common divisor of `\(a\)` and `\(b\)`.

* If `\(a=0\)` and `\(b=0\)`, then the algorithm returns `\(0\)` which is correct, since `\(0\)` is the only integer, which is divisible by all common divisors of `\(0\)` and `\(0\)`, i.e. all integers `\(t\neq 0\)`. This fulfills the properties of the [greatest common divisor][bookofproofs$1280].
* So let `\(a\neq 0\)` or `\(b\neq 0\)`. 
* It is possible to remove the sign by setting `\(a=|a|\)` and `\(b=|b|\)` at the beginning of the algorithm, since for any divisor `\(d\mid -a\)` it holds that `\(d\mid a\)` and thus we can assume positive integers.
* Let, without loss of generality, `\(a\ge b\)`. 
* If `\(b=0\)`, the algorithm returns `\(a\)`, which equals `\(\gcd(a,0)\)` for all `\(a\in\mathbb N\)`. 
* Now, assume that `\(b > 0\)`. 
* According to [Euclid's lemma about the division with quotient and remainder][bookofproofs$818], we find a [monotonically decreasing sequence][bookofproofs$1155] of natural numbers `\[r_0=b > r_1 > r_2 > \ldots > r_{n-1} > r_n\]` defined by

`\[\begin{array}{rclclcl}
a & = & q_0\cdot b & + & r_1 & \text{with} & 0  < r_1 < b\\
b & = & q_1\cdot r_1 & + & r_2 & \text{with} & 0 < r_2 < r_1\\
r_1 & = & q_2\cdot r_2 & + & r_3 & \text{with} & 0 < r_3 < r_2\\
&\vdots&\\
r_{n-3} & = & q_{n-2}\cdot r_{n-2} & + & r_{n-1} & \text{with} & 0 < r_{n-1} < r_{n-2}\\
r_{n-2} & = & q_{n-1}\cdot r_{n-1} & + & r_{n} & \text{with} & 0 < r_{n} < r_{n-1}\\
r_{n-1} & = & q_{n}\cdot r_{n}
\end{array}\]`

* From the [connection between quotient, remainder, the modulo operation and the floor function][bookofproofs$1284], we can re-write the above calculation scheme  without changing its meaning and get:

`\[\begin{array}{rclclcl}
a & = & q_0\cdot b & + & a\mod b & \text{with} & 0 < r_1 < b\\
b & = & q_1\cdot r_1 & + & b\mod r_1 & \text{with} & 0 < r_2 < r_1\\
r_1 & = & q_2\cdot r_2 & + & r_1\mod r_2 & \text{with} & 0 < r_3 < r_2\\
&\vdots&\\
r_{n-3} & = & q_{n-2}\cdot r_{n-2} & + & r_{n-3}\mod r_{n-2} & \text{with} & 0 < r_{n-1} < r_{n-2}\\
r_{n-2} & = & q_{n-1}\cdot r_{n-1} & + & r_{n-2}\mod r_{n-1} & \text{with} & 0  < r_{n} < r_{n-1}\\
r_{n-1} & = & q_{n}\cdot r_{n}
\end{array}\quad\quad ( * )\]`

* Since the program begins with the assignment `\(r:=b\)`, exactly the above calculation steps are represented by the commands inside the `\(\mathtt{WHILE}\)` loop `\[\begin{array}{l}
r:= a\mod b;\\
 a:= b;\\
b:=r
\end{array}\]`

* If `\(r_1=0\)`, then the algorithm stops and returns `\(\gcd(a,b)=b\)`, which is correct, since in this case `\(b\mid a\)`. * Otherwise the loop is repeated. 
* Since the set of all `\(r_i\)`, `\(i=0,1,2,\ldots\)` calculated that way is a non-empty set of natural numbers, it has a smallest element. 
* By virtue of the [well-ordering principle][bookofproofs$698], the `\(\mathtt{WHILE}\)` loop must always terminate, i.e. the index `\(n\)` is well-defined as the last index, for which `\(r_{n}\neq 0\)`.
* From the [divisibility laws][bookofproofs$508] it follows for any common divisor `\(t\)` of `\(a\)` and `\(b\)` that 
`\[t\mid a\wedge t\mid b\Longrightarrow t\mid r_{i}\wedge t\mid r_{i+1}\text{ for }i=0,\ldots,n\]`

* Therefore, `\(t\mid r_n\)`, and this is true for any __arbitrary  common divisor__ `\(t\)` of `\(a\)` and `\(b\)`. Moreover, from the last equation of `\( ( * ) \)` we have that  `\(r_n\mid r_{n-1}\)`, from the secont to last equotion that  `\(r_{n-1}\mid r_{n-2}\)`, etc. 
* Again because the [divisibility laws][bookofproofs$508] (in particular the transitivity of divisibility), we have that `\(r_n\mid a\)` and `\(r_n\mid b\)`. Thus, `\(r_n\)` fulfills [both defining properties of the greatest common divisor][bookofproofs$1280] and we have `\[r_n=\gcd(a,b).\]`
