layout: theorem
categories: branches,probability-theory-and-statistics
nodeid: bookofproofs$1838
orderid: 300
parentid: bookofproofs$236
title: Theorem of Large Numbers for Relative Frequencies
description: THEOREM OF LARGE NUMBERS FOR RELATIVE FREQUENCIES JAKOB BERNOULLI &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$856
keywords: bernoulli,frequencies,jakob,large,numbers,relative,theorem
contributors: bookofproofs

---


---

Let the [probability][bookofproofs$858] of an [event][bookofproofs$857] `\(A\)` occurring in a [Bernoulli experiment][bookofproofs$1812] be `\(P:=p(A)\)`. We define members of a [real sequence][bookofproofs$875] `\((F_n)_{n\in\mathbb N}\)` as follows:

* Let `\(F_1:=F_1(A)\)` be the [relative frequency][bookofproofs$1837] of `\(A\)` occurring, if we repeat the experiment `\(n=1\)` times.
* Let `\(F_2:=F_2(A)\)` be the [relative frequency][bookofproofs$1837] of `\(A\)` occurring, if we repeat the experiment `\(n=2\)` times.
* Let `\(F_3:=F_3(A)\)` be the [relative frequency][bookofproofs$1837] of `\(A\)` occurring, if we repeat the experiment `\(n=3\)` times.
* etc.

Then it is almost certain that the sequence members `\(F_n\)` will approximate the probability `\(P\)` with virtually any accuracy, if `\(n\)` is large enough. Formally, 

`\[\lim_{n\to\infty}p(|F_n(A)-P|\le \epsilon)=1\]`

for arbitrarily small (but fixed) [real number][bookofproofs$1105] `\(\epsilon > 0\)`. We can also say that the relative frequencies of an event in a Bernoulli experiment (if repeated a large number of times) approximate the probability of that event:

`\[F_n(A)\approx p(A).\]`
