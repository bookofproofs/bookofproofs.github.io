layout: proof
categories: branches,logic
nodeid: bookofproofs$6877
orderid: 50
parentid: bookofproofs$6876
title: 
description:  Proof of NEGATION OF AN IMPLICATION &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$711
keywords: implication,negation,negation of implication,negation of an implication,negate implication,negation implication,implication negation,negate an implication,how to negate an implication,how to negate implication,negating an implication,what is the negation of an implication,what is the negation of implication,negated implication,proof
contributors: bookofproofs


---


---

### Context

* Let `$x,y$` be two [propositions][bookofproofs$710].
* We want to show that `$\neg (x\Rightarrow y)\Longleftrightarrow (x \wedge \neg y).$`

### Hypothesis

* Take the negated implication `$\neg(x\Rightarrow y)$`.

### Implications

* According to the definition of the [implication][bookofproofs$1304] and [negation][bookofproofs$714], the [truth table][bookofproofs$7868] is 


`\(\models(x)\)` | `\(\models(y)\)` | `\(\models(x \Rightarrow y)\)` | `\(\models\neg(x \Rightarrow y)\)`
:------------- |:------------- |:------------- |:-------------
 `\(1\)`| `\(1\)`| `\(1\)`| `\(0\)`
 `\(0\)`| `\(1\)`| `\(1\)`| `\(0\)`
 `\(1\)`| `\(0\)`| `\(0\)`| `\(1\)`
 `\(0\)`| `\(0\)`| `\(1\)`| `\(0\)`

* Based on the truth tables of the [negation][bookofproofs$714] and [conjunction][bookofproofs$712], the truth table of `$(x\wedge \neg y)$` is given by

 `\(\models(x)\)`| `\(\models(y)\)`| `\(\models(\neg y) \)`| `\(\models(x \wedge \neg y)\)`
 `\(1\)`| `\(1\)`| `\(0\)`| `\(0\)`
 `\(0\)`| `\(1\)`| `\(0\)`| `\(0\)`
 `\(1\)`| `\(0\)`| `\(1\)`| `\(1\)`
 `\(0\)`| `\(0\)`| `\(1\)`| `\(0\)`


### Conclusion

* Since the outcomes (columns to the right) of both truth tables are equal, we have shown the [equivalence][bookofproofs$1305]  `$\neg (x\Rightarrow y)\Longleftrightarrow (x \wedge \neg y).$`
