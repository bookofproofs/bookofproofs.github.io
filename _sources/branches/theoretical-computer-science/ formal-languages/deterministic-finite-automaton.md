layout: definition
categories: branches,theoretical-computer-science, formal-languages
nodeid: bookofproofs$8499
orderid: 50
parentid: bookofproofs$8498
title: Deterministic Finite Automaton (DFA)
description: DETERMINISTIC FINITE AUTOMATON (DFA) ★ bring your math skills to the graduate level ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$1086,bookofproofs$7895
keywords: deterministic finite automaton,dfa,condition,state,conditions,states,final state,final states,starting state,starting states,final condition,final conditions,starting condition,starting conditions,accepts,accept,accepting,deterministic finite automata
contributors: bookofproofs

---
We start with a formal definition of a _deterministic finite automaton_.

---

A **deterministic finite automaton**  **DFA**) is a [tuple][bookofproofs$747] `$A=(C,\Sigma,\delta,F,s_0)$`, containing

* a [finite set][bookofproofs$985] `$C$` of conditions (or states),
* a finite input [alphabet][bookofproofs$708] `$\Sigma$`,
* the state transition [function][bookofproofs$592] `$\delta:C\times\Sigma\to C$`,
* the set of **final states** `$F\subseteq C$`, and
* the **starting condition** `$s_0.$`

We say that the DFA **accepts** an input [word][bookofproofs$708] `$\omega$` if and only if the DFA reaches a final condition `$f\in F$` after consuming `$\omega.$`

The [formal language][bookofproofs$94] `$L(\operatorname{DFA})$` **accepted by** the DFA can be defined as a set of all [words over the alphabe][bookofproofs$708]t `$\Sigma$`, for which the [image][bookofproofs$592] of [function compositions][bookofproofs$1314] of `$\delta$` is contained in `$F,$` formally: `$$L(\operatorname{DFA}):=\{\sigma_0\sigma_1\ldots\sigma_n\in\Sigma^*\mid \delta(\ldots\delta(\delta(s_0,\sigma_0),\sigma_1),\ldots,\sigma_n)\in F\}.$$`

The **class of all languages accepted by a DFA** is denoted by `$\mathcal L(\operatorname{DFA})$`.

### Notes

* The DFA is an acceptor since it has no output, only input.
* It starts at the starting condition `$s_0.$`
* An input [word][bookofproofs$708] `$\omega=\sigma_0\sigma_1\ldots\sigma_n$` changes the states of the DFA by the formula `$s_{i+1}:=\delta(s_i,\sigma_i)$`. In other words, the transition function `$\delta$` calculates for each symbol `$\sigma_i$`, given the current state `$s_i$`, the new state `$s_{i+1}.$` 
* The DFA is always deterministic, since `$\delta$` is a [function][bookofproofs$592] (it is [right-unique][bookofproofs$1308], the new state `$s_{i+1}$` is always completely determined by the current state `$s_i$` and the current symbol `$\sigma_i.$`) 
* Whether or not the DFA accepts the [empty word][bookofproofs$708] `$\epsilon\in\Sigma^*$` can be read immediately from the definition of the DFA. This is the case if and only if `$s_0\in F$`, i.e. the starting condition is also one of its final states.
