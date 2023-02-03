layout: example
categories: branches,set-theory
nodeid: bookofproofs$8082
orderid: 100
parentid: bookofproofs$8079
title: Some Other Examples Of Mostowski Functions and Collapses
description: SOME OTHER EXAMPLES OF MOSTOWSKI FUNCTIONS AND COLLAPSES &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$8055
keywords: collapses,examples,functions,mostowski,other,some
contributors: bookofproofs


---


---

The above introductory example was quite easy. Is also shows why it is important to have a [well-founded][bookofproofs$8058] to be able to calculate its [Mostowski function and collapse][bookofproofs$8079]. To get more familiar with the latter two concepts, let us take some more [examples of well-founded relations][bookofproofs$8060] and calculate their Mostowski functions and collapses. 

### Ad Example 2

The relation `$R\subset \mathbb N\times \mathbb N$`  defined by  `$nRm:\Leftrightarrow n+1=m$` ("successor relation" defined on natural numbers) has been identified as a [well-founded][bookofproofs$8058] relation. We calculate some first values of the [Mostowski function][bookofproofs$8079]:

`$$\begin{array}{rcl}
\pi(0)&=&\emptyset\\
\pi(1)&=&\{\pi(0)\}=\{\emptyset\}\\
\pi(2)&=&\{\pi(1)\}=\{\{\emptyset\}\}\\
\pi(3)&=&\{\pi(2)\}=\{\{\{\emptyset\}\}\}\\
&\vdots&
\end{array}$$`

Historically, this series of sets was used by <a href="https://mathshistory.st-andrews.ac.uk/Biographies/Zermelo/">Zermelo</a> to define the [natural numbers][bookofproofs$718] `$\mathbb N$` and can be visualized as follows:


![axiom8_1](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/axiom8_1.jpg?raw=true)


The Mostowski collapse here is the set containing all of the above sets as its elements:

`$$\pi([\mathbb N])=\{\emptyset,\{\emptyset\},\{\{\emptyset\}\},\{\{\{\emptyset\}\}\},\ldots\}.$$`

In contrast to the first example of the [von Neumann][bookofproofs$8080] series, this Mostowski collapse does not correspond to the value of the Mostowski function `$\pi(n)$`, as `$n$` tends to infinity.

### Ad Example 3

For a set `$X$` and its [power set][bookofproofs$6831] `$\mathcal P(X)$`, the relation `$R\subseteq \mathcal P(X)\times \mathcal P(X)$`  defined by  `$xRy:\Leftrightarrow x\subset y$` ($x$ being a proper subset of `$y$`) has been identified as a [well-founded][bookofproofs$8058] relation. As an example, we take `$X=\{a,b,c\}.$` Then `$\mathcal P(X)=\{\emptyset,\{a\},\{b\},\{c\},\{a,b\},\{a,c\},\{b,c\},\{a,b,c\}\}$`. Since in this example, the set is finite, we can calculate all values of the [Mostowski function][bookofproofs$8079]:

`$$\begin{array}{rcl}
\pi(\emptyset)&=&\emptyset\\
\pi(\{a\})&=&\{\pi(\emptyset)\}=\{\emptyset\}\\
\pi(\{b\})&=&\{\pi(\emptyset)\}=\{\emptyset\}\\
\pi(\{c\})&=&\{\pi(\emptyset)\}=\{\emptyset\}\\
\pi(\{a,b\})&=&\{\pi(\emptyset),\pi(\{a\}),\pi(\{b\})\}=\{\emptyset, \{\emptyset\}\}\\
\pi(\{a,c\})&=&\{\pi(\emptyset),\pi(\{a\}),\pi(\{c\})\}=\{\emptyset, \{\emptyset\}\}\\
\pi(\{b,c\})&=&\{\pi(\emptyset),\pi(\{b\}),\pi(\{c\})\}=\{\emptyset, \{\emptyset\}\}\\
\pi(\{a,b,c\})&=&\{\pi(\emptyset),\pi(\{a\}),\pi(\{b\}),\pi(\{c\}),\pi(\{a,b\}),\pi(\{a,c\}),\pi(\{b,c\})\}\\
&=&\{\emptyset, \{\emptyset\},\{\emptyset, \{\emptyset\}\}\}
\end{array}$$`

The Mostowski collapse is the set `$$\pi[\mathcal P(\{a,b,c\})]=\{\emptyset, \{\emptyset\}, \{\emptyset, \{\emptyset\}\}, \{\emptyset, \{\emptyset\},\{\emptyset, \{\emptyset\}\}\}\}.$$`


### Ad Example 4


The divisibility relation  `$R$`  defined on the set `$X_k:=\{1,2,3,\ldots,k\}$`  with  `$nRm:\Leftrightarrow n\mid m\wedge n\neq m$` ($n$ is a divisor of `$m$` which is unequal `$m$`) has been identified as a well-defined relation. We calculate all values of the [Mostowski function][bookofproofs$8079] for `$k=10:$`

`$$\begin{array}{rcl}
\pi(1)&=&\emptyset\\
\pi(2)&=&\{\pi(1)\}=\{\emptyset\}\\
\pi(3)&=&\{\pi(1)\}=\{\emptyset\}\\
\pi(4)&=&\{\pi(1),\pi(2)\}=\{\emptyset,\{\emptyset\}\}\\
\pi(5)&=&\{\pi(1)\}=\{\emptyset\}\\
\pi(6)&=&\{\pi(1),\pi(2),\pi(3)\}=\{\emptyset,\{\emptyset\}\}\\
\pi(7)&=&\{\pi(1)\}=\{\emptyset\}\\
\pi(8)&=&\{\pi(1),\pi(2),\pi(4)\}=\{\emptyset,\{\emptyset\}\}\\
\pi(9)&=&\{\pi(1),\pi(3)\}=\{\emptyset,\{\emptyset\}\}\\
\pi(10)&=&\{\pi(1),\pi(2),\pi(5)\}=\{\emptyset,\{\emptyset\}\}\\
\end{array}$$`

The Mostowski function equals `$\emptyset$` for `$1$`, `$\{\emptyset\}$` for all prime numbers `$p\le k,$` and `$\{\emptyset,\{\emptyset\}\}$` for all composite numbers `$n\le k.$` The Mostowski collapse equals (for all `$k$`) the set 
`$$\pi[X_k]=\{\emptyset,\{\emptyset\},\{\emptyset,\{\emptyset\}\}\}.$$`
