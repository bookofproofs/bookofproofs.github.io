layout: solution
categories: branches,fun,dudeney,combination-and-group-problems
nodeid: bookofproofs$7786
orderid: 0
parentid: bookofproofs$7203
title: 
description: SOLUTION OF COUNTER CROSSES &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$6929
keywords: counter,crosses solution
contributors: @H-Dudeney,bookofproofs

---


---

Let us first deal with the Greek Cross. There are just eighteen forms in which the numbers may be paired for the two arms. Here they are:—

`$$\begin{array}{ccc}
12978&13968&	14958\\
34956&24957&	23967\\
23958&	13769&	14759\\
14967&	24758&	23768\\
12589&	23759&	13579\\
34567&	14768&	24568\\
14569&	23569&	14379\\
23578&	14578&	25368\\
15369&	24369&	23189\\
24378&	15378&	45167\\
24179&	25169&	34169\\
35168&	34178&	25178
\end{array}$$`

Of course, the number in the middle is common to both arms. The first pair is the one I gave as an example. I will suppose that we have written out all these crosses, always placing the first row of a pair in the upright and the second row in the horizontal arm. Now, if we leave the central figure fixed, there are `$24$` ways in which the numbers in the upright may be varied, for the four counters may be changed in `$1 \times 2 \times 3 \times 4 = 24$` ways. And as the four in the horizontal may also be changed in `$24$` ways for every arrangement on the other arm, we find that there are `$24 \times 24 = 576$` variations for every form; therefore, as there are `$18$` forms, we get `$18 \times 576 = 10,368$` ways. But this will include half the four reversals and half the four reflections that we barred, so we must divide this by `$4$` to obtain the correct answer to the Greek Cross, which is thus `$2,592$` different ways. The division is by `$4$` and not by `$8,$` because we provided against half the reversals and reflections by always reserving one number for the upright and the other for the horizontal.

In the case of the Latin Cross, it is obvious that we have to deal with the same `$18$` forms of pairing. The total number of different ways, in this case, is the full number, `$18 \times 576.$` Owing to the fact that the upper and lower arms are unequal in length, permutations will repeat by reflection, but not by reversal, for we cannot reverse. Therefore this fact only entails division by `$2.$` But in every pair we may exchange the figures in the upright with those in the horizontal (which we could not do in the case of the Greek Cross, as the arms are there all alike); consequently, we must multiply by `$2.$` This multiplication by `$2$` and division by `$2$` cancel one another. Hence `$10,368$` is here the correct answer.
