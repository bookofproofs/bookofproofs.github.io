layout: theorem
categories: branches,graph-theory
nodeid: bookofproofs$6400
orderid: 200
parentid: bookofproofs$6349
title: Characterization of Planar Hamiltonian Graphs
description: CHARACTERIZATION OF PLANAR HAMILTONIAN GRAPHS ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$1591
keywords: characterization of hamiltonian planar graphs,planar hamiltonian graphs,planar hamiltonian graph
contributors: bookofproofs

---


---

(Note that finding a Hamiltonian cycle is an NP-hard problem and there is much research going on to find theoretical results about finding not only necessary but also sufficient criteria for a graph to be Hamiltonian. The following theorem is one such research[^1591] result in providing a necessary and sufficient criterion for a planar graph to be Hamiltonian. The theorem is also the main motivation for defining the concept of [minimal tree decomposability][bookofproofs$6393] `\(\tau(G)\)` of a graph `\(G\)`.) 

For all [simple][bookofproofs$523] [planar][bookofproofs$1226] [connected][bookofproofs$1166] graphs `\(G\)`, the following equivalence holds: `\(G\)` is [Hamiltonian][bookofproofs$6349], if and only if the [minimal tree decomposability][bookofproofs$6393] of every of its [dual graphs][bookofproofs$6391] equals `\(2\)`, formally:

`\[\text{Simple and planar }G:~G\text{ is Hamiltonian}\quad\Longleftrightarrow\quad \tau(G^*)=2\text{ for all dual graphs }G^*\text{ of }G.\]`

### Example

The idea for this equivalence is illustrated in the following example:
* The planar graph is drawn using the orange color (here a dodecahedron graph). 
* The bold orange lines mark a Hamiltonian circle. 
* The blue graph is the dual (here an icosahedron graph).
* The bold black lines mark the decomposition of the icosahedron graph into two tree graphs (marked solid and dotted).
* The theorem states for this example that the dodecahedron graph is Hamiltonian if and only if the minimum decomposition of its dual icosahedron graph leads to exactly two trees (but not more and not less than two trees).  
* The constructive nature of the proof makes use of the fact that a Hamiltonian cycle of a planar graph (if it is Hamiltonian) can be constructed from the edges dual to exactly those edges of the dual graph, which are not part of the decomposition trees (in the example below those are the thin blue edges crossing the bold orange edges), or by removing the edges crossed by the dual edges of the decomposition trees (in the example below those are the thin orange edges crossed by the bold black edges).  

!{max-width:100%;}https://www.bookofproofs.org/graphics/examples/dualplanarhamiltonian1.png!

new:branchcorollary:The 4-colors Problem and Planar Hamiltonian Graphs

Let `$G$` be a [simple][bookofproofs$523] [planar][bookofproofs$1226] which is also [Hamiltonian][bookofproofs$6349]. Then it can be colored in
