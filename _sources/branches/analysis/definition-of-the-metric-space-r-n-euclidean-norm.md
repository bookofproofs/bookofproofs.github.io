layout: proposition
categories: branches,analysis
nodeid: bookofproofs$1206
orderid: 600
parentid: bookofproofs$29
title: Definition of the Metric Space `\(\mathbb R^n\)`, Euclidean Norm
description: DEFINITION OF THE METRIC SPACE R^N, EUCLIDEAN NORM &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$582
keywords: definition,euclidean,euclidean distance,metric,norm,space
contributors: bookofproofs

---


---

Let `\(n\)` be a [natural number][bookofproofs$718]. The [cartesian product][bookofproofs$738] of the `\(n\)` [sets of real numbers][bookofproofs$1105].
`\[\mathbb R^n:=\underbrace{\mathbb R\times \mathbb R\times\cdots\times \mathbb R}_{n\text{ times}}.\]`  

constitutes a [vector space][bookofproofs$560] over `\(\mathbb R\)`, also called the **Euclidean vector space** of dimension `\(n\)`, and denoted by `\(\mathbb R^n\)`. It means that:

1. `\((\mathbb R^n, + )\)` is an [Abelian group][bookofproofs$553].
1. For `\(\alpha,\beta\in \mathbb R\)` and `\(x,y\in \mathbb R^n\)` the following axioms of scalar multiplication hold:
#1. `\((\alpha + \beta) x=\alpha x + \beta x\)`,
#1. `\(\alpha(x + y)=\alpha x + \alpha y\)`, 
#1. `\((\alpha\beta) x=\alpha (\beta x)\)`,
#1. `\(1\cdot x=x\)`.

With the 
`\[\text{vector addition "+"}:=\pmatrix{
x_{1}\cr
x_{2}\cr
\vdots \cr
x_{n} \cr
}+\pmatrix{
y_{1}\cr
y_{2}\cr
\vdots \cr
y_{n} \cr
}=\pmatrix{
x_{1}+y_1\cr
x_{2}+y_2\cr
\vdots \cr
x_{n}+y_n \cr
}
\]`
`\[\text{and scalar multiplication "}\cdot\text{"}:=\alpha\cdot\pmatrix{
x_{1}\cr
x_{2}\cr
\vdots \cr
x_{n} \cr
}=\pmatrix{
\alpha\cdot x_{1}\cr
\alpha\cdot x_{2}\cr
\vdots \cr
\alpha\cdot x_{n} \cr
}
\]`


We consider the [dot product][bookofproofs$1049] `\(\langle x,y\rangle:=x_1y_1 + x_2y_2 + \ldots + x_ny_n\)` of two vectors `\(x=(x_{1},\ldots,x_{n})^T\)` and `\(y=(y_{1},\ldots,y_{n})^T\)` in `\(\mathbb R^n\)`.  The **Euclidean norm** of any vector `\(x\in\mathbb R^n\)` is defined as the [square root][bookofproofs$1161] of the dot product of `\(x\)` with itself:

`\[||x||:=\sqrt{\langle x,x\rangle}=\sqrt{x_1^2+\ldots+x_n^2}.\]`

The **Euclidean distance** of any two vectors `\(x,y\in\mathbb R^n\)` is the Euclidean norm of the difference of these vectors:

`\[d(x,y)=||x-y||:=\sqrt{\langle x-y,x-y\rangle}=\sqrt{(x_1-y_1)^2+\ldots+(x_n-y_n)^2}.\]`

Together with the distance defined as above, the pair `\((\mathbb R^n,d)\)` constitutes a [metric space][bookofproofs$617].
Together with the norm defined as above, the pair `\((\mathbb R^n,||~||)\)` constitutes a [normed vector space][bookofproofs$846].