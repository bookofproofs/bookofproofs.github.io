layout: example
categories: branches,theoretical-computer-science, formal-languages
nodeid: bookofproofs$8532
orderid: 50
parentid: bookofproofs$8498
title: Examples of `$\epsilon$`-NFA
description: EXAMPLES OF EPSILON-NFA; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$1086,bookofproofs$7895
keywords: examples of epsilon nfa
contributors: bookofproofs

---


---

[$\epsilon$-NFA][bookofproofs$8531] can be illustrated using diagrams like it was the case for the [DFA][bookofproofs$8500] and the [NFA][bookofproofs$8501].
### Example 1 - Every NFA is an example of an `$\epsilon$`-NFA

Please note that the `$\epsilon$`-NFA are more general than [NFA][bookofproofs$8501]. Their definition include NFA as a special case. Of course, also the [DFA][bookofproofs$8499] are included as a special case.

### Example 2

The following example of an `$\epsilon$`-NFA accepts all [strings over the alphabet][bookofproofs$708] `$\{0,1\}$` with the following structure `$$L=\{101\}^*\{0\}\{0\}^*\cup\{101\}^*\{1\}\cup \{01\}$$`


![epsilonnfa2](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/epsilonnfa2.png?raw=true) 


### Example 3

The following example of an `$\epsilon$`-NFA accepts all [strings over the alphabet][bookofproofs$708] `$\{1,2,3\}$` with the following structure `$$L=\{1^i2^j3^k\mid i,j,k\in\mathbb N\}$$`


![epsilonnfa1](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/epsilonnfa1.png?raw=true) 


The empty word `$\epsilon$` will be accepted, although `$a$` is not one of the [final states][bookofproofs$8531].
