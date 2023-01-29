layout: solution
categories: branches,fun,dudeney,moving-counter-problems
nodeid: bookofproofs$7597
orderid: 1
parentid: bookofproofs$7137
title: 
description: SOLUTION OF THE SIX FROGS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$6929
keywords: frogs solution,six
contributors: bookofproofs

---


---

Move the frogs in the following order: `$2,$` `$4,$` `$6,$` `$5,$` `$3,$` `$1$` (repeat these moves in the same order twice more), `$2,$` `$4, 6.$` This is a solution in twenty-one moves — the fewest possible.

If `$n,$` the number of frogs, be even, we require `$\frac{n^2+n}2$` moves, of which `$\frac{n^2-n}2$` will be leaps and `$n$` simple moves. If `$n$` be odd, we shall need `$\frac{n^2+3n}2-4$` moves, of which `$\frac{n^2-n}2$` will be leaps and `$2n-4$` simple moves.

In the even cases write, for the moves, all the even numbers in ascending order and the odd numbers in descending order. This series must be repeated `$\frac 12n$` times and followed by the even numbers in ascending order once only. Thus the solution for `$14$` frogs will be `$(2,$` `$4,$` `$6,$` `$8,$` `$10,$` `$12,$` `$14,$` `$13,$` `$11,$` `$9,$` `$7,$` `$5,$` `$3, 1)$` repeated `$7$` times and followed by `$2,$` `$4,$` `$6,$` `$8,$` `$10,$` `$12,$` `$14 = 105$` moves.

In the odd cases, write the even numbers in ascending order and the odd numbers in descending order, repeat this series `$\frac 12(n-1)$` times, follow with the even numbers in ascending order (omitting `$n-1$`), the odd numbers in descending order (omitting `$1$`), and conclude with all the numbers (odd and even) in their natural order (omitting `$1$` and `$n$`). Thus for `$11$` frogs: ($2,$ `$4,$` `$6,$` `$8,$` `$10,$` `$11,$` `$9,$` `$7,$` `$5,$` `$3,$` `$1$`) repeated `$5$` times, `$2,$` `$4,$` `$6,$` `$8,$` `$11,$` `$9,$` `$7,$` `$5,$` `$3,$` and `$2,$` `$3,$` `$4,$` `$5,$` `$6,$` `$7,$` `$8,$` `$9,$` `$10 = 73$` moves.

This complete general solution is published here for the first time.
