layout: definition
categories: branches,theoretical-computer-science, computability
nodeid: bookofproofs$1776
orderid: 50
parentid: bookofproofs$84
title: Computational Problem, Solution
description: COMPUTATIONAL PROBLEM - A FORMAL DEFINITION ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$8480
keywords: computational problem,problem,problems,decision problem,decision problems
contributors: bookofproofs

---


---

A **computational problem** (or just **problem**) `\(P\)` can be viewed as a triple `\[P:=(D, I, Q),\]` where `\(D\)` is a [set][bookofproofs$550], called the **problem domain**, `\(I\in D\)` is a particular **instance** of the problem, and `\(Q\)` is 
* a **question**, which can be asked about any one of the instances of `\(D\)`, 
* which is being asked about the particular instance `\(I\)`,
* and the answer of which belongs to a certain set `$A$` of answers types. 

A **solution** to `$P$` is a [partial function][bookofproofs$592] `$f:D\to A$`, `$$f(I)=\begin{cases}a&\text{if }\exists a\in A \text{ answering }Q\\\operatorname{undef.}&\text{else}\end{cases}$$`

If `$A$` equals the set of [truth values][bookofproofs$707] `$A=\mathbb B=\{\text{yes},\text{no}\},$` the problem is called a **decision problem**.
