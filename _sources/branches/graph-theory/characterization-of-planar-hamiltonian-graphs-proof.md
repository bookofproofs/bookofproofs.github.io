layout: proof
categories: branches,graph-theory
nodeid: bookofproofs$6401
orderid: 50
parentid: bookofproofs$6400
title: 
description: Proof of CHARACTERIZATION OF PLANAR HAMILTONIAN GRAPHS ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$1591
keywords: characterization of hamiltonian planar graphs,planar hamiltonian graphs,planar hamiltonian graph,proof
contributors: bookofproofs


---


---

## Proof

In the following proof, we assume that `\(G(V,E)\)` is a [simple][bookofproofs$523], [planar][bookofproofs$1226] and [connected][bookofproofs$1166] graph with `\(n:=|V|\)` vertices.

### "`\(\Rightarrow\)`"

* Assume, `\(G\)` is [Hamiltonian][bookofproofs$6349]. We have to prove that the [minimal tree decomposability][bookofproofs$6393] of all dual graphs `\(G^\ast\)` of `\(G\)` is `\(\tau(G^\ast)=2\)`.
* Since `\(G\)` is planar, it has a [planar drawing][bookofproofs$1212] `\(\mathcal D\)`.
* Take __any__ [planar drawing][bookofproofs$1212] `\(\mathcal D\)` of `\(G\)`.
* Construct the corresponding [dual graph][bookofproofs$6391] `\(G^\ast_{\mathcal D}\)`.
* Since `\(G\)` is Hamiltonian, there is a [Hamiltonian cycle][bookofproofs$330] `\(C^n\)` of `\(G\)`; let `\(C^n\)` denote the Hamiltonian cycle drawn inside `\(\mathcal D\)`. 
* Identify vertices `\(v_1,\ldots v_m\)` of `\(G^\ast_{\mathcal D}\)`, which are enclosed by `\(C^n\)` in `\(\mathcal D\)`. 
* By the [lemma about the dual graph of faces contained inside a planar Hamiltonian cycle][bookofproofs$6398], the [subgraph induced][bookofproofs$390] in `\(G^\ast_{\mathcal D}\)`, i.e. the graph `\(G^\ast_{\mathcal D}[v_1,\ldots v_m]\)`, is a [tree][bookofproofs$96], say `\(T_1.\)`
* Since the vertices `\(v_1,\ldots v_m\)` are only those vertices of `\(G^\ast_{\mathcal D}\)`, which are enclosed by the Hamiltonian cycle `\(C^n\)`, there is at least one other vertex `\(w\)` of `\(G^\ast_{\mathcal D}\)`, e.g. the vertex corresponding to the [infinite face][bookofproofs$6373] of the planar drawing `\(\mathcal D\)`. Therefore, `\(w\)` is contained in the non-empty subset of vertices `\(V^\ast\setminus\{v_1,\ldots,v_m\}\)`, where `\(V^\ast\)` denotes all the vertices of `\(G^\ast_{\mathcal D}\)`. 
* Again, by the [lemma about the dual graph of faces contained inside a planar Hamiltonian cycle][bookofproofs$6398], the subgraph induced by the vertices `\(V^\ast\setminus\{v_1,\ldots,v_m\}\)` in `\(G^\ast_{\mathcal D}\)`, i.e. the graph `\(G^\ast_{\mathcal D}[V^\ast\setminus\{v_1,\ldots,v_m\}]\)`, is a also [tree][bookofproofs$96], say `\(T_2,\)` because the Hamiltonian cycle `\(C^n\)` encloses the vertices `\(V^\ast\setminus\{v_1,\ldots,v_m\}\)` in similar way as it encloses the vertices `\(\{v_1,\ldots,v_m\}\)`. 
* Thus, the dual graph `\(G^\ast_{\mathcal D}\)` can be [decomposed into two trees][bookofproofs$6392]: `\(T_1\)` and `\(T_2\)`, thus `\(\tau(G^\ast_{\mathcal D})\le 2\)`.
* It remains to be show that this decomposition is [minimal][bookofproofs$6393], i.e. to prove that indeed `\(\tau(G^\ast_{\mathcal D})=2\)`. This will be proven by [contradiction][bookofproofs$744]; Assume, `\(\tau(G^\ast_{\mathcal D}) < 2\)`.  
   * Case `\(\tau(G^\ast_{\mathcal D})=0\)`: 
      * In this case, the "proof of the lemma for the bounds for the minimal tree decomposability":https://www.bookofproofs.org/branches/bounds-for-the-minimal-tree-decomposability/proof/ shows that the [dual graph][bookofproofs$6391] `\(G^\ast_{\mathcal D}\)` contains [loops][bookofproofs$523]. This can only happen, if the planar graph `\(G\)` contains a [subgraph][bookofproofs$390], which is a [tree][bookofproofs$96], since the planar drawing of a tree is contained in a single [infinite face][bookofproofs$6373] of the plane,  this face in the dual graph corresponds to a single vertex with as many loops, as there are edges in the tree.
      * Because `\(G\)` contains a subgraph which is a tree, it is not [biconnected][bookofproofs$1227], since each vertex of such a tree is a [cutvertex][bookofproofs$1166] of `\(G\)`.
      * Since [biconnectivity is a necessary condition for Hamiltonian graphs][bookofproofs$6396], `\(G\)` cannot be Hamiltonian, because it contains a tree subgraph, contradicting the case `\(\tau(G^\ast_{\mathcal D})=0\)`.
   * Case `\(\tau(G^\ast_{\mathcal D})=1\)`: 
      * Again, according to the "proof of the lemma for the bounds for the minimal tree decomposability":https://www.bookofproofs.org/branches/bounds-for-the-minimal-tree-decomposability/proof/, `\(\tau(G^*_{\mathcal D})=1\)` holds only, if the dual graph `\(G^\ast_{\mathcal D}\)` is itself a tree. This can only happen, if the planar graph `\(G\)` consists of a single vertex with as many loops, as there are edges in the tree being its dual graph `\(G^\ast_{\mathcal D}\)`. 
      * However, `\(G\)` is a simple graph by hypothesis and so it cannot contain any loops, which contradicts the case `\(\tau(G^\ast_{\mathcal D})=1\)`.
