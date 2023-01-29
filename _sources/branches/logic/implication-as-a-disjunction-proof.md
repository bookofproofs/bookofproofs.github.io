layout: proof
categories: branches,logic
nodeid: bookofproofs$6875
orderid: 50
parentid: bookofproofs$6874
title: 
description:  Proof of IMPLICATION AS A DISJUNCTION &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$711
keywords: disjunction,implication,proof
contributors: bookofproofs


---


---

### Context

* Let `$x,y$` be two [propositions][bookofproofs$710].
* We want to show that `$(x\Rightarrow y)\Longleftrightarrow (\neg x \vee y).$`

### Hypothesis

* We are given the implication `$x\Rightarrow y$`.

### Implications

* According to the definition of [implication][bookofproofs$1304], the [truth table][bookofproofs$7868] is 


`\(\models(x)\)` | `\(\models(y)\)` | `\(\models(x \Rightarrow y)\)`
:------------- |:------------- |:-------------
 `\(1\)`| `\(1\)`| `\(1\)`
 `\(0\)`| `\(1\)`| `\(1\)`
 `\(1\)`| `\(0\)`| `\(0\)`
 `\(0\)`| `\(0\)`| `\(1\)`

* Based on the truth tables of the [negation][bookofproofs$714] and [disjunction][bookofproofs$713], the truth table of `$(\neg x\vee y)$` is given by

 `\(\models(x)\)`| `\(\models(y)\)`| `\(\models(\neg x) \)`| `\(\models(\neg x \vee y)\)`
 `\(1\)`| `\(1\)`| `\(0\)`| `\(1\)`
 `\(0\)`| `\(1\)`| `\(1\)`| `\(1\)`
 `\(1\)`| `\(0\)`| `\(0\)`| `\(0\)`
 `\(0\)`| `\(0\)`| `\(1\)`| `\(1\)`


### Conclusion

* Since the outcomes (columns to the right) of both truth tables are equal, we have shown the [equivalence][bookofproofs$1305] `$(x\Rightarrow y)\Longleftrightarrow (\neg x \vee y).$`
