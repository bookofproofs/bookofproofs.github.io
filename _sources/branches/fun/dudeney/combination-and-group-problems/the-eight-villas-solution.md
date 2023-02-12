layout: solution
categories: branches,fun,dudeney,combination-and-group-problems
nodeid: bookofproofs$7785
orderid: 0
parentid: bookofproofs$7202
title: 
description: SOLUTION OF THE EIGHT VILLAS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$6929
keywords: eight,villas solution
contributors: @H-Dudeney,bookofproofs

---


---

There are several ways of solving the puzzle, but there is very little difference between them. The solver should, however, first of all bear in mind that in making his calculations he need only consider the four villas that stand at the corners, because the intermediate villas can never vary when the corners are known. One way is to place the numbers nought to `$9$` one at a time in the top left-hand corner, and then consider each case in turn.

![a276](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/dudeney/a276.png?raw=true)

Now, if we place `$9$` in the corner as shown in the Diagram A, two of the corners cannot be occupied, while the corner that is diagonally opposite may be filled by `$0,$` `$1,$` `$2,$` `$3,$` `$4,$` `$5,$` `$6,$` `$7,$` `$8,$` or `$9$` persons. We thus see that there are `$10$` solutions with a `$9$` in the corner. If, however, we substitute `$8,$` the two corners in the same row and column may contain `$0,$` `$0,$` or `$1,$` `$1,$` or `$0,$` `$1,$` or `$1,$` `$0.$` In the case of `$B,$` ten different selections may be made for the fourth corner; but in each of the cases `$C, D,$` and `$E,$` only nine selections are possible, because we cannot use the `$9.$` Therefore with `$8$` in the top left-hand corner there are `$10 + (3 \times 9) = 37$` different solutions. If we then try `$7$` in the corner, the result will be `$10 + 27 + 40,$` or `$77$` solutions. With `$6$` we get `$10 + 27 + 40 + 49 = 126;$` with `$5,$` `$10 + 27 + 40 + 49 + 54 = 180;$` with `$4,$` the same as with `$5, + 55 = 235$` ; with `$3,$` the same as with `$4, + 52 = 287;$` with `$2,$` the same as with `$3, + 45 = 332;$` with `$1,$` the same as with `$2, + 34 = 366,$` and with nought in the top left-hand corner the number of solutions will be found to be `$$10 + 27 + 40 + 49 + 54 + 55 + 52 + 45 + 34 + 19 = 385.$$` As there is no other number to be placed in the top left-hand corner, we have now only to add these totals together thus, `$$10 + 37 + 77 + 126 + 180 + 235 + 287 + 332 + 366 + 385 = 2,035.$$` We therefore find that the total number of ways in which tenants may occupy some or all of the eight villas so that there shall be always nine persons living along each side of the square is `$2,035.$` Of course, this method must obviously cover all the reversals and reflections, since each corner in turn is occupied by every number in all possible combinations with the other two corners that are in line with it.

Here is a general formula for solving the puzzle: `$$\frac{(n^2 + 3n + 2)(n^2 + 3n + 3)}6.$$` Whatever may be the stipulated number of residents along each of the sides (which number is represented by n), the total number of different arrangements may be thus ascertained. In our particular case the number of residents was nine. Therefore `$(81 + 27 + 2) \times (81 + 27 + 3)$` and the product, divided by `$6,$` gives `$2,035.$` If the number of residents had been `$0,$` `$1,$` `$2,$` `$3,$` `$4,$` `$5,$` `$6,$` `$7,$` or `$8,$` the total arrangements would be `$1,$` `$7,$` `$26,$` `$70,$` `$155,$` `$301,$` `$532,$` `$876,$` or `$1,365$` respectively.