* Since we have proven that `\(\tau(G^\ast_{\mathcal D}) \not < 2\)` and   `\(\tau(G^\ast_{\mathcal D}) \le 2\)`, it follows  `\(\tau(G^\ast_{\mathcal D}) =2\)`.
* Since `\(G^\ast_{\mathcal D}\)` was an arbitrary dual graph (because it was constructed from an arbitrary planar drawing `\({\mathcal D}\)` of `\(G\)`), this property holds for all dual graphs of the planar Hamiltonian graph `\(G\)`. 


### "`\(\Leftarrow\)`"

* Assume, the [minimal tree decomposability][bookofproofs$6393] of all dual graphs `\(G^\ast\)` of `\(G\)` is `\(\tau(G^\ast)=2\)`. We have to prove that `\(G\)` is Hamiltonian. We will do this by constructing a [Hamiltonian cycle][bookofproofs$330] in `\(G\)`.
* Construct the dual graph `\(G^\ast_{\mathcal D}\)` from an arbitrary planar drawing `\(\mathcal D\)` of `\(G\)`.
* Since `\(\tau(G^\ast_{\mathcal D})=2\)`, identify trees `\(T_1\)` and `\(T_2\)`, into which `\(G^\ast_{\mathcal D}\)` can be [decomposed][bookofproofs$6392].
* Let `\(V^\ast(T_1)\)` and `\(V^\ast(T_2)\)` denote the vertices of both trees, respectively. 
* We claim that there are exactly `\(n\)` edges of `\(G^\ast_{\mathcal D}\)` connecting the vertices `\(V^\ast(T_1)\)` with the vertices `\(V^\ast(T_2)\)`, where `\(n\)` equals the number of the vertices of the original graph `\(G\)`. Proof:
   * For the dual graph `\(G^\ast_{\mathcal D}\)`, the [Eulerian characteristic for planar graphs][bookofproofs$6374] leads to the equation `\[|V^\ast|-|E^\ast| + n =2,\]` where `\(|V^\ast|\)` is the number of its vertices, `\(|E^\ast|\)` is the number of its edges, and `\(n\)` equals the number of its faces (actually, it also equals the number of the vertices of the original graph `\(G\)`).
   * By definition of [tree decomposition][bookofproofs$6392], `\(V^\ast(T_1)\)` and `\(V^\ast(T_2)\)` are non-empty sets and build a partition of the `\(n\)` vertices of `\(G^\ast_{\mathcal D}\)`. Replacing `\(n\)` by the sum `\(|V^\ast(T_1)|+|V^\ast(T_2)|\)` leads to the equation `\[|V^\ast(T_1)|+|V^\ast(T_2)|-|E^\ast| + n =2.\]`
   * Let `\(E^\ast(T_1)\)` denote the number of edges of the tree `\(T_1\)` and let `\(E^\ast(T_2)\)` denote the number of edges of the tree `\(T_2\)`. Therefore, the number of the edges of `\(G^\ast_{\mathcal D}\)` can be written as the sum `\(|E^\ast|=|E^\ast(T_1)|+|E^\ast(T_2)|+|E^\ast( R)|\)`, where `\(|E^\ast( R)|\)` denotes the number of any remaining edges in `\(G^\ast_{\mathcal D}\)`, if they exist. Clearly, `\(|E^\ast( R)|\ge 0\)` and this leads to the equation
