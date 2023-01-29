layout: proof
categories: branches,set-theory
nodeid: bookofproofs$8029
orderid: 50
parentid: bookofproofs$8028
title: 
description: PROOF OF JUSTIFICATION OF SET UNION &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$983
keywords: justification,set,union,proof
contributors: bookofproofs


---


---

* Let  `$A$`  and  `$B$`  be sets.


![axiomsunionsproof1](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/axiomsunionsproof1.png?raw=true)


* By the [axiom of pairing][bookofproofs$667] there is a set `$Z$` containing `$A$` and `$B$` as elements:


![axiomsunionsproof2](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/axiomsunionsproof2.png?raw=true)


* By the [axiom of separation][bookofproofs$667] there is a [subset][bookofproofs$552] `$Z'\subseteq Z$` containing exactly `$A$` and `$B$` as elements:


![axiomsunionsproof3](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/axiomsunionsproof3.png?raw=true)


* By the "axiom of union":https://www.bookofproofs.org/branches/axiom-of-union-ernst/ there is a set `$Z^*$` containing the elements of `$A$` or[^1] the elements of `$B.$`


![axiomsunionsproof4](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/axiomsunionsproof4.png?raw=true)


* By the [axiom of separation][bookofproofs$675] there is a [subset][bookofproofs$552] `$Z^\dagger \subseteq Z^*$` containing exactly the elements of `$A$` or[^1] the elements of `$B.$`, i.e. `$Z^\dagger =\{z\mid z\in A\vee z\in B\}.$`


![axiomsunionsproof5](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/axiomsunionsproof5.png?raw=true)


* This is the required [set union][bookofproofs$6827]  `$A\cup B:=Z^\dagger .$` 
* The [axiom of extensionality][bookofproofs$551] ensures the uniqueness of such a set.
* Altogether, we have shown:


![axiomsunionsproof6a](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/axiomsunionsproof6a.png?raw=true)


[^1]: We mean the logical [or operation][bookofproofs$713], in the natural English language "and/or".
