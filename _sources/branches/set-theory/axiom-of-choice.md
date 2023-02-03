layout: axiom
categories: branches,set-theory
nodeid: bookofproofs$8041
orderid: 1000
parentid: bookofproofs$1427
title: Axiom of Choice
description: AXIOM OF CHOICE ★ bring your math skills to the graduate level ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$656,bookofproofs$983
keywords: axiom of choice,choice postulate,choice
contributors: bookofproofs


---
The last axiom of the Zermelo-Frankel axioms is an axiom developed by <a href="https://mathshistory.st-andrews.ac.uk/Biographies/Zermelo/">Zermelo</a>. The axiom ensures the possibility of selecting elements from sets and forming a completely new set out of these elements. This axiom is needed to ensure the existence of a [quotient set][bookofproofs$7991] of a given [equivalence class][bookofproofs$7990] - a very important concept in mathematics.

The assumption that we can always choose elements from sets is an idealization, and it had been controversially discussed whether the axiom is really independent of the other Zermelo-Fraenkel (ZF) axioms or can be somehow derived from them. In 1938, <a href="https://mathshistory.st-andrews.ac.uk/Biographies/Godel/">Kurt Gödel</a> (1906 - 1978) proved that this assumption is [consistent][bookofproofs$7887] with the remaining ZF axioms. A quarter of a century later, 
[Paul Cohen](https://mathshistory.st-andrews.ac.uk/Biographies/Cohen/) (1934 - 2007) proved that also its negation is consistent with the remaining ZF axioms. In other words, the axiom of choice is undecidable among the other ZF axioms and it is natural to add it to the system ZF. This extended system of axioms is usually abbreviated by **ZFC**.

---

For every set `$X$` of disjoint and non-empty sets there is a set `$Y$` containing exactly one element from each of these sets. Formally,

`$$\begin{array}{rll}
\forall x(\\
&\forall uw(\\
&&(u\in x\wedge w\in x \Rightarrow u\neq \emptyset\wedge (u=w\vee u\cap w=\emptyset))\\
&&\Rightarrow\\
&&(\exists y(\forall v(v\in x\Rightarrow \exists z(y\cap v=\{z\}))))\\
&)\\
).&
\end{array}$$`



![axiomchoice](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/axiomchoice.png?raw=true)

