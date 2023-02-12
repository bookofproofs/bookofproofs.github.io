layout: solution
categories: branches,fun,dudeney,puzzle-games
nodeid: bookofproofs$7746
orderid: 0
parentid: bookofproofs$7674
title: 
description: SOLUTION OF A MATCH MYSTERY &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$6929
keywords: match,mystery solution
contributors: @H-Dudeney,bookofproofs

---


---

If you form the three heaps (and are therefore the second to draw), any one of the following thirteen groupings will give you a win if you play correctly: 
* `$15,$` `$14,$` `$1;$` 
* `$15,$` `$13,$` `$2;$` 
* `$15,$` `$12,$` `$3;$` 
* `$15,$` `$11,$` `$4;$` 
* `$15,$` `$10,$` `$5;$` 
* `$15,$` `$9,$` `$6;$` 
* `$15,$` `$8,$` `$7;$` 
* `$14,$` `$13,$` `$3;$` 
* `$14,$` `$11,$` `$5;$` 
* `$14,$` `$9,$` `$7;$` 
* `$13,$` `$11,$` `$6;$` 
* `$13,$` `$10,$` `$7;$` 
* `$12,$` `$11,$` `$7.$`

The beautiful general solution to this problem is as follows. Express the number in every heap in powers of `$2,$` avoiding repetitions and remembering that `$2^0 = 1.$` Then if you so leave the matches to your opponent that there is an even number of every power, you can win. And if at the start you leave the powers even, you can always continue to do so throughout the game. Take, as an example, the last grouping given above — `$12, 11, 7.$` Expressed in powers of `$2$` we have—
`$$\begin{array}{rccccc}
12&=&8&4&-&-\\
11&=&8&-&2&1\\
7&=&-&4&2&1\\
\hline
&&2&2&2&2\\
\end{array}$$`

As there are thus two of every power, you must win. Say your opponent takes `$7$` from the `$12$` heap. He then leaves—
`$$\begin{array}{rccccc}
5&=&-&4&-&1\\
11&=&8&-&2&1\\
7&=&-&4&2&1\\
\hline
&&1&2&2&3
\end{array}$$`

Here the powers are not all even in number, but by taking `$9$` from the `$11$` heap you immediately restore your winning position, thus—
`$$\begin{array}{rccccc}
5&=&-&4&-&1\\
2&=&-&-&2&-\\
7&=&-&4&2&1\\
\hline
&&-&2&2&2
\end{array}$$`

And so on, to the end. This solution is quite general and applies to any number of matches and any number of heaps. A correspondent informs me that this puzzle game was first propounded by Mr. W.M.F. Mellor, but when or where it was published I have not been able to ascertain.
