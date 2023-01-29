layout: proof
categories: branches,graph-theory
nodeid: bookofproofs$912
orderid: 50
parentid: bookofproofs$1242
title: By Induction
description: Proof of EQUIVALENT DEFINITIONS OF TREES ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$570
keywords: equivalent definitions of trees,proof
contributors: bookofproofs

---


---

By hypothesis, `$G(V,E,\gamma)$` is an [undirected graph][bookofproofs$523].
### `$(1)\Rightarrow(2)$`

* Let `\(G\)` be a [tree][bookofproofs$96].
* Let `$G^\prime(V,E^\prime,\gamma^\prime)$` be a [supergraph][bookofproofs$390] of `$G$` containing at least one additional [edge][bookofproofs$523] `$e^\prime\in E^\prime\setminus E.$`
* Without loss of generality, assume `$e^\prime$` is not a [loop][bookofproofs$523] (otherwise, `$G^\prime$` would contain a [cycle][bookofproofs$1165]).
* In other words, without loss of generality, `$\gamma^\prime(e^\prime)=\{v,u\}$` with `$u\neq v.$`
* Since `$G$` is a tree, it is [connected][bookofproofs$1166].
* Therefore, there is a [path][bookofproofs$159] `$P$` connecting `$u$` and `$v$`.
* Since `$e^\prime$` connects `$u$` and `$v$` directly, `$P$`+$e^\prime$ is a [cycle][bookofproofs$1165].
* Thus, `$G$` contains no cycle and any supergraph of `$G$` contains a cycle.

### `$(2)\Rightarrow(3)$`

* Let `$G$` contain no cycle and let any supergraph of `$G$` contain a cycle.
* Let `$u,v\in V$` be a pair of any vertices. 
* Because `$G$` contains no cycle, it also contains no [loops][bookofproofs$523]. Therefore, we can assume `$u\neq v.$`
* Let `$e^\prime=\{u,v\}$` be an additional edge of the supergraph `$G^\prime:=(V,E\cup\{e^\prime\},\gamma).$`
* By assumption `$G^\prime$` contains a cycle and this cycle must contain `$e^\prime$`, since `$G$` had no cycles.
* Without loss of generality, set `$C=(v=v_0,e^\prime,u=v_1,e_2,\ldots,e_k,v_k=v)$` to a cycle containing `$e^\prime.$`
* It follows that `$P=(u=v_1,e_2,\ldots,e_k,v_k=v)$` is a [path][bookofproofs$1164] connecting `$u$` and `$v$` in `$G.$`
* Assume, there exists another path `$Q=(u=v_1,e^\prime_2,\ldots,e^\prime_k,v_k=v)$` connecting `$u$` and `$v$` in `$G.$`
   * By assumption `$P\neq Q$` and therefore, there are indices `$i\in\{2,\ldots,k\}$` such that `$e_i\neq e^\prime_i.$`
   * By the [well-ordering principle][bookofproofs$698], there is a minimal such index `$i\ge 2.$`
   * Then, the edges `$e_i$` and `$e^\prime_i$` connect the vertex `$v_{i-1}$` with two different vertices `$v_{i}$` and `$v^\prime_{i},$` otherwise `$(v_{i-1},e_i,v_i,e^\prime_i,v_{i-1})$` woud be a cycle.
   * Since both `$P$` and `$Q$` end at the same vertex `$v_k=v,$` the set of indices `$j$` such that `$j>i$` and `$v_j=v^\prime_j,$` is not empty.
   * Using the well-ordering principle once again, there is a minimal index `$j$` such that `$i < j\le k,$` and at which both paths `$P$` und `$Q$` meet together again.
   * This would mean that between `$v_{i-1}$` and `$v_j$` there is a cycle formed by parts of the paths `$P$` and `$Q$`.
   * This is a [contradiction][bookofproofs$744] to the hypothesis, `$G$` contained no cycle.
   * Thus, `$P$` and `$Q$` are identical.
* It follows that for every pair of vertices `$u,v\in V$` there is exactly one [path][bookofproofs$1164] `$P^k:=x_0x_1\ldots x_{k-1}x_k$` in `$G$` with `$x_0=u$` and `$x_k=v$`.

