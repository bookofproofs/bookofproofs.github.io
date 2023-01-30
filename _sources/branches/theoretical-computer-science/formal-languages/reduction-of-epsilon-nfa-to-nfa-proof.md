layout: proof
categories: branches,theoretical-computer-science, formal-languages
nodeid: bookofproofs$8534
orderid: 50
parentid: bookofproofs$8533
title: 
description: PROOF OF REDUCTION OF EPSILON-NFA TO NFA ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$1086
keywords: reduction of epsilon nfa to nfa,proof
contributors: bookofproofs

---


---

We will prove the theorem by showing the [set equality][bookofproofs$6841] `$\mathcal L(\epsilon-\operatorname{NFA})=\mathcal L(\operatorname{NFA}).$`

### `$\mathcal L(\operatorname{NFA}) "\subseteq" \mathcal L(\epsilon-\operatorname{NFA})$`

* The definition of the [non-deterministic finite automaton][bookofproofs$8501]. NFA is a special case of the definition of the [epsilon non-deterministic finite automaton][bookofproofs$8531] `$\epsilon$`-NFA.
* This is because we can replace a given NFA definition `$A=(C,\Sigma,\Delta_A,F,s_0),$` by replacing `$\Delta_A\subset (C\times\Sigma)\times C$` by a `$\Delta_B:=(C\times\Sigma^*)\times C,$` getting a definition of an `$\epsilon$`-NFA `$B=(C,\Sigma,\Delta_B,F,s_0)$`. In other words, we can replace the transition relation `$\Delta_A$` by a more generalized transition relation `$\Delta_B\supset\Delta_A$`.

### `$\mathcal L(\operatorname{NFA}) "\supseteq" \mathcal L(\epsilon-\operatorname{NFA})$`

* Let `$A=(C,\Sigma,\Delta,F,s_0)$` be an `$\epsilon$`-NFA. 
* We construct an NFA `$A^\prime=(C^\prime,\Sigma,\Delta^\prime,F,s_0)$` as follows: We do not have to replace the sets of [states][bookofproofs$8531] `$C$`, the alphabet `$\Sigma$`, the set of [final states][bookofproofs$8531] `$F$` and the [starting state][bookofproofs$8531] `$s_0$`.
   * Every transition of [symbols][bookofproofs$709] ([words][bookofproofs$708] of length `$1$`) remain unchanged, formally, `$$\Delta^\prime(s_i,\sigma)=s_{i+1}\Longleftrightarrow \Delta(s_i,\sigma)=s_{i+1}$$` for all `$s_i\in C$` and `$\sigma\in\Sigma$` 
 with `$\sigma\neq\epsilon.$`
   * Every transition `$\Delta$` of a word `$\omega=\sigma_1\ldots\sigma_n$` of length `$|\omega|=n\ge 2$` in the form `$\Delta(s,\omega)=q$`, `$s,q\in C$` is to be replaced by a chain of transitions of `$\Delta^\prime$` with some intermediate states `$p_\omega(1),\ldots,p_\omega(n-1)\in C^\prime$` with 
`$$\begin{array}{rcl}
\Delta^\prime(s,\sigma_1)&=&p_\omega(1)\\
\Delta^\prime(p_\omega(1),\sigma_2)&=&p_\omega(2)\\
\vdots&&\vdots\\
\Delta^\prime(p_\omega(n-2),\sigma_{n-1})&=&p_\omega(n-1)\\
\Delta^\prime(p_\omega(n-1),\sigma_n)&=&q\\
\end{array}$$`
   * Every transition `$\Delta$` of the [empty word][bookofproofs$708] `$\epsilon$` in the form `$\Delta(s,\epsilon)=q$`, `$s,q\in C$` is to be replaced as follows: We look for any predecessor state of `$s$` in `$A^\prime$`, i.e. a transition of the form `$\Delta^\prime(t,a)=s$`. If such a predecessor state can be found, we add the transition `$\Delta^\prime(t,a)=q$`. Otherwise, (i.e. we cannot find any such predecessor transition), there shall be neither a direct transition `$\Delta^\prime$` from the state `$s$` to the state `$q.$`
   * We replace `$C$` by the set `$C^\prime:=C\cup\{\text{all states added in the construction process}\}$`. 
* It follows by construction, that `$A^\prime$` is an [NFA][bookofproofs$8501] accepting exactly the same words as the original [$\epsilon$-NFA][bookofproofs$8531].
