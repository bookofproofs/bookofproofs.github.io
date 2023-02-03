layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$8357
orderid: 50
parentid: bookofproofs$8356
title: 
description: PROOF OF ABELIAN PARTIAL SUMMATION METHOD &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$586
keywords: abelian partial summation,partial summation method,abelian summation method,abelian summation by parts,proof
contributors: bookofproofs

---


---

* By hypothesis, `$a_1,\ldots,a_n$` and `$b_1,\ldots,b_n,b_{n+1}$` are given elements of a [unit ring][bookofproofs$683] `$(R,+,\cdot).$` 
* By setting `$A_0:=0$` and `$A_k:=\sum_{i=1}^k a_i,$` we get `$a_k=A_k-A_{k-1}$` for `$k=1,\ldots,n.$`
* Thus, it follows 
   * `$\sum_{k=1}^n a_kb_k=\sum_{k=1}^n(A_k-A_{k-1})b_k$` by definition of `$A_k,$`
   * `$=\sum_{k=1}^n A_kb_k-\sum_{k=1}^n A_{k-1}b_k$` by [distributive law for sums][bookofproofs$1114],
   * `$=\sum_{k=1}^n A_kb_k-\sum_{k=0}^{n-1} A_{k}b_{k+1}$` by replacing the summation index in the second term,
   * `$=\sum_{k=1}^n A_kb_k-\sum_{k=1}^{n-1} A_{k}b_{k+1}$` because `$A_0=0,$` 
   * `$=\sum_{k=1}^n A_kb_k-\sum_{k=1}^{n} A_{k}b_{k+1}+A_nb_{n+1}$`  because `$0=-A_nb_{n+1}+A_nb_{n+1},$` 
   * `$=\sum_{k=1}^n A_k(b_k-b_{k-1})+A_nb_{n+1}$` applying distributive law for sums again.
