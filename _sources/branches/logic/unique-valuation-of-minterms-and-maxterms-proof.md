layout: proof
categories: branches,logic
nodeid: bookofproofs$7903
orderid: 50
parentid: bookofproofs$7902
title: 
description:  Proof of UNIQUE VALUATION OF MINTERMS AND MAXTERMS &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$711,bookofproofs$7895
keywords: maxterms,minterms,unique,valuation,proof
contributors: bookofproofs

---


---

Let `$x_1,\ldots,x_n$` be [Boolean variables][bookofproofs$1307], `$I$` be an [interpretation][bookofproofs$710] and `$[[]]_I$` be the corresponding [valuation function][bookofproofs$710] in the [semantics of propositional logic][bookofproofs$7871].
### Proof for Minterms

* Let  `$m=(\neg)x_1\wedge\ldots\wedge(\neg)x_n$` be a  [minterm][bookofproofs$7901].
* We first show by construction the existence of an `$n$`-tuple of [truth values][bookofproofs$707]  `$([[x_1]]_I,\ldots,[[x_n]]_I)\in\mathbb B^n$` such that `$[[m]]_I=1:$`
   * If the literal `$(\neg)x_i$` denotes `$x_i$`, [valuate][bookofproofs$710] `$x_i$` as true: `$[[x_i]]_I=1.$`
   * If the literal `$(\neg)x_i$` denotes `$\neg x_i$`, [valuate][bookofproofs$710] `$x_i$` as false: `$[[x_i]]_I=0.$`
   * Then, from the definition of [negation][bookofproofs$714] it follows that `$[[\neg x_i]]_I=1.$`
   * Since all literals in `$m$` are connected using a [conjunction][bookofproofs$712] "$\wedge$" and since all are true, it follows that `$m$` is valuated true: `$[[m]]_I=1,$` by construction.
* We now show that this `$n$`-tuple is unique [by contradiction][bookofproofs$744].
   * Assume `$(a_1,\ldots,a_n)$` and  `$(b_1,\ldots,b_n)$` are two different `$n$`-touples of valutions of `$x_1,\ldots,x_n$` for which `$[[m]]_I=1.$`
   * Then there is at least one literal `$(\neg)x_i$` valued true: `$[[(\neg)x_i]]_I=1$` for which  `$[[x_i]]_I=a_i$` and `$[[x_i]]_I=b_i$` and `$a_i\neq b_i$`.
   * But a [proposition cannot be both, true and false][bookofproofs$1322].
   * Since this is a contradiction, the `$n$`-tuple of valutions of `$x_1,\ldots,x_n$` for which `$[[m]]_I=1$` is unique.

### Proof for Maxterms

* Let  `$M=(\neg)x_1\vee\ldots\vee(\neg)x_n$` be a  [maxterm][bookofproofs$7901].
* We first show by construction the existence of an `$n$`-tuple of [truth values][bookofproofs$707]  `$([[x_1]]_I,\ldots,[[x_n]]_I)\in\mathbb B^n$` such that `$[[M]]_I=0:$`
   * If the literal `$(\neg)x_i$` denotes `$x_i$`, [valuate][bookofproofs$710] `$x_i$` as false: `$[[x_i]]_I=0.$`
   * If the literal `$(\neg)x_i$` denotes `$\neg x_i$`, [valuate][bookofproofs$710] `$x_i$` as true: `$[[x_i]]_I=1.$`
   * Then, from the definition of [negation][bookofproofs$714] it follows that `$[[\neg x_i]]_I=0.$`
   * Since all literals in `$M$` are connected using a [disjunction][bookofproofs$713] "$\vee$" and since all are false, it follows that `$M$` is valuated false: `$[[M]]_I=0,$` by construction.
* We now show that this `$n$`-tuple is unique by [contradiction][bookofproofs$744].
   * Assume `$(a_1,\ldots,a_n)$` and  `$(b_1,\ldots,b_n)$` are two different `$n$`-touples of valutions of `$x_1,\ldots,x_n$` for which `$[[M]]_I=0.$`
   * Then there is at least one literal `$(\neg)x_i$` valued false: `$[[(\neg)x_i]]_I=0$` for which  `$[[x_i]]_I=a_i$` and `$[[x_i]]_I=b_i$` and `$a_i\neq b_i$`.
   * But a [proposition cannot be both, true and false][bookofproofs$1322].
   * Since this is a contradiction, the `$n$`-tuple of valutions of `$x_1,\ldots,x_n$` for which `$[[M]]_I=0$` is unique.
