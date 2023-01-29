layout: proof
categories: branches,analysis
nodeid: bookofproofs$6699
orderid: 50
parentid: bookofproofs$6698
title: 
description:  Proof of FUNCTIONS CONTINUOUS AT A POINT AND NON-ZERO AT THIS POINT ARE NON-ZERO IN A NEIGHBORHOOD OF THIS POINT &#9733; master maths &#10004; visit BookOfProofs!
references: bookofproofs$581
keywords: are,continuous,functions,neighborhood,non,point,this,zero,proof
contributors: bookofproofs

---


---

* Let `\(D\)` be a subset of [real numbers][bookofproofs$1105] `\(\mathbb R\)`.
* Let `\(a\in D\)`.
* Let `\(f:D\to\mathbb R\)` be [continuous at `$a$`][bookofproofs$219].
* Let `$f(a)\neq 0.$` 
* We want to show that there exists a real number `$\delta > 0$` such that `$f(x)\neq 0$` for all `$x\in D$` with `$|x-a| < \delta.$`
   * Set `$\epsilon=|f(a)| > 0,$` where `$|f(a)|$` denotes the [absolute value][bookofproofs$583].
   * According to the [$\epsilon-\delta$-definition of continuity at `$a$`][bookofproofs$219], there exists a `$\delta > 0,$`, such that `$|f(x)-f(a)| < \epsilon$`  for all `$x\in D$`  with `$|x-a| < \delta.$` 
   * From `$|f(x)-f(a)| < \epsilon=|f(a)|,$` and the [rules of calculation for inequalities][bookofproofs$594] it follows that `$|f(a)|-|f(x)-f(a)| > 0$`  for all `$x\in D$`  with `$|x-a| < \delta.$` 
   * Thus, `$|f(a)|\ge |f(a)|-|f(x)-f(a)| > 0$` for all `$x\in D$`  with `$|x-a| < \delta.$` 
   * Thus, `$|f(a)| > 0$` for all `$x\in D$`  with `$|x-a| < \delta.$`
   * Thus, `$f(a)\neq  0$` for all `$x\in D$`  with `$|x-a| < \delta.$`
