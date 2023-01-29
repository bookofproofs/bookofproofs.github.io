layout: proof
categories: branches,probability-theory-and-statistics
nodeid: bookofproofs$1811
orderid: 50
parentid: bookofproofs$1810
title: 
description:  Proof of REPLACING MUTUALLY INDEPENDENT EVENTS BY THEIR COMPLEMENTS &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$856
keywords: complements,events,independent,mutually,replacing,their,proof
contributors: bookofproofs

---


---

Assume `\(A_1,...,A_n\)` are [mutually independent events][bookofproofs$1808]. Without any loss of generality, we can replace `\(A_1\)` by the [complement event][bookofproofs$861] `\(\overline{A_1}\)`. It follows from the [probability of event difference][bookofproofs$867] and the [probability of the complement event][bookofproofs$861]:

`\[\begin{array}{rcll}
p(\overline{A_1}\cap A_2\cap\ldots \cap A_n)&=&p(A_2\cap\ldots \cap A_n)-p(A_1\cap A_2\cap\ldots \cap A_n)&\text{probability of event difference}\\
&=&p(A_2)\cdot\ldots \cdot p(A_n)-p(A_1)\cdot p(A_2)\cdot \ldots \cdot p(A_n)&\text{mutual independence}\\
&=&(1-p(A_1))\cdot p(A_2)\cdot\ldots \cdot p(A_n)&\text{distributivity of real numbers}\\
&=&p(\overline{A_1})\cdot p(A_2)\cdot\ldots \cdot p(A_n)&\text{probability of complement event}\\
\end{array}
\]`

Thus, replacing any `\(A_i\)` by the [complement event][bookofproofs$861] `\(\overline{A_i}\)` results in mutually independent events.
