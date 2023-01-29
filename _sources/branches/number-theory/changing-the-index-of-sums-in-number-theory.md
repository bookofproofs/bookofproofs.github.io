layout: explanation
categories: branches,number-theory
nodeid: bookofproofs$8146
orderid: 100
parentid: bookofproofs$8144
title: Changing the Index Of Sums in Number Theory
description: CHANGING THE INDEX OF SUMS IN NUMBER THEORY &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$1591
keywords: changing,index,number,sums,theory
contributors: bookofproofs


---


---

Please note that in the "proof of the above lemma":https://www.bookofproofs.org/branches/moebius-and-floor-functions-combined/proof/ we also changed the outer summation index `$n$` by the inner summation `$d$` and got rid of one sum. This is a very common technique in number theory and it is worth an explanation. The reader is invited to verify, what exactly happens in the proof using this technique in the following example.

Imagine, we write down all summands for each `$n$` by rows and for each `$d$` by columns, then the first sum will go line by line and the second column by column, but we will be still adding up the same summands. For instance, if `$x=12,$` then the first sum, `$1=\sum_{n=1}^{12}\sum_{d\mid n}\mu(d)$` goes row by row 

`$$\begin{array}{rccccccccccccc|r}
d&=&1&2&3&4&5&6&7&8&9&10&11&12&n\\
\hline\\
1&=&+1&&&&&&&&&&&&1\\
&&+1&-1&&&&&&&&&&&2\\
&&+1&&-1&&&&&&&&&&3\\
&&+1&-1&&+0&&&&&&&&&4\\
&&+1&&&&-1&&&&&&&&5\\
&&+1&-1&-1&&&+1&&&&&&&6\\
&&+1&&&&&&-1&&&&&&7\\
&&+1&-1&&+0&&&&+0&&&&&8\\
&&+1&&-1&&&&&&+0&&&&9\\
&&+1&-1&&&-1&&&&&+1&&&10\\
&&+1&&&&&&&&&&-1&&11\\
&&+1&-1&-1&+0&&+1&&&&&&+1&12\\
\end{array}$$`

In the second sum, `$1=\sum_{d=1}^{12}\left\lfloor \frac {12}d\right\rfloor\mu(d)$`, we add the same table column by column and get exactly `$\left\lfloor\frac{12}{1}\right\rfloor(+1)$` from the first column, `$\left\lfloor\frac{12}{2}\right\rfloor(-1)$` from the second, `$\left\lfloor\frac{12}{3}\right\rfloor(-1)$` from the third, `$\left\lfloor\frac{12}{4}\right\rfloor(0)$` from the forth, etc. Of course, both summation schemes sum up to the value `$1$` because of the special properties of the [Möbius function][bookofproofs$8116].