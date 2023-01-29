layout: solution
categories: branches,fun,dudeney,unicursal-and-route-problems
nodeid: bookofproofs$7636
orderid: 0
parentid: bookofproofs$7178
title: 
description: Solution of A BANK HOLIDAY PUZZLE &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$6929
keywords: bank,holiday,puzzle solution
contributors: bookofproofs

---


---

The simplest way is to write in the number of routes to all the towns in this manner. Put a `$1$` on all the towns in the top row and in the first column. Then the number of routes to any town will be the sum of the routes to the town immediately above and to the town immediately to the left. Thus the routes in the second row will be `$1,$` 2, `$3,$` 4, `$5,$` 6, etc., in the third row, `$1,$` `$3,$` `$6,$` `$10,$` `$15,$` `$21,$` etc.; and so on with the other rows. It will then be seen that the only town to which there are exactly `$1,365$` different routes is the twelfth town in the fifth row — the one immediately over the letter `$E.$` This town was, therefore, the cyclist's destination.

The general formula for the number of routes from one corner to the corner diagonally opposite on any such rectangular reticulated arrangement, under the conditions as to direction, is `$$\frac{(m + n) &#33;}{m &#33;n &#33;},$$` where m is the number of towns on one side, less one, and n the number on the other side, less one. Our solution involves the case where there are `$12$` towns by `$5.$` Therefore m = `$11$` and `$n = 4.$` Then the formula gives us the answer `$1,365$` as above.
