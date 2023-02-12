layout: solution
categories: branches,fun,dudeney,combination-and-group-problems
nodeid: bookofproofs$7788
orderid: 0
parentid: bookofproofs$7205
title: 
description: SOLUTION OF THE BARRELS OF BALSAM &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$6929
keywords: balsam solution,barrels
contributors: @H-Dudeney,bookofproofs

---


---

This is quite easy to solve for any number of barrels — if you know how. This is the way to do it. There are five barrels in each row Multiply the numbers `$1,$` `$2,$` `$3,$` `$4,$` `$5$` together; and also multiply `$6,$` `$7,$` `$8,$` `$9,$` `$10$` together. Divide one result by the other, and we get the number of different combinations or selections of ten things taken five at a time. This is here `$252.$` Now, if we divide this by `$6$` ($1$ more than the number in the row) we get `$42,$` which is the correct answer to the puzzle, for there are `$42$` different ways of arranging the barrels. Try this method of solution in the case of six barrels, three in each row, and you will find the answer is `$5$` ways. If you check this by trial, you will discover the five arrangements with `$123,$` `$124,$` `$125,$` `$134,$` `$135$` respectively in the top row, and you will find no others.

The general solution to the problem is, in fact, this:
`$$\frac{\binom{2n}n}{n + 1}$$`
where `$2n$` equals the number of barrels. The symbol `$\binom{2n}n$`, of course, implies that we have to find how many combinations, or selections, we can make of `$2n$` things, taken `$n$` at a time.
