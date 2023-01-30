layout: proof
categories: branches,theoretical-computer-science, formal-languages
nodeid: bookofproofs$8504
orderid: 50
parentid: bookofproofs$8503
title: 
description: PROOF OF RABIN-SCOTT THEOREM ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$1086,bookofproofs$7895
keywords: rabin-scott theorem,proof
contributors: bookofproofs

---


---

We will prove the theorem by showing the [set equality][bookofproofs$6841] `$\mathcal L(\operatorname{NFA})=\mathcal L(\operatorname{DFA}).$`

### `$\mathcal L(\operatorname{DFA}) "\subseteq" \mathcal L(\operatorname{NFA})$`

* The definition of the [deterministic finite automaton][bookofproofs$8499]. DFA is a special case of the definition of the [non-deterministic finite automaton][bookofproofs$8501]. NFA.
* This is because in a given DFA definition `$A=(C,\Sigma,\delta,F,s_0),$` we just have to replace `$s_0$` by the set `$S=\{s_0\}$` and the [function][bookofproofs$592] `$\delta$` is a special case of a [relation][bookofproofs$571] `$\Delta$` (in fact, every function is a [left-total][bookofproofs$1308], [right-unique][bookofproofs$1308] relation. 
* With these replacements, we have `$A=(C,\Sigma,\Delta,F,S)$` as a special case of an NFA.

just to replace the function definition by the other by replacing the function `$\d


### `$\mathcal L(\operatorname{DFA}) "\supseteq" \mathcal L(\operatorname{NFA})$`

* Let `$A=(C,\Sigma,\Delta,F,s_0)$` be an NFA. 
* We construct a DFA `$A^\prime=(C^\prime,\Sigma,\delta,F^\prime,s_0^\prime)$` by making the following replacements:
   * We replace the set of states `$C$` of the NFA by the [power set][bookofproofs$6831] of `$C$`, i.e. `$$C^\prime:=\mathcal P( C).$$` Note that the power set has also [finitely many][bookofproofs$985] elements, just like `$C$` has.
   * We set the [starting state][bookofproofs$8499] of the DFA to `$$s_0^\prime:=\{s_0\}\in C^\prime$$` (the [singleton][bookofproofs$8034] containing the [starting state][bookofproofs$8501] of the NFA).
   * Note that if for a [string][bookofproofs$708] `$\sigma_0,\sigma_1,\ldots,\sigma_n\in\Sigma^*$` the NFA is in a state `$q$`, this means by the definition of `$L(\operatorname{NFA})$` that there is a starting state `$s_0\in S$` with `$q=\Delta(\ldots\Delta(\Delta(s_0,\sigma_0),\sigma_1),\ldots,\sigma_n)\in F$`.
   * We define for all words `$\sigma_0,\sigma_1,\ldots,\sigma_n\in\Sigma^*$` and all states `$Q\in C^\prime$` the function `$\delta:(C^\prime\times \Sigma^*)\to C^\prime$` by `$$\delta(\ldots\delta(\delta(s_0,\sigma_0),\sigma_1),\ldots,\sigma_n)=Q\in C^\prime\Longleftrightarrow \exists s_0\in S,\; \Delta(\ldots\Delta(\Delta(\{s_0\},\sigma_0),\sigma_1),\ldots,\sigma_n)=q\in Q\subseteq C$$`
   * This means, we define the DFA to be exactly in the [state][bookofproofs$8499] `$Q\in C^\prime,$` if and only if for the same word the corresponding NFA produces one of the states `$q\in Q\subseteq C.$` 
   * The [final states][bookofproofs$8499] `$F^\prime$` will be defined by all `$Q\in C^\prime$` containing at least one [final state][bookofproofs$8499] `$q\in F$`, in other words, `$$F^\prime:=\{Q\in C^\prime\mid Q\cap F\neq\emptyset\}.$$`
* It follows by construction, that `$A^\prime$` is a [DFA][bookofproofs$8499] accepting exactly the same words as the given [NFA][bookofproofs$8501].
