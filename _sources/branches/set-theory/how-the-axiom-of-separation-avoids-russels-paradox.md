layout: explanation
categories: branches,set-theory
nodeid: bookofproofs$8019
orderid: 300
parentid: bookofproofs$675
title: How the Axiom of Separation Avoids Russell's Paradox
description: HOW THE AXIOM OF SEPARATION AVOIDS RUSSEL'S PARADOX &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$656,bookofproofs$983
keywords: avoids,axiom,how,paradox,russels,separation
contributors: bookofproofs

---


---

It now time to demonstrate how the [axiom of separation][bookofproofs$675] avoids the [Russell's paradox][bookofproofs$7987]. Recall that [Cantors' naive set definition][bookofproofs$550] allowed the construction of a “set of all sets which do not contain themselves.” Formally, using the [set-builder notation][bookofproofs$587], we could write `$$Y:=\{z\mid z\text{ is a set and } z\not\in z\}.$$`  
The Russell's paradox was that 
`$$\begin{array}{rrcll}
\text{if}&Y\in Y&\text{then}&Y\text{ is a set and }Y\not\in Y&\text{which is false, since }Y\in Y,\\
\text{if}&Y\not\in Y&\text{then}& Y\text{ is not a set or }Y\in Y&\text{which is false, since }Y\text{ is a set.}\end{array}$$` 
Therefore, altogether it led to a [contradiction][bookofproofs$7880].
With the axiom of separation, this cannot happen anymore. Now, the elements `$z\in Y$` can only be taken from an _existing_ set `$X$`. In comparison to the general axiom of comprehension, where `$Y$` could become anything, with the axiom of separation `$Y$` becomes a subset of an existing set `$X$`.  Using the [set-builder notation][bookofproofs$8017], we can now write `$$Y:=\{z\in X\mid   z\not\in z\}=\{z\mid z\in X\text{ and }  z\not\in z\}.$$`
Now, 
`$$\begin{array}{rrcll}
\text{if}&Y\in Y&\text{then}&Y\in X\text{ and }Y\not\in Y&\text{which is false, since }Y\in Y,\\
\text{if}&Y\not\in Y&\text{then}& Y\not\in X\text{ or }Y\in Y&\text{which is true only for }Y\not\in X.\end{array}$$`

Thus, the definition is not contradictory anymore and everything is alright.
