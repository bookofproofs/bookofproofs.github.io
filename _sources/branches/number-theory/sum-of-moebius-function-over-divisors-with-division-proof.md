layout: proof
categories: branches,number-theory
nodeid: bookofproofs$3246
orderid: 50
parentid: bookofproofs$3247
title: 624 BC
description: PROOF OF SUM OF MöBIUS FUNCTION OVER DIVISORS WITH DIVISION &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: 
keywords: division,divisors,function,moebius,over,sum,proof
contributors: bookofproofs

---


---

* Let `$n$` be a [natural number][bookofproofs$718] with the [factorization][bookofproofs$803] `$\prod_{k=1}^r p_k^{e^k}.$`
* With the [elementary symmetric functions][bookofproofs$8151], we have
`$$\begin{array}{rcll}\prod_{k=1}^r\left(1-\frac 1{p_k}\right)&=&1^r+(-1)^1\Sigma_11^{r-1}+(-1)^2\Sigma_21^{r-2}+\ldots+(-1)^{r-1}\Sigma_{r-1}1+(-1)^{r}\Sigma_r\\
&=&1-\Sigma_1+\Sigma_2-\ldots+(-1)^{r-1}\Sigma_{r-1}+(-1)^{r}\Sigma_r&( * )
\end{array}$$`
* The coefficients `$\Sigma_1,\ldots,\Sigma_r$` are given by the [sums][bookofproofs$261].
`$$\begin{array}{rcl}
\Sigma_1(a_1,\ldots,a_r)&:=&\sum_{1\le k\le r}\frac {1}{p_k}\\\
\Sigma_2(a_1,\ldots,a_r)&:=&\sum_{1\le k < l\le r}\frac {1}{p_kp_l}\\
\Sigma_3(a_1,\ldots,a_r)&:=&\sum_{1\le k < l < m\le r}\frac {1}{p_kp_lp_m}\\
\vdots&&\\
\Sigma_r(a_1,\ldots,a_r)&:=&\frac {1}{p_1\cdots p_r}\\
\end{array}$$`
* The number `$1$` in the sum `$( * )$`  and the nominators of the summands `$\Sigma_1,\ldots,\Sigma_r$` correspond exactly to the [square-free][bookofproofs$8116] [divisors][bookofproofs$700] `$d\mid p_1\cdots p_r$` with `$d \ge 1,$` grouped by the increasing number `$\rho$` of primes dividing `$d$`, i.e. `$\rho=0,1,2,\ldots,r.$`
* The signs of the summands in `$( * )$` correspond exactly to the values of the [Möbius function][bookofproofs$8116] for these square-free divisors, which only depend on the number of distinct prime factors `$\rho$` and equals `$\mu(d)=(-1)^\rho.$` 
* Therefore, we have 
`$$\prod_{k=1}^r\left(1-\frac 1{p_k}\right)=\sum_{d\mid p_1\cdots p_r}\frac{\mu(d)}{d}.$$`
* Since, by definition, `$\mu(d)=0$` for all non-square-free `$d$`, we can complement the sum by those divisors and get the required result
`$$\prod_{k=1}^r\left(1-\frac 1{p_k}\right)=\sum_{d\mid n}\frac{\mu(d)}{d}.$$`
