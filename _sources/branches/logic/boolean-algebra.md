layout: definition
categories: branches,logic
nodeid: bookofproofs$7872
orderid: 700
parentid: bookofproofs$66
title: Boolean Algebra
description: BOOLEAN ALGEBRA &#9733; bring your math skills to the graduate level &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$641
keywords: algebra,boolean,boolean algebra,product,sum
contributors: bookofproofs


---
<a href="https://mathshistory.st-andrews.ac.uk/Biographies/Boole/">George Bool</a>, a poor shoemaker's son, never attended secondary school, college, or university. He was a gifted autodidact and at the age of 34, in 1849, he was appointed Professor of Mathematics at Queen's College, Cork, where he published his book entitled _An Investigation of the Laws of Thought_. In this book, he introduced a new type of algebra, later known as **Boolean Algebra**, which is a kind of ordinary numerical algebra studying the rules of equations involving variables such as `$a,b,x,y,...$`, in which the values of all variables are limited to `$0$` and `$1$`. The Boolean Algebra was dormant until 1939, when "Shannon":https://www.bookofproofs.org/history/claude-elwood-shannon/ discovered that it was appropriate language to describe switching circuits, laying the foundations for modern computers.

We will now define Boolean algebra formally and show how it can be used to study propositional logic.

---

Any [set][bookofproofs$550] `\((B,\sqcap,\sqcup,1,0)\)` with the operations
* **product** `$"\sqcap":B\times B\to B$`, `$(x,y)\to x\sqcap y$` for all `$x,y\in B$`,
* **sum** `$"\sqcup":B\times B\to B$`, `$(x,y)\to x\sqcup y$` for all `$x,y\in B$`,
* and the designated elements `$1,0\in B$` 

is called a **Boolean algebra** if and only if:


1. `$\sqcap$` and `$\sqcup$` are [associative][bookofproofs$668] in `\(B\)`, i.e. for all `\(x,y,z\in B\)` `$$\begin{array}{c}x\sqcap(y\sqcap z)=(x\sqcap y)\sqcap z,\\x\sqcup (y\sqcup z)=(x\sqcup y)\sqcup z,\end{array}$$`
1. `$\sqcap$` and `$\sqcup$` are [commutative][bookofproofs$672] in `\(B\)`,  i.e. for all `\(x,y \in B\)` `$$\begin{array}{c}x\sqcap y=y \sqcap x,\\x\sqcup y=y\sqcup x,\end{array}$$` 
1. "`\(\sqcap\)`" and "`\(\sqcup\)`" are [distributive][bookofproofs$682] over each other in `\(B\)`, i.e. for all `\(x,y,z\in B\)` `$$\begin{array}{c}x\sqcap(y\sqcup z)=(x\sqcap y)\sqcup (x\sqcap z),\\x\sqcup (y\sqcap z)=(x\sqcup y)\sqcap (x\sqcup z),\end{array}$$`
1. there is an element `$0\in B$` with `$0\sqcap x=0$` and `$x\sqcup 0=x$` for all `$x\in B$`; `$0$` is called the **smallest element** of `$B,$`
1. there is an element `$1\in B$` with `$1\sqcap x=x$` and `$x\sqcup 1=1$` for all `$x\in B$`; `$1$` is called the **greatest element** of `$B,$`
1. there is an element `$1\in B$` with `$1\sqcap x=x$` and `$x\sqcup 1=1$` for all `$x\in B$`; `$1$` is called the **greatest element** of `$B,$`
