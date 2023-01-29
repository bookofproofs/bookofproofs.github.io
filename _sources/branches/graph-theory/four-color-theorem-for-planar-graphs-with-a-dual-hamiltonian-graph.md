layout: theorem
categories: branches,graph-theory
nodeid: bookofproofs$8462
orderid: 400
parentid: bookofproofs$8453
title: Four Color Theorem for Planar Graphs With a Dual Hamiltonian Graph
description: FOUR COLOR THEOREM FOR PLANAR GRAPHS WITH A DUAL HAMILTONIAN GRAPH ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$1591
keywords: four color theorem for planar graphs with a dual hamiltonian graph
contributors: bookofproofs

---
The proof of the [four color theorem for planar graphs][bookofproofs$8458] found in 1976 was computer-assisted. Due to its complexity, it cannot be directly verified by humans. Only the validity of the proving computer algorithm can be verified. This is a highly unsatisfactory situation for mathematicians. In fact, some mathematicians do not accept computer-assisted proofs as mathematical proofs. 

The following theorem is a direct implication of the [characterization of planar hamiltonian graphs][bookofproofs$6400] proved by me in 2014. To my knowledge (as of 2020) it is also one of only a few strict proofs of a special instance of the 4-color theorem, which can be verified by humans.

---

Let `$G$` be a [simple][bookofproofs$523], [connected][bookofproofs$1166], [planar][bookofproofs$1226] graph. If the [dual graph][bookofproofs$6391] `$G^*$` is [Hamiltonian][bookofproofs$6349], then the [chromatic number][bookofproofs$8448] of `$G$` obeys the following inequality `$$\chi(G)\le 4.$$`

### Notes

* This is a solution of the _4-color conjecture_ for special kinds of maps, in which the country borders allow a circular tour without visiting a border edge twice (i.e. a point at a border, at which more than two countries meet each other). In this case, the faces of `$G ^*$` and the vertices of `$G$` correspond to the countries and the edges of `$G^*$` are the country borders.
* In other words, the faces in a [planar drawing][bookofproofs$1212] of a Hamiltonian graph `$G^*$` can be colored with at most 4 colors.
