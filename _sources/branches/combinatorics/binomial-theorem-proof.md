layout: proof
categories: branches,combinatorics
nodeid: bookofproofs$1398
orderid: 50
parentid: bookofproofs$1397
title: By Induction
description:  Proof of BINOMIAL THEOREM &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$581
keywords: binomial theorem,proof
contributors: bookofproofs

---


---

Let `\(x,y\in R\)` and let `\((R,+,\cdot)\)` be a [ring][bookofproofs$683].
The proof is by [complete induction][bookofproofs$657] by the [natural number][bookofproofs$718]  `\(n\)`.

### `\((1)\)` Base case `\(n=0\)` 

Because `\((x+y)^0=1\)` and `\(\sum_{k=0}^0{0\choose k}x^{n-k}y^k={0\choose 0}x^{0}y^0=1\)`, it is true that 
`\[(x+y)^0=\sum_{k=0}^0{0\choose k}x^{n-k}y^k.\]`

### `\((2)\)` Induction step `\(n\to n+1\)` 

`\[\begin{array}{rcl}
(x+y)^{n+1}&=&(x+y)^n(x+y)\\
&=&\left(\sum_{k=0}^n{n\choose k}x^{n-k}y^k\right)(x+y)\\
&=&\sum_{k=0}^n{n\choose k}x^{n+1-k}y^k + \sum_{k=0}^n{n\choose k}x^{n-k}y^{k+1}\quad\quad\text{(distributivity and associativity laws in }R\text{)}\\
&=&\left(x^{n+1}+\sum_{k=1}^n{n\choose k}x^{n+1-k}y^k\right) + \left(\sum_{k=0}^{n-1}{n\choose k}x^{n-k}y^{k+1}+y^{n+1}\right)\quad\quad\text{(separation of terms from both sums)}\\
&=&\left(x^{n+1}+\sum_{k=1}^n{n\choose k}x^{n+1-k}y^k\right) + \left(\sum_{k=1}^{n}{n\choose {k-1}}x^{n-(k-1)}y^{k}+y^{n+1}\right)\quad\quad\text{(change of index in second sum)}\\
&=&x^{n+1}+\sum_{k=1}^n\left({n\choose k}+{n\choose {k-1}}\right)x^{n+1-k}y^k+y^{n+1}\quad\quad\text{(distributivity and associativity laws in }R\text{)}\\
\end{array}\]`

Now, it follows from the [recursive formula for binomial coefficients][bookofproofs$994] that

`\[\begin{array}{rcl}
x^{n+1}+\sum_{k=1}^n\left({n\choose k}+{n\choose {k-1}}\right)x^{n+1-k}y^k+y^{n+1}&=&\binom {n+1}0x^{n+1}+\sum_{k=1}^n\binom{n+1}{k}x^{n+1-k}y^k+\binom {n+1}{n+1}y^{n+1}\\
&=&\sum_{k=0}^{n+1}\binom{n+1}{k}x^{n+1-k}y^k.
\end{array}\]`
