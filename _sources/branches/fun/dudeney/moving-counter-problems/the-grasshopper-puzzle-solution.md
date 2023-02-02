layout: solution
categories: branches,fun,dudeney,moving-counter-problems
nodeid: bookofproofs$7598
orderid: 0
parentid: bookofproofs$7139
title: 
description: SOLUTION OF THE GRASSHOPPER PUZZLE &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$6929
keywords: counter,moving,problems,solution,grasshopper puzzle,solution
contributors: bookofproofs


---


---

Move the counters in the following order. The moves in brackets are to be made four times in succession. `$12,$` `$1,$` `$3,$` `$2,$` `$12,$` `$11,$` `$1,$` `$3,$` `$2$` `$(5,$` `$7,$` `$9,$` `$10,$` `$8,$` `$6,$` `$4),$` `$3,$` `$2,$` `$12,$` `$11,$` `$2,$` `$1, 2.$` The grasshoppers will then be reversed in forty-four moves.

The general solution to this problem is very difficult. Of course, it can always be solved by the method given in the solution of the last puzzle, if we have no desire to use the fewest possible moves. But to employ a full economy of moves we have two main points to consider. There are always what I call a lower movement ($L$) and an upper movement ($U$). `$L$` consists in exchanging certain of the highest numbers, such as `$12,$` `$11,$` `$10$` in our "Grasshopper Puzzle" with certain of the lower numbers, `$1,$` `$2,$` `$3;$` the former moving in a clockwise direction, the latter in a non-clockwise direction. `$U$` consists in reversing the intermediate counters. In the above solution for `$12,$` it will be seen that `$12,$` `$11,$` and `$1,$` `$2,$` `$3$` are engaged in the `$L$` movement, and `$4,$` `$5,$` `$6,$` `$7,$` `$8,$` `$9,$` `$10$` in the `$U$` movement. The `$L$` movement needs `$16$` moves and `$U$` `$28,$` making together `$44.$` We might also involve `$10$` in the `$L$` movement, which would result in `$L$` `$23,$` `$U$` `$21,$` making also together `$44$` moves. These I call the first and second methods. But any other scheme will entail an increase of moves. You always get these two methods (of an equal economy) for odd or even counters, but the point is to determine just how many to involve in `$L$` and how many in `$U.$` Here is the solution in table form. But first note, in giving values to n, that `$2,$` `$3,$` and `$4$` counters are special cases, requiring respectively `$3,$` `$3,$` and `$6$` moves, and that `$5$` and `$6$` counters do not give a minimum solution by the second method — only by the first.


### FIRST METHOD

 Total No. of Counters| `$L$` Movement No. of Counters| `$L$` Movement No. of Moves| `$U$` Movement No. of Counters| `$U$` Movement No. of Moves| Total No. of Moves
:---- | :---- | :---- |:---- |:---- |:---- |
 `$4n$`| `$n - 1$` and `$n$`| `$2(n\;- 1)^2 + 5n\;- 7$`| `$2n + 1$`| `$2n^2 + 3n + 1$`| `$4(n^2 + n\;- 1)$`
 `$4n\;- 2$`| `$n - 1$` and `$n$`| `$2(n\;- 1)^2 + 5n - 7$`| `$2n - 1$`| `$2(n\;- 1)^2 + 3n\;- 2$`| `$4n^2\;- 5$`
 `$4n + 1$`| `$n$` and `$n + 1$`| `$2n^2 + 5n\;- 2$`| `$2n$`| `$2n^2 + 3n\;- 4$`| `$2(2n^2 + 4n\;- 3)$`
 `$4n\;- 1$`| `$n \;- 1$` and `$n$`| `$2(n\;- 1)^2 + 5n\;- 7$`| `$2n$`| `$2n^2 + 3n\;- 4$`| `$4n^2 + 4n\;- 9$`


### SECOND METHOD
 Total No. of Counters| `$L$` Movement No. of Counters| `$L$` Movement No. of Moves| `$U$` Movement No. of Counters| `$U$` Movement No. of Moves| Total No. of Moves
:---- | :---- | :---- |:---- |:---- |:---- |
 `$4n$`| `$n$` and `$n$`| `$2n^2 + 3n\;- 4$`| `$2n$`| `$2(n - 1)^2 + 5n\;- 2$`| `$4(n^2 + n\;- 1)$`
 `$4n\;- 2$`| `$n\;- 1$` and `$n - 1$`| `$2(n - 1)^2 + 3n\;- 7$`| `$2n$`| `$2(n\;- 1)^2 + 5n\;- 2$`| `$4n^2\;- 5$`
 `$4n + 1$`| `$n$` and `$n$`| `$2n^2 + 3n\;- 4$`| `$2n + 1$`| `$2n^2 + 5n\;- 2$`| `$2(2n^2 + 4n\;- 3)$`
 `$4n\;- 1$`| `$n$` and `$n$`| `$2n^2 + 3n\;- 4$`| `$2n - 1$`| `$2(n\;- 1)^2 + 5n\;- 7$`| `$4n^2 + 4n-9$`

More generally we may say that with m counters, where m is even and greater than `$4,$` we require `$(m^2 + 4m - 16)/4$` moves; and where `$m$` is odd and greater than `$3,$` `$(m^2 + 6m - 31)/4$` moves. I have thus shown the reader how to find the minimum number of moves for any case, and the character and direction of the moves. I will leave him to discover for himself how the actual order of moves is to be determined. This is a hard nut, and requires careful adjustment of the L and the U movements, so that they may be mutually accommodating.
