layout: example
categories: branches,theoretical-computer-science, formal-languages
nodeid: bookofproofs$8500
orderid: 50
parentid: bookofproofs$8498
title: Examples of DFA
description: EXAMPLES OF DFA ★ bring your math skills to the graduate level ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$1086,bookofproofs$7895
keywords: examples of dfa
contributors: bookofproofs

---


---

### Example 1

This DFA accepts words over the alphabet `$\{0,1,2,3,4,5,6,7,8,9\}$` and decides whether or not they denote a positive integer [divisible][bookofproofs$700] by `$5$`.


![dfa3](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/dfa3.png?raw=true)


For instance, the input word `$19403$` will lead to the states `$abbbab$`, and the end state `$b$` shows that `$19403$` is not divisible by `$5$`. The input word `$925$` will lead to the states `$abba$`, and the end state `$a$` shows that `$925$` is divisible by `$5$`.

### Example 2

This DFA accepts words over the alphabet `$\{0,1\}$` with exactly two `$1$`'s.


![dfa2](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/dfa2.png?raw=true)


If a string has more than two `$1$`'s, the DFA will enter the state `$d$` which is not demarked as final.

### Example 3

This DFA accepts words from the alphabet `$\{0,1\}$` containing an [even][bookofproofs$8130] number of `$1$`'s.  


![dfa4](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/dfa4.png?raw=true)

