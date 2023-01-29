layout: example
categories: branches,logic
nodeid: bookofproofs$7938
orderid: 900
parentid: bookofproofs$184
title: Existence and Uniqueness of Solutions
description: EXISTENCE AND UNIQUENESS OF SOLUTIONS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$6823,bookofproofs$7937
keywords: existence,existence problem,solutions,uniqueness,uniqueness problem
contributors: bookofproofs

---


---

In many cases in mathematics, we are given an equation (or some equations) which depend on some unknowns and we want to find a solution to this / these equation(s). Let denote our equation by `$f(x)=0$` and the unknown by `$x$`. The problem of finding a solution `$x$` can usually be split into two different key questions. 

### Question 1: Does `$f(x)=0$` has __at least__ one solution?

This question is known as the **existence problem** of finding a solution for `$f(x)=0.$` We can solve the existence problem by the following strategies:

# __Strategy 1__: Finding an explicit solution
Usually, it is possible to apply this strategy in some very few special cases. The disadvantage of this strategy is that it requires a way to solve the equation(s) and that is usually not applicable for finding the solutions in generalized cases.
# __Strategy 2__: Abstract argumentation
Sometimes, it is possible to find a logical argument for the existence of a solution, for instance, [by contradiction][bookofproofs$744]. The disadvantage of this strategy is that does not supply us with an explicit solution.
# __Strategy 3__: Finding a procedure (algorithm) to find a solution
If we manage to find an algorithm which needs only a finite number of steps to find a solution to `$f(x)=0,$` then this algorithm also solves the above existence problem.

If mathematicians succeed to solve the existence problem by applying e.g. the above-mentioned strategies, then they say

__"$f(x)=0$ has at least one solution."__ 

### Question 2: Does `$f(x)=0$` has __at most__ one solution?

This question is known as the **uniqueness problem** of finding a solution for `$f(x)=0.$` Like for the existence problem, there are multiple strategies to tackle the uniqueness problem:

# __Strategy 1__: Proof by contradiction
First, we assume that `$x,y$` are both solutions, i.e. `$f(x)=0$` and `$f(y)=0,$` and that `$x\neq y.$` From these assumptions, we try to conclude a contradiction. This implies that `$x=y$` which is equivalent to the uniqueness of any existing solution. 
# __Strategy 2__: Proof by [contraposition][bookofproofs$1330].
In this strategy, we try to conclude that from `$x\neq y$` it follows that `$x$` and `$y$` cannot be both solutions of `$f.$` If we succeed, then it implies the uniqueness of any existing solution. 

If mathematicians succeed to solve the uniqueness problem by applying e.g. the above-mentioned strategies, then they say

__"$f(x)=0$ has at most one solution."__ 

Usually, the existence and the uniqueness problems can be treated independently from each other.
