layout: proof
categories: branches,number-theory
nodeid: bookofproofs$3530
orderid: 50
parentid: bookofproofs$8181
title: 
description:  Proof of ALL SOLUTIONS GIVEN A SOLUTION OF AN LDE WITH TWO VARIABLES &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$1272
keywords: all,given,lde,solution,solutions,two,variables,proof
contributors: bookofproofs

---


---

### Number pairs `$x,y$` with the required form are solutions.

* Let `$x_0,y_0$` be a solution of the linear [Diophantine equation][bookofproofs$8158] (LDE) `$ax+by=c.$`
* Set `$x:=x_0+h\frac b{\gcd(a,b)}$` and `$y:=y_0-h\frac a{\gcd(a,b)}$` for any `$h\in\mathbb Z.$` 
* Then `$ax+by=ax_0+b_y=c.$`

### All pairs of numbers `$x,y$` being solutions have the required form.

* Assume, `$x,y$` is any solution of the above LDE. We will show that it has always the required form.
* By assumption, `$ax+by=c=ax_0+by_0.\label{eq:E18579}\tag{1}$`
* We can assume `$b\neq 0,$` otherwise we can exchange `$a$` and `$b.$` Furthermore, by the existence part, `$\pm h$` are allowed in the formulae `$x_0+h\frac b{\gcd(a,b)}$` and `$y_0-h\frac a{\gcd(a,b)}.$`  
* From `$(\ref{eq:E18579}),$` it follows `$$\begin{array}{rcl}(ax)(|b|)&\equiv&c(|b|)\\(ax_0)(|b|)&\equiv&c(|b|)\end{array}\label{eq:E18579a}\tag{2}.$$`
* With the [existence and number of solutions of an LDE with one variable][bookofproofs$8178], it follows that `$(\ref{eq:E18579a})$` has exactly one solution of the form `$$x\equiv x_0\mod \frac{|b|}{\gcd(a,b)},$$` where `$\gcd(a,b)$` is the [greatest common divisor][bookofproofs$1280] of `$a$` and `$b.$`
* Therefore, we can write `$x=x_0+h\frac bd$` for some "integer:https://www.bookofproofs.org/branches/definition-of-integers/ `$h\in\mathbb Z.$`
* It follows `$$\begin{array}{rcl}by&=&c-ax\\
&=&c-a\left(x_0+h\frac b{\gcd(a,b)}\right)\\
&=&(c-ax_0)-b\frac{ha}{{\gcd(a,b)}}\\
&=&by_0-b\frac{ha}{{\gcd(a,b)}}\\
&=&b(y_0-h\frac{a}{{\gcd(a,b)}}.
\end{array}$$`
* It follows that any solution has the claimed form.
