layout: proof
categories: branches,set-theory
nodeid: bookofproofs$8638
orderid: 50
parentid: bookofproofs$8637
title: 
description: PROOF OF ZORN'S LEMMA IS EQUIVALENT TO THE AXIOM OF CHOICE ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$1591
keywords: zorn's lemma is equivalent to the axiom of choice,proof
contributors: bookofproofs

---


---

### "`$\Rightarrow$`"

* Assume, the [axiom of choice][bookofproofs$8041] holds.
* See the proof of [Zorn's Lemma][bookofproofs$8061], how it follows.

### "`$\Leftarrow$`"

* Assume [Zorn's Lemma][bookofproofs$8061] is true.
* Let `$X$` be a [set][bookofproofs$550] of disjoint and non-empty sets `$X=\{V_i\mid i\in I,i\neq j\Longleftrightarrow V_i\cap V_j=\emptyset\}$` for some [index set][bookofproofs$6198] `$i\in I$`. We want to construct a set `$Y$` containing exactly one element from each of these sets, i.e. we want to derive the [axiom of choice][bookofproofs$8041].
   * We define `$\mathcal F$` as the set of all non-empty [subsets][bookofproofs$552] of the respective disjoint sets `$V_i$`: `$$\mathcal F:=\{T_i\subseteq V_i\mid i\in I,\; T_i\neq\emptyset\}.$$`
   * Obviously, `$(\mathcal F,\preceq)$` is a [poset][bookofproofs$576] if and only if we set `$$T\preceq T^\prime\Longleftrightarrow T^\prime\subseteq T,$$` i.e. we consider `$T^\prime$` greater or equal `$T$` if `$T^\prime$` is a (non-empty) [subset][bookofproofs$552] of `$T.$` 
   * Note that `$T,T^\prime\in\mathcal F$` are only comparable by "`$\preceq$`" if they are subsets of the same original set `$V_i$` for some `$i\in I$` and one is contained in the other. This is because all `$V_i$` are disjoint.
   * By assumption, the Zorn's lemma is correct, i.e. if every [chain][bookofproofs$6191] `$C\subseteq \mathcal F$` that has an [upper bound][bookofproofs$7995], then `$\mathcal F$` contains at least one [maximal][bookofproofs$7995] element.
   * We have therefore first to check if every chain in `$\mathcal F$` has an upper bound.
      * Let `$C\subseteq\mathcal F$` be a chain, i.e. for all `$T,T^\prime\in C$` we have `$T^\prime\preceq T$` or `$T\preceq T^\prime.$`
      * By construction, since all pairs `$T$` and `$T^\prime$` in the chain `$C$` are only comparable, if they are subsets of the same original set `$V_i$` for some `$i\in I$` and one is contained in the other, we can identify exactly one `$V_i\in\mathcal F$` for which `$C$` is a chain. Therefore, can we write `$C_i$` for each chain `$C\in\mathcal F.$` 
      * In other words, in `$F$`, there exist only chains `$C_i$` that can be built from the subsets of the respective `$V_i,$` which are contained in each other.
      * Since all subsets are non-empty, by construction, for each chain `$C_i$` we can build the [set intersection][bookofproofs$6828] `$B_i:=\bigcap_{T\in C_i} T.$`
      * `$B_i$` is both, non-empty and, by construction, an element of each `$C_i$` for all `$i\in I.$`
      * Thus, for all `$i\in I,$` `$B_i$` is an [upper bound][bookofproofs$7995] of `$C_i$` since `$B_i\subseteq T$` for all `$T\in C_i.$` 
      * Thus, every chain in `$\mathcal F$` has an upper bound. 
   * It follows now from Zorn's lemma that `$\mathcal F$` has at least one [maximal][bookofproofs$7995] element.
   * In particular, it has at least one maximal element for each `$i\in I,$` namely a `$B_i,$` since only the subsets inside a single `$V_i$` are comparable.
   * Now, for all `$i\in I$`, the found example of a maximal element `$B_i$` must be a [singleton][bookofproofs$8034], i.e. containing exactly one element of `$V_i,$` otherwise it would either be empty (which it is not by construction) or not maximal with respect to the [partial order][bookofproofs$576] `$\preceq.$`
* Set `$Y:=\bigcup_{i\in I} B_i.$` We have constructed a set `$Y$` that contains exactly one element from the original disjoint sets `$V_i,$` `$i\in I.$`
* It follows the [axiom of choice][bookofproofs$8041].
