layout: proof
categories: branches,set-theory
nodeid: bookofproofs$6660
orderid: 50
parentid: bookofproofs$6659
title: Uncountable Set
description:  Proof of RATIONAL NUMBERS ARE COUNTABLE &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$581
keywords: rational numbers are countable,proof
contributors: bookofproofs

---


---

* Consider the following diagonal indexing (start counting in the left-upper corner, go to the right, then diagonally to the left, until you come back to the first column, and then start a new diagonal, beginning in the first row):
`\[\begin{array}{ccccccc}
\left(\frac{1}{1}\right)_1,&\left(\frac{1}{2}\right)_2,&\left(\frac{1}{3}\right)_4,&\left(\frac{1}{4}\right)_7,&\left(\frac{1}{5}\right)_{11},&\cdots\\
\left(\frac{2}{1}\right)_3,&\left(\frac{2}{2}\right)_5,&\left(\frac{2}{3}\right)_8,&\left(\frac{2}{4}\right)_{12},&\cdots\\
\left(\frac{3}{1}\right)_6,&\left(\frac{3}{2}\right)_9,&\left(\frac{3}{3}\right)_{13},&\cdots\\
\left(\frac{4}{1}\right)_{10},&\left(\frac{4}{2}\right)_{14},&\cdots\\
\left(\frac{5}{1}\right)_{15},&\cdots\\
\vdots
\end{array}\]`
* By the proposition about the [union of countable many countable sets][bookofproofs$796] it follows that there is an injective function `$f:\mathbb Q\to\mathbb N.$`
* By the definition of [countable][bookofproofs$772] sets, this means that `$\mathbb Q$` is countable.
