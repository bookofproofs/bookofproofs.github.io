layout: explanation
categories: branches,analysis
nodeid: bookofproofs$6777
orderid: 100
parentid: bookofproofs$6776
title: Local Extrema on  a Closed Interval
description: LOCAL EXTREMA ON  A CLOSED INTERVAL &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$581
keywords: closed,extrema,interval,local
contributors: bookofproofs

---


---

The [proposition about the zero-derivative as a necessary condition for a local extremum][bookofproofs$6776] can be used to test if a value `$x$` can be a local extremum. If `$f'(x)\neq 0$` for some `$x$`, then we have a proof that `$x$` cannot be an extremum. But if `$f'(x)=0$`, `$x$` can be a local extremum (but does not have to, taking the function `$f(x):=x^3$` as an example).

### Caution

When using this test, it is important to make sure that the function `$f$` is defined on an [open real interval][bookofproofs$1153] `$]a,b[$`. For if the interval was closed, then our test might fail. Take the function `$f:[0,1]\to\mathbb R$`, `$x\to x$` as an example. It has a minimum at `$0$` and a maximum at `$1$`, but it has nevertheless a non-zero derivative `$f'=1$`. Thus, according to a [corresponding proposition][bookofproofs$6696], every continuous function on a closed interval takes its maximum (or minimum), even though its derivative (if it exists) might be non-zero.
