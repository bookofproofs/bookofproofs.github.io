layout: proof
categories: branches,algebra
nodeid: bookofproofs$7958
orderid: 0
parentid: bookofproofs$7957
title: 
description:  Proof of RELATIONSHIP BETWEEN THE SOLUTIONS OF HOMOGENEOUS AND INHOMOGENEOUS SLES &#9733; master graduate maths &#10004; visit BookOfProofs now!
references: bookofproofs$7937
keywords: between,homogeneous,inhomogeneous,relationship,sles,solutions,proof
contributors: bookofproofs

---


---

* By hypothesis, `$u_1,\ldots,u_n$` be a solution of the [inhomogeneous system of linear equations][bookofproofs$1044], i.e. `$$\sum_{\nu=1}^n \alpha_{\mu\nu}u_\nu=\beta_\mu\quad\quad\text{ for all }\,\mu=1,\ldots,m.\quad\quad  ( \dagger  )$$`
* The same holds for other solutions (if any) `$w_1,\ldots,w_n$`: `$$\sum_{\nu=1}^n \alpha_{\mu\nu}w_\nu=\beta_\mu\quad\quad\text{ for all }\,\mu=1,\ldots,m.\quad\quad  ( \dagger  \dagger  )$$`
* Therefore, subtracting the equations of both systems `$( \dagger  )$` and `$( \dagger  \dagger  )$` line by line from each other results in `$$\sum_{\nu=1}^n \alpha_{\mu\nu}(u_\nu -w_\nu)=0\quad\quad\text{ for all }\,\mu=1,\ldots,m,$$` which means that `$h_\nu:=u_\nu-w_\nu$` for all `$\nu=1,\ldots,n$` is a solution of the corresponding [homogeneous system][bookofproofs$1044].
* Conversely, if `$h_1,\ldots,h_n$` is __any__ solution of the corresponding homogeneous system, then we have `$$\sum_{\nu=1}^n \alpha_{\mu\nu}h_\nu=0\quad\quad\text{ for all }\,\mu=1,\ldots,m.\quad\quad (\dagger  \dagger  \dagger  )$$`
* Therefore, adding the equations of both systems `$( \dagger \dagger\dagger )$` and `$( \dagger  )$` line by line results in `$$\sum_{\nu=1}^n \alpha_{\mu\nu}(u_\nu + h_\nu)=\beta_\mu\quad\quad\text{ for all }\,\mu=1,\ldots,m,$$` which means that `$w_\nu:=u_\nu+h_\nu$` for all `$\nu=1,\ldots,n$` is a solution of the corresponding [inhomogeneous system][bookofproofs$1044].
* Alltogether, it follows that all solutions of the inhomogeneous system are given by `$w_\nu:=u_\nu\pm h_\nu$` for all `$\nu=1,\ldots,n$`, where `$u_1,\ldots,u_n$` is one of its solutions and `$h_1,\ldots,h_n$` is a solution the corresponding homogeneous system.
