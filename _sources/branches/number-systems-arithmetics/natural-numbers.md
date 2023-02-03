layout: part
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$103
orderid: 50
parentid: bookofproofs$195
title: Natural Numbers
description: NATURAL NUMBERS &#9733; bring your math skills to the graduate level &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: 
keywords: natural,numbers
contributors: bookofproofs

---


---

The natural numbers `\(0,~1,~2,~3,\ldots\)`, otherwise known as the _non-negative integers_[^1], are the numbers familiar even to young children. It is the natural numbers that we use for the very basic mathematical purpose of counting things (see [cardinal numbers][bookofproofs$185]). We also can use them to order things (see [ordinal numbers][bookofproofs$112]). 

From the formal point of view, natural numbers can be [constructed using sets][bookofproofs$718]. In particular, we can use the concept of the empty set `\(\emptyset\)` and call it `\(0\)`, then construct a set containing this empty set and call it `\(1\)`, then construct a set containing the empty set and also the previous set and call it `\(2\)`, etc.:

`\[\begin{array}{cclcl}0&:=&\emptyset&=&\emptyset\\1&:=&\left\{0\right\}&=&\left\{\emptyset\right\}\\2&:=&\left\{0,~1\right\}&=&\left\{\emptyset,~\left\{\emptyset\right\}\right\}\\3&:=&\left\{0,~1,~2\right\}&=&\left\{\emptyset,~\left\{\emptyset,~\left\{\emptyset\right\}\right\}\right\}\\\vdots&&\vdots&&\vdots\\\end{array}\]`

Another way to define natural numbers is to use a suitable axiomatic system. One of such axiomatic systems are the [Peano Axioms][bookofproofs$504].

[^1]: Please note: Another common way is to understand the set of natural numbers is as __positive integers__, excluding the number 0. In <strong><span style='color:orange'>BookOf</span><span style='color:lightblue'>Proofs</span></strong>, natural numbers are always including 0, by convention.
