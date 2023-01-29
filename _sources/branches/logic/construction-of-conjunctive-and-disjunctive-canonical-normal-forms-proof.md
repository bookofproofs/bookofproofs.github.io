layout: proof
categories: branches,logic
nodeid: bookofproofs$7906
orderid: 50
parentid: bookofproofs$7905
title: 
description:  Proof of CONSTRUCTION OF CONJUNCTIVE AND DISJUNCTIVE CANONICAL NORMAL FORMS &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$711,bookofproofs$7895
keywords: canonical,conjunctive,construction,disjunctive,forms,normal,conjunctive and,proof
contributors: bookofproofs

---


---

### Context

* Let `$\phi$` be a [proposition][bookofproofs$1307] with a [Boolean function][bookofproofs$1316] `$f_\phi.$`
* Without loss of generality, we can assume that `$\phi$` contains exactly `$n\ge 1$` [prime propositions][bookofproofs$7867] `$x_1,\ldots,x_n.$`[^1]  
* Let `$T$` be the corresponding [truth table][bookofproofs$7868] of `$f_\phi$`. Note that 
   * `$T$` contains `$n+1$` colums: `$n$` columns for the valuations of each prime proposition `$[[p_i]]_I$` and one column for the valuation `$[[\phi]]_I.$`
   * `$T$` has either rows with `$[[\phi]]_I=0$` only or with `$[[\phi]]_I=1$` only, or both types of rows.

### Existence of `$\operatorname{dcnf}(\phi)$`, respectively `$\operatorname{ccnf}(\phi)$`

1. Assume that there are only rows with `$[[\phi]]_I=1$`, then continue with step 3. 
1. Assume that there are only rows with `$[[\phi]]_I=0$`, then continue with step 4.
1. If we have `$d\ge 1$` rows with `$[[\phi]]_I=1,$` then we construct the [minterms][bookofproofs$7901] `$m_1,\ldots,m_d,$` as follows: 
   * For the `$j$`-th row with the valuation `$[[\phi]]_I=1$`, `$j=1,\ldots,d$`:
      * If  `$[[p_i]]_I=0$` in the `$j$`-th row, then take the [literal][bookofproofs$7901] `$\neg p_i$`, otherwise take the literal `$p_i$`.
      * Form the [conjunction][bookofproofs$712] of these literals to form the minterm `$m_j:=(\neg)p_1\wedge\ldots\wedge(\neg)p_n$` of the `$j$`-th row.
   * Form the [disjunction][bookofproofs$713] of all minterms to form the [disjunctive canonical normal form][bookofproofs$7904] `$\operatorname{dcnf}(\phi):=m_1\vee \ldots\vee m_d.$`
1. If we have `$c\ge 1$` rows with `$[[\phi]]_I=0,$` then we construct the [maxterms][bookofproofs$7901] `$M_1,\ldots,M_c,$` as follows: 
   * For the `$j$`-th row with the valuation `$[[\phi]]_I=0$`, `$j=1,\ldots,c$`:
      * If  `$[[p_i]]_I=0$` in the `$j$`-th row, then take the [literal][bookofproofs$7901] `$p_i$`, otherwise take the literal `$\neg p_i$`.
      * Form the [disjunction][bookofproofs$713] of these literals to form the maxterm `$M_j:=(\neg)p_1\vee\ldots\vee(\neg)p_n$` of the `$j$`-th row.
   * Form the [conjunction][bookofproofs$712] of all maxterms to form the [conjunctive canonical normal form][bookofproofs$7904] `$\operatorname{ccnf}(\phi):=M_1\wedge \ldots\wedge M_c.$`

It follows that there is either the [disjunctive canonical normal form][bookofproofs$7904] `$\operatorname{dcnf}(\phi)$`, or the [conjunctive canonical normal form][bookofproofs$7904] `$\operatorname{ccnf}(\phi)$`, or both simultaneously, depending on the cases 1 to 4.
 
### Uniqueness of `$\operatorname{dcnf}(\phi)$`, respectively `$\operatorname{ccnf}(\phi)$`

