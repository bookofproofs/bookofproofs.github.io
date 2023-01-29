layout: proof
categories: branches,geometry,analytic-geometry
nodeid: bookofproofs$7981
orderid: 50
parentid: bookofproofs$7980
title: 
description:  Proof of PRESENTATION OF A STRAIGHT LINE IN A PLANE AS A LINEAR EQUATION &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$7937
keywords: equation,line,linear,plane,presentation,straight,proof
contributors: bookofproofs

---


---

By assumption, `$L$` is a [straight line][bookofproofs$7961] in the [number plane][bookofproofs$7959] `$\mathbb R^2.$`

#### `$L$` through the origin / homogenous equation

* "$\Rightarrow$" Let `$L$` go through the origin.
   * By a [previous lemma][bookofproofs$7962], a parameterized description of `$L$` using two vectors does not depend on a specific choice of these vectors.
   * Therefore, without loss of generality, we can choose the zero vector `$\overrightarrow{OO}$` as the starting vector and an arbitrary point (but not the origin itself) `$A\in L$` with the coordinates `$A=(a_1,a_2)$` as a valid parameterized description of `$L:=\{P\in\mathbb R^2:\;\overrightarrow{OP}=\overrightarrow{OO}+t\cdot \overrightarrow{OA}=t\cdot \overrightarrow{OA}=(t a_1,t a_2),\; t\in \mathbb R\}.$`
   * Consider the set of points `$S:=\{(x_1,x_2)\in\mathbb R^2:\;(x_1,x_2)\text{ solve }a_2x_1-a_1x_2=0.\}$`
   * It follows that `$L\subseteq S,$` since `$a_2\cdot t a_1-a_1\cdot t a_2=0$` for all `$t\in\mathbb R.$`
   * Thus, `$L$` is a solution of some homogenous equation.
* "$\Leftarrow$" Let `$L$` be the solution of a homogenous equation `$\alpha_1x_1+\alpha_2x_2=0$`.
   * To keep notation and the proof simple, we choose without loss of generality `$\alpha_1:=a_2$` and `$\alpha_2:=-a_1$` for some coordinates of a point `$A=(a_1,a_2)$` which is not the origin.
   * Since `$A$` was not the origin, not both `$a_1,a_2$` can be zero.
   * Assume `$a_1\neq 0.$` In this case a pair of numbers `$(x_1,x_2)$` solves the equation `$a_2x_1-a_1x_2=0$` if and only if `$x_2=\frac {a_2}{a_1}x_1.$` This means that `$S$` is a straight line with the parameterized description `$S=\{Q\in\mathbb R^2:\;\overrightarrow{OQ}=(t,t\frac{a_2}{a_1}), t\in \mathbb R\}.$` This is a straight line going through the origin and the point `$A=(a_1,a_2)$` (for `$t=a_1$`). Thus, by a [previous lemma][bookofproofs$7962], `$S=L$`.
   * Now assume `$a_1=0.$` In this case `$a_2\neq 0$` and `$a_2x_1=0$` holds only if `$x_1=0$`. Therefore, `$S=\{Q\in\mathbb R^2:\;\overrightarrow{OQ}=(0,t a_2), t\in \mathbb R\}.$` Again, this is a straight line going through the origin and the point `$A=(0,a_2)$` (for `$t=1$`). Again, [previous lemma][bookofproofs$7962] shows that we must have `$S=L$`.
   * Altogether, `$L$` goes through the origin if and only if it equals the set `$S$` of solutions of some [homogenous linear equation][bookofproofs$1043] `$\alpha_1x_1+\alpha_2x_2=0$`  (here with `$\alpha_1:=a_2$` and `$\alpha_2:=-a_1.$`)

#### `$L$` not through the origin / inhomogenous equation

*  "$\Rightarrow$" Let `$L$` do not go through the origin.
   * Assume, that `$L$` goes through two points `$A=(a_1,a_2)$` and `$B=(b_1,b_2)$` and that we have the parameterized description `$L:=\{P\in\mathbb R^2:\;P:=(b_1,b_2) + (t a_1,t a_2),\; t\in \mathbb R\}.$`
   * We have just proven that if `$L_0:=\{Q\in\mathbb R^2:\;Q:=(t a_1,t a_2),\; t\in \mathbb R\}$`, then `$L_0$` is a straight line going through the origin and solving the homogenous linear equation `$a_2x_1-a_1x_2=0.$`
   * Therefore, `$L=\{(b_1,b_2)+(t x_1,t x_2):\;a_2x_1-a_1x_2=0\}=\{(y_1,y_2):\; a_2y_1-a_1y_2=a_2b_1-a_1b_2\}.$`
   * Since both, `$A$` and `$B$`, are not origin, we have `$\beta:=a_2b_1-a_1b_2\neq 0.$`
   * Thus, `$L$` is a solution of some inhomogenous equation.
* "$\Leftarrow$" Let `$L$` be the solution of an inhomogenous equation `$\alpha_1x_1+\alpha_2x_2=\beta$` with `$\beta\neq 0.$`
   * We have seen that if `$A=(a_1,a_2)$` is not the origin and lies on `$L$` then we can find a straight line `$L_0$` going through the origin and `$A$` and solving the homogenous equation `$a_2x_1-a_1x_2=0.$`
   * Since `$A$` lies also on `$L$`, we have  by assumption `$a_2b_1-a_1b_2=\beta$` for some point `$B=(b_1,b_2)$`.
   * Since `$\beta\neq 0$` and `$A$` is not the origin, we have that `$B$` is also not the origin.
   * Moreover, `$B\neq A$` (otherwise  `$a_2a_1-a_1a_2=0.$`)
   * Thus, `$L$` is a straight line going through two points `$A$` and `$B$`, both not being the origin and the lines `$L_0$` and `$L$` meet at the point `$A$`.
   * Assume `$L$` went through `$A$` and the origin, like `$L_0$` does. Then from the [existence and uniqueness of a straight line through two points][bookofproofs$7964] it would follow that `$L$` and `$L_0$` are identical, in [contradiction][bookofproofs$744] with `$\beta\neq 0$`. 
   * It follows that `$L$` does not go through the origin.
