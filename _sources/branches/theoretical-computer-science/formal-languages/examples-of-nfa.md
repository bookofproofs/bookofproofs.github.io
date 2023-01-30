layout: example
categories: branches,theoretical-computer-science, formal-languages
nodeid: bookofproofs$8502
orderid: 50
parentid: bookofproofs$8498
title: Examples of NFA
description: EXAMPLES OF NFA ★ bring your math skills to the graduate level ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$1086,bookofproofs$7895
keywords: examples of nfa
contributors: bookofproofs

---


---

[Non-deterministic finite automata][bookofproofs$8501] can be illustrated using diagrams like it was the case for the [DFA][bookofproofs$8500].
### Example 1 - Every DFA is an example of an NFA

Please note that the [NFA][bookofproofs$8501] definition is more general than the DFA definition since it replaces a [function][bookofproofs$592] `$\delta$` by a [relation][bookofproofs$571] `$\Delta$` (every function is a relation but not every relation is a function).

### Example 2

The following example of an NFA accepts all [strings over the alphabet][bookofproofs$708] `$\{0,1\}$` whose second to the last symbol is `$1.$`


![nfa1](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/nfa1.png?raw=true)


Note that the same strings can be accepted by this, more complex, [DFA][bookofproofs$8499]:


![dfa5](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/dfa5.png?raw=true)


### Example 3

The following example of an NFA accepts all [strings over the alphabet][bookofproofs$708] `$\{0,1\}$` that are concatenations of `$10$` and `$101$`. In other words, the language accepted by the NFA is `$\{10,101\}^*$`:


![nfa2](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/nfa2.png?raw=true)


As in example 2, the same strings can be accepted by another, much more complex, [DFA][bookofproofs$8499]:


![dfa6](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/dfa6.png?raw=true)

