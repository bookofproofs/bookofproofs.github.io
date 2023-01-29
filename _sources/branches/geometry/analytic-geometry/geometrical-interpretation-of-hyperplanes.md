layout: explanation
categories: branches,geometry,analytic-geometry
nodeid: bookofproofs$7983
orderid: 50
parentid: bookofproofs$7982
title: Geometrical Interpretation of Hyperplanes
description: GEOMETRICAL INTERPRETATION OF HYPERPLANES &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$7937
keywords: geometrical,hyperplanes,interpretation
contributors: bookofproofs

---


---

As we have seen in the [above proposition][bookofproofs$7980], a hyperplane solving a [linear equation][bookofproofs$1043] with `$n=2$` unknowns is a straight line. But what about the general case `$n\ge 1$`? 

If `$A=(\alpha_1,\ldots,\alpha_n)\in\mathbb R^n$` is not the origin, and `$\beta\in\mathbb R$`, the linear equation might have the form

`$$\alpha_1x_1+\alpha_2x_2+\ldots+\alpha_nx_n=\beta.\quad ( * ) $$` 

We have seen how to [identify points with vectors in number spaces][bookofproofs$7960]. By interpreting the points `$P\in \mathbb R^n$` solving the equation `$( * )$` as vectors `$\overrightarrow{OP}$` we can easily interpret hyperplanes geometrically. In order to do so, we first have to reformulate the equation `$( * )$` a little bit. We can re-index the `$\alpha_i$` to achieve that `$\alpha_1\neq 0$`. In this case, we can solve the linear equation for `$x_1$` and get

`$$x_1=\frac{\beta}{\alpha_1}-\frac{\alpha_2}{\alpha_1}x_2-\ldots-\frac{\alpha_n}{\alpha_1}x_n.\quad( * * )$$` 
 
Therefore, the value of the unknown `$x_1$` depends on the specific choices of the values of the unknowns `$x_2, \ldots,x_n$`. In other words, we can represent `$x_1$` by choosing specific values of the other variables. Any choice of these `$n-1$` variables will give us one value of `$x_1$`. Thus, the set of all solutions of an equation of `$n$` unknowns can be completely described by all possible choices of `$n-1$` variables. In order to illustrate this, we write any point `$P$` solving the equation `$( * )$` as a vector `$\overrightarrow{OP}$` with the coordinates `$x_1,\ldots,x_n$`, in which we replace `$x_1$` by the expression `$( * * )$`: 

`$$\overrightarrow{OP}=\pmatrix{\frac{\beta}{\alpha_1}-\frac{\alpha_2}{\alpha_1}x_2-\ldots-\frac{\alpha_n}{\alpha_1}x_n\\x_2\\\vdots\\x_n}.$$`

While the vector `$\overrightarrow{OP}$` depends on the values of the `$n-1$` variables `$x_2,\ldots,x_n$`, we can use [vector addition and scalar multiplication][bookofproofs$560] to write it as a sum of vectors depending on only one of these variables each:

`$$\pmatrix{\frac{\beta}{\alpha_1}-\frac{\alpha_2}{\alpha_1}x_2-\ldots-\frac{\alpha_n}{\alpha_1}x_n\\x_2\\\vdots\\x_n}=\pmatrix{\frac{\beta}{\alpha_1}\\0\\\vdots\\0}+x_2 \pmatrix{-\frac{\alpha_2}{\alpha_1}\\1\\\vdots\\0}+\cdots+x_n\pmatrix{-\frac{\alpha_n}{\alpha_1}\\0\\\vdots\\1}.$$`

In case the equation `$( * )$` is [homogeneous][bookofproofs$1043], this representation simplifies to

`$$\pmatrix{-\frac{\alpha_2}{\alpha_1}x_2-\ldots-\frac{\alpha_n}{\alpha_1}x_n\\x_2\\\vdots\\x_n}=x_2 \pmatrix{-\frac{\alpha_2}{\alpha_1}\\1\\\vdots\\0}+\cdots+x_n\pmatrix{-\frac{\alpha_n}{\alpha_1}\\0\\\vdots\\1}.$$`

Obviously, the `$n-1$` vectors `$$\pmatrix{-\frac{\alpha_2}{\alpha_1}\\1\\\vdots\\0},\cdots,\pmatrix{-\frac{\alpha_n}{\alpha_1}\\0\\\vdots\\1}$$` are not multiplies of each other, thus they form an `$n-1$` dimensional [basis][bookofproofs$299] of an `$n-1$` dimensional number space `$H\subseteq \mathbb R^{n}$`. This is the reason, why a hyperplane `$H$` being a solution of a linear equation with `$n$` unknowns has always a dimension which is one less than the number of dimensions of the space `$\mathbb R^n$` it is part of.

Now, it is easy to use all these observations to conclude, how to interpret hyperplanes for different values of `$n$`.

#### Case `$n=1$`

A linear equation in the one-dimensional number line `$\mathbb R^1$` has the form `$\alpha_1x_1=\beta,$` and the hyperplane solving it is always a zero-dimensional point `$\pmatrix{\frac{\beta}{\alpha_1}}.$`

#### Case `$n=2$`

A linear equation in the two-dimensional number plane `$\mathbb R^2$` has the form `$\alpha_1x_1+\alpha_2x_2=\beta,$` and the hyperplane solving it is always a one-dimensional straight line 
`$$\pmatrix{\frac{\beta}{\alpha_1}\\0}+x_2 \pmatrix{-\frac{\alpha_2}{\alpha_1}\\1}.$$`


#### Case `$n=3$`

A linear equation in the three-dimensional number space `$\mathbb R^3$` has the form `$\alpha_1x_1+\alpha_2x_2+\alpha_3x_3=\beta,$` and the hyperplane solving it is always a two-dimensional plane

`$$\pmatrix{\frac{\beta}{\alpha_1}\\0\\0}+x_2 \pmatrix{-\frac{\alpha_2}{\alpha_1}\\1\\0}+x_3\pmatrix{-\frac{\alpha_3}{\alpha_1}\\0\\1}.$$`

#### Case `$n\ge 4$`

A linear equation in the `$n$`-dimensional number space `$\mathbb R^n$` has the form `$\alpha_1x_1+\ldots+\alpha_n x_n=\beta,$` and the hyperplane solving it is always an `$n-1$`-dimensional hyperplane

`$$\pmatrix{\frac{\beta}{\alpha_1}\\0\\\vdots\\0}+x_2 \pmatrix{-\frac{\alpha_2}{\alpha_1}\\1\\\vdots\\0}+\cdots+x_n\pmatrix{-\frac{\alpha_n}{\alpha_1}\\0\\\vdots\\1}.$$`
