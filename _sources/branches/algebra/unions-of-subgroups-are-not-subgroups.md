layout: explanation
categories: branches,algebra
nodeid: bookofproofs$8650
orderid: 7
parentid: bookofproofs$212
title: Unions of Subgroups Are Not Subgroups
description: UNIONS OF SUBGROUPS ARE NOT SUBGROUPS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$8311
keywords: unions of subgroups
contributors: bookofproofs

---


---

The [subgroup intersection criterion][bookofproofs$811] makes sure that any [set intersection][bookofproofs$6828] of subgroups of a [group][bookofproofs$671] `$G$` is also its [subgroup][bookofproofs$554] But how about the [set union][bookofproofs$6827] of subgroups? The following counterexample shows that it is not true in general:

Consider the two subgroups `$$\begin{array}{rcl}H_1&:=\{2n\mid n\in\mathbb Z\}=\{\ldots,-6,-4,-2,0,2,4,6,\ldots\}\\
H_2&:=\{3n\mid n\in\mathbb Z\}=\{\ldots,-9,-6,-3,0,2,6,9,\ldots\}\end{array}$$` of the additive group `$(\mathbb Z,+)$` of all integers. The union `$$H_1\cup H_2=\{\ldots,-9,-8,-6,-4,-3,-2,0,2,3,4,6,9,\ldots\}$$` cannot be a group (and more than ever a subgroup) because it is not [closed][bookofproofs$1103] under the addition operation. For instance, `$$-3+2=1\not\in H_1\cup H_2.$$`
