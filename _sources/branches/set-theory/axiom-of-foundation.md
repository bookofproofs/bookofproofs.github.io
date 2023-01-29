layout: axiom
categories: branches,set-theory
nodeid: bookofproofs$717
orderid: 700
parentid: bookofproofs$1427
title: Axiom of Foundation
description: AXIOM OF FOUNDATION ★ bring your math skills to the graduate level ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$656,bookofproofs$983
keywords: axiom of foundation,foundation axiom,foundation postulate,postulate of foundation,axiom of regularity,axiom of foundation set theory
contributors: bookofproofs


---
The existence of a [singleton][bookofproofs$8034] `$\{X\}$` for every set `$X$` raises the question if both are equal. If we take the definition of [set equality][bookofproofs$6841] as a basis, then we must ask ourselves if `$X\subseteq \{X\}$` and if `$\{X\}\subseteq X$`. Certainly, `$X\in \{X\}$` by definition of the singleton, and, using the [axiom of separation][bookofproofs$675], we can separate this element to get a subset _containing_ the element `$X$` which is a subset of the initial singleton `$\{X\}.$` But this subset is again a singleton of `$X$`, by construction, and we get the trivial result `$\{X\}\subseteq \{X\}$`. By symmetry, we also get `$\{X\}\supseteq \{X\}$` and we only get the trivial result `$\{X\}=\{X\}.$`

Another approach to decide, if `$X=\{X\}$` would be to assume this and check if this assumption leads to a [contradiction][bookofproofs$744]. Let us try. Assume `$X=\{X\}$`. Since `$X\in \{X\}$`, we get `$X\in X,$` i.e. a set containing itself. Please note that even with the [axiom of extensionality][bookofproofs$551] we cannot decide, if such a set can exist. Obviously, if such a set existed, then we would allow never-ending chains `$\ldots\in X\in X\in\ldots\in X\in\ldots$` or circular referencec, like for instance in the following chain `$X\in X_1\in X_2\in X.$`

Therefore, we have to determine, if we want to allow such constructions in our set theory or not. The additional axiom of foundation forbids such constructions. It was added to the original set of axioms of "Zermelo":https://www.bookofproofs.org/history/ernst-friedrich-ferdinand-zermelo/ by "Fraenkel":https://www.bookofproofs.org/history/adolf-abraham-halevi-fraenkel/ and "von Neumann":https://www.bookofproofs.org/history/john-von-neumann/ and helps to avoid paradoxes mentioned in the [historical development of the set theory][bookofproofs$8012], which threw mathematics in a fundamental crisis at the beginning of the 20th century.

---

Every non-empty set `\(X\)` contains an element that is disjoint from `\(X\)`. This can be formalized as

`\[\forall X(X\neq\emptyset \Rightarrow\exists z(z\in X \wedge X\cap z=\emptyset)).\]`

Note: The following figure demonstrates this axiom for the singleton:


![axiomfoundation](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/axiomfoundation.png?raw=true)


and makes sure that `$X\neq \{X\}$` for all sets `$X.$`
