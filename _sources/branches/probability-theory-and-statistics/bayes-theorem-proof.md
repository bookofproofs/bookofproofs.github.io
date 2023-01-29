layout: proof
categories: branches,probability-theory-and-statistics
nodeid: bookofproofs$1833
orderid: 50
parentid: bookofproofs$464
title: 
description:  Proof of BAYES' THEOREM &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$856
keywords: bayes,theorem,proof
contributors: bookofproofs

---


---

By hypothesis, `\(p(B) > 0\)`. It follows from the definition of [conditional probability][bookofproofs$428].
`\[p(A_i|B)=\frac{p(A_i\cap B)}{p(B)}=\frac{p(B\cap A_i)}{p(B)},\quad\quad i=1,2,\ldots,n.\quad\quad( * )\]`

Applying the [probability of joint events][bookofproofs$1802] to the nominator of `\(( * )\)` , we get 
`\[p(A_i|B)=\frac{p(B|A_i)p(A_i)}{p(B)},\quad\quad i=1,2,\ldots,n.\quad\quad( * * )\]`

Because by hypothesis all events `\(A_1,A_2,\ldots,A_n\)` are [mutually exclusive and collectively exhaustive][bookofproofs$859] with `\(p(A_i) > 0\)` for `\(i=1,2,\ldots,n\)`, we can apply the law of total probability to the denominator of `\( ( * * ) \)` and get the required result:

`\[p(A_i|B)=\frac{p(B|A_i)p(A_i)}{\sum_{i=1}^np(B|A_i)p(A_i)},\quad\quad i=1,2,\ldots,n.\]`
