layout: proof
categories: branches,combinatorics
nodeid: bookofproofs$8611
orderid: 50
parentid: bookofproofs$994
title: 
description: PROOF OF RECURSIVE FORMULA FOR BINOMIAL COEFFICIENTS &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$977
keywords: recursive formula for binomial coefficients,binomial coefficient recursive formula,binomial coefficient recursive,binomial coefficient formula,recursive binomial coefficient,binomial coefficient recursion,recurrence relation binomial coefficients,binomial recursive formula,recursive binomial,recursive formula binomial coefficient,recursive formula,
contributors: bookofproofs

---


---

This proof is a simple recalculation of the formula, following the closed formula

`$$\begin{align}
\binom{n-1}{k-1}+\binom{n-1}{k}&=\frac{(n-1) !}{(n-1-k+1) !\cdot (k-1) !}+\frac{(n-1) !}{(n-1-k) !\cdot k !}\nonumber\\
&=\frac{(n-1) !}{(n-1) !\cdot (k-1) !}+\frac{(n-1) !}{(n-1-k) !\cdot k !}\nonumber\\
&=\frac{k(n-1) !}{(n-1) !\cdot k !}+\frac{(n-k)(n-1) !}{(n-k) !\cdot k !}\nonumber\\
&=\frac{k(n-1) ! + (n-k)(n-1) !}{(n-k) !\cdot k !}\nonumber\\
&=\frac{n !}{(n-k) !\cdot k !}\nonumber\\
&=\binom nk\nonumber\\
\end{align}$$`
