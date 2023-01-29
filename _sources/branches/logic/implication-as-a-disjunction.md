layout: lemma
categories: branches,logic
nodeid: bookofproofs$6874
orderid: 50
parentid: bookofproofs$1304
title: Implication as a Disjunction
description: IMPLICATION AS A DISJUNCTION &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$711,bookofproofs$7838
keywords: disjunction,implication
contributors: bookofproofs

---
The following lemma is sometimes very helpful in proving implications in mathematics. It uses the fact that the [implication][bookofproofs$1304] `$x\Rightarrow y$` can be represented by the [disjunction][bookofproofs$713] `$\neg x\vee y$`.

---

Any [implication][bookofproofs$1304] `$x\Rightarrow y$` is [equivalent][bookofproofs$1305] to the [disjunction][bookofproofs$713] of the [negated][bookofproofs$714] [antecedent][bookofproofs$1304] `$\neg x$` and the [consequent][bookofproofs$1304] `$y$`, formally `$$(x\Rightarrow y)\Longleftrightarrow (\neg x \vee y).$$`

### Example

This lemma is a little bit surprising because, in natural language, it is not intuitive. Consider for instance the following propositions:

> `$x=$`"Socrates is human."

> `$y=$`"Socrates is mortal."

Then the following compound propositions are equivalent:

> `$x\Rightarrow y$`: "If Socrates is human, then Socrates is mortal."

> `$\neg x \vee y$`: "Socrates is not human, or Socrates is mortal."
