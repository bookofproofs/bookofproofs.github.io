layout: application
categories: branches,theoretical-computer-science, formal-languages
nodeid: bookofproofs$8505
orderid: 50
parentid: bookofproofs$8498
title: Application of the Rabin-Scott Theorem - the Rabin-Scott Algorithm
description: APPLICATION OF THE RABIN-SCOTT THEOREM - THE RABIN-SCOTT ALGORITHM ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$1086,bookofproofs$7895
keywords: application of the rabin-scott theorem,rabin-scott algorithm
contributors: bookofproofs


---


---

As an application of the [Rabin-Scott Theorem][bookofproofs$8503] we can design the following algorithm to change any given [NFA][bookofproofs$8501] `$(C,\Sigma,\Delta,F,s_0)$` to a corresponding [DFA][bookofproofs$8499] `$(C^\prime,\Sigma,\delta,F^\prime,s_0^\prime)$`.

1. Label in a table all columns with the symbols in the [alphabet][bookofproofs$708] `$\Sigma$`.
1. Set `$i=0$`.
1. Label the `$0$`-th row of the table with the [singleton][bookofproofs$8034] `$\{s_0\}$` of the starting state `$s_0$`.
1. Fill in the `$i$`-th row with the label `$s_i^\prime$` for each symbol `$\sigma\in \Sigma$` (column label) exactly the subset `$Q\subseteq C$` of states which can be reached in the NFA by applying `$\Delta$` to the pair `$(s_i^\prime,\sigma)$` 
1. Add as many new rows to the table, as there are new subsets `$Q\in C$` found in the previous row and label them with these subsets. Increment `$i$` by the number of rows added.
1. Repeat the procedure from step 4, until no more new subsets `$Q\in C$` are found.
1. Draw the diagram of the DFA accordingly, mark `$\{s_0\}$` as the starting state and those states `$s_i^\prime$` as final states of the DFA, which contain at least one final state of the NFA.

We want to apply this algorithm to one of the NFA shown in the [examples of NFA][bookofproofs$8502]:


![nfa2](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/nfa2.png?raw=true)


This NFA accepts the [language][bookofproofs$7842] `$L=\{10,101\}^*$`. The table created by the algorithm is this:

`$$\begin{array}{c|c|c|c}
i&s_i^\prime&1&0\\
\hline
0&\{a\}&\{b\}&\{\emptyset\}\\
1&\{b\}&\{\emptyset\}&\{a,c\}\\
2&\{\emptyset\}&\{\emptyset\}&\{\emptyset\}\\
3&\{a,c\}&\{a,b\}&\{\emptyset\}\\
4&\{a,b\}&\{b\}&\{a,c\}\\
\end{array}$$`

It is now clear that the rows of the table are labeled by the states of the constructed DFA. The number of these rows cannot (by the Rabin-Scott theorem) exceed `$2^3=8$`, which is the number of elements of the [power set][bookofproofs$6831] of the set of the states `$\{a,b,c\}$` of the given NFA. The resulting DFA can be drawn as


![dfa7](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/dfa7.png?raw=true)


Finally, we can re-label the nodes to make the drawing more concise, and we are done. We have found a DFA accepting exactly the same language as the given NFA. 


![dfa6](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/dfa6.png?raw=true)


Rabin and Scott were honored 1976 for their [paper](https://www.cse.chalmers.se/~coquand/AUTOMATA/rs.pdf) with the [Turing award](https://en.wikipedia.org/wiki/Turing_Award). They demonstrated that NFA and DFA provide an efficient model for the study of [formal languages][bookofproofs$94]. Moreover, they stimulated the theoretical computer science by their ideas of determinism and non-determinism of finite automata. They wrote:

> "A nondeterministic automaton is not a probabilistic machine but rather a machine with many choices in its moves. At each stage of its motion across a tape it will be at liberty to choose one of several new internal states. Of course, some sequence of choices will lead either to impossible situations from which no moves are possible or to final states not in the designated class `$F.$` We disregard all such failures, however, and agree to let the machine accept a tape if there is at least one winning combination of choices of states leading to a designated final state."
