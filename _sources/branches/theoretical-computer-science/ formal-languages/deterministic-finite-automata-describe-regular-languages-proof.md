layout: proof
categories: branches,theoretical-computer-science, formal-languages
nodeid: bookofproofs$8539
orderid: 50
parentid: bookofproofs$8538
title: 
description: PROOF OF DETERMINISTIC FINITE AUTOMATA DESCRIBE REGULAR LANGUAGES &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$1086,bookofproofs$7895
keywords: deterministic finite  automata describe regular languages,proof
contributors: bookofproofs

---


---

* We first show that every language `$L$` accepted by a [deterministic finite automaton][bookofproofs$8499] `$DFA$` is [regular][bookofproofs$8494].
   * Let `$DFA=(C,\Sigma,\delta,F,s_0)$` be a [deterministic finite automaton][bookofproofs$8499].
   * We construct a [grammar][bookofproofs$709] `$G=(V,T,R,S)$` corresponding to the DFA as follows: 
      * Set `$T=\Sigma$`, i.e. the terminal symbols of the grammar are the alphabet `$\Sigma.$`  
      * Set `$A_0\in V$` to correspond to the [starting state][bookofproofs$8499] `$s_0.$` 
      * Interprete all other states `$s\in C$` of the DFA as some other variables `$A_i$` of `$G$` i.e. for every `$s_i\in C$` there is a variable `$A_i\in V$` and vice versa (and `$A_0$` stands for the starting state `$s_0.$`) 
      * Every state transition `$s_{i+1}=\delta(s_i,\sigma)$` of the DFA can be interpreted as a production rule `$A_i\to \sigma A_{i+1}\in R.$`
      * If `$s_{i+1}\in F$` is a [final state][bookofproofs$8499], we add `$A_{i+1}\to\epsilon$` to the rules, in order to stop the construction of the word in `$G$` exactly at the same time when the DFA stops at a final state. 
      * By this construction, the grammar `$G$` [generates the language][bookofproofs$94] of the given DFA, i.e. `$L(G)=L(\operatorname{DFA}).$`
      * Moreover, it is a grammar of a [regular language][bookofproofs$8494], since the conclusion `$Q$` of every production `$P\to Q\in R$` is either the empty string `$\epsilon$` or it is a [concatenation][bookofproofs$708] of some non-empty string of [terminals][bookofproofs$709] ending with a [variable][bookofproofs$709] `$\sigma A_{i+1}$` (in other words, `$G$` is [right-linear][bookofproofs$8494]).
* Now, we show that for every regular language there is a DFA accepting it.
   * Let `$G=(V,T,R,S)$` be a grammar of a [regular language][bookofproofs$8494], 
   * It suffices to find a [non-deterministic finite automaton][bookofproofs$8501] `$NFA=(C,\Sigma,\Delta,F,s_0)$` which accepts the same language. It will then follow from [Rabin-Scott theorem][bookofproofs$8503], than there is an appropriate DFA.
      * Set `$\Sigma=T$`, i.e. the alphabet of the NFA are exactly the terminal symbols of the grammar `$G$`. 
      * Create a separate state `$s_i\in C$` of the NFA or every variable `$A_i\in V$` of the grammar `$G.$`
      * Since `$G$` is regular, every production rule is [left-linear][bookofproofs$8494] or [right-linear][bookofproofs$8494].
      * Without loss of generality[^1], let `$G$` be right-linear, i.e. let every of its production rules be either of the form `$A_i\to\epsilon$` or `$A_i\to \sigma A_{i+1}.$`
      * In the case `$A_i\to \sigma A_{i+1},$` we mark the transition from the state `$s_i$` to the state `$s_{i+1}$` of the NFA with `$\sigma.$`
      * In the case `$A_i\to \epsilon,$` the state `$s_i$` is a [final state][bookofproofs$8501] of the `$NFA,$` i.e. we set `$F=\{s_k\mid (A_k\to\epsilon)\in R\}.$`
      * Note, that `$NFA$` is in general non-deterministic since the grammar `$G$` can have more than one production rule for a variable `$A_i$` and an input character `$\sigma.$` 

[^1]: A similar construction can be found for left-linear grammars. It is left for the reader as an exercise to recognize that the argument works also for left-linear grammars.
