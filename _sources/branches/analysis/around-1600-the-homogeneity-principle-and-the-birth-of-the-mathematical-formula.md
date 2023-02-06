layout: chapter
categories: branches,analysis
nodeid: bookofproofs$8286
orderid: 100
parentid: bookofproofs$8284
title: Around 1600 - The homogeneity principle and the birth of the mathematical formula
description: AROUND 1600 - THE HOMOGENEITY PRINCIPLE AND THE BIRTH OF THE MATHEMATICAL FORMULA &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$8285
keywords: homogeneity principle, mathematical formula, who invented the mathematical formula
contributors: bookofproofs


---


---

Until about 1600, mathematics had to get along without mathematical formulae. For almost two thousand years, only geometrical objects like [straight lines][bookofproofs$645], [circles][bookofproofs$690], and [rectilinear figures][bookofproofs$687] were perceived as real mathematical objects. The purpose of calculations was to find solutions to concrete problems, e.g. finding the length of a [segment][bookofproofs$645], or the area of a [triangle][bookofproofs$6432]. Since [Euclid's Elements][bookofproofs$621], numbers did not have any meaning on their own but had only a meaning when interpreted as the lengths, the areas, or the volumes of geometric objects.
One of the big problems of this approach was the so-called _homogeneity principle_, which was commonly accepted by contemporary mathematicians. The homogeneity principle insisted on not mixing up numbers meaning lengths, areas, and volumes when adding and subtracting them. It would forbid even a simple modern formula like `$b\cdot a+a=1,$` since in this formula, the length `$a$` was mixed up with the area `$b\cdot a.$` What kind of weird geometrical object would this mean, a length added to an area? Therefore, such formulae were simply inconceivable. Moreover, the notation of formulae was not invented yet. Although [François Viète][bookofproofs$Viete] (1540 - 1613) tried to write down first algebraic formulations, in his notation, a formula like `$ba+2a=10$` would be written like this:

`$$b\text { times }a +  2\text{ times } a \text{ be equal }10.$$`

The first philosopher and mathematician who broke with the homogeneity principle and simplified the notation - in other words, the inventor of the "mathematical formula" - 
was [René Descartes][bookofproofs$Descartes] (1596 - 1650). Like contemporary mathematicians, he also considered numbers as valid only, if they could be interpreted as lengths, areas, and volumes. Therefore, he had to somehow bypass the homogeneity principle. Surprisingly, he found a solution in the [Prop 6.02][bookofproofs$1988] in the ancient [Elements][bookofproofs$621] of 
[Euclid](https://mathshistory.st-andrews.ac.uk/Biographies/Euclid/), also known as the **intercept theorem**, but nobody was able to discover this solution before Descartes. The intercept theorem states that in a geometrical arrangement like this,


![intercept1](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/intercept1.png?raw=true)


the following lengths are proportional:

`$$\frac{|\overline{AB}|}{|\overline{AD}|}=\frac{|\overline{AC}|}{|\overline{AE}|}.$$`

Descartes' solution to the homogeneity problem was this:
* Assume, the length `$|\overline{AB}|$` equals `$1$` and interpret the variables `$a,b,c,d$` as follows: `$a=|\overline{AB}|=1$`, `$b=|\overline{AD}|,$` `$c=|\overline{AC}|$` and `$d=|\overline{AE}|.$`
* Then, the intercept theorem tells us that `$$\frac 1b=\frac cd,$$` or `$1\cdot d=d=cb.$`

This meant that you may well add and compare _length_ magnitudes like `$d$` with _area_ magnitudes, like the [area of a rectangle][bookofproofs$1014] with the sides `$c$` and `$b.$` With this argument, Descartes rejected the homogeneity principle as an unnecessary burden to mathematics and paved the way to modern formulae. He also proposed to denote "knowns" in an equation with letters at the beginning of the Latin alphabet, like `$a,b,c$`, while the "unknowns" should be, according to Descartes, denoted by letters at the end of the Latin alphabet, like `$x,y,z.$` This convention is very often used even nowadays.
