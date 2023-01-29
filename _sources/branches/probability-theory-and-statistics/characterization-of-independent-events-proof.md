layout: proof
categories: branches,probability-theory-and-statistics
nodeid: bookofproofs$1805
orderid: 50
parentid: bookofproofs$1804
title: 
description:  Proof of CHARACTERIZATION OF INDEPENDENT EVENTS &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$856
keywords: characterization,events,independent,proof
contributors: bookofproofs

---


---

Assuming `\(0 < p(B) < 1\)`, we have to show the equivalence

`\[p(A|B)=p(A|\overline{B})\Longleftrightarrow p(A)=p(A|B).\]`

### "`\(\Rightarrow\)`"

Assume the events `\(A\)` and `\(B\)` are [independent][bookofproofs$395]. Then the equation `\(p(A|B)=p(A|\overline{B})\)` holds (hypothesis). Because `\(A=(A\cap B )\cup(A\cap\overline{B})\)`, it follows from the  

* [probability of event union][bookofproofs$868],
* [probability of impossible event][bookofproofs$862],
* [probability of joint events][bookofproofs$1802], 
* [distributivity of real numbers][bookofproofs$520], and
* [probability of complement event][bookofproofs$861] that

`\[\begin{array}{rcll}
p(A)&=&p((A\cap B )\cup(A\cap\overline{B}))&\text{because }A=(A\cap B )\cup(A\cap\overline{B})\\
&=&p(A\cap B )+p(A\cap\overline{B})-p(A\cap B\cap A\cap\overline{B})&\text{probability of event union}\\
&=&p(A\cap B )+p(A\cap\overline{B})-p(\emptyset)&\text{because }B\cap \overline{B}=\emptyset\text{ and }A\cap \emptyset=\emptyset\\
&=&p(A\cap B )+p(A\cap\overline{B})&\text{probability of impossible event}\\
&=&p(A|B)p(B)+p(A|\overline{B})p(\overline{B})&\text{probability of joint events}\\
&=&p(A|B)p(B)+p(A|B)p(\overline{B})&\text{by hypothesis}\\
&=&p(A|B)(p(B)+p(\overline{B}))&\text{distributivity law of real numbers}\\
&=&p(A|B)(p(B)+1-p(B))&\text{probability of complement event}\\
&=&p(A|B)&\text{cancellation of }p(B)\text{ and multiplication by }1\\
\end{array}\]`

### "`\(\Leftarrow\)`"

Now assume that `\(p(A|B)=p(A)\)` (hypothesis). Because `\(0 < p(B) < 1\)`, it follows from the [probability of complement event][bookofproofs$861] that `\(1 > p(\overline{B}) > 0\)`.

By applying

* [conditional probability][bookofproofs$428],
* [probability of event difference][bookofproofs$867].
* [probability of joint events][bookofproofs$1802], 
* [distributivity of real numbers][bookofproofs$520], and
* [probability of complement event][bookofproofs$861], we obtain


`\[\begin{array}{rcll}
p(A|\overline{B})&=&\frac{p(A\cap \overline{B})}{p(\overline{B})}&\text{conditional probability and }p(\overline{B}) > 0\\
&=&\frac{p(A)- p(A\cap B)}{p(\overline{B})}&\text{probability of event difference}\\
&=&\frac{p(A)- p(A|B)p(B)}{p(\overline{B})}&\text{probability of joint events}\\
&=&\frac{p(A)- p(A)p(B)}{p(\overline{B})}&\text{hypothesis}\\
&=&\frac{p(A)(1-p(B))}{p(\overline{B})}&\text{distributivity of real numbers}\\
&=&\frac{p(A)(p(\overline{B}))}{p(\overline{B})}&\text{probability of complement event}\\
&=&p(A)&\text{cancelling }p(\overline{B})
\end{array}\]`