* First of all, note that each literal of all minterms and maxterms is clearly defined by above construction and depends on the valuations `$[[\phi]]_I$` in `$j$`-th row and `$[[p_i]]_I$` in `$i$`-th column of the truth table.
* Next, the semantics of each minterm `$m_j=(\neg)p_1\wedge\ldots\wedge(\neg)p_n$` does not change with the order of literals because of the [commutativity][bookofproofs$1834] and [associativity of conjunction][bookofproofs$6844] "$\wedge$".
* The same holds for each maxterm `$M_j=(\neg)p_1\vee\ldots\vee(\neg)p_n$` due of the [commutativity][bookofproofs$1835] and [associativity of disjunction][bookofproofs$6846] "$\vee$".
* By the same argument, the semantics of the `$\operatorname{dcnf}(\phi)=m_1\vee \ldots\vee m_d$`, respectively `$\operatorname{dcnf}(\phi)=M_1\wedge \ldots\wedge M_c$` does not change with the order of the minterms `$m_j$`, respectively maxterms `$M_j.$`

It follows that the constructed `$\operatorname{dcnf}(\phi)$` respectively `$\operatorname{ccnf}(\phi)$` are unique except for the order of minterms resp. maxterms and literals in each minterm, respectively maxterms.

### Correctness of `$\operatorname{dcnf}(\phi)$`, respectively `$\operatorname{ccnf}(\phi)$`

We want to verify, that `$\phi$`, `$\operatorname{dcnf}(\phi)$` and  `$\operatorname{ccnf}(\phi)$` indeed represent the same [Boolean function][bookofproofs$1316].
* If `$\operatorname{dcnf}(\phi)$` exists, then: 
   * According to the definition of [conjunction][bookofproofs$712], each minterm `$m_j=(\neg)p_1\wedge\ldots\wedge(\neg)p_n$` is valued true, if and only if each of its literals `$(\neg)p_i$` is valued true. 
   * According to the lemma about the [unique valuation of minterms][bookofproofs$7902], there is exactly one `$n$`-tuple of [truth values][bookofproofs$707] assigned  to `$p_1,\ldots,p_n$`, for which `$m_j$` is true. 
   * Therefore, `$m_j$` is by its construction true, if and only if `$\phi$` is true for the same `$n$`-tuple of truth values assigned to `$p_1,\ldots,p_n$`.
   * The disjunction `$m_1\vee\ldots\vee m_d$` iterates through all and only such tuples for which `$m_j$` and `$\phi$` are valued true, and connects them by the logical "or". 
   * By definition of disjunction, the whole `$\operatorname{dcnf}(\phi)$`  is true if and only if at least one minterm is true. 
   * Thus, `$\operatorname{dcnf}(\phi)$` is true if and only if `$\phi$` is true.
   * Thus, `$\operatorname{dcnf}(\phi)$` represents the same Boolean function as `$\phi$`, formally `$f_\phi=f_{\operatorname{dcnf}(\phi)}.$` 
* If `$\operatorname{ccnf}(\phi)$` exists, then: 
   * According to the definition of [disjunction][bookofproofs$713], each maxterm `$M_j=(\neg)p_1\vee\ldots\vee(\neg)p_n$` is valued false, if and only if each of its literals `$(\neg)p_i$` is valued false. 
   * According to the lemma about the [unique valuation of maxterms][bookofproofs$7902], there is exactly one `$n$`-tuple of [truth values][bookofproofs$707] assigned  to `$p_1,\ldots,p_n$`, for which `$M_j$` is false. 
   * Therefore, `$M_j$` is by its construction false, if and only if `$\phi$` is false for the same `$n$`-tuple of truth values assigned to `$p_1,\ldots,p_n$`.
   * The conjunction `$M_1\wedge\ldots\wedge M_c$` iterates through all and only such tuples and connects them by the logical "and".
   * By definition of conjunction, the whole `$\operatorname{ccnf}(\phi)$`  is false if and only if at least one maxterm is false. 
   * Thus, `$\operatorname{ccnf}(\phi)$` is false if and only if `$\phi$` is false.
   * Thus `$\operatorname{ccnf}(\phi)$` represents the same Boolean function as `$\phi$`, formally `$f_\phi=f_{\operatorname{ccnf}(\phi)}.$` 

[^1]: By definition, this can be either Boolean variables or Boolean constants.
