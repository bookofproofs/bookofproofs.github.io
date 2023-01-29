layout: proof
categories: branches,analysis
nodeid: bookofproofs$620
orderid: 50
parentid: bookofproofs$618
title: 
description: DIRECT PROOF Proof of THE DISTANCE OF REAL NUMBERS MAKES REAL NUMBERS A METRIC SPACE. &#9733; master graduate maths &#10004; visit BookOfProofs now!
references: bookofproofs$581
keywords: absolute value and metric space of real numbers,real numbers are a metric space,triangle inequality,proof
contributors: bookofproofs

---


---

We have to prove that the [absolute value][bookofproofs$583] of the [difference][bookofproofs$1588] `\(|x-y|\)` is a [metric][bookofproofs$614] function on the [field of real numbers][bookofproofs$1638] `\((\mathbb R, + ,\cdot)\)`, i.e. to show that it fulfills in `\(\mathbb R\)` the general properties of any metric.

1. Following the [existence of negative numbers][bookofproofs$35] and their [uniqueness][bookofproofs$50] it follows that `\(|x-y|=0\)` if and only if `\(x=y\)`, so the first property of a metric is fulfilled.
1. To show the symmetry `\(|x-y|=|y-x|\)` as the second property of a metric, we assume without loss of generality that `\(x\ge y\)`. Then we have by [definition][bookofproofs$583] `\(|x-y| = x-y\)`, which is equal `\(-y-(-x)=-1(y-x)\)`. Using the [properties 1 and 2 of the absolute value][bookofproofs$619], we get the desired result by `\(-1(y-x)=|-1||y-x|=|1||y-x|=|y-x|\)`.
1. In order to prove the triangle inequality: `\(|x-z|\le |x-y|+|y-z|\)` for all `\(x,y,z\in \mathbb R\)`, we observe that `\((x-y)\le |x-y|\)` and `\((y-z)\le |y-z|\)`. Applying the [rule 4 of calculation with inequalities][bookofproofs$594] we get   
`\[x-z=x-y+y-z\le |x-y|+|y-z| \]`
Because also `\(-(x-y)\le |x-y|\)` and `\(-(y-z)\le |y-z|\)`, it follows with the same argument that
`\[-(x-z)=-(x-y)+(-(y-z))\le |x-y|+|y-z|. \]`
By [definition of absolute value][bookofproofs$583], both results give us 
`\[|x-z|\le |x-y|+|y-z|. \]`
