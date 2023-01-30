layout: application
categories: branches,theoretical-computer-science, formal-languages
nodeid: bookofproofs$8535
orderid: 50
parentid: bookofproofs$8498
title: Application of the Theorem to Reduce `$\epsilon$`-NFA to NFA
description: APPLICATION OF THE THEOREM TO REDUCE EPSILON-NFA TO NFA ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$1086,bookofproofs$7895
keywords: application of the theorem to reduce epsilon nfa to nfa
contributors: bookofproofs

---


---

The following are examples to apply the construction given in the proof of the [theorem about the reduction of `$\epsilon$`-NFA to NFA][bookofproofs$8533], reducing the [examples of `$\epsilon$`-NFA][bookofproofs$8532] to the corresponding NFA.

### Ad Example `$(2)$`


![epsilonnfa2reduced](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/epsilonnfa2reduced.png?raw=true)


Please note that in this example, the intermediate states `$p_{01}(1), p_{101}(1)$` and `$p_{101}(2)$` have been added to reflect transitions marked by words with length `$\ge 2$` in the original graph of the second `$\epsilon$`-NFA example. Also, the original `$\epsilon$` transition from the state `$a$` to the state `$b$` disappeared, since there is no predecessor state `$t$` and symbol `$x\in\{0,1\}$` such that `$\Delta^\prime(t,x)=a.$`


### Ad Example `$(3)$`


![epsilonnfa1reduced](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/epsilonnfa1reduced.png?raw=true)


In this example, no new intermediate states are needed to reduce the original `$\epsilon$`-NFA to an NFA. However, we have to deal with the original `$\epsilon$` transitions between the states `$a\to b$` and `$b\to c$` and replace them according to the construction in the [proof][bookofproofs$8533]proof/. The construction steps are as follows:

1. We first take over all loop transitions `$a\to a$` via `$1$`, `$b\to b$` via `$2$` and `$c\to c$` via `$3$`. Those remain unchanged since they use words of length `$1.$`
1. Dealing with `$a\to b$` via the empty word `$\epsilon$` in the original graph: There is only one predecessor transition of `$a$` in the new graph, namely `$\Delta^\prime(a,1)=a.$` Therefore, we add `$\Delta^\prime(a,1)=b.$`
1. Dealing with `$a\to b$` via the empty word `$\epsilon$` in the original graph: There is only one predecessor transition of `$a$` in the new graph, namely `$\Delta^\prime(a,1)=a.$` Therefore, we add `$\Delta^\prime(a,1)=b.$`
