layout: chapter
categories: branches,algebra
nodeid: bookofproofs$138
orderid: 100
parentid: bookofproofs$121
title: Linear Equations and Systems of Linear Equations (SLEs)
description: LINEAR EQUATIONS AND SYSTEMS OF LINEAR EQUATIONS SLES &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$7937
keywords: equations,linear,linear equations,,sles,systems,systems of linear equations
contributors: bookofproofs

---


---

*Linear equations,* like `${3x} -2 = 13,$` are the very first type of equations a schoolchild meets. This equation is called [linear" since its graph is a "straight line][bookofproofs$645] To solve it, one treats `$x$` as an unknown and applies usual rules of [arithmetics][bookofproofs$195] to `$x,$` as if it was a number. By applying these rules, you can transform the equation into a much simpler one, finally finding the **solution** - the number `$x$` which satisfies the equation[^1]:
`$$\begin{array}{rclll}
{3x} -2&=&13&&|+2\\
{3x}&=&15&&|\div 3\\
x&=&5
\end{array}$$`

*Systems of linear equations* (SLEs) contain more than one linear equation. SLEs are well-studied mathematical objects and "simple" in the sense that they can be solved by applying the same rules of arithmetics needed to solve a single linear equation. A solution to an SLE are unknowns satisfying all linear equations at once. 

### Example

A word problem which can be solved using an SLE is known since antiquity:

> "There are rabbits and chickens in a cage. The number of heads is `$4$`, the number of legs is `$10.$` How many rabbits and chickens are in the cage?"

This word problem can be solved as follows: Let `$r$` and `$c$` denote the numbers of rabbits and chickens, respectively. Obviously, these unknowns satisfy the following linear equations simultaneously:

`$$\begin{array}{rcl}
r + c&=&4\\
4r + 2c&=&10\\
\end{array}\quad ( * )$$`

Using the first equation, we can express the number of chickens as `$c=4-r.$` Substituting `$c$` by `$4-r$` in the second equation gives us

`$$\begin{array}{rclll}
4r + 2(4-r)&=&10&&\\
4r + 8-2r&=&10&&|-8\\
2r&=&2&&|\div 2\\
r&=&1
\end{array}$$`

Now, we know that there is only one rabbit in the cage. With this result, we can solve the first equation:

`$$\begin{array}{rclll}
1 + c&=&4&&|-1\\
c&=&3
\end{array}$$`

### Real practical problems - SLEs with many unknowns

SLEs have a broad field of practical applications, including the economy, mechanics, electronics, geology, to mention just a few. Real practical problems from these fields lead to SLEs with many, often thousands, millions or even billions of unknowns. In comparison, the above SLE has only two unknowns - `$c$` and `$r.$` If an SLE has many equations in many unknowns, it is conceptually simpler to think of them as one equation in one unknown. This sounds impossible, but it is perfectly possible if we introduce more complicated mathematical objects - called [matrices][bookofproofs$1048] and [vectors][bookofproofs$560] For instance, the SLE given in `$( * )$` can be written as a single equation 

`$$ Ax=b,\quad ( * * )$$`

with the matrix `$$A=\pmatrix{1&1\\4&2}$$`
and the vectors `$$x=\pmatrix{r\\c}\quad\text{and}\quad b=\pmatrix{4\\10},$$`
in which the vector `$x$` is the unknown vector satisfying the equation `$( * * ).$` 

### What you will learn in this chapter of <strong><span style='color:orange'>Bookof</span><span style='color:lightblue'>Proofs</span></strong>?

In the following, we will 

* establish the theoretical foundations to solve SLEs with an arbitrary number of unknowns 
* learn about the conditions for the existence and uniqueness of solutions to SLEs 
* introduce (computer) algorithms to solve SLEs with an arbitrary number of unknowns
* discuss the performance of these algorithms and ways to improve them


[^1]: The bar "|" to the right of each step denotes that we perform the same arithmetic operation on both sides of the equation, e.g. adding `$2$` or dividing by `$3.$`
