layout: solution
categories: branches,fun,dudeney,arithmetical-and-algebraic-problems,various-other-aa-problems
nodeid: bookofproofs$7495
orderid: 0
parentid: bookofproofs$7028
title: 
description: SOLUTION OF THE TORN NUMBER &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$6929
keywords: number solution,torn
contributors: @H-Dudeney,bookofproofs

---


---

The other number that answers all the requirements of the puzzle is `$9,801.$` If we divide this in the middle into two numbers and add them together we get `$99,$` which, multiplied by itself, produces `$9,801.$` It is true that `$2,025$` may be treated in the same way, only this number is excluded by the condition which requires that no two figures should be alike.

The general solution is curious. Call the number of figures in each half of the torn label `$n.$` Then, if we add `$1$` to each of the exponents of the prime factors (other than `$3$`) of `$10^n - 1$` ($1$ being regarded as a factor with the constant exponent, `$1$`), their product will be the number of solutions. Thus, for a label of six figures, `$n = 3.$` The factors of `$10^n - 1$` are `$11 \times 371$` (not considering the `$33$`), and the product of `$2 \times 2= 4,$` the number of solutions. This always includes the special cases `$98 - 01,$` `$00 - 01,$` `$998 - 01,$` `$000 - 001,$` etc. The solutions are obtained as follows:— 
1. Factorize `$103$` - `$1$` in all possible ways, always keeping the powers of `$3$` together, thus, `$37 \times 27,$` `$999 \times 1.$` 
1. Then solve the equation `$37x = 27y + 1.$` Here `$x = 19$` and `$y = 26.$` 

Therefore, `$19 \times 37 = 703,$` the square of which gives one label, `$494,209.$` A complementary solution (through `$27y = 37x + 1$`) can at once be found by `$10^n - 703 = 297,$` the square of which gives `$088,209$` for second label. (These non-significant noughts to the left must be included, though they lead to peculiar cases like `$00238 - 04641 = 4879^2,$` where `$0238 - 4641$` would not work.) The special case `$999 \times 1$` we can write at once `$998,001,$` according to the law shown above, by adding nines on one half and noughts on the other, and its complementary will be `$1$` preceded by five noughts, or `$000001.$` Thus we get the squares of `$999$` and `$1.$` These are the four solutions.
