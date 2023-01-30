layout: definition
categories: branches,theoretical-computer-science, formal-languages
nodeid: bookofproofs$8531
orderid: 50
parentid: bookofproofs$8498
title: Epsilon Non-Deteriministic Finite Automaton (`$\epsilon$`-NFA)
description: EPSILON NON-DETERIMINISTIC FINITE AUTOMATON EPSILON-NFA ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$1086,bookofproofs$7895
keywords: epsilon nfa,epsilon non-deterministic finite automata,epsilon non-deterministic finite automaton,condition,state,conditions,states,final state,final states,starting state,starting states,final condition,final conditions,starting condition,starting conditions,accepts,accept,accepting
contributors: bookofproofs


---
We have seen that the non-deterministic finite automata [NFA]https://www.bookofproofs.org/branches/non-deterministic-finite-automata-nfa/ provide ways to simplify the diagrams of finite automata describing [formal languages][bookofproofs$94], as compared to the [deterministic finite automata][bookofproofs$8499]. DFA. The so-called _epsilon non-deterministic finite automata_ `$\epsilon$`-NFA add yet another concept to the NFA allowing even more simplifications of the diagrams. However, the simplifications introduced by `$\epsilon$`-NFA will not substantially increase the set of languages that can be described as a whole. We will prove that every `$\epsilon$`-NFA can be reduced to a suitable [deterministic finite automaton][bookofproofs$8499], just as it was the case for the usual NFA.

---

An *epsilon non-deterministic finite automaton* (*$\epsilon$-NFA*) is a [tuple][bookofproofs$747] `$A=(C,\Sigma,\Delta,F,s_0)$`, containing

* a [finite set][bookofproofs$985] `$C$` of conditions (or states),
* a finite input [alphabet][bookofproofs$708] `$\Sigma$`,
* the state transition [relation][bookofproofs$571] `$\Delta\subseteq (C\times\Sigma^*)\times  C$`, 
* the set of **final states** `$F\subseteq C$`, and
* the **starting state** `$s_0\in C.$`

We say that the `$\epsilon$`-NFA **accepts** an input [word][bookofproofs$708] `$\omega$` if and only if the `$\epsilon$`-NFA reaches a final state `$q\in F$` after consuming `$\omega,$` starting at `$s_0\in S$`.

The [formal language][bookofproofs$94] `$L(\epsilon-\operatorname{NFA})$` **accepted by** the `$\epsilon$`-NFA can be defined as a set of all [words over the alphabet][bookofproofs$708] `$\Sigma$`, which can be consumed by the [composition of the relation][bookofproofs$1309] `$\Delta$` with itself, starting from some state in `$s_0\in S$`, and ending at some state in `$q\in F,$` formally: `$$L(\epsilon-\operatorname{NFA}):=\{\omega_i\in\Sigma^*, \omega_0\omega_1\ldots\omega_n\in\Sigma^*\mid \exists s_0\in S,\; q=\Delta(\ldots\Delta(\Delta(s_0,\omega_0),\omega_1),\ldots,\omega_n)\in F\}.$$`

The *class of all languages accepted by an `$\epsilon$`-NFA* is denoted by `$\mathcal L(\epsilon-\operatorname{NFA})$`.

### Notes

* The `$\epsilon$`-NFA is an acceptor since it has no output, only an input (just as it was the case for the [DFA][bookofproofs$8499] and the [NFA][bookofproofs$8501]).
* Unlike in the case of a usual NFA, the transition relation `$\Delta$` of an `$\epsilon$`-NFA takes a pair `$(s_i,\omega_i)$` as input, where `$\omega_i$` can be a whole word in `$\Sigma^*$`, including the [empty word][bookofproofs$708] `$\epsilon\in\Sigma^*.$` 
* Note the difference: In the case of a usual NFA, the input was `$(s_i,\sigma_i)$`, where `$\sigma_i$` could be only a symbol in `$\Sigma$`. Therefore, the `$\epsilon$`-NFA can do a transition from one state to another also with a whole word (including `$\epsilon$`). Its transitions in a diagram (when we draw a diagram for the `$\epsilon$`-NFA) can be labeled with whole words, not only symbols, including `$\epsilon$`.
* Another important difference is that `$\epsilon$` can be excepted even if the starting state is not one of the final states.
* Whether or not an `$\epsilon$`-NFA can start with an input `$\omega$`, depends on this word `$\omega$` and the definition of the transition relation `$\Delta$` for the pair of values `$(s_0,\omega)$`. If that transition relation `$\Delta$` is _not_ defined for this pair, the `$\epsilon$`-NFA cannot start accepting the word, unless (!) `$\Delta$` is defined for the input `$(s_0,\epsilon).$` This is because `$\omega=\epsilon\omega$`, and the `$\epsilon$`-NFA could start accepting `$(s_0,\omega)$` by first changing its state from `$s_0$` to `$s_1$` by consuming the empty word and then start to accept `$\omega$` from the state `$s_1$`.
* Similarly to a usual NFA, `$\Delta$` can be _any_ relation and does not have to be [left-total][bookofproofs$1308] nor [right-unique][bookofproofs$1308] (like it was the case for the function `$\delta$` in a [DFA][bookofproofs$8499]). This means that the new state `$\Delta(s_0,\omega_0)$` is either necessarily defined _for all_ possible inputs, nor _determined_. Potentially, there might be many outcomes in the `$i$`th step of `$\Delta(s_i,\omega_i)$` or none.
* The only accepted [words][bookofproofs$708] `$\omega$` are concatenations of (empty or non-empty other words) `$\omega_0\omega_1\ldots \omega_{n-1}$` leading to a state `$s_n\in F.$` 
* Non-excepted words will make the `$\epsilon$`-NFA get stuck in a loop at some non-final state, or the `$\epsilon$`-NFA won't even start at all (similarly as for the NFA).
