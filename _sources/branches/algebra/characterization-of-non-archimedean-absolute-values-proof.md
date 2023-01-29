layout: proof
categories: branches,algebra
nodeid: bookofproofs$8668
orderid: 50
parentid: bookofproofs$8667
title: 
description: PROOF OF CHARACTERIZATION OF NON-ARCHIMEDEAN ABSOLUTE VALUES ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$6735
keywords: characterization of non-archimedean absolute values,proof
contributors: bookofproofs

---


---

In the following prove, `$(F,+,\cdot)$` is a [field][bookofproofs$557].
### Ad `$(1)$`

* Assume, `$|\cdot|$` is a [non-archimedean absolute value][bookofproofs$8659] on `$F.$`
* Then `$|1|=1$` and by the forth axiom of non-archimedean absolute value, `$|2|=|1+1|\le\max(|1|,|1|)=1,$` `$|3|=|1+1+1|\le\max(|2|,|1|)=1.$`
* [By induction][bookofproofs$657], we get `$|n|\le 1.$`

### Ad `$(2)$`

* Assume, there is a constant `$C$` with `$|n|\le C,$` where `$n=\underbrace{1+\ldots+1}_{n\text{ times}},$` `$1\in F.$`
* Then, for fixed `$x,y\in F,$` we get with the [binomial theorem][bookofproofs$1397].
`$$|(x+y)^n|=\left|\sum_{k=0}^n{n\choose k}x^{n-k}y^k\right|\le nC\max(|x|,|y|)^n,$$`
in which, by abuse of notation, we regard `$n$` also as a [natural number][bookofproofs$718].
* Taking `$n$`-th [roots][bookofproofs$46] on both sides a letting `$n$` [tend to infinity][bookofproofs$1345], we get by the standard results from analysis ([limit of nth root of n][bookofproofs$6724] and [limit of the nth root of a positive constant][bookofproofs$6709]), we get `$$|x+y|\le\max (|x|,|y|).$$`
* It follows that `$|\cdot|$` is [non-archimedean][bookofproofs$8659].
