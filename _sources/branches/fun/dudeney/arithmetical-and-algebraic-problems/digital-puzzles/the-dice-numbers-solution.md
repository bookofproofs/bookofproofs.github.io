layout: solution
categories: branches,fun,dudeney,arithmetical-and-algebraic-problems,digital-puzzles
nodeid: bookofproofs$7478
orderid: 0
parentid: bookofproofs$7010
title: 
description: SOLUTION OF THE DICE NUMBERS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$6929
keywords: dice,numbers solution
contributors: @H-Dudeney,bookofproofs

---


---

The sum of all the numbers that can be formed with any given set of four different figures is always `$6,666$` multiplied by the sum of the four figures. Thus, `$1, 2, 3, 4 $` add up `$10,$` and ten times `$6,666$` is `$66,660.$` Now, there are thirty-five different ways of selecting four figures from the seven on the dice — remembering the `$6$` and `$9$` trick. The figures of all these thirty-five groups add up to `$600.$` Therefore `$6,666$` multiplied by `$600$` gives us `$3,999,600$` as the correct answer.

Let us discard the dice and deal with the problem generally, using the nine digits, but excluding naught. Now, if you were given simply the sum of the digits — that is, if the condition were that you could use any four figures so long as they summed to a given amount — then we have to remember that several combinations of four digits will, in many cases, make the same sum.
`$$\begin{array}{ccccccccccc}
10&11&12&13&14&15&16&17&18&19&20\\
1&1&2&3&5&6&8&9&11&11&12\\
\hline
21&22&23&24&25&26&27&28&29&30\\
11&11&9&8&6&5&3&2&1&1
\end{array}$$`

Here the top row of numbers gives all the possible sums of four different figures, and the bottom row the number of different ways in which each sum may be made. For example, `$13$` may be made in three ways: `$1237, 1246,$` and `$1345.$` It will be found that the numbers in the bottom row add up to `$126,$` which is the number of combinations of nine figures taken four at a time. From this table, we may at once calculate the answer to such a question as this: What is the sum of all the numbers composed of our different digits (naught excluded) that add up to `$14$`? Multiply `$14$` by the number beneath t in the table, `$5,$` and multiply the result by `$6,666,$` and you will have the answer. It follows that to know the sum of all the numbers composed of four different digits, if you multiply all the pairs in the two rows and then add the results together, you will get `$2,520,$` which, multiplied by `$6,666,$` gives the answer `$16,798,320.$`

The following general solution for any number of digits will doubtless interest readers. The solutions uses [factorials][bookofproofs$1005] Let `$n$` represent the number of digits, then `$5 (10^n - 1) ) 8!$` divided by `$(9 - n)!$` equals the required sum. Note that `$0!$` equals `$1.$` This may be reduced to the following practical rule: Multiply together `$4 \times 7 \times 6 \times 5\ldots$`  to `$(n - 1)$` factors; now add `$(n + 1)$` ciphers to the right, and from this result subtract the same set of figures with a single cipher to the right. Thus for `$n = 4$` (as in the case last mentioned), `$4 \times 7 \times 6 = 168.$` Therefore `$16,800,000$` less `$1,680$` gives us `$16,798,320$` in another way.
