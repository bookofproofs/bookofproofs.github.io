layout: proof
categories: branches,probability-theory-and-statistics
nodeid: bookofproofs$976
orderid: 50
parentid: bookofproofs$975
title: 
description:  Proof of PROBABILITY OF LAPLACE EXPERIMENTS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$856
keywords: experiments,laplace,probability,proof
contributors: bookofproofs

---


---

According to the axiom [probability of certain event][bookofproofs$871] we have that 
`\[p(\Omega)=p(\{\omega_1,\ldots,\omega_n\})=1.\]`
By definition of [Laplace experiments][bookofproofs$973], all elementary events `\(\omega_i\)` are  [mutually exclusive][bookofproofs$859], we can  [add their probabilities][bookofproofs$873], resulting in 
`\[p(\Omega)=p(\{\omega_1\})+\ldots+p(\{\omega_n\})=1.\]`
Because we have a Laplace experiment by hypothesis, it follows that 
`\[p(\Omega)=p(\{\omega_1\})+\ldots+p(\{\omega_n\})=\underbrace{p + \ldots + p}_{n\text{ times}}=1,\]`
and therefore
`\[p(\omega_i)=\frac 1n~~~~~~~~~~~~(i=1,\ldots n).\]`

It follows for the [finite][bookofproofs$986] subset `\(A\subseteq\Omega\)` that we have to sum the probability `\(\frac 1n\)` the number of times, the event `\(\omega_i\)` belongs to the event `\(A\)`. Again, because all events are mutualy exclusive, we get 

`\[p(A)=\sum_{\omega_i\in A}\frac 1n=\frac{|A|}{|\Omega|}.\]`
