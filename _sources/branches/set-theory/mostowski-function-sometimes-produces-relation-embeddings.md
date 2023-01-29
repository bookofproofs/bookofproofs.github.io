layout: motivation
categories: branches,set-theory
nodeid: bookofproofs$8084
orderid: 300
parentid: bookofproofs$8079
title: Observation 2: The Mostowski Function (Sometimes) Produces Relation Embeddings
description: OBSERVATION 2: THE MOSTOWSKI FUNCTION SOMETIMES PRODUCES RELATION EMBEDDINGS &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$8055
keywords: embeddings,function,mostowski,produces,relation,sometimes
contributors: bookofproofs


---


---

We now take again the [initial example][bookofproofs$8080] and the [other examples][bookofproofs$8082] to make another observation. Remember that we can treat the [contained relation][bookofproofs$8066] `$\in_X$` as a real [relation][bookofproofs$571] between the elements of some given set `$X.$` Moreover, please recall the introduced concept of an [order embedding][bookofproofs$8083], in the case `$X$` is ordered. Now, the relation `$R$` used to define a [Mostowski function][bookofproofs$8079] `$$\pi(x):=\{\pi(y)\mid y\in V\wedge yRx\}$$` 
has not necessarily to be an order relation, but it must be a [well-founded][bookofproofs$8058] relation. We want to observe, if `$\pi$` is capable to produce **embeddings** of `$R$` in the sense, that the following [equivalence][bookofproofs$1305] is fulfilled:
 
`$$nRm\Longleftrightarrow \pi(n)\in_X\pi(m).\quad ( * )$$` 

Please note that the Mostowski function `$\pi$` is [right-unique][bookofproofs$1308], as every [function][bookofproofs$592] is. The above equivalence is fulfilled in the cases, in which `$\pi$` is, in addition, [left-unique][bookofproofs$1308] (i.e. injective). 

After these preliminary considerations, we can now start to make our observations. In our case, the set `$X,$` in which the contained relation `$\in_X$` is defined, is the [Mostowski collapse][bookofproofs$8079] `$X:=\pi([V]).$` The first two examples seem to fulfill the property `$( * ),$` and we write below `$\in$` instead of `$\in_{\pi([V])}$` for readability reasons, but the reader should be aware that we mean the [contained relation][bookofproofs$8066] defined on the corresponding Mostowski collapse.

### Ad Example 1

Two natural numbers `$n$` and `$m$` are in the strict order `$n < m$` if and only if the corresponding image of the Mostowski function `$\pi(n)$` is an element of the image `$\pi(m).$` In other words, we have for all `$n,m\in\mathbb N$` the relation embedding

`$$n < m\Longleftrightarrow \pi(n)\in \pi(m).$$` 

It is left for the reader as an exercise to verify it for some special cases, for instance `$n=1, m=2$` or `$n=1, m=3.$` 

### Ad Example 2

The natural number `$m$` is the successor of the natural number `$n$`, if and only if the corresponding image of the Mostowski function `$\pi(n)$` is an element of the image `$\pi(m).$` In other words, we have for all `$n,m\in\mathbb N$` the relation embedding

`$$n+1=m\Longleftrightarrow \pi(n)\in \pi(m).$$`

It is left for the reader as an exercise to verify it for some special cases, for instance `$n=1, m=2$` or `$n=2, m=3.$` 

### Ad Examples 3 and 4

In theses examples, there is no embedding possible and the property `$( * )$` is only fulfilled in one direction `$nRm\Longrightarrow \pi(n)\in_X\pi(m).$` The opposite direction is broken. For instance:

* In the example 3: `$\pi(\{b\})\in\pi(\{a,c\})$` but `$\{b\}\not\in \{a,c\}.$`
* In the example 4: `$\pi(2)\in\pi(9)$` but `$2$` does not divide `$9.$`

In the above examples, the new question arises, why `$\pi$` in some cases does produce an embedding `$( * )$` and why it does not in other cases. [Mostowski][mo] discovered that this has to do with the question, whether the underlying relation `$R$` is [extensional][bookofproofs$8059] or not. 

[mo][https://mathshistory.st-andrews.ac.uk/Biographies/Mostowski/]

* We have seen that [strict orders are extensional][bookofproofs$8075], therefore, in example 1 there is an embedding possible.
* In example 2, the successor relation `$nRm:\Leftrightarrow n+1=m$` is also extensional, since from `$\{n\in\mathbb N\mid n+1=m_1\}=\{n\in\mathbb N\mid n+1=m_2\}$` it follows that `$m_1=m_2.$` 
* It is left for the reader as an exercise to verify that the relations in the examples 3 and 4 are not extensional.
