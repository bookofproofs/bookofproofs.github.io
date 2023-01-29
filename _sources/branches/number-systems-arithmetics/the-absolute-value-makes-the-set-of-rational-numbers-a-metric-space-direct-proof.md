layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1091
orderid: 50
parentid: bookofproofs$1090
title: 
description: DIRECT PROOF Proof of THE ABSOLUTE VALUE MAKES THE SET OF RATIONAL NUMBERS A METRIC SPACE. &#9733; master graduate maths &#10004; visit BookOfProofs now!
references: bookofproofs$581,bookofproofs$696
keywords: absolute,makes,metric,numbers,rational,set,space,value,proof
contributors: bookofproofs

---


---

We have to show that the [absolute value defined for rational numbers][bookofproofs$1081] defines a [metric][bookofproofs$614] on the set of rational numbers `\(\mathbb Q\)`, i.e. to show that it fulfills in `\(\mathbb Q\)` the general properties of any metric. Let `\(\frac ab,~\frac cd,~\frac ef\in \mathbb Q\)`.

### `\((1)\)` We have to show that `\(\left|\frac ab-\frac cd\right|=0\)` if and only if `\(\frac ab=\frac cd\)`.

It follows from the [definition of rational numbers][bookofproofs$1033] that `\(|\frac ab-\frac cd|=0\)` if and only if both fractions represent the same equivalence relation `\((a,b)\sim (c,d)\Leftrightarrow ad=bc\)`, in other words `\(\frac ab=\frac cd\)`. Thus,  this property of a metric is fulfilled.

### `\((2)\)` We have to show the symmetry `\(|\frac ab-\frac cd|=|\frac cd-\frac ab|\)`.

Assume without loss of generality that `\(\frac ab\ge \frac cd\)`. Then we have by [definition of absolute value for rational numbers][bookofproofs$1081] that `\(\left|\frac ab-\frac cd\right| = \frac ab-\frac cd\)`. On the other side, we have `\(\left|\frac cd-\frac ab\right| = - \frac cd - \left( - \frac ab \right) = - \frac cd + \frac ab \)`. Since the addition of rational numbers is commutative[^1], we have `\(- \frac cd + \frac ab = \frac ab - \frac cd \)`, so both absolute values are equal.

### `\((3)\)` We have to show the triangle inequality `\(\left|\frac ab-\frac ef\right|\le \left|\frac ab-\frac cd\right|+\left|\frac cd-\frac ef\right|\)`.

We observe that `\(\left(\frac ab-\frac cd\right)\le \left|\frac ab-\frac cd\right|\)` and `\(\left(\frac cd-\frac ef\right)\le \left|\frac cd-\frac ef\right|\)`. We have therefore
`\[\frac ab-\frac ef=\frac ab-\frac cd+\frac cd-\frac ef\le \left|\frac ab-\frac cd\right|+\left|\frac cd-\frac ef\right|.\]`

Because also `\(-\left(\frac ab-\frac cd\right)\le \left|\frac ab-\frac cd\right|\)` and `\(-\left(\frac cd-\frac ef\right)\le \left|\frac cd-\frac ef\right|\)`, it follows with the same argument that

`\[-\left(\frac ab - \frac ef\right)=-\left(\frac ab-\frac cd\right)+\left(-\left(\frac cd-\frac ef\right)\right)\le \left|\frac ab-\frac cd\right|+\left|\frac cd-\frac ef\right|.\]`

Together with the  [definition of absolute value for rational numbers][bookofproofs$1081], it follows 

`\[\left|\frac ab-\frac ef\right|\le \left|\frac ab-\frac cd\right|+\left|\frac cd-\frac ef\right|\]`

[^1]: Note that the `\((\mathbb Q, + ,\cdot)\)` is a field [we have constructed][bookofproofs$1033] from the integral domain `\((\mathbb Z, +)\)`, in which the addition was proven to be commutative.
