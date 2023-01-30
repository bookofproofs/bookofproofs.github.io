layout: chapter
categories: branches,theoretical-computer-science, formal-languages
nodeid: bookofproofs$8498
orderid: 500
parentid: bookofproofs$78
title: Finite Automata (Finite Sequential Machines)
description: FINITE AUTOMATA FINITE SEQUENTIAL MACHINES ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$1086,bookofproofs$7895
keywords: finite automata,finite sequential machine,finite sequential machines,fsm,fa
contributors: bookofproofs

---


---

Many technical machines (for instance an ATM) have a different number of states (e.g. off, idle, customer authentication, selecting transaction, transaction, out of service, etc.) and their complexity grows with the growing number of states. _Finite automata_ are models helping to systematically describe such systems. These can be technical systems and machines (like an ATM), but, surprisingly, we can also use finite automata to solve theoretical problems in conjunction with [formal languages][bookofproofs$94], which will be shown to be very good models of computation.

The following example illustrates the concept of a finite automaton. The example has two states `$a$` and `$b$`. The state `$a$` is the starting state (denoted by an incoming arrow `$\downarrow$`). At the same time, the states `$a$` and `$b$` are end states (denoted by double circles). The automaton accepts [strings][bookofproofs$708] which are decimal numbers, reads them digit by digit from left to right and ends at the state `$a$` if and only if the number is divisible by `$5$`, otherwise the end state will be `$b$`.


![dfa1](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/dfa1.png?raw=true)




In this section, we will learn about different types of finite automata (FA), including:
* FA without an output (so-called _acceptors_):
   * DFA - deterministic finite automata
   * NFA - non-deterministic finite automata
   * `$\epsilon$`-NFA - `$\epsilon$` non-deterministic automata
* FA with output (so-called _transducers_):
   * Moore Machine
   * Mealy Machine
