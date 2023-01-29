layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1558
orderid: 50
parentid: bookofproofs$1555
title: 
description:  Proof of ORDER RELATION FOR NATURAL NUMBERS, REVISED &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$1538
keywords: natural,numbers,order,relation,revised,proof
contributors: bookofproofs

---


---

#### `\((1)\)` Proof of `\(y > x\Longleftrightarrow y \ge  x +1\)`

### `\((i)\)` Proof of "`\(\Rightarrow\)`"

If `\(y > x\)`, then it follows from the [definition of order relation][bookofproofs$697] that there exist a natural number `\(u\neq 0\)` with `\(y=x+u\)`. According to the fact that [every natural number is greater or equal zero][bookofproofs$1556], we must have `\(u > 0\)`. Because `\(1=0^+\)` is the unique successor of `\(0\)`, it is also the smallest number `\(u\)`, for which `\(u > 0\)`. Therefore, if `\(u=1\)`, then `\(y = x +1\)`. Otherwise `\(y > x+1\)`. Altogether, it follows `\(y \ge x+1\)`.

### `\((ii)\)` Proof of "`\(\Leftarrow\)`"

Assume `\( y \ge  x +1\)` and `\( y >  x +1\)`. Then we have `\(x + 1 > x\)` and by the [transitivity of the order relation][bookofproofs$1549], `\(y > x\)`.

Assume `\( y \ge  x +1\)` and `\( y  =  x +1\)`. Then we have `\(x + 1 > x\)` and we have trivially `\(y > x\)`.

#### `\((2)\)` Proof of `\(y < x\Longleftrightarrow y + 1 \le   x\)`


The proof is analogous to the proof of `\((1)\)`, for symmetry reasons.
