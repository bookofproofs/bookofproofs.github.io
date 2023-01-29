layout: definition
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$261
orderid: 50
parentid: bookofproofs$1113
title: Sums
description: SUMS ★ bring your math skills to the graduate level ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$1112
keywords: sum,summands,sums,iverson notation
contributors: bookofproofs


---
The `\(\Sigma\)`-notation was introduced in 1870 by Joseph Fourier.

---

A general **sum** is an expression of the form  
`\[a_1+a_2+\cdots+a_n\]`

where the elements `\(a_k\)` are called the **summands** of the sum. If not stated otherwise, it is assumed, that the terms are elements of a [field][bookofproofs$557]. This could, for instance, be:

* the [field of rational numbers][bookofproofs$1647] `\(\mathbb Q\)`,
* the [field of real numbers][bookofproofs$1638] `\(\mathbb R\)`, or 
* the [field of complex numbers][bookofproofs$1690] `\(\mathbb C\)`.

The [axiom of associativity][bookofproofs$668], which holds in any field, makes sure that the sum is well-defined, i.e. that it does not depend on the order, in which we **add** the respective **summands**. 

But the concept of sums can also be successfully used for all other algebraic structures, in which the axiom of associativity also holds, for instance, rings, groups or even monoids.
 
### The "Three-Dot" Notation 

The three dots "`\(\cdots\)`" in the sum indicate that we have to complete the pattern established by the surrounding terms. For instance, if we write

`\[1 + 2 + \cdots + n\]`

then it means that we sum over all integers from `\(1\)` to `\(n\)`. Sometimes, this notation is ambiguous. For example, if we write

`\[1 + 2 + \cdots + 2^n\]`

this could mean that the sum goes over all integers from `\(1\)` to `\(2^n\)` or that it goes over all powers of `\(2\)`, from `\(2^0\)` to `\(2^n\)`. To avoid such ambiguities, we should then write explicitly

`\[2^0 + 2^1 + \cdots + 2^n\]`

### The Delimited `\(\Sigma\)`-Notation ("Sigma"-Notation)

The Greek letter `\(\Sigma\)` (upper case sigma) is used to write a delimited form of sums. This notation was introduced in 1870 by "Joseph Fourier":https://www.bookofproofs.org/history/jean-baptiste-joseph-fourier/. The sum `\(a_1+a_2+\cdots+a_n\)` can be written as 
`\[\sum_{k=1}^n a_k\quad\quad ( * )\]`
and read "sum over `\(k\)`, from `\(1\)` to `\(n\)`". The terms after  `\(\Sigma\)`  (here `\(a_k\)`) are called the **summands**. The index `\(k\)` is said to be **bound** to the `\(\Sigma\)`  sign, since any other letter could be substituted for `\(k\)` without changing the meaning of `\(( * )\)`:

`\[\sum_{k=1}^n a_k=\sum_{j=1}^n a_j=\sum_{m=1}^n a_m=\cdots.\]`

### The Generalized `\(\Sigma\)`-Notation 

The generalized `\(\Sigma\)`-notation is characterized by writing one or more conditions under the `\(\Sigma\)` sign for the index. For instance, the sum `\( ( * ) \)` can be also written as

`\[\sum_{1\le k\le n} a_k\]`

The generalized  `\(\Sigma\)`-notation is even more useful than the delimited `\(\Sigma\)` notation since it allows to work with sums over index sets that aren't restricted to consecutive integers. For example, the sum

`\[\sum_{
\substack{
1\le k\le 1000 \\
k \text{ odd}
}}k^2\quad\quad( * * )\]`

would be a short-form notation of the sum of all squares of odd positive integers from `\(1\)` to `\(999\)`:
`\[1^2 + 3^2+ 5^2 + \cdots + 997^2 + 999^2 \]`
The equivalent of `\( ( * * )\)` in the delimited notation would be

`\[\sum_k^{499}(2k +1)^2 \]`
which is less clear and more cumbersome. Another advantage of the general notation is that it allows using separate indices running through different domains or with different limits. For example, the sum

`\[\sum_{
\substack{
1\le k\le n \\
0\le j\le m}} a_kb_j\]`
is a sum, the summands of which consist of the terms `\(a_k\)` and `\(b_j\)` depending on the independent indices `\(k\)` and `\(j\)`. 

The probably biggest advantage of the general `\(\Sigma\)`-notation is that it is more easy to manipulate than the delimited form. Consider for example changing the index from `\(k\)` to `\((k+1)\)` in both notations, as shown in the below table:


General Sum Notation  | Delimited Sum Notation
:------------- |:-------------
 `$\sum_{1\le k\le n} a_k=\sum_{1\le k+1\le n} a_{k+1}$` | `$\sum_1^n a_k=\sum_0^{n-1}a_{k+1}$` 

> Comparison of manipulating the index (here shifting the index from `\(k\)` to `\((k+1\)`) in general and delimited sum notations.

The manipulation in the general notation is more simply done than in the delimited form. In the latter, it is harder to see what happened and it is more likely to make a mistake.

### The Iverson-Notation 

Kenneth I. Iverson introduced in his "APL programming language":http://www.jsoftware.com/papers/APL.htm a very useful concept of a **relational statement** `\([\alpha~R~\beta]\)`, which is a __logical variable__ defined by:

`\[[\alpha~R~\beta]:=\cases{1,\quad \alpha R \beta\\0\quad\text{else}}\]`

This concept can be adapted to write sums in the form

`\[\sum_{k}a_k[P(k)],\]`

which allows creating any constraints whatsoever on the index of summation. The attached variable in brackets `\([P(k)]\)` is a logical true-or-false variable and the summands equal

`\[a_k[P(k)]:=\cases{a_k,\text{ if }P(k)\text{ is true for the index }k\\0\quad\text{else}}\]`

This notation is very powerful since it significantly simplifies the manipulation of sums by allowing logical and set operations inside the summation terms. In this notation, the sum `\( ( * * )\)` above would have the form

`\[\sum_{k}k\cdot[(1\le k \le 1000)\wedge (k\text{ odd})]=\sum_{k}k\cdot[1\le k \le 1000]\cdot[k\text{ odd}],\]`
