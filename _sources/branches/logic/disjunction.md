layout: definition
categories: branches,logic
nodeid: bookofproofs$713
orderid: 500
parentid: bookofproofs$7871
title: Disjunction
description: DISJUNCTION &#9733; bring your math skills to the graduate level &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: 
keywords: disjunction
contributors: bookofproofs


---


---

Let `\(L\)` be a [set of propositions][bookofproofs$1307] with the [interpretation][bookofproofs$710] `$I$` and the corresponding [valuation function][bookofproofs$710] `$[[]]_I$`. 
A **disjunction** "`\(\vee\)`"  is a [Boolean function][bookofproofs$1316].
`$$\vee :=\begin{cases}
L \times L  & \mapsto  L \\
(x,y) &\mapsto x \vee y.
\end{cases}$$`

defined by the following [truth table][bookofproofs$7868]:


Truth Table of the Conjunction
:-------------
 `$[[x]]_I$`| `$[[y]]_I$`| `$[[x\vee y]]_I$`
 `\(1\)`| `\(1\)`| `\(1\)`
 `\(0\)`| `\(1\)`| `\(1\)`
 `\(1\)`| `\(0\)`| `\(1\)`
 `\(0\)`| `\(0\)`| `\(0\)`


We read the disjunction `$x\vee y$`  

“$x$ __or__ `$y$`”. 

### Notes

* The disjunction of two propositions is only false if the two propositions are both false. Otherwise, it is true. 
* The word __or__ in the natural English language does not correspond to the logical __or__ disjunction. Consider the following example:

>  `$x=$`"The month is January", `$y=$`"The month is February"

> The logical disjunction `$x\vee y$` is true if one of `$x,y$` (or both) are true, but in English, only one can be true, but never both.
