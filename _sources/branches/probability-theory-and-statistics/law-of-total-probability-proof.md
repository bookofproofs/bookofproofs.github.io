layout: proof
categories: branches,probability-theory-and-statistics
nodeid: bookofproofs$1828
orderid: 50
parentid: bookofproofs$449
title: 
description:  Proof of LAW OF TOTAL PROBABILITY &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$856
keywords: law,law of total probability,probability,total,proof
contributors: bookofproofs

---


---

Because, by hypothesis, the events `\(A_1,A_2,\ldots,A_n\)`  are [mutually exclusive and collectively exhaustive][bookofproofs$859], it follows from the [definition of probability][bookofproofs$858].
`\[1=p(\Omega)=p(A_1\cup A_2\cup\ldots \cup A_n)=\sum_{i=1}^n p(A_i).\quad\quad ( * )\]`

For any [event][bookofproofs$857] `\(B\)`, the events `\((B\cap A_1), (B\cap A_2),\ldots, (B\cap A_n)\)` are also mutually exclusive. Therefore, we have

`\[p((B\cap A_1)\cup (B\cap A_2)\cup\ldots\cup (B\cap A_n))=\sum_{i=1}^n p(B\cap A_i).\quad\quad ( * * )\]`

By hypothesis, we have `\(p(A_i) > 0\)` for `\(i=1,2,\ldots,n\)` and it follows from the [conditional probability formula][bookofproofs$428]:

`\[\begin{array}{rcll}
p(B)&=&p(B\cap \Omega)&\text{definition of probability space}\\
&=&p(B\cap (A_1\cup A_2\cup\ldots \cup A_n))&\text{by }( * )\\
&=&p((B\cap A_1)\cup (B\cap A_2)\cup\ldots\cup (B\cap A_n))&\text{distributivity law for sets}\\
&=&\sum_{i=1}^n p(B\cap A_i)&\text{by }( * * )\\
&=&\sum_{i=1}^n p(B|A_i)p(A_i)&\text{conditional probability formula and }p(A_i) > 0\text{ for } i=1,2,\ldots,n.\\
\end{array}\]`
