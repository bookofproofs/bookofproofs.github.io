layout: example
categories: branches,topology
nodeid: bookofproofs$8615
orderid: 50
parentid: bookofproofs$129
title: Example of Continuous Functions in Topological Spaces
description: EXAMPLE OF CONTINUOUS FUNCTIONS IN TOPOLOGICAL SPACES &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$8336,bookofproofs$8560,bookofproofs$8613
keywords: examples of continuous functions in topological spaces
contributors: bookofproofs

---


---

### Example 1

The [identity function][bookofproofs$371] `$id:X\to X$` on any given [topological space][bookofproofs$6189] `$(X,\mathcal O)$` is [continuous][bookofproofs$8583].
### Example 2

If `$(X,\mathcal O_X)$` and `$(Y,\mathcal O_Y)$` are [topological spaces][bookofproofs$6189], then the [constant function][bookofproofs$6342] `$f:X\to Y$`, `$f(x)=y\in Y$` for all `$x\in X$` is continuous, since for an `$B\subseteq Y$` we have
* either `$f^{-1}[B]=\emptyset,$` if `$y\not\in B,$`
* or `$f^{-1}[B]=X,$` if `$y\in B.$`

Both, `$\emptyset$` and `$X$` are open in `$X$` by definition of [topological space][bookofproofs$6189].

### Example 3

Consider `$(X,\mathcal O_X)$` and `$(Y,\mathcal O_Y)$` as [topological spaces][bookofproofs$6189]. The continuity of `$f:X\to Y$` depends on both topologies, `$\mathcal O_X$` and `$\mathcal O_Y.$` For instance:

* If `$\mathcal O_X$` is the [discrete topology][bookofproofs$8557] and `$\mathcal O_Y$` is the [indiscrete topology][bookofproofs$8557], then every [function][bookofproofs$592] `$f:X\to Y$` is continuous.
* If `$\mathcal O_X$` is the [indiscrete topology][bookofproofs$8557] and `$\mathcal O_Y$` is the [discrete topology][bookofproofs$8557], then only the [constant functions][bookofproofs$592] `$f:X\to Y$` are continuous.

### Example 4

If `$f:X\to Y$` is a continuous function defined on two topological spaces `$(X,\mathcal O_X)$` and `$(Y,\mathcal O_Y)$`, then `$f$` remains continuous if we replace the [topology][bookofproofs$6189] `$\mathcal O_X$` by a [finer][bookofproofs$8559] one, and the topology `$\mathcal O_Y$` by a [coarser][bookofproofs$8559] one.
