layout: axiom
categories: branches,set-theory
nodeid: bookofproofs$667
orderid: 400
parentid: bookofproofs$1427
title: Axiom of Pairing
description: AXIOM OF PAIRING ★ bring your math skills to the graduate level ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: 
keywords: axiom of pairing,pairing axiom,pairing postulate,postulate of pairing
contributors: bookofproofs


---
The axioms we introduced so far, the [axiom of existence][bookofproofs$8015], the axiom of [empty set][bookofproofs$666], the [axiom of extensionality][bookofproofs$551], and the [axiom of separation][bookofproofs$675] do not suffice to justify the [union][bookofproofs$6827] operation "`$\cup$`" on sets. Of course, for two given sets `$A, B$`, we could use the axiom of separation to justify the set union by 
`$$A\cup B:=\{z\mid x\in A\vee x\in B \},$$`
like we did in the [proof of justification of the set intersection][bookofproofs$8023]. However, circumstances are quite different now. While in the case of set intersection the elements `$z$` _were already_ the common elements of both sets, in the case of a set union _no common elements_ have to exist at all. In other words, we cannot just take it for granted that we can combine _any_ elements of two _arbitrary_ sets `$X$` and `$Y$` to form a new set `$A\cup B$`. In order to enforce this possibility, we need two new axioms, the axiom of pairing, and the axiom of union, which we will now introduce:

---

For any two sets `$X,Y$` there exists a set `$Z:=\{X,Y\}$` containing both sets as its elements, formally

`$$\forall X~\forall Y~\exists Z~\forall z~(z\in Z\Leftrightarrow z=X\vee z=Y)$$`


![axiom3](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/axiom3.jpg?raw=true)

