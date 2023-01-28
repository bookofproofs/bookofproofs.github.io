layout: definition
categories: branches,algebra
nodeid: bookofproofs$560
orderid: 50
parentid: bookofproofs$276
title: Vector Space
description: VECTOR SPACE ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: 
keywords: vector space,vector spaces,vector,scalar,scalar multiplication,multiply by a scalar
contributors: bookofproofs

---


---

Let (`\(F,+,\cdot)\)` be a [field][bookofproofs$557] A non-empty [set][bookofproofs$550] `\(V\)` of elements called **vectors** with two [maps][bookofproofs$592] 

`\[
\cases{
V\times V\mapsto V:(x,y)\mapsto x\oplus y  & \text{(the vector addition)}\\
F\times V\mapsto V:(\alpha,x)\mapsto \alpha \odot x & \text{(the scalar multiplication)}
}\]`

is called a **vector space over the field** `$F$` (or a *$F$-vector space* or a **linear space over** `$F$`), if:
1. `\((V,\oplus)\)` is an [Abelian group][bookofproofs$553], in particular:
   * The addition `$[\oplus"$` of vectors is "associative][bookofproofs$668]: `$x\oplus (y\oplus z)=(x\oplus y)\oplus z$` for all `$x,y,z\in V.$`
   * `$[\oplus"$` has a "neutral element][bookofproofs$661], called the **zero vector** `$o\in V$` with `$x\oplus o=o\oplus x=x$` for all `$x\in V.$`
   * Every vector `$x\in V$` has an [inverse][bookofproofs$670] `$-x\in V$` with `$x\oplus(-x)=(-x)\oplus x=o.$` 
   * `$[\oplus"$` is "commutative][bookofproofs$672], i.e. `$x\oplus y=y\oplus x$` for all `$x,y\in V.$`
1. For `\(\alpha,\beta\in F\)` and `\(x,y\in V\)` the following **axioms of scalar multiplication** hold:
   *  `$(\alpha + \beta)\odot x=\alpha\odot x \oplus \beta\odot x,$`
   * `$\alpha\odot(x\oplus y)=\alpha\odot x \oplus \alpha\odot y,$` 
   * `$(\alpha\cdot \beta)\odot x=\alpha\odot (\beta\odot x),$`
   * If `$1\in F$` is the neutral element of the field, then it is also a neutral element of the scalar multiplication in `$V,$` i.e. `$1\odot x=x.$`



### A note on notation 

Whenever any misunderstandings can be excluded, <strong><span style='color:orange'>Bookof</span><span style='color:lightblue'>Proofs</span></strong> follows the convention used in most mathematical literature, making no difference in the notation of vector addition  `$"\oplus"$` and the addition of field elements  `$" + "$` as well as the scalar multiplication `$"\odot"$` and the multiplication of field elements `$"\cdot".$` However, to keep field elements and vectors apart, the latter will be denoted by small Latin letters, e.g. `$x,y,a,b,\ldots,$` while field elements will be denoted by small Greek letters `$\alpha,\beta,\gamma,\ldots.$`


### Vector notation with respect to a basis

If `\(V\)` has a [finite][bookofproofs$985] [basis][bookofproofs$299], `\(B=\{b_1,\ldots, b_n\}\subseteq V\)`, the  [uniqueness lemma][bookofproofs$1039] ensures that we can write any vector `\(v\in V\)` as a unique [linear combination][bookofproofs$1035] of the basis vectors:
`\[v = \alpha_1b_1+\ldots+\alpha_nb_n.\]` 
With respect to the basis `\(B\)`, we can write the vector `\(v\)` in its column notation

`\[
v=\pmatrix{
\alpha_{1}\cr
\alpha_{2}\cr
\vdots \cr
\alpha_{n} \cr
}
\]`

There are some things to mention: 

1. This notation depends on the chosen basis, i.e. the same vector will have different notations for two different bases. 
1. Writing the vector as a column is a common convention.
1. The above-mentioned rules of `\((V, \oplus)\)` being an Abelian group as well as scalar multiplication `\(\odot\)` are easily verified for the following operations (for `\(\alpha_i,\beta_i,\lambda\in F\)`):

`\[\text{vector addition }\oplus:=\pmatrix{
\alpha_{1}\cr
\alpha_{2}\cr
\vdots \cr
\alpha_{n} \cr
}+\pmatrix{
\beta_{1}\cr
\beta_{2}\cr
\vdots \cr
\beta_{n} \cr
}=\pmatrix{
\alpha_{1}+\beta_1\cr
\alpha_{2}+\beta_2\cr
\vdots \cr
\alpha_{n}+\beta_n \cr
}
\]`
`\[\text{scalar multiplication}\odot:=\lambda\cdot\pmatrix{
\alpha_{1}\cr
\alpha_{2}\cr
\vdots \cr
\alpha_{n} \cr
}=\pmatrix{
\lambda\cdot\alpha_{1}\cr
\lambda\cdot\alpha_{2}\cr
\vdots \cr
\lambda\cdot\alpha_{n} \cr
}
\]`
