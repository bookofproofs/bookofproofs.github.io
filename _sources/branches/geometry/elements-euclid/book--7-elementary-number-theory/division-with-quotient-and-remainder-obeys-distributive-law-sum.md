layout: proposition
categories: branches,geometry,euclidean-geometry,elements-euclid,book--7-elementary-number-theory
nodeid: bookofproofs$2336
orderid: 500
parentid: bookofproofs$1879
title: 7.06: Division with Quotient and Remainder Obeys Distributive Law (Sum)
description: 7.06: DIVISION WITH QUOTIENT AND REMAINDER OBEYS DISTRIBUTIVE LAW SUM &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$6419,bookofproofs$6908
keywords: distributive,division,law,obeys,quotient,remainder,sum
contributors: bookofproofs,@fitzpatrick

---


---

### (Proposition 6 from Book 7 of Euclid's “Elements”)

> If a number is [parts][bookofproofs$2323] of a number, and another (number) is the same [parts][bookofproofs$2323] of another, then the sum (of the leading [numbers][bookofproofs$2315]) will also be the same [parts][bookofproofs$2323] of the sum (of the following [numbers][bookofproofs$2315]) that one (number) is of another.
* For let a number `$AB$` be [parts][bookofproofs$2323] of a number `$C$`, and another (number) `$DE$` (be) the same [parts][bookofproofs$2323] of another (number) `$F$` that `$AB$` (is) of `$C$`.
* I say that the sum `$AB$`, `$DE$` is also the same [parts][bookofproofs$2323] of the sum `$C$`, `$F$` that `$AB$` (is) of `$C$`.


![fig06e](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/euclid/Book07/fig06e.png?raw=true)


### Modern Formulation

See [divisibility law no. 9][bookofproofs$508].
### Notes

This proposition states (for integers `$0 < r_0 < AG$` and `$0 < r_1 < DH$`) 
`$$\begin{array}{rclclc}C&=&AB+r_0&=&n\cdot AG+r_0&\wedge\\
F&=&DE+r_1&=&n\cdot DH+r_1\\
&\Downarrow&\\
C+F&=&(AB+DE)+(r_0+r_1)&=&n(AG+DH)+(r_0+r_1)
\end{array}$$`

with `$0 < (r_0+r_1) < (AG+DH).$` In particular, 

`$$n\not\mid (C+F)\Rightarrow n\not\mid C\vee n\not\mid F.$$`
