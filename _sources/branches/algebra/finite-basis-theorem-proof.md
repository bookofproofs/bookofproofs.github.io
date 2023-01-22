layout: proof
categories: branches,algebra
nodeid: bookofproofs$1046
orderid: 0
parentid: bookofproofs$1042
title: 
description:  Proof of FINITE BASIS THEOREM &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$561,bookofproofs$1038
keywords: basis,finite,theorem,finite basis,finite basis theorem,basis theorem,the basis theorem,proof
contributors: bookofproofs

---


---

#### Proof for `\( (1) \)`: `\(V\)` has a [finite][bookofproofs$985] [basis][bookofproofs$299]

Since `\(V\)` is a vector space over a field `\(F\)` with a finite dimension `\(dim(V)=n < \infty\)`, the number `\(n\)` is [by definition of the dimension][bookofproofs$1041] the maximum number of [linearly independent][bookofproofs$1036] vectors contained in `\(V\)`. Let `\(B:=\{v_1,\ldots,v_n\}\subseteq V\)` be any such linearly independent vectors. We note that, for any subset `\(A\subseteq B\)`, the vectors in `\(A\)` have also to be independent. In order to show that `\(B\)` is a basis, it remains to show that `\(B\)` is a [generating system][bookofproofs$279] of `\(V\)`. 

If `\(V=\{0\}\)`, then `\(B=\{0\}\)`, and trivially the vector `\(v_1=0\in V\)` can be represented as a linear combination of the basis[^1] `\(v_1=0=\alpha v_1\)` for all  `\(\alpha\in F\)`, so `\(V=Span(B)\)`.

If `\(V\neq\{0\}\)`, `\(B:=\{v_1,\ldots,v_n\}\)` and `\(b\in V\)` with `\(b\neq 0\)`, then, since `\(n\)` is maximal by assumption, the set of vectors `\(B\cup \{b\}\)` must be linearly dependent, i.e. the equation
`\[\begin{array}{ccl}
0&=&\alpha_1v_1+\ldots+\alpha_nv_n+\beta b\\
&\Updownarrow\\
-\beta b&=&\alpha_1v_1+\ldots+\alpha_nv_n~~~~~~~~~~~~~~~~( * ) 
\end{array}\]`
can be solved either for `\(\beta\neq 0\)` or `\(\alpha_i\neq 0\)` for at least one `\(i=1,\ldots,n\)`. Note that  `\(\beta\neq 0\)`, for if `\(\beta=0\)`, we would have the the case `\[0=\alpha_1v_1+\ldots+\alpha_nv_n\]`
which can only be solved trivially by `\(\alpha_1=\ldots=\alpha_n=0\in F\)` because of the linear independence of the `\(v_i\)`. Therefore, we can divide both sides of the equation `\( ( * ) \)` by `\(-\beta\)`, resulting in 
`\[b=\frac{\alpha_1}{- \beta} v_1+\ldots+\frac{\alpha_n}{- \beta} v_n.\]`
Since `\(\alpha_i,\beta\in F\)` were all arbitrary, we have shown that any non-zero vector `\(b\in V\)` can be represented as a linear combination of the `\(v_i\in B\)`. Thus, we have again `\(V=Span(B)\)`.

[^1]: `\(v_1\)` is linearly independent, since `\(0=\alpha\cdot v_1\)` can be solved only trivially by `\(\alpha=0\)`, since `\(v_1\neq 0\)`.

#### Proof for `\( (2) \)`: Two different bases of `\(V\)` have the same number of elements, and this number equals `\(n=dim(V)\)`.

In `\( (1) \)` we have shown already the existence of a basis `\(B=\{v_1,\ldots,v_n\}\)` with `\(n\)` elements, `\(n=dim(V)\)`. It remains to show that no basis of `\(V\)` can have a different number of elements. Suppose the existence of such a basis, say `\(A:=\{w_1,\ldots,w_m\}\)` with `\(m\neq n\)`. 

`\(m > n\)` would mean a [contradiction][bookofproofs$744] to the property of `\(n\)` as the maximum number of linearly independent vectors in `\(V\)` and the definition of `\(A\)` as a [basis][bookofproofs$299] 

`\(m < n\)` would mean that we can generate all vectors of `\(V\)` using a smaller number of independent vectors then its dimension `\(n\)`. Since there are (!) some `\(n\)` linearly independent vectors `\(v_1,\ldots, v_n\)`, after all, we shall be able to generate them with a smaller number the independent vectors `\(w_1,\ldots, w_m\)`. We will show that this is impossible.

Suppose in contrary that it is possible. In other words, we have

`\[
\begin{array}{ccc}
\alpha_{11}w_1+\ldots + \alpha_{1m}w_m&=&v_1\\
\alpha_{21}w_1+\ldots + \alpha_{2m}w_m&=&v_2\\
\vdots&\vdots&\vdots\\
\alpha_{n1}w_1+\ldots + \alpha_{nm}w_m&=&v_n\\
\end{array}
\]`

