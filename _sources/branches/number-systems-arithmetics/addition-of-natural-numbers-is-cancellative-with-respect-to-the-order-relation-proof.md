layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1554
orderid: 50
parentid: bookofproofs$1551
title: 
description:  Proof of ADDITION OF NATURAL NUMBERS IS CANCELLATIVE WITH RESPECT TO INEQUALITIES &#9733; master graduate maths &#10004; visit BookOfProofs now!
references: bookofproofs$1538
keywords: addition,cancellative,natural,numbers,order,relation,respect,proof
contributors: bookofproofs

---


---

Let `\(x,y,z\)` be [arbitrary natural numbers][bookofproofs$718].
#### `\((1)\)` Proof of `\(x < y\Longleftrightarrow x + z < y + z\)` 

### `\((i)\)` "`\(\Rightarrow \)`"

According to the [definition of order relation of natural numbers][bookofproofs$697], we there exists a natural number `\(u\neq 0\)` with `\(y=x+u\)`. By virtue of the [associativity][bookofproofs$1428] and [commutativity laws][bookofproofs$1430] for adding natural numbers Therefore we have `\[y+z=(x+u)+z=x+(u+z)=x+(z+u)=(x+z)+u.\]`

It follows, `\(x+z < y + z\)`.


### `\((ii)\)` "`\(\Leftarrow \)`"

Assume, `\(x + z < y + z\)` , but not `\(x < y\)`. According to the [trichotomy of the order relation for natural numbers][bookofproofs$1552], we must have otherwise `\(x = y\)` or `\(x > y\)`. If `\(x = y\)`, it would follow from the [cancellation law for adding natural numbers][bookofproofs$1432] that  `\(x + z = y + z\)`, which is a [contradiction][bookofproofs$744] to the assumption `\(x + z < y + z\)`. If `\(x > y\)`, then it would exist a natural number `\(v\neq 0\)` with `\(x=y+v\)`. Then we would get `\((y+v) + z < y + z\)`, or equivalently (applying the associativity and commutativity of adding natural numbers) `\((y+z) +v < y+z\)`. This is again a [contradiction][bookofproofs$744], since `\((y + z) + v > y + z\)`. Thus, we must have `\(x < y\)`.

#### `\((1a)\)` Proof of `\(x < y\Longleftrightarrow  z + x < z + y\)` 

Follows from `\((1)\)` and the [commutativity of adding natural numbers][bookofproofs$1430].


#### `\((2)\)` Proof of `\(x > y\Longleftrightarrow x + z > y + z\)` and of `\(x > y\Longleftrightarrow z + x > z + x\)`

The proof is analogous to the proof of `\((1)\)` and `\((1a)\)`, for symmetry reasons. 


#### `\((3)\)` Proof of `\(x \le y\Longleftrightarrow x + z \le y + z\)` and of `\(x \le y\Longleftrightarrow z + x \le z + y\)` 

In the "`\( < \)`" case, the proof is identical to the proof `\((1)\)` or  `\((1a)\)`, for symmetry reasons. For the "`\( = \)`" case, the proof is identical to the proof of the [cancellation law for adding natural numbers][bookofproofs$1432].


#### `\((4)\)` Proof of `\(x \ge y\Longleftrightarrow x + z \ge y + z\)` and of `\(x \ge y\Longleftrightarrow z + x \ge z + y\)` 

The proof is analogous to the proof of `\((3)\)`, for symmetry reasons.
