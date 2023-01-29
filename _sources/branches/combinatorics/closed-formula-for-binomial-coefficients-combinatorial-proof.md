layout: proof
categories: branches,combinatorics
nodeid: bookofproofs$1401
orderid: 50
parentid: bookofproofs$1400
title: 
description: COMBINATORIAL PROOF Proof of CLOSED FORMULA FOR BINOMIAL COEFFICIENTS &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$1112
keywords: closed formula for binomial coefficients,closed formula for the binomial coefficient,proof
contributors: bookofproofs

---


---

We have to show that the closed formula for the [binomial coefficient][bookofproofs$993].
`\[\binom nk=\frac{n(n-1)\cdots(n-k+1)}{k(k-1)\cdots 2\cdot 1}\]`
can be interpreted as the number of subsets with exactly `\(k\)` elements of a given [finite set][bookofproofs$985] `\(X\)` with exactly `\(n\)` elements `\((|X|=n)\)`. 

We enumerate each element of `\(X\)` and get an index set `\(I=\{1,2,\cdots n\}\)`. Instead of counting the subsets of `\(X\)` with `\(k\)` elements, in which the order of elements does not count, we start to count the subsequences of length `\(k\)`, which can be built from `\(I\)`, in which the order of sequence elements does count. 

There are `\(n\)` choices for the first element of the sequence; for each, there are `\(n-1\)` choices for the second; and so on, until there are `\(n - k +1\)` choices for the `\(k\)`-th. This gives the [falling factorial power][bookofproofs$1399] `\(n^{\underline{k}}=n(n-1)\cdots(n-k+1)\)` of choices for a sequence with `\(k\)` sequence elements. 

Observe that the [definition of factorial][bookofproofs$1005] `\(k(k-1)\cdots 2\cdot 1\)` gives the number of possibilities, we can arrange a sequence with `\(k\)` sequence elements. This number of possible orderings of sequences counts each subset exactly `\(k!\)` times. To get our answer, we simply divide by `\(k!\)` and get

`\[\frac{n^{\underline{k}}}{k!}=\frac{n(n-1)\cdots(n-k+1)}{k(k-1)\cdots 2\cdot 1}=\binom nk.\]`
