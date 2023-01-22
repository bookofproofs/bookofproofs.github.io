layout: proof
categories: branches,algebra
nodeid: bookofproofs$1040
orderid: 0
parentid: bookofproofs$1039
title: 
description: PROOF BY CONTRADICTION Proof of UNIQUENESS LEMMA OF A FINITE BASIS &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$561
keywords: basis,lemma,uniqueness,proof
contributors: bookofproofs

---


---

Let `\(v\)` be a vector in a vector space `\(V\)` with the basis `\(B\)`.

If `\(B\)` is [finite][bookofproofs$985], then we have `\(B=\{b_1,\ldots, b_n\}\)`. Suppose that there are two different representations 
`\[\begin{array}{ccl}
v&=&\alpha_1b_1+\ldots+\alpha_nb_n,\\
v&=&\beta_1b_1+\ldots+\beta_nb_n.\\
\end{array}~~~~~~~~~~~~~~~~~( * )\]` 
Then we have
`\[\begin{array}{ccl}
0&=&(\alpha_1-\beta_1)b_1+\ldots+(\alpha_n-\beta_n)b_n,
\end{array}\]` 
Because the representations `\( ( * ) \)` are different by assumption, there is at least one `\(i\)` for which `\(\alpha_i\neq \beta_i\)`. But this would mean that `\(\{b_1,\ldots, b_n\}\)` are [linearly dependent][bookofproofs$1036], in [contradiction][bookofproofs$744] to the [definition of a basis][bookofproofs$299]
