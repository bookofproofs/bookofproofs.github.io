layout: proposition
categories: branches,geometry,elements-euclid,book--7-elementary-number-theory
nodeid: bookofproofs$2338
orderid: 700
parentid: bookofproofs$1879
title: 7.08: Division with Quotient and Remainder Obeys Distributivity Law (Difference)
description: 7.08: DIVISION WITH QUOTIENT AND REMAINDER OBEYS DISTRIBUTIVITY LAW DIFFERENCE &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$6419,bookofproofs$6908
keywords: difference,distributive,division,law,obeys,quotient,remainder
contributors: @Fitzpatrick,bookofproofs

---


---

### (Proposition 8 from Book 7 of Euclid's “Elements”)

> If a number is those [parts][bookofproofs$2323] of a number that a ([part][bookofproofs$703]) taken away (is) of a ([part][bookofproofs$703]) taken away then the remainder will also be the same [parts][bookofproofs$2323] of the remainder that the whole (is) of the whole.

* For let a number `$AB$` be those [parts][bookofproofs$2323] of a number `$CD$` that a ([part][bookofproofs$703]) taken away `$AE$` (is) of a ([part][bookofproofs$703]) taken away `$CF$`.
* I say that the remainder `$EB$` is also the same [parts][bookofproofs$2323] of the remainder `$FD$` that the whole `$AB$` (is) of the whole `$CD$`.


![fig08e](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/euclid/Book07/fig08e.png?raw=true)


### Modern Formulation

See [divisibility law no. 9][bookofproofs$508].
### Notes

This proposition states (for integers `$0 < r_1 < r_0 < AL$` and `$0 < m < n$`) 
`$$\begin{array}{rclclc}CD&=&AB+r_0&=&n\cdot AL+r_0&\wedge\\
CF&=&AE+r_1&=&m\cdot AL+r_1\\
&\Downarrow&\\
CD-CF&=&(AB-AE)+(r_0-r_1)&=&(n-m)AL+(r_0-r_1)
\end{array}$$`

with `$0 < (r_0-r_1) < AL.$` In particular, 

`$$AL\not\mid (CD-CF)\Rightarrow AL\not\mid CD\vee AL\not\mid CF.$$`