`\[|V^\ast(T_1)|+|V^\ast(T_2)|-|E^\ast(T_1)|-|E^\ast(T_2)|-|E^\ast( R)| + n =2.\]`
   * From the [equivalent definitions of trees][bookofproofs$1242], we know that `\(|E^\ast(T_1)|=|V^\ast(T_1)|-1\)` and that `\(|E^\ast(T_2)|=|V^\ast(T_2)|-1\)`. This leads to the equation
`\[|V^\ast(T_1)|+|V^\ast(T_2)|-(|V^\ast(T_1)|-1)-(|V^\ast(T_2)|-1)-|E^\ast( R)| + n =2.\]`
   * This is equivalent to `\(|E^\ast( R)=n|\)`, as required.
* Note that, for planarity reasons, none of the remaining `\(n\)` edges of `\(G^\ast_{\mathcal D}\)` connecting the vertices `\(V^\ast(T_1)\)` with the vertices `\(V^\ast(T_2)\)` are crossing each other. Thus, they form faces in the plane together with the edges of the trees `\(T_1\)` and `\(T_2\)`, which they are connecting together. Moreover, if we virtually draw in the plane a simple closed curve around e.g. the tree `\(T_1\)` in a way in which the curve never crosses the edges of `\(T_1\)`, but always crosses the `\(n\)` remaining edges  of `\(G^\ast_{\mathcal D}\)`  connecting `\(T_1\)` with `\(T_2\)`, our curve will also cross each of the `\(n\)` faces and induce a circular order on them.  
* By construction of the dual graph `\(G^\ast_{\mathcal D}\)`: 
   * There must be a [bijection][bookofproofs$771] between each of such `\(n\)` faces and all the `\(n\)` vertices of the original graph `\(G\)`. 
   * There must be a bijection between the `\(n\)` remaining edges of `\(G^\ast_{\mathcal D}\)` not included in `\(T_1\)` and `\(T_2\)` and some `\(n\)` edges of the original graph `\(G\)`. 
   * Finally, these `\(n\)` edges of the original graph connect exactly the `\(n\)` vertices of `\(G\)`. 
* The alternating chain of `\(n\)` edges and `\(n\)` vertices of `\(G\)` defines a Hamiltonian cycle if and only if all vertices and all edges are distinct. But that is how they have been constructed in the above proof, because the above circular order of the faces corresponds to a circular order of the vertices in the Hamiltonian cycle. 
* Thus, `\(G\)` is [Hamiltonian][bookofproofs$6349].