layout: definition
categories: branches,logic
nodeid: bookofproofs$1304
orderid: 600
parentid: bookofproofs$7871
title: Implication
description: IMPLICATION &#9733; bring your math skills to the graduate level &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$7838
keywords: antecedent,consequent.,contradiction,implication,valid argument
contributors: bookofproofs


---
All the binary connectives we have learned so far - [conjunction][bookofproofs$712], [disjunction][bookofproofs$713] and [exclusive disjunction][bookofproofs$7869], were commutative - the order of the propositions connected by them did not matter. Now, we will learn an important binary connective which is not commutative - the __implication__.

---

Let `\(L\)` be a [set of propositions][bookofproofs$1307] with the [interpretation][bookofproofs$710] `$I$` and the corresponding [valuation function][bookofproofs$710] `$[[]]_I$`. 
An **implication** "`\(\Rightarrow\)`" is a [Boolean function][bookofproofs$1316].
`\[\Rightarrow :=\begin{cases}L \times L & \mapsto  L \\
(x,y) &\mapsto x \Rightarrow y.
\end{cases}\]`

defined by the following [truth table][bookofproofs$7868]:


Truth Table of the Implication

 `$[[x]]_I$`| `$[[y]]_I$`| `$[[x \Rightarrow y]]_I$`
:-------------|:-------------|:-------------
 `\(1\)`| `\(1\)`| `\(1\)`
 `\(0\)`| `\(1\)`| `\(1\)`
 `\(1\)`| `\(0\)`| `\(0\)`
| `\(0\)`| `\(0\)`| `\(1\)`

We read the implication `$x\Rightarrow y$`  

“__if__ `$x$` __then__ `$y$`”. 


### Notes

* It is apparent from the truth table that the implication is not commutative - the order of the propositions connected by it counts. Therefore, both propositions have specific names - the first one is called the **antecedent**, the second one the *consequent.*
* The implication of two propositions is only false if a true antecedent implies a false consequent. This is called a **contradiction**. Note that a false antecedent can imply both a true and a false consequent, without creating a contradiction. 
* But if a true antecedent implies a true consequent, we say it is a **valid argument**.
* There are more different readings of the implication `$x\Rightarrow y$`:
   * If `$x$`, then `$y$`.
   * `$y$` follows from `$x$`.
   * `$x$` is **sufficient** for `$y$`.
   * `$y$` is **necessary** for `$x$`.
   * `$y$`, if `$x$`.
   * `$x$`, only if `$y$`.
* It is helpful to think about the implication as a __cause__ and __effect__ chain.
