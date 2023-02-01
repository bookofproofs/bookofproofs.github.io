layout: solution
categories: branches,fun,dudeney,arithmetical-and-algebraic-problems,various-other-aa-problems
nodeid: bookofproofs$7520
orderid: 0
parentid: bookofproofs$7053
title: 
description: SOLUTION OF THE ARTILLERYMAN'S DILEMMA &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$6929
keywords: artillerymans,dilemma solution
contributors: bookofproofs

---


---

We were required to find the smallest number of cannon balls that we could lay on the ground to form a perfect square, and could pile into a square pyramid. I will try to make the matter clear to the merest novice.
`$$\begin{array}{rrrrrrr}
1&2&3&4&5&6&7\\
1&3&6&10&15&21&28\\
1&4&10&20&35&56&84\\
1&5&14&30&55&91&140\\
\end{array}$$`

Here in the first row we place in regular order the natural numbers. Each number in the second row represents the sum of the numbers in the row above, from the beginning to the number just over it. Thus `$1,$` `$2,$` `$3,$` `$4,$` added together, make `$10.$` The third row is formed in exactly the same way as the second. In the fourth row, every number is formed by adding together the number just above it and the preceding number. Thus `$4$` and `$10$` make `$14,$` `$20$` and `$35$` make `$55.$` Now, all the numbers in the second row are triangular numbers, which means that these numbers of cannon balls may be laid out on the ground so as to form equilateral triangles. The numbers in the third row will all form our triangular pyramids, while the numbers in the fourth row will all form square pyramids.

Thus the very process of forming the above numbers shows us that every square pyramid is the sum of two triangular pyramids, one of which has the same number of balls in the side at the base, and the other one ball fewer. If we continue the above table to twenty-four places, we shall reach the number `$4,900$` in the fourth row. As this number is the square of `$70,$` we can lay out the balls in a square and can form a square pyramid with them. This manner of writing out the series until we come to a square number does not appeal to the mathematical mind, but it serves to show how the answer to the particular puzzle may be easily arrived at by anybody. As a matter of fact, I confess my failure to discover any number other than `$4,900$` that fulfills the conditions, nor have I found any rigid proof that this is the only answer. The problem is a difficult one, and the second answer, if it exists (which I do not believe), certainly runs into big figures.

For the benefit of more advanced mathematicians I will add that the general expression for square pyramid numbers is `$(2n^3 + 3n^2 + n)/6.$` For this expression to be also a square number (the special case of `$1$` excepted) it is necessary that `$n = p^2 - $`1$ = 6t^2,$ where `$2p^2 - 1 = q^2$` (the "Pell's Equation"). In the case of our solution above, `$n = 24, p = 5, t = 2, q = 7.$`
