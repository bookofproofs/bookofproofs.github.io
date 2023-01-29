layout: chapter
categories: branches,fun,dudeney,combination-and-group-problems
nodeid: bookofproofs$7187
orderid: 6
parentid: bookofproofs$6930
title: Combination and Group Problems
description: COMBINATION AND GROUP PROBLEMS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$6929
keywords: combination,group,problems
contributors: bookofproofs
issues: malformed-tables

---


---

> "A combination and a form indeed."
Hamlet, iii. 4.

Various puzzles in this class might be termed problems in the "geometry of situation," but their solution really depends on the theory of combinations which, in its turn, is derived directly from the theory of permutations. It has seemed convenient to include here certain group puzzles and enumerations that might, perhaps, with equal reason have been placed elsewhere; but readers are again asked not to be too critical about the classification, which is very difficult and arbitrary. As I have included my problem of "The Round Table" (No. 273), perhaps a few remarks on another well-known problem of the same class, known by the French as La Problême des Ménages, may be interesting. If n married ladies are seated at a round table in any determined order, in how many different ways may their n husbands be placed so that every man is between two ladies but never next to his own wife?

This difficult problem was first solved by Laisant, and the method shown in the following table is due to Moreau:—



Numb. of married couples | Auxiliary calculation | Result
:------------- |:------------- |:-------------
 4| 0| 2
 5| 3| 13
 6| 13| 80
 7| 83| 579
 8| 592| 4738
 9| 4821| 43387
 10| 43979| 439792

The first column shows the number of married couples. The numbers in the second column are obtained in this way: `$$5 \times 3 + 0\; - 2 = 13$$` `$$6 \times 13 + 3 + 2 = 83$$` `$$7 \times 83 + 13\; - 2 = 592$$` `$$8 \times 592 + 83 + 2 = 4821$$` and so on. Find all the numbers, except `$2,$` in the table, and the method will be evident. It will be noted that the `$2$` is subtracted when the first number (the number of couples) is [odd][bookofproofs$2318], and added when that number is [even][bookofproofs$2317] The numbers in the third column are obtained thus: `$$13 - 0 = 13$$` `$$83 - 3 = 80$$` `$$592 - 13 = 579$$` `$$4821 - 83 = 4738$$` and so on. The numbers in this last column give the required solutions. Thus, four husbands may be seated in two ways, five husbands may be placed in thirteen ways, and six husbands in eighty ways.

The following method, by Lucas, will show the remarkable way in which chessboard analysis may be applied to the solution of a circular problem of this kind. Divide a square into thirty-six cells, six by six, and strike out all the cells in the long diagonal from the bottom left-hand corner to the top right-hand corner, also the five cells in the diagonal next above it and the cell in the bottom right-hand corner. The answer for six couples will be the same as the number of ways in which you can place six rooks (not using the canceled cells) so that no rook shall ever attack another rook. It will be found that the six rooks may be placed in eighty different ways, which agrees with the above table.
