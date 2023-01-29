layout: definition
categories: branches,graph-theory
nodeid: bookofproofs$1212
orderid: 50
parentid: bookofproofs$178
title: Planar Drawing (Embedding)
description: PLANAR DRAWING PLANAR EMBEDDING ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$1209
keywords: planar drawing,planar embedding,planar drawings,planar embeddings
contributors: bookofproofs

---


---

Let `\(\mathbb R^2\)` be an [Euclidean plane][bookofproofs$1206] and let `\(a,b\in\mathbb R\)`, `\(b > a\)` be two real numbers. Furthermore, let `\(I=[a,b]\)` be a [closed real interval][bookofproofs$1153].
.
A **planar drawing** (or a **planar embedding**) `\(\mathcal D\)` of an [undirected graph][bookofproofs$523] `\(G(V,E,\gamma)\)` consists of 

> `\((i)\)` an [injective][bookofproofs$769] function[^1] `\(f:V\to \mathbb R^2,\)`

> `\((ii)\)` for each edge `\(e_i\in E\)`, functions `\(\epsilon_i: I\to \mathbb R^2\)` such that:
* `\(\epsilon_i\)` is a [simple closed curve][bookofproofs$1211], if `\(e_i\)` is a loop[^2],
* `\(\epsilon_i\)` is a [simple curve][bookofproofs$1210], if `\(e_i\)` is not a loop[^3],
* if `\(x,y\)` are the ends of the edge `\(e_i\)`, we either have `\(\epsilon_i(a)=f(x)\)` and `\(\epsilon_i(b)=f(y)\)` or we have `\(\epsilon_i(a)=f(y)\)` and `\(\epsilon_i(b)=f(x)\)`, depending on at which vertex the curve starts and at which it ends[^4].
* The images of the [restrictions][bookofproofs$1170] of the curves `\(e_i\)` on the open interval `\(J:=(a,b)\)`, i.e. the functions `\({\epsilon_i|}_{J} : I \to \mathbb R^2\)` are mutually exclusive[^5], formally
`\[\epsilon_i(J)\cap\epsilon_j(J)=\emptyset\quad\quad i\neq j.\]`

### Example

A graph:


![planar1](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/planar1.jpg?raw=true)


and examples of its planar drawings:


![planar](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/planar.jpg?raw=true)



![planar2](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/planar2.jpg?raw=true)


Please note that a graph can have different planar drawings. 

For educational reasons, each vertex has been drawn not as a point in the plane, but as a labeled circle to enable the reader to compare all graphs.


[^1]: The injectivity of `\(f\)` makes sure that `\(f\)` assigns to each vertex of `\(G\)` a unique point in the Euclidean plane `\(\mathbb R^2\)`, i.e. the same point of the plane is never assigned to two different vertices.

[^2]: This property ensures that the drawing `\(\epsilon_i\)` of a loop does not cross itself. 

[^3]: This property ensures that the drawing `\(\epsilon_i\)` of the edge does not cross itself.

[^4]: Please note that since `\(f(x), f(y)\)` are the points in the plane, which are drawings of the vertices `\(x,y\)`, this property ensures that the drawing of any edge connecting these vertices (i.e. the curve `\(\epsilon_i\)`) starts (`\(\epsilon_i(a)\)`) and ends (`\(\epsilon_i(b)\)`) exactly at these points in the plane.

[^5]: This property makes sure that the drawings of any two edges do not cross, except at the endpoints (i.e. the vertices).
