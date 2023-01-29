layout: proof
categories: branches,combinatorics
nodeid: bookofproofs$999
orderid: 50
parentid: bookofproofs$998
title: By Induction
description: PROOF BY INDUCTION Proof of NUMBER OF SUBSETS OF A FINITE SET &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$977
keywords: finite set subsets,subsets of a finite set,proof
contributors: bookofproofs

---


---

If `\(X\)` is a [finite set][bookofproofs$985] with `\(|X|=n\)`, then following the [definition of binomial coefficients][bookofproofs$993] the number of its subsets `\(X_i\subseteq X\)` must be

`\[|\{X_i,~X_i\subseteq X\}|=\sum_{k=0}^n \binom nk~~~~~~~~~~~~~~~~~~~~( * ).\]`

Moreover, we observe some special cases.

#### Special case `\(n=0\)`.

Since `\(X=\emptyset\)`, there is **only one** subset `\(X_i\subseteq\emptyset\)`, namely `\(X_i=\emptyset\)`, thus `\(|\{X_i,X_i\subseteq \emptyset\}|=1=2^0\)`.

#### Special case `\(n=1\)`.

Let `\(S=\{a\}\)`. Then there are **two** subsets `\(X_i\subseteq\{a\}\)`, namely `\(\{\emptyset\}\)` and `\(\{a\}\)`, thus `\(|\{X_i,X_i\subseteq \{a\}\}|=2=2^1\)`.

#### Special case `\(n=2\)`.

Let `\(X=\{a,b\}\)`. Then there are **four** subsets `\(X_i\subseteq\{a,b\}\)`, namely `\(\{\emptyset\}\)`, `\(\{a\}\)`, `\(\{b\}\)`, and `\(\{a,b\}\)`, thus `\(|\{X_i,X_i\subseteq \{a,b\}\}|=4=2^2\)`.

#### Special case `\(n=3\)`.

Let `\(X=\{a,b,c\}\)`. Then there are **eight** subsets `\(X_i\subseteq\{a,b,c\}\)`, namely `\(\{\emptyset\}\)`, `\(\{a\}\)`, `\(\{b\}\)`, `\(\{c\}\)`, `\(\{a,b\}\)`, `\(\{b,c\}\)`, `\(\{a,c\}\)`, and `\(\{a,b,c\}\)`, thus `\(|\{X_i,X_i\subseteq \{a,b,c\}\}|=8=2^3\)`.

The above special cases suggest that the general formula is 
`\[|\{X_i,X_i\subseteq X\}|=2^{|X|}.\]`
Comparing this with the formula `\(( * )\)`, we conjecture for `\(|X|=n\)`, `\(n\ge 0\)` that  
`\[|\{X_i,X_i\subseteq X\}|=\sum_{k=0}^n \binom nk=2^n~~~~~~~~~~~~~~~~~~~~( * * ),\]`
and prove the formula `\(( * * )\)` by [induction][bookofproofs$657].
#### Base Case (see also special case `\(n=0\)` above)

`\[\sum_{k=0}^0\binom nk=\binom 00=2^0=1.\]`

#### Induction step: Let `\(( * * )\)` be proven for all `\(n\ge 0\)`. 

Then

`\[\begin{array}{ccl}
\sum_{k=0}^{n+1}\binom {n+1}k&=&\binom {n+1}0+\sum_{k=1}^{n+1}\binom {n+1}k~~~~~~~~~~~~~~~~~( *** )\\
&=&1+\sum_{k=1}^{n}\left(\binom nk+\binom n{k-1}\right)~~~~~~~~~~~~~~~~~( **** )\\
&=&1+\left(-1+\sum_{k=0}^{n}\binom nk\right)+\left(\sum_{j=0}^{n}\binom n{j}\right)~~~~~~~~~~~~~~~~~( ***** )\\
&=&2^n+2^n=2\cdot 2^n=2^{n+1}~~~~~~~~~~~~~~~~~( ****** ).\\
\end{array}\]`

Thereby, in `\( ( *** ) \)` we have split the sum into the first term `\(\binom{n+1}0\)` from the rest of the sum, which equals `\(1\)`, since there is only one subset with the cardinality `\(0\)` (i.e. `\(\emptyset\)`) of any set `\(X\)` with the cardinality `\(n+1\)`.
In `\( ( **** ) \)` we have applied the [recursive formula for binomial coefficients][bookofproofs$994].
In `\( ( ***** ) \)` we have included in the first sum the term `\(\binom n0\)` which equals `\(1\)`. By doing so, we corrected this inclusion by `\(-1\)`, which cancels with the `\(+1\)` included in the previous step. We also have shifted the index of the second, replacing `\(k-1\)` by `\(j=k-1\)`.
In `\( ( ****** ) \)` we have performed the induction step.
