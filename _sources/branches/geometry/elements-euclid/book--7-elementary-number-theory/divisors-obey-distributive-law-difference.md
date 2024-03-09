layout: proposition
categories: branches,geometry,elements-euclid,book--7-elementary-number-theory
nodeid: bookofproofs$2337
orderid: 600
parentid: bookofproofs$1879
title: 7.07: Divisors Obey Distributive Law (Difference)
description: 7.07: DIVISORS OBEY DISTRIBUTIVE LAW DIFFERENCE &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$6419,bookofproofs$6908
keywords: difference,distributive,divisors,law,obey
contributors: @Fitzpatrick,bookofproofs

---


---

### (Proposition 7 from Book 7 of Euclid's “Elements”)

> If a number is that [part][bookofproofs$703] of a number that a ([part][bookofproofs$703]) taken away (is) of a ([part][bookofproofs$703]) taken away then the remainder will also be the same [part][bookofproofs$703] of the remainder that the whole (is) of the whole.

* For let a number `$AB$` be that [part][bookofproofs$703] of a number `$CD$` that a ([part][bookofproofs$703]) taken away `$AE$` (is) of a [part][bookofproofs$703] taken away `$CF$`.
* I say that the remainder `$EB$` is also the same [part][bookofproofs$703] of the remainder `$FD$` that the whole `$AB$` (is) of the whole `$CD$`.


![fig07e](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/euclid/Book07/fig07e.png?raw=true)


### Modern Formulation

See [divisibility law no. 6][bookofproofs$508].
### Notes

This proposition states 
`$$\begin{array}{rcl}
\underbrace{n\cdot (AE+EB)}_{n\cdot AB}=\underbrace{n\cdot AB}_{CD}&=&\underbrace{n\cdot AE}_{CF}+\underbrace{n\cdot EB}_{FD}\\
&\Downarrow&\\
n\cdot EB&=&\underbrace{n\cdot (AB-AE)}_{=FD}.
\end{array}$$`
In particular, 
`$$n\mid (CF+FD)\wedge n\mid CF\Rightarrow n\mid FD.$$`
