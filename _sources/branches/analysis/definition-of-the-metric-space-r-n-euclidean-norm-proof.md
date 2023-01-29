layout: proof
categories: branches,analysis
nodeid: bookofproofs$1207
orderid: 50
parentid: bookofproofs$1206
title: 
description:  Proof of DEFINITION OF THE METRIC SPACE \\MATHBB R^N\, EUCLIDEAN NORM &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$582
keywords: definition,euclidean,euclidean distance,metric,norm,space,proof
contributors: bookofproofs

---


---

The proof consists of three steps:

### `\( (1) \)` We show that `\(\mathbb R^n\)` is a [vector space][bookofproofs$560] over `\(\mathbb R\)`.

In order to show that the [cartesian product][bookofproofs$748] of the `\(n\)` [sets of real numbers][bookofproofs$1105].
`\[\mathbb R^n:=\underbrace{\mathbb R\times \mathbb R\times\cdots\times \mathbb R}_{n\text{ times}}.\]`  

constitutes a vector space over `\(\mathbb R\)`, we have to verify the following rules:

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
 
in `\(\mathbb R^n\)` these rules follow immediately from the fact that `\((\mathbb R,\cdot, + )\)` is a [field][bookofproofs$1638].
### `\( (2) \)` We show that the Euclidean norm `\(\|x\|\)` of a vector `\(x\in\mathbb R^n\)` is a [norm][bookofproofs$846]. Accordingly, the pair `\((\mathbb R^n,\|~\|)\)` constitutes a [normed vector space][bookofproofs$846].
The Euclidean norm of a vector `\(x\in\mathbb R^n\)` is defined as the [square root][bookofproofs$1161] of the [dot product][bookofproofs$1049] of this vector with itself, i.e.:

`\[||x||:=\sqrt{\langle x,x\rangle}=\sqrt{x_1^2+\ldots+x_n^2}.\]`

In order to show that this definition constitutes a norm, we have to prove the following properties: 

> `\((i)\)` `\(\|x\|=0\)` if and only if `\(x=0\)`.
Clearly, if `\(x=0\)`, i.e. if all coordinates of the vector `\(x_i=0\)` for `\(1\le i \le n\)`, then `\(||x||=0\)`. Conversely, if `\(||x||=0\)`, all coordinates must equal `\(0\)`, because `\(\sqrt{\alpha^2} > 0\)` for all `\(\alpha > 0\)`. 

> `\((ii)\)` `\(\|\lambda x\|=|\lambda|\cdot\|x\|\)` for all `\(\lambda\in\mathbb R\)`.
`\[\begin{array}{rclcl}
\|\lambda x\|&=&\sqrt{(\lambda\cdot x_1)^2+\ldots+(\lambda\cdot x_n)^2}&=&\\
&=&\sqrt{\lambda^2\cdot (x_1^2+\ldots+x_n)^2}&=&\\
&=&|\lambda|\cdot\sqrt{\cdot (x_1^2+\ldots+x_n)^2}&=&|\lambda|\cdot\|x\|\\
\end{array}\]`

> `\((iii)\)` `\(\|x+y\|\le \|x\|+\|y\|\)` for all `\(x,y\in \mathbb R^n\)`.
According to the [triangle inequality][bookofproofs$588], for all pairs of coordinates `\(x_i,y_i\)` , `\(1\le i\le n\)` we have
`\[\begin{array}{rclcl}
|x_i+y_i|&=&\sqrt{(x_i+y_i)^2}&\le&\\
&\le&\sqrt{x_i^2}+\sqrt{y_i^2}&=&\\
&=&|x_i|+|y_i|.
\end{array}\]`Therefore, we have
`\[\begin{array}{rclcl}
\|x+y\|&=&\sqrt{(x_1+y_1)^2+\ldots+(x_n+y_n)^2}&\le&\\
&\le&\sqrt{x_1^2+\ldots+x_n^2}+\sqrt{y_1^2+\ldots+y_n^2}&=&\|x\|+\|y\|.\end{array}\]`

It follows, that the pair `\((\mathbb R^n,||~||)\)` constitutes a normed vector space.

### `\( (3) \)` We show that the Euclidean distance of two vectors `\(x,y\in\mathbb R^n\)` is a [distance][bookofproofs$846]. Accordingly, the pair `\((\mathbb R^n,d)\)` constitutes a [metric space][bookofproofs$617].
According to `\((1)\)`, `\((\mathbb R^n,\|~\|)\)` is a normed vector space. Thus, according to the [corresponding proposition][bookofproofs$847], the norm of the difference of two vectors `\(x,y\in\mathbb R^n\)` defines a distance:

`\[d(x,y):=||x-y||=\sqrt{\langle x-y,x-y\rangle}=\sqrt{(x_1-y_1)^2+\ldots+(x_n-y_n)^2}.\]`

Thus, the pair `\((\mathbb R^n,d)\)` constitutes a metric space.
