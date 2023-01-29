layout: definition
categories: branches,logic
nodeid: bookofproofs$7904
orderid: 400
parentid: bookofproofs$7898
title: Conjunctive and Disjunctive Canonical Normal Forms
description: CONJUNCTIVE AND DISJUNCTIVE CANONICAL NORMAL FORMS &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$711,bookofproofs$7895
keywords: canonical,conjunctive,conjunctive canonical normal form,disjunctive,disjunctive canonical normal form,forms,normal
contributors: bookofproofs

---
Particularly important types of [canonical normal forms][bookofproofs$7900] are the __conjunctive canonical normal form__ `$\operatorname{ccnf}$` and the __disjunctive canonical normal form__ `$\operatorname{dcnf}$`, which we will now formally define:

---

Let `$\phi$` be a [proposition][bookofproofs$1307] with the [Boolean variables][bookofproofs$1307] `$x_1,\ldots,x_n.$`

A **conjunctive canonical normal form** of `$\phi$` is a proposition `$\operatorname{ccnf}(\phi)$` such that:
* `$\operatorname{ccnf}(\phi)$` is a [canonical normal form][bookofproofs$7900] of `$\phi$`, i.e. `$\phi$` and `$\operatorname{ccnf}(\phi)$` have identical [Boolean functions][bookofproofs$1316] `$f_\phi=f_{\operatorname{ccnf}(\phi)}.$`
* `$\operatorname{ccnf}(\phi)$` has the following syntax:
`$$\begin{array}{rcl}\operatorname{ccnf}(\phi)&=&M_1\wedge \ldots \wedge M_n\\
&=&\bigwedge_{i=1}^n(\neg)x_1\vee \ldots\vee (\neg)x_n,
\end{array}$$`
where all [maxterms][bookofproofs$7901] `$M_i$` are pairwise different.

A **disjunctive canonical normal form** of `$\phi$` is a proposition `$\operatorname{dcnf}(\phi)$` such that:
* `$\operatorname{dcnf}(\phi)$` is a [canonical normal form][bookofproofs$7900] of `$\phi$`, i.e. `$\phi$` and `$\operatorname{dcnf}(\phi)$` have identical [Boolean functions][bookofproofs$1316] `$f_\phi=f_{\operatorname{dcnf}(\phi)}.$`
* `$\operatorname{dcnf}(\phi)$` has the following syntax:
`$$\begin{array}{rcl}\operatorname{dcnf}(\phi)&=&m_1\vee \ldots \vee m_n\\
&=&\bigvee_{i=1}^n(\neg)x_1\wedge \ldots\wedge (\neg)x_n,
\end{array}$$`
where all [minterms][bookofproofs$7901] `$m_i$` are pairwise different.
