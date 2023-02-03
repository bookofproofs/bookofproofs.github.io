layout: axiom
categories: branches,set-theory
nodeid: bookofproofs$675
orderid: 300
parentid: bookofproofs$1427
title: Schema of Separation Axioms (Restricted Principle of Comprehension)
description: AXIOM OF SEPARATION RESTRICTED PRINCIPLE OF COMPREHENSION ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$656,bookofproofs$983
keywords: axiom of separation,separation axiom,separation postulate,postulate of separation,axiom of comprehension,comprehension principle,comprehension axiom
contributors: bookofproofs


---
If you recall the [historical development of set theory][bookofproofs$8012], the general principle of comprehension led to contradictions. Zermelo restricted this principle and limited a general comprehension to the following axiom of separation:

---

If `\(p(z)\)` is a definite property, then for all sets `\(X\)` there is a subset `\(Y\)` consisting of those elements `\(z\)`, for which `\(p(z)\)` is satisfied. Formally, this axiom can be written as

`\[\forall X~\exists Y~\forall z~(z\in Y \Leftrightarrow z\in X\wedge p(z)).\]`

<a href="https://mathshistory.st-andrews.ac.uk/Biographies/Skolem/">Albert Skolem</a> (1887 - 1963) proposed to state "definite property" more precisely by replacing `$p(z)$` by an [atomic formula in predicate logic][bookofproofs$6226] `$p(z,x_1,\ldots,x_n).$` This makes the axiom in fact a whole **schema**  for infinitely many axioms, in which the placeholder `$p(z,X_1,\ldots,X_n)$` stands for an arbitrary, `$n+1$`-ary logical formula, in which `$z$` is a [free variable][bookofproofs$6221]. With this specification, and if we abbreviate the aliteration `$x_1,\ldots,x_n$` by `$\overset{n}{x}$`, the axiom states: For every predicate of the form `$p(z,\overset{n}{x})$` the following axiom holds: For all `$\overset{n}{x}$` and all sets `$x$` there is a set `$y$` containing exactly those elements `$z$` of `$x$` fulfilling `$p(z,\overset{n}{x})$`: `$$\forall \overset{n}{x}(\forall X(\exists Y(\forall z(z\in Y\Rightarrow z\in X\wedge p(z,\overset{n}{x}))))).$$`
 
The schema justifies the [set-builder][bookofproofs$587] notation, since it ensures the existence (and with the [axiom of extensionality][bookofproofs$551] the uniqueness) of a subset of elements of a set `$x$` fulfilling some given property `$p(z,\overset{n}{x})$`:
`$$\forall \overset{n}{x} (\forall X(\exists Y(Y=\{z\in X\mid p(z,\overset{n}{x})\}))).$$` 


![axiomseparation](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/axiomseparation.png?raw=true)

