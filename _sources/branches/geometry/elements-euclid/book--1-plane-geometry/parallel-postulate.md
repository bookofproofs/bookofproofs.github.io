layout: axiom
categories: branches,geometry,elements-euclid,book--1-plane-geometry
nodeid: bookofproofs$939
orderid: 400
parentid: bookofproofs$684
title: 1.5: Parallel Postulate
description: 1.5: PARALLEL POSTULATE ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$6419,bookofproofs$6908
keywords: parallel,postulate,fifth,axiom,parallel postulate,fifth postulate,fifth axiom,parallel axiom
contributors: @Fitzpatrick,bookofproofs

---


---

### (Postulate 5 from Book 1 of Euclid's “Elements”)

> And that if a [straight line][bookofproofs$645] falling across two (other) [straight lines][bookofproofs$645] makes internal angles on the same side (of itself whose sum is) less than two [right angles][bookofproofs$653], then the two (other) [straight lines][bookofproofs$645], being produced to infinity, meet on that side (of the original [straight line][bookofproofs$645]) that the (sum of the internal angles) is less than two [right angles][bookofproofs$653] (and do not meet on the other side).[^1]

if `$\alpha+\beta < 180^\circ,$` 

![post5a](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/post5a.jpg?raw=true)


then

![post5b](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/post5b.jpg?raw=true)


### Modern (Equivalent)[^2] Formulation

In a [plane][bookofproofs$647], through a given [point][bookofproofs$631] `\(A\)` lying not on a given [straight line][bookofproofs$645] `\(g\)`, exactly one straight line `\(h\)` can be drawn, which is [parallel][bookofproofs$788] to the given straight line.


![post5_3](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/post5_3.jpg?raw=true)



[^1]: This postulate effectively specifies that we are dealing with the geometry of _flat_, rather than  curved, space.

[^2]: The formulations are equivalent, since only if the straight lines `\(g\)` and `\(h\)` are parallel, the segment `\(AB\)` is perpendicular to both straight lines (i.e. the angles `\(\alpha,\beta\)` are [right angles][bookofproofs$653]). In other words, every other straight line drawn through the point `\(A\)` would cause the angle `\(\beta\)` to become either [obtuse or acute][bookofproofs$689]. If it became acute, we would have the situation of the first formulation. If it became obtuse, the same formulation would apply for the [supplemental angles][bookofproofs$652] of `\(\alpha\)` and `\(\beta\)`.

### Note from the founder of <strong><span style='color:orange'>Bookof</span><span style='color:lightblue'>Proofs</span></strong>

In my opinion, from the standpoint of a modern [axiomatic method][bookofproofs$7081], the 5th postulate could be removed from the “Elements” without changing their validity! As far as I'm aware of, this observation is new and has never been dealt with in literature. I would appreciate receiving any comment, please contact me.

This is why:

* According to the [Corollary to Proposition 1.16][bookofproofs$786] of the “Elements”, the _existence_ of straight lines in the plane not meeting at any point is ensured. 
* The construction of the lines in the proof of this corollary uses two points for each straight line, through which the parallel lines have to go.
* Therefore, according to [postulate 1][bookofproofs$692], this kind of construction also ensures the _uniqueness_ of the constructed parallel lines.
* Moreover, up to the corollary to the 16th proposition of the First Book of "Elements", the 5th postulate is never used by Euclid. 
* In other words, all propositions up to the 16th proposition of the First Book do not use the 5th postulate, while the _existence_ and _uniqueness_ of parallel straight lines in the plane is already proven using the remaining four axioms!
