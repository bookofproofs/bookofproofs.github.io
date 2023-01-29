layout: proof
categories: branches,logic
nodeid: bookofproofs$1329
orderid: 50
parentid: bookofproofs$1328
title: 
description:  Proof of EVERY CONTRAPOSITION TO A PROPOSITION IS A TAUTOLOGY TO THIS PROPOSITION &#9733; master graduate maths &#10004; visit BookOfProofs now!
references: bookofproofs$711
keywords: contraposition,every,proposition,tautology,this,proof
contributors: bookofproofs


---


---

We want to show that for any two [propositions][bookofproofs$710]  `\(x,y\)`, the [implication][bookofproofs$1304] `\(x\Rightarrow y\)` is [equivalent][bookofproofs$1305] to its [contrapositive][bookofproofs$1306] `\(\neg y\Rightarrow \neg x\)`.

By [definition of implication][bookofproofs$1304], for all [semantics][bookofproofs$7871] of `$x$` and `$y$` have the following [truth table][bookofproofs$7868]:


`\([[x]]_I\)` | `\([[y]]_I\)` | `\([[x \Rightarrow y]]_I\)`
:------------- |:------------- |:-------------
 `\(1\)`| `\(1\)`| `\(1\)`
 `\(0\)`| `\(1\)`| `\(1\)`
 `\(1\)`| `\(0\)`| `\(0\)`
 `\(0\)`| `\(0\)`| `\(1\)`

Similarly, for the [contrapositive][bookofproofs$1306], we get the respective truth table

 `\([[\neg y]]_I\)`| `\([[\neg x]]_I\)`| `\([[\neg y\Rightarrow \neg x]]_I\)`
 `\(0\)`| `\(0\)`| `\(1\)`
 `\(0\)`| `\(1\)`| `\(1\)`
 `\(1\)`| `\(0\)`| `\(0\)`
 `\(1\)`| `\(1\)`| `\(1\)`

`\(x\Rightarrow y\)` is equivalent to `\(\neg y\Rightarrow \neg x\)`, if the [equivalence][bookofproofs$1305] `$(x\Rightarrow y)\Leftrightarrow(\neg y\Rightarrow \neg x)$` is a [tautology][bookofproofs$7880]. Putting the above results together into the [truth table of equivalence][bookofproofs$1305], we can confirm that:

 `\([[x \Rightarrow y]]_I\)`| `\([[\neg y \Rightarrow \neg x]]_I\)`| `\([[(x\Rightarrow y)\Leftrightarrow(\neg y\Rightarrow \neg x)]]_I\)`
 `\(1\)`| `\(1\)`| `\(1\)`
 `\(0\)`| `\(0\)`| `\(1\)`
