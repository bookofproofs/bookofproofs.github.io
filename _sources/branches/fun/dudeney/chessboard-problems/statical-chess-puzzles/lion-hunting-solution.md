layout: solution
categories: branches,fun,dudeney,chessboard-problems,statical-chess-puzzles
nodeid: bookofproofs$7827
orderid: 0
parentid: bookofproofs$7250
title: 
description: Solution of LION-HUNTING &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$6929
keywords: hunting solution,lion
contributors: bookofproofs

---


---

There are `$6,480$` ways of placing the man and the lion if there are no restrictions whatever except that they must be in different spots. This is obvious because the man may be placed on any one of the `$81$` spots, and in every case, there are `$80$` spots remaining for the lion; therefore `$81 \times 80 = 6,480.$` Now, if we deduct the number of ways in which the lion and the man may be placed on the same path, the result must be the number of ways in which they will not be on the same path. The number of ways in which they may be in line is found without much difficulty to be `$816.$` Consequently, `$6,480- 816 = 5,664,$` the required answer.

The general solution is this: `$$\frac{1}{3}n(n - 1) (3n^2 - n + 2).$$` This is, of course, equivalent to saying that if we call the number of squares on the side of a "chessboard" `$n,$` then the formula shows the number of ways in which two bishops may be placed without attacking one another. Only, in this case, we must divide by two, because the two bishops have no distinct individuality, and cannot produce a different solution by a mere exchange of places.
