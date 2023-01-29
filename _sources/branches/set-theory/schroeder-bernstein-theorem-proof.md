layout: proof
categories: branches,set-theory
nodeid: bookofproofs$8052
orderid: 50
parentid: bookofproofs$8051
title: 
description:  Proof of SCHRöDER-BERNSTEIN THEOREM &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: 
keywords: bernstein,schroeder,theorem,schröder bernstein theorem,schroeder bernstein theorem,schroeder bernstein theorem proof,proof
contributors: bookofproofs


---


---

The following proof is a _special case_ of a more general fixpoint theorem formulated by "Tarski":https://www.bookofproofs.org/history/alfred-tarski/ for lattices, which we will be studying later in more detail.

* Let `$A$` and `$B$` be [sets][bookofproofs$550] with the [cardinalities][bookofproofs$980]  `$|A|$` and `$|B|$`.
* By hypothesis, `$|A|\le |B|$` and `$|B|\le |A|.$` 
* By the definition of [comparing cardinal numbers][bookofproofs$984] this means that there are [injective functions][bookofproofs$769] `$f:A\to B$` and `$g:B\to A.$`
* On the [power sets][bookofproofs$6831] `$\mathcal P(A)$` and `$\mathcal P(B),$` we define a function `$\Phi:\mathcal P(A)\to \mathcal P(B)$` such that for every subset `$X\subseteq A$` `$$\Phi(X):=A\setminus g[B\setminus f[X]],$$`
here we use the [set differences][bookofproofs$6830] "`$\setminus$`" and denote by `$f[X]$` and `$g[B\setminus f[X]]$` the respective [ranges][bookofproofs$592] of the functions `$f$` and `$g.$`
* `$f$` is injective by hypothesis, therefore 
`$$(\forall X,Y\in A):X\subseteq Y\Rightarrow f(X)\subseteq f(Y).$$`
* By analogy, since `$g$` is injective by hypothesis,
`$$(\forall X,Y\in B):X\subseteq Y\Rightarrow g(X)\subseteq g(Y).$$`
* Because the [composition of two injective functions is again injective][bookofproofs$6864], by analogy:
`$$(\forall X,Y\in \mathcal P(A)):X\subseteq Y\Rightarrow \Phi(X)\subseteq \Phi(Y).\quad\quad( * )$$`
* We will now show that `$\Phi$` has a **fixed point**, i.e. that there exists a subset `$U\in \mathcal P(A)$` with `$\Phi(U)=U.$` 
   * We set `$U:=\bigcap_{Z\in \mathcal U}$`, where the set `$\mathcal U$` is defined by 
`$$\mathcal U:=\{Z\in\mathcal P(A)\mid \Phi(Z)\subseteq Z\}.$$`
   * By definition of the [set intersection][bookofproofs$6828], for every `$Z\in\mathcal U$` we have `$U\subseteq Z$`, which leads to `$\Phi(U)\subseteq\Phi(Z)\subseteq Z,$` by `$( * )$` and the definition of `$\mathcal U.$` 
   * By the [behaviour of functions with set intersection ][bookofproofs$294] we also have `$\Phi(U)\subseteq \bigcap_{Z\in \mathcal U}=U.$`
   * Therefore, `$U$` is a fixed point of `$\Phi.$`
* Now, we are able to study what happens if we build the value `$\Phi(U).$` By definition, `$U=\Phi(U)=A\setminus g[B\setminus f[U]],$` or in other words `$g[B\setminus f[U]]=A\setminus U$` and we have the situation illustrated in the below [Venn-diagram][bookofproofs$587]:


![schroederbernstein](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/schroederbernstein.png?raw=true)


* The diagram shows that all elements of the fixed point `$U$` are mapped by the composition `$g\circ f$` of the injective functions `$f$` and `$g$` exactly to the elements of the [set complement][bookofproofs$6829] `$A\setminus U.$` By symmetry, the same can be said of mapping all elements of `$f[U]$` by the composition `$f\circ g$` to the set complement `$B\setminus f[U].$`
* Now we define a new function `$h:A\to B$` as follows:
`$$h(a):\begin{cases}
f(a)&\text{ for }a\in U\\
g^{-1}(a)&\text{ for }a\in A\setminus U
\end{cases}$$`
* Obviously, the function `$h:A\to B$` is [bijective][bookofproofs$771].
* Therefore, `$|A|=|B|.$`
