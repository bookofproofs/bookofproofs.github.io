layout: solution
categories: branches,fun,dudeney,arithmetical-and-algebraic-problems,digital-puzzles
nodeid: bookofproofs$7467
orderid: 0
parentid: bookofproofs$6999
title: 
description: SOLUTION OF THE CAB NUMBERS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$6929
keywords: cab,numbers solution
contributors: @H-Dudeney,bookofproofs

---


---

The highest product is, I think, obtained by multiplying `$8,745,231$` by `$96$` — namely, `$839,542,176.$`

Dealing here with the problem generally, I have shown in the last puzzle that with three digits there are only two possible solutions and with four digits only six different solutions.

These cases have all been given. With five digits there are just twenty-two solutions, as follows: —


`$$\begin{array}{rcrcr}
3&\times&4128&=&12384\\
3&\times&4281&=&12843\\
3&\times	& 7125	&=&21375\\
3&\times	& 7251	&=&21753\\
2541&\times	& 6	&=&15246\\
651&\times	& 24	&=&15624\\
678	&\times	& 42	&=&28476\\
246&\times	& 51	&=&12546\\
57&\times	& 834	&=&47538\\
75&\times	& 231	&=&17325\\
624&\times	& 78	&=&48672\\
435&\times	& 87	&=&37845\\
\hline
9&\times	& 7461	&=&67149\\
72&\times	& 936	&=&67392\\
\hline
2&\times	& 8714	&=&17428\\
2&\times	& 8741		&=&17482\\
65&\times	& 281	&=&18265\\
65&\times	& 983	&=&63985\\
\hline
4973&\times	& 8	&=&39784\\
6521&\times	& 8	&=&52168\\
14&\times	& 926	&=&12964\\
86	&\times	& 251	&=&21586\\
\end{array}$$`

Now, if we took every possible combination and tested it by multiplication, we should need to make no fewer than `$30,240$` trials, or, if we at once rejected the number `$1$` as a multiplier, `$28,560$` trials — a task that I think most people would be inclined to shirk. But let us consider whether there be no shorter way of getting at the results required. I have already explained that if you add together the digits of any number and then, as often as necessary, add the digits of the result, you must ultimately get a number composed of one figure. This last number I call the "digital root." It is necessary in every solution of our problem that the root of the sum of the digital roots of our multipliers shall be the same as the root of their product. There are only four ways in which this can happen: when the digital roots of the multipliers are `$3$` and `$6,$` or `$9$` and `$9,$` or `$2$` and `$2,$` or `$5$` and `$8.$` I have divided the twenty-two answers above into these four classes. It is thus evident that the digital root of any product in the first two classes must be `$9,$` and in the second two classes 4.

Owing to the fact that no number of five figures can have a digital sum less than `$15$` or more than `$35,$` we find that the figures of our product must sum to either `$18$` or `$27$` to produce the root `$9,$` and to either `$22$` or `$31$` to produce the root `$4.$` There are `$3$` ways of selecting five different figures that add up to `$18,$` there are `$11$` ways of selecting five figures that add up to `$27,$` there are `$9$` ways of selecting five figures that add up to `$22,$` and `$5$` ways of selecting five figures that add up to `$31.$` There are, therefore, 28 different groups, and no more, from any one of which a product may be formed.

We next write out in a column these `$28$` sets of five figures and proceed to tabulate the possible factors, or multipliers, into which they may be split. Roughly speaking, there would now appear to be about `$2,000$` possible cases to be tried, instead of the `$30,240$` mentioned above; but the process of elimination now begins, and if the reader has a quick eye and a clear head he can rapidly dispose of the large bulk of these cases, and there will be comparatively few test multiplications necessary. It would take far too much space to explain my own method in detail, but I will take the first set of figures in my table and show how easy it is done by the aid of little tricks and dodges that should occur to everybody as he goes along.

My first product group of five figures is `$84,321.$` Here, as we have seen, the root of each factor must be `$3$` or a multiple of `$3.$` As there is no `$6$` or `$9,$` the only single multiplier is `$3.$` Now, the remaining four figures can be arranged in `$24$` different ways, but there is no need to make `$24$` multiplications. We see at a glance that, in order to get a five-figure product, either the `$8$` or the `$4$` must be the first figure to the left. But unless the `$2$` is preceded on the right by the `$8,$` it will produce when multiplied either a `$6$` or a `$7,$` which must not occur. We are, therefore, reduced at once to the two cases, `$3 \times 4,128$` and `$3 \times 4,281,$` both of which give correct solutions. Suppose next that we are trying the two-figure factor, `$21.$` Here we see that if the number to be multiplied is under `$500$` the product will either have only four figures or begin with `$10.$` Therefore we have only to examine the cases `$21 \times 843$` and `$21 \times 834.$` But we know that the first figure will be repeated and that the second figure will be twice the first figure added to the second. Consequently, as twice `$3$` added to `$4$` produces a naught in our product, the first case is at once rejected. It only remains to try the remaining case by multiplication, when we find it does not give a correct answer. If we are next trying the factor `$12,$` we see at the start that neither the `$8$` nor the `$3$` can be in the units place, because they would produce a `$6,$` and so on. A sharp eye and an alert judgment will enable us thus to run through our table in a much shorter time than would be expected. The process took me a little more than three hours.

I have not attempted to enumerate the solutions in the cases of six, seven, eight, and nine digits, but I have recorded nearly fifty examples with nine digits alone.
