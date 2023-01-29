layout: definition
categories: branches,logic
nodeid: bookofproofs$1305
orderid: 700
parentid: bookofproofs$7871
title: Equivalence
description: EQUIVALENCE &#9733; bring your math skills to the graduate level &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: 
keywords: equivalence,equivalent statements
contributors: bookofproofs


---
One of the most important [connectives][bookofproofs$7867] in logic is the __equivalence__ which is a kind of both-sided implication.

---

Let `\(L\)` be a [set of propositions][bookofproofs$1307] with the [interpretation][bookofproofs$710] `$I$` and the corresponding [valuation function][bookofproofs$710] `$[[]]_I$`. 
An **equivalence** "`\(\Leftrightarrow\)`" is a [Boolean function][bookofproofs$1316].
`\[\Leftrightarrow:=\begin{cases}L \times L & \mapsto  L \\
(x,y) &\mapsto x \Leftrightarrow y\\
\end{cases}\]`

defined using a [conjunction][bookofproofs$712] of two [implications][bookofproofs$1304]:

`$$x \Leftrightarrow y :=(x\Rightarrow y)\wedge (y\Rightarrow y).$$`

We read the equivalence 

"$x$ __if, and only if__ `$y$`."

It has the following [truth table][bookofproofs$7868]:


[semantics][bookofproofs$710]: 

`$[[x]]_I$` | `$[[y]]_I$` | `$[[x \Leftrightarrow  y]]_I$`
:------------- |:------------- |:-------------
 `\(1\)`| `\(1\)`| `\(1\)`
 `\(0\)`| `\(1\)`| `\(0\)`
 `\(1\)`| `\(0\)`| `\(0\)`
 `\(0\)`| `\(0\)`| `\(1\)`

### Notes

* The equivalence of two propositions is only true if both propositions have the same truth value assigned.
* Propositions, the equivalence of which is true, are called **equivalent statements**. Equivalent statements can be interpreted as the way of "saying the same" in two different ways.
