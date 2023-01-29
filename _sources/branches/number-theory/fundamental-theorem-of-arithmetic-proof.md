layout: proof
categories: branches,number-theory
nodeid: bookofproofs$802
orderid: 50
parentid: bookofproofs$8094
title: 
description:  Proof of FUNDAMENTAL THEOREM OF ARITHMETIC &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: 
keywords: arithmetic,factorized,fundamental,theorem,fundamental theorem of arithmetic,the fundamental theorem of arithmetic,arithmetic fundamental theorem,fundamental theorem of arithmetics,proof
contributors: bookofproofs

---


---

#### Proof of existence

* Let `\(n > 1\)`. 
* According [existence of prime divisors][bookofproofs$8098], we can find a prime divisor `\(p\mid n\)`. 
* In the series of consecutive [prime numbers][bookofproofs$473], `\(p_1=2, p_2=3, \ldots\)`, we also can find an index `\(i\)`, for which we can write `$n=p_{i}^1\cdot n_1,$` with `\(p_i=p\)` and some `\(n_1 < n\)`. 
* Since `\(n\)` was either [composite][bookofproofs$8097] or [prime][bookofproofs$473], we have that `\(n_1 > 1\)` or `\(n_1=1\)`. * In the latter case, we are done. 
* In the first case, `\(n_1\)` is another, non-trivial divisor of `\(n\)`. 
* Repeating the same argument for `\(n_1\)` we will find other prime `\(q\)` and a new divisor `\(n_2 < n_1\)`, whereby we have 
`\[\begin{array}{ccl}
n&=&p_i^2\cdot n_2,\text{ if }q=p_i\text{ or }\\
n&=&p_i\cdot p_j\cdot n_2 \text{ else.}
\end{array}
\]`
* Since `\(n_1\)` was either composite or prime, we have again that `\(n_2 > 1\)` or `\(n_2=1\)`, so we can repeat the above argument. 
* By doing so, we will possibly find even further divisors `\(n_2, n_3,\ldots\)` of `\(n\)` and the corresponding primes `\(p_k\mid n\)`, grouping them by the corresponding powers `\(p_k^{e_k}\)`.
* Obviously, the set of these numbers is a [non-empty][bookofproofs$550] [subset][bookofproofs$552] of [natural numbers][bookofproofs$718].
* Following the [well-ordering principle][bookofproofs$698], the set of all `\(\{n_k\}\)`, `\(k=1,2,\ldots\)`, with all `\(n > n_1 > n_2 >\ldots > 1 \)`, for which we repeat the argument, must have a [minimum][bookofproofs$7995] `\(n_{p} > 1 \)`. 
* By the [corresponding corollary][bookofproofs$801], `\(n_p\)` must be a prime number. 
* Thus, the repetition of the above steps will finally end and we will find a factorization of the form 
`\[n = p_1^{e_1}\cdot p_2^{e_2}\cdot\ldots\cdot p_r^{e_r},\]`
where `\(p_r\)` denotes the biggest prime we have found, the `\(p_1,\ldots p_r\)` denote consecutive primes (i.e. starting with `\(p_1=2, p_2=3,\ldots\)` and ending at `\(p_r\)`), and `\(e_i\)` denote the number of times we have found the prime `\(p_i\)` in the procedure.

#### Proof of Uniqueness 

* Assume that, applying the above procedure more then once, we can find two different factorizations of `\(n\)`:
`\[\begin{array}{cclr} 
n&=&p_1^{e_1}\cdot p_2^{e_2}\cdot\ldots\cdot p_r^{e_r},&~~~~~~~~~~(1)\\
n&=&p_1^{f_1}\cdot p_2^{f_2}\cdot\ldots\cdot p_s^{f_s}.&~~~~~~~~~~(2)
\end{array}
\]`
* Without loss of generality, assume `\(r\ge s\)`. 
* If `\(r > s\)`, then it follows from `\((1)\)` that `\(p_r\mid n\)` and from `\((2)\)` that `\(p_r\not\mid n\)`, which is a [contradiction][bookofproofs$744], because a divisor of `\(n\)` cannot be mutually not a divisor of `\(n\)`.
* By construction, our two factorizations list all consecutive primes, `\(p_1 < p_2 < \ldots < p_r\)`. 
* Thus, it must be `\(r=s\)`. 
* Now, if `\((1)\)` and `\((2)\)` are two different factorizations by hypothesis, then it must be `\(f_i\neq e_i\)` for at least one `\(i\)`. 
* Let, without loss of generality, assume `\(f_i < e_i\)`. 
* Then, from `\((1)\)` it follows that `\(p_i^{e_i}\mid n\)` and from `\((2)\)` that `\(p_r^{e_i}\not\mid n\)`, which is again is a [contradiction][bookofproofs$744], by the same argument. 
* Thus, the two factorizations must be in fact identical.
