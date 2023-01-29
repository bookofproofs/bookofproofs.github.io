layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$7831
orderid: 50
parentid: bookofproofs$7830
title: 
description:  Proof of ORDER RELATION FOR INTEGERS IS STRICT TOTAL &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: 
keywords: integers,order,relation,strict,total,transitivity,trichotomy,proof
contributors: bookofproofs

---


---

Let `$x,y,z\in \mathbb Z$` be any  [integers][bookofproofs$844].
We first show the trichotomy of the [order relation for integers][bookofproofs$1075] "$ < `$".

* If `$x < y$`, then it follows from the definition of the order relation for integers that `$x-y = [0,a]$` for some [natural number][bookofproofs$718] `$a\neq 0$`.
* Analogously, if `$x > y$`, it follows that `$x-y = [b,0]$` for some [natural number][bookofproofs$718] `$b\neq 0$`.
* Finally, if `$x=y$`, it follows that `$x-y = [0,0]$`.
* Since `$a\neq 0\neq b$`, we have, therefore the implications
   * `$x < y\Longrightarrow x \neq y$` and  `$x \not > 0$`.
   * `$x > y\Longrightarrow x \neq y$` and  `$x \not < 0$`.
   * `$x = y\Longrightarrow x \not > y$` and  `$x \not < 0$`.

Now, we shot the transitivity.

* Let `$x < y$` and `$y < z$`.
* Applying the definition of the order relation for integers we get `$x-y = [0,a]$` and `$y-z=[0,b]$` for some natural numbers `$a,b\neq 0$`.
* [Adding][bookofproofs$890] both equations results in `$x - y + y - z = [0,a+b]$`.
* By the [existence of inverse integers with respect to addition][bookofproofs$1511] we get  `$x-z=[0,a+b]$`.
* Since `$a+b\neq 0$` in the set of natural numbers `$\mathbb N$`, we get the relation `$x < z$` in the set of integers `$\mathbb Z$`.

The transitivity of the relations "`$>$`", "`$\ge$`", and "`$\le$`" follows analogously.
