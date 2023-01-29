layout: proposition
categories: branches,geometry,euclidean-geometry,elements-euclid,book--2-geometric-algebra
nodeid: bookofproofs$1025
orderid: 1000
parentid: bookofproofs$1011
title: 2.11: Constructing the Golden Ratio of a Segment
description: 2.11: CONSTRUCTING THE GOLDEN RATIO OF A SEGMENT &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$626,bookofproofs$628
keywords: constructing,golden,golden ratio,ratio,segment
contributors: bookofproofs,@calahan,@casey

---


---

### (Proposition 11 from Book 2 of Euclid's “Elements”)

> To cut a given [straight line][bookofproofs$645] such that the [rectangle][bookofproofs$909] [contained][bookofproofs$1014] by the whole ([straight line][bookofproofs$645]), and one of the pieces (of the [straight line][bookofproofs$645]), is equal to the [square][bookofproofs$909] on the remaining piece.
* Let `$AB$` be the given [straight line][bookofproofs$645].
* So it is required to cut `$AB$` such that the [rectangle][bookofproofs$909] [contained][bookofproofs$1014] by the whole ([straight line][bookofproofs$645]), and one of the pieces (of the [straight line][bookofproofs$645]), is equal to the [square][bookofproofs$909] on the remaining piece.


![fig11e](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/euclid/Book02/fig11e.png?raw=true)


### Modern Formulation

It is possible to divide a given  segment (`\(\overline{AB}\)`) into two segments (at `\(H\)`) such that the rectangle contained by the whole line (`\(\overline{AB}=\overline{BD}\)`), and one segment (`\(\overline{BH}\)`) is equal in area to the square on the other segment (`\(\overline{AH}\)`). Algebraically, proposition 2.11 solves the equation `\(\overline{AB}\cdot \overline{BH}=\overline{AH}^{2}\)`. By setting `\(a=AB\)`, we want to find an `\(x\)` such that `\(a(a-x)=x^{2}\)`. Specifically,

`\[\begin{array}{ccl}
a(a-x)&=&x^{2}\\a^{2}-ax&=&x^{2}\\x^{2}+ax&=&a^{2}\\&\Longrightarrow&\\x&=&-\frac{a}{2}(1\pm\sqrt{5})\end{array}.\]`

Note that `\(\gamma=\frac{1+\sqrt{5}}{2}\)` is called the **Golden Ratio**.