In matrix form we can write
`\[\pmatrix{
\uparrow  & \uparrow  & \ldots & \uparrow \cr
w_1 & w_2 & \ldots & w_m \cr
\downarrow  & \downarrow  & \ldots & \downarrow \cr
}\cdot\pmatrix{
\alpha_{11} & \alpha_{12} & \ldots & \alpha_{1n} \cr
\alpha_{21} & \alpha_{22} & \ldots & \alpha_{2n} \cr
\vdots & \vdots & \ddots & \vdots \cr
\alpha_{m1} & \alpha_{m2} & \ldots & \alpha_{mn} \cr
}=\pmatrix{
\uparrow  & \uparrow  & \ldots & \uparrow \cr
v_1 & v_2 & \ldots & v_n \cr
\downarrow  & \downarrow  & \ldots & \downarrow \cr
}\]`
Since `\(m < n\)`, the matrix with the coefficients `\(\alpha_{ij}\)` has more columns then rows. Following the [fundamental lemma][bookofproofs$1045], the homogeneous equation system 

`\[\pmatrix{
\alpha_{11} & \alpha_{12} & \ldots & \alpha_{1n} \cr
\alpha_{21} & \alpha_{22} & \ldots & \alpha_{2n} \cr
\vdots & \vdots & \ddots & \vdots \cr
\alpha_{m1} & \alpha_{m2} & \ldots & \alpha_{mn} \cr
}\cdot\pmatrix{
X_{1} \cr
X_{2} \cr
\vdots \cr
X_{n} \cr
}=\pmatrix{
0 \cr
0 \cr
\vdots \cr
0 \cr
}\]`
has more unknowns as equations, and as such, a nontrivial solution `\(X_1 = \beta_1 , X_2=\beta_2,\ldots X_n = \beta_n\)`:
`\[\pmatrix{
\alpha_{11} & \alpha_{12} & \ldots & \alpha_{1n} \cr
\alpha_{21} & \alpha_{22} & \ldots & \alpha_{2n} \cr
\vdots & \vdots & \ddots & \vdots \cr
\alpha_{m1} & \alpha_{m2} & \ldots & \alpha_{mn} \cr
}\cdot\pmatrix{
\beta_{1} \cr
\beta_{2} \cr
\vdots \cr
\beta_{n} \cr
}=\pmatrix{
0 \cr
0 \cr
\vdots \cr
0 \cr
}\]`
In other words 
`\[\pmatrix{
\uparrow  & \uparrow  & \ldots & \uparrow \cr
w_1 & w_2 & \ldots & w_m \cr
\downarrow  & \downarrow  & \ldots & \downarrow \cr
}\cdot\pmatrix{
\alpha_{11} & \alpha_{12} & \ldots & \alpha_{1n} \cr
\alpha_{21} & \alpha_{22} & \ldots & \alpha_{2n} \cr
\vdots & \vdots & \ddots & \vdots \cr
\alpha_{m1} & \alpha_{m2} & \ldots & \alpha_{mn} \cr
}\cdot\pmatrix{
\beta_{1} \cr
\beta_{2} \cr
\vdots \cr
\beta_{n} \cr
}=\pmatrix{
\uparrow  & \uparrow  & \ldots & \uparrow \cr
v_1 & v_2 & \ldots & v_n \cr
\downarrow  & \downarrow  & \ldots & \downarrow \cr
}\cdot\pmatrix{
\beta_{1} \cr
\beta_{2} \cr
\vdots \cr
\beta_{n} \cr
}\]`

`\[0 w_1 + \ldots + 0w_m = 0 = \beta_1v_1+\ldots+\beta_nv_n\]`
would be a non-trivial representation of `\(0\)`, which again is a contradiction to `\(v_i\)` being independent.

Therefore `\(m=n\)`.

#### Proof for `\( (3) \)`: [Linearly independent][bookofproofs$1036] vectors `\(v_1,\ldots,v_r\)` with `\(r < n\)` can be completed by vectors `\(v_{r+1},\ldots,v_{n}\)` to create a basis `\(v_1,\ldots,v_n\)`  of `\(V\)`.

Let `\(A_r:=\{v_1,\ldots,v_r\}\)`. Because `\(A_r\)` is a set of linearly independent vectors and because `\(r < n\)`, the vector space `\(Span(A_r)\)` a proper subspace of `\(V\)`, i.e. there is a vector `\(v_{r+1}\in V\)` with `\(v_{r+1}\not\in Span(A_r)\)`. Therefore, `\(v_{r+1}\)` is linearly independent from `\(A_r\)`. We can repeat the argument for `\(A_{r+1}=A_r\cup\{v_{r+1}\}\)`. This will end, once we have reached the dimension of `\(V\)`, which by definition is the maximum number of independent vectors in `\(V\)`.
