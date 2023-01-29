layout: definition
categories: branches,theoretical-computer-science, formal-languages
nodeid: bookofproofs$8501
orderid: 50
parentid: bookofproofs$8498
title: Non-deterministic Finite Automaton (NFA)
description: NON-DETERMINISTIC FINITE AUTOMATON (NFA) ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$1086,bookofproofs$7895
keywords: non-deterministic finite automata,non-deterministic finite automaton,nfa,condition,state,conditions,states,final state,final states,starting state,starting states,final condition,final conditions,starting condition,starting conditions,accepts,accept,accepting
contributors: bookofproofs

---
The [DFA][bookofproofs$8499] are deterministic. It means that if a DFA reads in a state `$c_i$` the symbol `$\sigma_i$`, the next state `$c_{i+1}$` is fixed and pre-determined. There are also _non-deterministic finite automata_ which can have many - or none - possible next states. A formal definition of such automata follows.

---

A *non-deterministic finite automaton*  **NFA**) is a [tuple][bookofproofs$747] `$A=(C,\Sigma,\Delta,F,s_0)$`, containing

* a [finite set][bookofproofs$985] `$C$` of conditions (or states),
* a finite input [alphabet][bookofproofs$708] `$\Sigma$`,
* the state transition [relation][bookofproofs$571] `$\Delta\subseteq (C\times\Sigma)\times  C$`, 
* the set of **final states** `$F\subseteq C$`, and
* the **starting state** `$s_0\in C.$`

We say that the NFA **accepts** an input [word][bookofproofs$708] `$\omega$` if and only if the NFA reaches a final state `$q\in F$` after consuming `$\omega,$` starting at `$s_0\in S$`.

The [formal language][bookofproofs$94] `$L(\operatorname{NFA})$` **accepted by** the NFA can be defined as a set of all [words over the alphabet][bookofproofs$708] `$\Sigma$`, which can be consumed by the [composition of the relation][bookofproofs$1309] `$\Delta$` with itself, starting from some state in `$s_0\in S$`, and ending at some state in `$q\in F,$` formally: `$$L(\operatorname{NFA}):=\{\sigma_0\sigma_1\ldots\sigma_n\in\Sigma^*\mid \exists s_0\in S,\; q=\Delta(\ldots\Delta(\Delta(s_0,\sigma_0),\sigma_1),\ldots,\sigma_n)\in F\}.$$`

The **class of all languages accepted by an NFA** is denoted by `$\mathcal L(\operatorname{NFA})$`.

### Notes

* The NFA is an acceptor since it has no output, only an input.
* Whether it can start or not with the input `$\omega$`, depends on the first symbol `$\sigma_0$` of the input, and the definition of the transition relation `$\Delta$` for the pair of values `$(s_0,\sigma_0)$`. If that transition relation `$\Delta$` is _not_ defined for this pair, the NFA cannot start accepting the word. This is one important difference to the definition of the DFA, in which the function `$\delta$` is (since a function) a [left-total][bookofproofs$1308] relation. `$\Delta$` can be any relation and does not have to be left-total.
* Another important definition is this: The relation `$\Delta$` does have to be [right-unique][bookofproofs$1308] (like it was the case for the function `$\delta$` in a DFA). This means that the new state `$\Delta(s_0,\sigma_0)$` is not determined. Potentially, there might be many outcomes in the `$i$`th step of `$\Delta(s_i,\sigma_i)$`.
* Only accepted [words][bookofproofs$708] `$\omega=\sigma_0\sigma_1\ldots \sigma_{n-1}$` will lead to a state `$s_n\in F.$` Non-excepted words will make the NFA get stuck in a loop at some non-final state, or the NFA won't even start at all.
* Whether or not the NFA accepts the [empty word][bookofproofs$708] `$\epsilon\in\Sigma^*$` can be read immediately from the definition of the NFA. This is the case if and only if `$s_0\in F.$`
