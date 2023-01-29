layout: proof
categories: branches,probability-theory-and-statistics
nodeid: bookofproofs$1817
orderid: 50
parentid: bookofproofs$1816
title: 
description:  Proof of MONOTONICALLY INCREASING PROPERTY OF PROBABILITY DISTRIBUTIONS &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$581,bookofproofs$1796
keywords: distributions,increasing,monotonically,probability,property,proof
contributors: bookofproofs

---


---

### `\((i)\)` Proof of monotonically increasing property

We first show that the [probability distribution][bookofproofs$1815] is [monotonically increasing][bookofproofs$282]. Assume `\(x < y\)`. Then, we have for the [left-open intervals][bookofproofs$1153] `\((-\infty,x]\)` and `\((-\infty,y]\)` that `\((-\infty,x]\subset (-\infty,y]\)`. For the events `\(X\le x\)` and `\(X\le y\)`, we gain by virtue of the [probability of included event][bookofproofs$865] the required property
`\[x < y\Longrightarrow p(X\le x)\le p(Y\le y).\]`

### `\((ii)\)` Proof of `\(\lim_{x\to-\infty} p(X\le x)=0\)`
 
Note that [following the definition of a random variable][bookofproofs$1813], `\(X\)` is a [total map][bookofproofs$592]. Therefore, `\(X\)` will map __every__ outcome of the [given random experiment][bookofproofs$857] to the [set of real numbers][bookofproofs$1105] `\(\mathbb R\)`. In particular, there is some real number `\(x_\emptyset\in\mathbb R\)`, to which `\(X\)` maps the [impossible][bookofproofs$183] realization `\(\emptyset\)`:

`\[X(\emptyset)=x_\emptyset.\]`

For any real sequence `\((x_n)_{n\in\mathbb N}\)` [tending to minus infinity][bookofproofs$1345], `\(\lim_{n\to\infty} x_n=-\infty\)`, there exists an index `\(N_\emptyset\in\mathbb N\)` such that 
`\[x_n < x_\emptyset\quad\quad\text{for all }n \ge N_\emptyset.\]`

It follows from `\((i)\)` and the [probability of the impossible event][bookofproofs$862] that

`\[p(X\le x_n)\le p(X\le x_\emptyset)=0\quad\quad\text{for all }n \ge N_\emptyset.\]`

Because of the [axiom telling us that every probability is a non-negative number][bookofproofs$872], we get 

`\[0\le p(X\le x_n)\le p(X\le x_\emptyset)=0\quad\quad\text{for all }n \ge N_\emptyset,\]`

or 

 `\[\lim_{x\to-\infty} p(X\le x)=0.\]`


### `\((iii)\)` Proof of `\(\lim_{x\to+\infty} p(X\le x)=1\)`
 
Similarly to `\((ii)\)`, since `\(X\)` is a total map, there is some real number `\(x_\Omega\in\mathbb R\)`, to which `\(X\)` maps the [certain][bookofproofs$183] realization `\(\Omega\)`:

`\[X(\Omega)=x_\Omega.\]`

For any real sequence `\((x_n)_{n\in\mathbb N}\)` [tending to plus infinity][bookofproofs$1345], `\(\lim_{n\to\infty} x_n=+\infty\)`, there exists an index `\(N_\Omega\in\mathbb N\)` such that 
`\[x_\Omega < x_n\quad\quad\text{for all }n \ge N_\Omega.\]`

It follows from `\((i)\)` and the [probability of the certain event][bookofproofs$871] that

`\[1=p(X\le x_\Omega)\le p(X\le x_n)\quad\quad\text{for all }n \ge N_\Omega.\]`

Because of the [axiom telling us that the probability is the certain event][bookofproofs$871] equals `\(1\)`, we get 

`\[1=p(X\le x_\Omega)\le p(X\le x_n)=1\quad\quad\text{for all }n \ge N_\Omega.\]`

or 

 `\[\lim_{x\to+\infty} p(X\le x)=1.\]`
