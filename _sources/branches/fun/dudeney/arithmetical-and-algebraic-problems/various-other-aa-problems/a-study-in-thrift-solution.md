layout: solution
categories: branches,fun,dudeney,arithmetical-and-algebraic-problems,various-other-aa-problems
nodeid: bookofproofs$7519
orderid: 0
parentid: bookofproofs$7052
title: 
description: SOLUTION OF A STUDY IN THRIFT &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$6929
keywords: study,thrift solution
contributors: @H-Dudeney,bookofproofs

---


---

Mrs. Sandy McAllister will have to save a tremendous sum out of her housekeeping allowance if she is to win that sixth present that her canny husband promised her. And the allowance must be a very liberal one if it is to admit of such savings. The problem required that we should find five numbers higher than `$36$` the units of which may be displayed so as to form a square, a triangle, two triangles, and three triangles, using the complete number in every one of the four cases.

Every triangular number is such that if we multiply it by `$8$` and add `$1$` the result is an odd square number. For example, multiply `$1, 3, 6, 10, 15$` respectively by `$8$` and add `$1,$` and we get `$9, 25, 49, 81, 121,$` which are the squares of the odd numbers `$3, 5, 7, 9, 11.$` Therefore, in every case where `$8x^2 + 1 =$` a [square number][bookofproofs$2326], `$x^2$` is also a triangular. This point is dealt with in our puzzle, "The Battle of Hastings." I will now merely show again how, when the first solution is found, the others may be discovered without any difficulty. First of all, here are the figures:—
`$$\begin{array}{lrr}
8	\times&	1^2	+ 1 =&	3^2\\
8	\times&	6^2	+ 1 =&	17^2\\
8	\times&	35^2	+ 1 =&	99^2\\
8	\times&	204^2	+ 1 =&	577^2\\
8	\times&	1189^2	+ 1 =&	3363^2\\
8	\times&	6930^2	+ 1 =&	19601^2\\
8	\times&	40391^2	+ 1 =&	114243^2
\end{array}$$`

The successive pairs of numbers are found in this way:—
`$$\begin{array}{rrrr}
(1 \times 3) + (3 \times 1)	=&	6& (8 \times 1) + (3 \times 3)	=&	17\\
(1 \times 17) + (3 \times 6)	=&	35&	 	(8 \times 6) + (3 \times 17)	=&	99\\
(1 \times 99) + (3 \times 35)	=&	204&	 	(8 \times 35) + (3 \times 99)	=&	577
\end{array}$$`

and so on. Look for the numbers in the table above, and the method will explain itself.

Thus we find that the numbers `$36,$` `$1225,$` `$41616,$` `$1413721,$` `$48024900,$` and `$1631432881$` will form squares with sides of `$6,$` `$35,$` `$204,$` `$1189,$` `$6930,$` and `$40391;$` and they will also form single triangles with sides of `$8,$` `$49,$` `$288,$` `$1681,$` `$9800,$` and `$57121.$` These numbers may be obtained from the last column in the first table above in this way: simply divide the numbers by `$2$` and reject the [remainder][bookofproofs$818] Thus the integral halves of `$17,$` `$99,$` and `$577$` are `$8,$` `$49,$` and `$288.$`

All the numbers we have found will form either two or three triangles at will. The following little diagram will show you graphically at a glance that every square number must necessarily be the sum of two triangulars, and that the side of one triangle will be the same as the side of the corresponding square, while the other will be just `$1$` less.

![a137](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/dudeney/a137.png?raw=true)

Thus a square may always be divided easily into two triangles, and the sum of two consecutive triangulars will always make a square. In numbers it is equally clear, for if we examine the first triangulars — `$1, 3, 6, 10, 15, 21, 28$` —, in turn,that by adding all the consecutive pairs in turn we get the series of square numbers — `$9, 16, 25, 36, 49,$` etc.

The method of forming three triangles from our numbers is equally direct, and not at all a matter of trial. But I must content myself with giving actual figures, and just stating that every triangular higher than `$6$` will form three triangulars. I give the sides of the triangles, and readers will know from my remarks when stating the puzzle how to find from these sides the number of counters or coins in each, and so check the results if they so wish.


Number | Side of Square | Side of Triangle  | Sides of Two Triangles  | Sides of Three Triangles
:------------- |:------------- |:------------- |:------------- |:-------------
 `$36$`| `$6$`|  `$8$`	| `$6 + 5$`| `$5 + 5 + 3$`
 `$1225$`|  `$35$`|  `$49$`| `$36 + 34$`| `$33 + 32 + 16$`
 `$41616$`|  `$204$`|  `$288$`| `$204 + 203$`| `$192 + 192 + 95$`
 `$1413721$`|  `$1189$`|  `$1681$`| `$1189 + 1188$`| `$1121 + 1120 + 560$`
 `$48024900$`|  `$6930$`|  `$9800$`| `$6930 + 6929$`| `$6533 + 6533 + 3267$`
 `$1631432881$`|  `$40391$`|  `$57121$`| `$40391 + 40390$`| `$38081 + 38080 + 19040$`

I should perhaps explain that the arrangements given in the last two columns are not the only ways of forming two and three triangles. There are others, but one set of figures will fully serve our purpose. We thus see that before Mrs. McAllister can claim her sixth £$5$ present she must save the respectable sum of £$1,631,432,881.$