### `$(3)\Rightarrow(4)$`

* Assume, every pair of vertices `$u,v\in V$` there is exactly one [path][bookofproofs$1164] `$P^k:=x_0x_1\ldots x_{k-1}x_k$` in `$G$` with `$x_0=u$` and `$x_k=v$`.
* Trivially, `$G$` is [connected][bookofproofs$1166].
* Now, let us remove any edge `$e\in E$` from `$G$` with `$\gamma(e)=\{u,v\}.$`
* If `$u=v,$` then `$e$` was a [loop][bookofproofs$523] and `$P=u$` and `$Q=(u,e)$` would be two different paths from `$u$` to `$u.$`
* Therefore, `$u\neq v.$`
* Assume `$G$` without the edge `$e$` is still connected.
   * Then there is a path `$Q$` from `$u$` to `$v$` not passing through the edge `$e.$`
   * But then, `$Q$` and `$P=(u,e,v)$` would be two different paths in `$G$` connecting `$u$` and `$v.$`
* It follows `$G$` is [connected][bookofproofs$1166] and the removal of any edge leaves `$G$` disconnected ($G$ is "minimally connected").

### `$(4)\Rightarrow(5)$`

* Let `$G$` be minimally connected.
* We prove first the inequality `$|E|\le |V|-1$` [by induction][bookofproofs$657] on `$n=|V|.$`
   * Base cases `$n=1$`
      * The inequality is correct since `$G$` is minimally connected, there are `$0$` edges in `$G,$` and `$0\le 1-1.$`
   * Induction step `$n\to n+1$`
      * Assume, for all trees with `$k$` vertices, `$1 \le k  < n,$` we have `$|E|\le |V|-1.$` 
      * `$(4)$` shows that removing any edge `$e$` disconnects `$G$` in some [components][bookofproofs$1221] `$G_1,\ldots G_p.$`
      * By induction assumption `$|E_i|\le |V_i|-1$` for all `$i=1,\ldots,p.$`
      * Because `$G_1,\ldots G_p$` are a [partition][bookofproofs$1221], we can sum up all `$p$` inequalities to get `$|E|\le |V|-p\le |V|-1.$`
   * It follows `$|E|\le |V|-1$` for all minimally connected graphs `$G.$`
* We now observe that for all minimally connected graphs `$|V|\le |E|+1,$` since any edge connects at most `$2$` different vertices. In other words `$|E|\ge |V|-1.$` 
* Since `$|E|\le |V|-1$` and `$|E|\ge |V|-1,$` it follows `$G$` is connected and `$|E|=|V|-1.$` 
 
### `$(5)\Rightarrow(6)$`

* Every `$G$` is connected and `$|E|=|V|-1.$`
* Assume, `$C$` is a [cycle][bookofproofs$1165] in `$G$` containing some edge `$e.$` 
* Then the [subgraph][bookofproofs$390] `$H$` retrieved from `$G$` by removing `$e$` is still connected and contains `$|V|-2$` edges.
* This is a contradiction to the hypothesis.
* Therefore, `$G$` has no cycle and  `$|E|=|V|-1.$`

### `$(6)\Rightarrow(1)$`

* Assume, `$G$` has no cycle and  `$|E|=|V|-1.$`
* By definition, `$G$` is a [forest][bookofproofs$96].
* Assume, `$G$` is not [connected][bookofproofs$1166] and consists of the [components][bookofproofs$1221] `$G_1,\ldots,G_p.$`
* Since every `$G_i$` is a [tree][bookofproofs$96], we have by the implications `$(1)\Rightarrow\ldots\Rightarrow(5)$` that `$|E_i|=|V_i|-1$` for `$i=1,\ldots,p.$`
* It follows `$$|V|-1=|E|=\sum_{i=1}^p |E_i|=\sum_{i=1}^p (|V_i|-1)=|V|-p.$$`
* Now, it follows `$p=1.$`
* Therefore, `$G$` is a [tree][bookofproofs$96].