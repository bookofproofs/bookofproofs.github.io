layout: definition
categories: branches,logic
nodeid: bookofproofs$7868
orderid: 200
parentid: bookofproofs$7871
title: Truth Table
description: TRUTH TABLE ★ bring your math skills to the graduate level ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$7838
keywords: truth table,truth tables
contributors: bookofproofs


---

The most convenient way to study Boolean functions is writing them in the form of tables called the __truth tables__. They were invented by "Charles Sanders Peirce":https://www.bookofproofs.org/history/charles-sanders-peirce/ in 1893. Truth tables have a great practical use in propositional logic since they allow to learn important examples of [connectives][bookofproofs$7867] as special [Boolean functions][bookofproofs$1316].

---

Let `$p_1,\ldots,p_n$` be `$n\ge 1$` [propositions][bookofproofs$1307] and let [$\circ$" be a "$k$-nary connective][bookofproofs$7867] such that `$\phi=p_1\circ \ldots \circ p_n$` is also a proposition. We have seen [in the corresponding lemma][bookofproofs$1316] that "`$\circ$`" 
induces a Boolean function `$f_\phi:\mathbb B^n\to\mathbb B$` defined on the [set of truth values][bookofproofs$707] `$\mathbb B=\{1,0\}=\{true, false\}$`: 

A **truth table** of the [Boolean function][bookofproofs$1316] `$f_\phi$` is a table listing all the possible [valuations][bookofproofs$710] `$[[]]_I$` of the `$n$` propositions `$p_1,\ldots,p_n$` and the resulting value of the boolean function `$f_\phi$`.


A schematic structure is the following. The `$b_i$` in the right column are one of `$1$` or `$0$` each.

 `$[[p_1]]_I$`| `$\ldots$`| `$[[p_n]]_I$`| `$[[p_1\circ\ldots\circ p_n]]_I$`
:-------------|:-------------|:-------------|:------------- 
`$0$`| `$\ldots$`| `$0$`| `$b_1$`
 `$1$`| `$\ldots$`| `$0$`| `$b_2$`
 `$\vdots$`| `$\vdots$`| `$\vdots$`| `$\vdots$`
 `$1$`| `$\ldots$`| `$1$`| `$b_{2^n}$`[^1]

[^1]: In general, it is also possible that a truth table contains less than `$2^n$` rows. This is especially the case if some of the propositions `$p_i$` are [Boolean constants][bookofproofs$1307].
