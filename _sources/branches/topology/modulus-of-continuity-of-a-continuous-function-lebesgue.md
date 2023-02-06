layout: definition
categories: branches,topology
nodeid: bookofproofs$6704
orderid: 100
parentid: bookofproofs$1254
title: Modulus of Continuity of a Continuous Function
description: MODULUS OF CONTINUITY OF A CONTINUOUS FUNCTION LEBESGUE &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$581
keywords: continuity,definition,delta,epsilon,epsilon delta definition of continuity,epsilon delta continuity,delta epsilon definition of continuity,definition of continuity epsilon delta,continuity epsilon delta,epsilon-delta definition of continuity,epsilon delta definition,epsilon delta definition of continuous function,epsilon delta definition continuity
contributors: bookofproofs


---


---

Let `\((X,d_x)\)` and `\((Y,d_y)\)` be [metric spaces][bookofproofs$617] and let `\(f:X\to Y\)` be a [continuous function][bookofproofs$1254] on `$X$`. Using the [$\epsilon-\delta$-definition of continuity][bookofproofs$1254], this means that for all `$a\in X$` we have that for every `$\epsilon > 0$` there is a `$\delta > 0$` such that `$d_y(f(\xi),f(a)) < \epsilon$` for all `\(\xi\in X\)` with `$d_x(\xi,a) < \delta.$`

The **modulus of continuity** of `$f$`, is the [function][bookofproofs$592] `$\omega_f:[0,\infty]\to[0,\infty]$`, which assigns to each positive real number `$\delta$` the  [supremum][bookofproofs$6669] of [distances][bookofproofs$614] `$d_y(f(a),f(b))$` in `$Y$` for all points `$a,b\in X$`, whose distance `$d_x(a,b)$` is at most `$\delta$` in `$X,$` formally

`$$\omega_f(\delta):=\sup\{d_y(f(a),f(b)):~a,b\in X,~d_x(a,b)\le\delta\}.$$`

Roughly speaking, the modulus of continuity can be interpreted as the greatest positive number `$\epsilon$` on whole `$X$`, for which for a given `$\delta$` the [$\epsilon-\delta$-property of continuity][bookofproofs$1254] still holds for the function `$f$`. The concept was invented by [Henri Lebesgue][bookofproofs$Lebesgue] in 1910.
