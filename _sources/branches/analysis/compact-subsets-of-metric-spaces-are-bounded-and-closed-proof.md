layout: proof
categories: branches,analysis
nodeid: bookofproofs$6590
orderid: 50
parentid: bookofproofs$6589
title: 
description:  Proof of COMPACT SUBSETS OF METRIC SPACES ARE BOUNDED AND CLOSED &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$582
keywords: compact sets are bounded and closed,bounded and closed,compact,closed,proof
contributors: bookofproofs

---


---

Let `\(A\)` be a [compact][bookofproofs$6575] [subset][bookofproofs$552] of a [metric space][bookofproofs$617] `\((X,d)\)`.
* We have to show that `$A$` is [bounded][bookofproofs$6574].
   * Choose an arbitrary point `$a\in X$`.
   * Note that `$X=\bigcup_{n=1}^\infty B(a,n)$`, where `$B(a,n)$` denotes the [open ball][bookofproofs$849] with the center `\(a\)` and radius `\(n\)`. 
   * Thus, `$\left(B(a,n)\right)_{n\ge 1}$` is an [open cover][bookofproofs$150] of `$A$`.
   * Since `$A$` is [compact][bookofproofs$6575], there is a finite subcover with indices `\(n_1,n_2,\ldots, n_k\)` such that `$$A\subset\bigcup_{j=1}^k B(a,n_j).$$`
   * Take `$n=\max(n_1,n_2,\ldots, n_k)$` and we have `$A\subset B(a,n)$`.
   * This means that `$A$` is [bounded][bookofproofs$6574].
* We have to show that `$A$` is [closed][bookofproofs$852].
   * Choose an arbitrary point `$x\in X\setminus A$`.
   * For `\(n\ge 1\)` set `$$U_n:=\left\{y\in X:~d(y,x) > \frac 1n\right\}.$$`
   * By definition, `$U_n$` is [open][bookofproofs$852] and we have 
`$$\bigcup_{n=1}^\infty U_n=X\setminus \{x\}\supset A,$$`
i.e. we have found an [open cover][bookofproofs$150] of `$A$`.
   * Since `$A$` is [compact][bookofproofs$6575], there is a finite subcover with indices `\(n_1,n_2,\ldots, n_k\)` such that `$$A\subset\bigcup_{j=1}^k U_{n_j}.$$`
   * Take `$n=\max(n_1,n_2,\ldots, n_k)$` and we have `$$B\left(x,\frac 1n\right)\subset X\setminus A.$$`
   * This means that `$X\setminus A$` is [open][bookofproofs$852].
   * It follows that `$A$` is [closed][bookofproofs$852].