layout: definition
categories: branches,logic
nodeid: bookofproofs$7871
orderid: 300
parentid: bookofproofs$66
title: Semantics of PL0
description: SEMANTICS OF PL0 ★ bring your math skills to the graduate level ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: 
keywords: semantics of pl0,pl0
contributors: bookofproofs

---
The [Law of Excluded Middle][bookofproofs$710] tells us that if a string of a formal language `$s\in L$` is a [proposition][bookofproofs$1307], then the valuation function can take only two values - either the proposition is true or false: `$[[s]]_I\in \mathbb B$` for all interpretations. This can also be expressed using the [satisfaction relation][bookofproofs$7880]: either we have `$\models s$` or `$\not{\models}s$`. 

However, we still do not know, how the satisfaction relation changes when we use the  [syntactical rules for building propositions][bookofproofs$1307]. The following definition closes the gaps by defining the __semantics of the propositional logic__.

---

Let `$L$` be a f[ormal language][bookofproofs$94] with the [syntax of propositional logic][bookofproofs$1307] `$PL0$` and let `$L'\subset L$` be the subset of `$L$` which consists of propositions (i.e. Boolean constants, Boolean variables, and Boolean terms). The [semantics][bookofproofs$7881] of `$PL0$`* is defined recursively as [its syntax][bookofproofs$1307] was. We provide two equivalent definitions - one using [interpretations][bookofproofs$710] "$I$" with the corresponding valuation functions `$[[]]_I$`, another using the [satisfaction relation][bookofproofs$710] "$\models$" of `$PL0$`:

### Definition I

For all [interpretations of `$PL0$`][bookofproofs$710] "$I$" of propositions, the corresponding valuation functions "$[[]]_I$" are defined as follows:
* Boolean constants: 
   * `$[[ 1 ]]_I=1.$`
   * `$[[ 0 ]]_I=0.$`
* Boolean variables `$x$`: 
   * `$[[ x ]]_I=1$` if and only if `$x=1.$` 
* Boolean terms `$\phi,\psi$` under special symbols "$\neg\phi,$” “$\phi\vee\psi,$” “$\phi\wedge\psi,$” “$\phi\Rightarrow\psi,$” “$\phi\Leftrightarrow \psi$”:
   * **Negation**: `$[[ \neg\phi ]]_I=1$` if and only if `$[[\phi ]]_I=0.$`
   * **Disjunction**: `$[[\phi \vee \psi]]_I=1$` if and only if `$[[\phi ]]_I=1$` or `$[[\psi ]]_I=1.$`
   * **Conjunction**: `$[[\phi \wedge\psi]]_I=1$` if and only if `$[[\phi ]]_I=1$` and `$[[\psi ]]_I=1.$`
   * **Implication**: `$[[\phi \Rightarrow\psi]]_I=1$` if and only if `$[[\phi ]]_I=0$` or `$[[\psi ]]_I=1.$`
   * **Equivalence**: `$[[\phi \Leftrightarrow \psi]]_I=1$` if and only if `$[[\phi \Rightarrow\psi]]_I=1$` and `$[[\psi \Rightarrow\phi]]_I=1.$`


### Equivalent Definition II 

The [satisfaction relation of `$PL0$`][bookofproofs$710] "$\models$" is given by:
* Boolean Constants: 
   * `$\;\models 1.$`
   * `$\not{\models}\; 0.$`
* Boolean variables `$x$`: 
   * `$\models x$` if and only if `$x=1.$` 
* Boolean terms `$\phi,\psi$` under special symbols "$\neg\phi,$” “$\phi\vee\psi,$” “$\phi\wedge\psi,$” “$\phi\Rightarrow\psi,$” “$\phi\Longleftrightarrow \psi$”: 
   * **Negation**: `$\models \neg(\phi)$` if and only if `$\not{\models}(\phi).$`
   * **Disjunction**: `$\models (\phi \vee \psi)$` if and only if `$\models (\phi)$` or `$\models (\psi).$`
   * **Conjunction**: `$\models (\phi \wedge\psi)$` if and only if `$\models (\phi)$` and `$\models (\psi).$`
   * **Implication**: `$\models (\phi \Rightarrow\psi)$` if and only if `$\not{\models} (\phi)$` or `$\models (\psi).$`
   * **Equivalence**: `$\models (\phi \Leftrightarrow \psi)$` if and only if `$\models (\phi \Rightarrow\psi)$` and `$\models (\psi \Rightarrow\phi).$`
