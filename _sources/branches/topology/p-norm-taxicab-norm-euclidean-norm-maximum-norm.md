layout: proposition
categories: branches,topology
nodeid: bookofproofs$6789
orderid: 50
parentid: bookofproofs$846
title: p-Norm, Taxicab Norm, Euclidean Norm, Maximum Norm
description: P-NORM, TAXICAB NORM, EUCLIDEAN NORM, MAXIMUM NORM ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$581
keywords: euclidean,maximum,norm,p-norm,taxicab,taxicab norm,taxi cab norm,p norm,euclidean norm,euclidian norm,maximum norm,norm p,p-norms,taxicab norm proof
contributors: bookofproofs

---


---

A generalization of the [Euclidean Norm][bookofproofs$1206] is defined by the *p-norm*. Let `$p$` be a [real number][bookofproofs$1105] `$\ge 1$`. Let `$x=(x_1,x_2,\ldots x_n)$` be a [vector][bookofproofs$560] of a vector space `\(V\)` over the [field of real numbers][bookofproofs$1638] `\(\mathbb R\)` or the [field of complex numbers][bookofproofs$1690] `\(\mathbb C\)`.

The *p-norm* of `$x$` is defined by 

`$$||x||_p:=\left(\sum_{\nu=1}^n|x_\nu|^p\right)^{1/p}.$$`

### Special Cases

* `$p=1$`: **taxicab norm** `$$||x||_1:=\sum_{\nu=1}^n|x_\nu|.$$`
* `$p=2$`: **Euclidean Norm** `$$||x||_2:=\sqrt{\sum_{\nu=1}^n|x_\nu|^2}.$$`
* `$p=3$`: *3-Norm* `$$||x||_3:=\sqrt[ 3 ]{\sum_{\nu=1}^n|x_\nu|^3}.$$`
* ...
* `$p\to\infty$`: **maximum norm** `$$||x||_\infty:=\max_{\nu} |x_\nu|.$$`

The p-norm can be visualized for two dimensional vectors `$x=(x_1,x_2)$` as follows: The below figure shows some unity circles (i.e. the values of coordinates `$(x_1,x_2)$`, for which the p-norm `$||x||_p$` takes the value `$1$`):


![vector-p-norms](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/vector-p-norms.png?raw=true) 

From Wikimedia by Quartl
