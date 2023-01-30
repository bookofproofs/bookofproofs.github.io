layout: definition
categories: branches,logic
nodeid: bookofproofs$1307
orderid: 100
parentid: bookofproofs$66
title: Syntax of PL0 - Propositions as Boolean Terms
description: SYNTAX OF PL0 - PROPOSITIONS AS BOOLEAN TERMS ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$656,bookofproofs$711
keywords: boolean,boolean constants,boolean term,boolean variables,pl0,proposition,propositions,syntax,terms
contributors: bookofproofs


---


---

The variables and functions defined in [signature of propositional logic `$PL0$`][bookofproofs$7893] are called **Boolean**, named after the English mathematician <a href="https://mathshistory.st-andrews.ac.uk/Biographies/Boole/">George Bool</a>. 

First, we agree that the [formal language][bookofproofs$94] `\(L\subseteq \Sigma^* \)` of `$PL0$` is defined over an [alphabet][bookofproofs$708] `\(\Sigma\)` containing the following letters:

* space character " ",
* **Boolean constants**: the characters "$1$" and "$0$",
* **Boolean variables**: small Latin letters `\("a","b","c",\ldots,"x","y","z"\)`, and letters indexed with natural numbers, e.g. `\("a_0","a_1","a_2",\ldots,"b_0","b_1","b_2",\ldots,\)`, 
* the parentheses "$($" and "$)$", and
* the following additional letters "`\(\neg\)`", "`\(\wedge\)`", "`\(\vee\)`", "`\(\Rightarrow\)`", "`\(\Leftrightarrow\)`".

We will now specify the [syntax][bookofproofs$709] of `$PL0$`: 

* A Boolean constant is a **proposition** (we also will use the notion **Boolean term** synonymously for "proposition").
* Boolean variables are propositions.
* If "`$\phi$`" and "`$\psi$`" are propositions, then "`$\neg \phi$`," "`$\phi\wedge\psi$`", "`$\phi\vee\psi$`", "`$\phi\Rightarrow\psi$`", "`$\phi\Leftrightarrow\psi$`" are propositions.
* If "`$\phi$`" is a proposition, then the [concatenation][bookofproofs$708]  "`$(\phi)$`" is a proposition.


### Examples 

This syntax enables us to construct propositions (Boolean terms): 
* `$x$`,
* `$(x)$`,
* `$\neg a$`,
* `\((\neg(\neg y))\)`,
* `\(((x\Rightarrow(y\vee(1\wedge(\neg w))))\wedge 0)\)`, 
* `\(((a\Leftrightarrow b)\vee(0\Rightarrow y))\)`.

Please note that we did not yet define any meaning (semantics) of propositions. We will catch up on this now.
