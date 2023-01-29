layout: proposition
categories: branches,analysis
nodeid: bookofproofs$6696
orderid: 50
parentid: bookofproofs$302
title: Continuous Real Functions on Closed Intervals Take Maximum and Minimum Values within these Intervals
description: CONTINUOUS REAL FUNCTIONS ON CLOSED INTERVALS TAKE MAXIMUM AND MINIMUM VALUES WITHIN THESE INTERVALS ★ master maths ✔ visit BookOfProofs!
references: bookofproofs$581
keywords: continuous functions,closed intervals,maximum,minimum
contributors: bookofproofs

---
The following proposition is an important result about how continuous functions behave on [closed real intervals][bookofproofs$1153]. It turns out that once a function is continuous, there is always a constant such that it cannot be exceeded by the function values, no matter which function we will take. This works only for closed intervals.

---

Let `\([a,b]\)` be a [closed real interval][bookofproofs$1153] and let `\(f:[a,b]\to\mathbb R\)` be an arbitrary [continuous real function][bookofproofs$1260]. Then there are two numbers `$p,q\in[a,b]$` with 
`$$\begin{array}{rcl}f(p)&=&\max\{f(x):~x\in[a,b]\},\\f(q)&=&\min\{f(x):~x\in[a,b]\}.\end{array}$$`

### Notes

* This proposition does not work if the interval is open. 
* For instance, the function `$f:(0,1]\to\mathbb R$`, `$f(x)=\frac 2x$` is continuous and it takes a minimum at `$x=1$` (which is `$2$`), but does not take a maximum on the open interval `$(0,1].$`
* Another example is the function `$g:(0,1)\to\mathbb R$`, `$g(x)=x.$` It neither takes a maximum nor a minimum for all values of `$x\in(0,1)$`.
