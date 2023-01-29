layout: proof
categories: branches,analysis
nodeid: bookofproofs$2961
orderid: 50
parentid: bookofproofs$6791
title: 
description: PROOF OF CAUCHY–SCHWARZ INEQUALITY ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$586
keywords: cauchy-schwarz inequality,proof
contributors: bookofproofs

---


---

* By hypothesis, `$x_1,x_2,\ldots x_n$` and `$y_1,y_2,\ldots y_n$` are [real numbers][bookofproofs$1105].
* The estimation is trivial, if all of them equal `$0$` therefore, assume that both [square roots][bookofproofs$1161] `$$A:=\left(\sum _{i=1}^{n}x_{i}^{2}\right)^{\frac 12},\quad B:=\left(\sum _{i=1}^{n}y_{i}^{2}\right)^{\frac 12}$$`
are [positive][bookofproofs$1107].
* Set `$a_i:=\frac{|x_i|}A$`, `$b_i:=\frac{|y_i|}B,$` where `$|x_i|$` and `$|y_i|$` denote the respective [absolute values][bookofproofs$583] of `$x_i$` and `$y_i$` for `$i=1,\ldots,n.$` 
* Dividing by `$AB$` and applying the [6th rule of calculations with inequalities][bookofproofs$594] the inequality 
`$$\sum _{i=1}^{n}|x_{i}y_{i}|\leq \left(\sum _{i=1}^{n}x_{i}^{2}\right)^{\frac 12}\left(\sum _{i=1}^{n}y_{i}^{2}\right)^{\frac 12}$$`
is equivalent to `$$\sum _{i=1}^{n}a_{i}b_{i}=\sum _{i=1}^{n}\frac{|x_{i}|}A\frac{|y_{i}|}B\leq 1.$$`
* Since by definition `$a_ib_i > 0$`, we have `$a_ib_i=\sqrt{a_i^2b_i^2}.$` 
* Because `$0\le \left(\sqrt{a_i^2}-\sqrt{b_i^2}\right)^2=a_i^2-2\sqrt{a_i^2b_i^2}+b_i^2$` for all `$i=1,\ldots,n$` we have `$$\sqrt{a_i^2b_i^2}\le \frac{a_i^2}2+\frac{b_i^2}2,\quad i=1,\ldots,n.$$`
* Therefore, we have `$$\sum _{i=1}^{n}a_{i}b_{i}\le \sum _{i=1}^{n}\left(\frac{a_i^2}2+\frac{b_i^2}2\right)=\frac 12\left(\sum _{i=1}^{n} a_i^2+\sum _{i=1}^{n}b_i^2\right)=\frac 12(1+1) = 1.$$`
