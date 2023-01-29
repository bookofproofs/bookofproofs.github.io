layout: proof
categories: branches,probability-theory-and-statistics
nodeid: bookofproofs$869
orderid: 50
parentid: bookofproofs$868
title: 
description:  Proof of PROBABILITY OF EVENT UNION &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$856
keywords: event,probability,union,proof
contributors: bookofproofs

---


---

We first note that

`\[A\cup B=(A\cap B)\cup(A\cap\overline B)\cup (\overline A\cap B).\]`

Because the events `\((A\cap B)\)`, `\((A\cap\overline B)\)` and `\((\overline A\cap B)\)` are [mutually exclusive][bookofproofs$859], it follows from the [definition of probability][bookofproofs$858] that 

`\[\begin{array}{ccl}
p(A\cup B)&=&p(A\cap B)+p(A\cap\overline B)+p(\overline A\cap B)\\
&=&p(A\cap(B\cup \overline B))+p(\overline A\cap B)\\
&=&p(A\cap\Omega)+p(\overline A\cap B)\\
&=&p(A)+p(\overline A\cap B)\\
\end{array}~~~~~~~~~~~( * ).\]`

Because `\(B=(A\cap B)\cup (\overline A\cap B)\)`, and because again, both events `\((A\cap B)\)` and `\((\overline A\cap B)\)` are [mutually exclusive][bookofproofs$859], we have `\[p(\overline A\cap B)=p(B)-p(A\cap B).\]`

Together with `\(( * )\)`, we get

`\[p(A\cup B)=p(A)+p(B)-p(A\cap B),\]`

 as required.
