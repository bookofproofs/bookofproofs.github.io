layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1584
orderid: 50
parentid: bookofproofs$1583
title: 
description:  Proof of MULTIPLICATION OF NATURAL NUMBERS IS CANCELLATIVE WITH RESPECT TO THE ORDER RELATION &#9733; master maths &#10004; visit BookOfProofs!
references: bookofproofs$1538
keywords: cancellative,multiplication,natural,numbers,order,relation,respect,proof
contributors: bookofproofs

---


---

Let `\(x,y,z\)` be [natural numbers][bookofproofs$718] with `\(z\neq 0\)`.

#### `\((1)\)` Proof of `\(x < y\Longleftrightarrow xz < yz\)` 

### `\((i)\)` "`\(\Rightarrow \)`"

According to the [definition of order relation of natural numbers][bookofproofs$697], we there exists a natural number `\(u\neq 0\)` with `\(y=x+u\)`. By virtue of the [distributivity law for natural numbers][bookofproofs$1030] we get 
`\[yz=(x+u)z=xz+uz.\]`

Since `\(uz\neq 0\)` by hypothesis, it follows, `\(xz < yz\)`.


### `\((ii)\)` "`\(\Leftarrow \)`"

Assume, `\(xz < yz\)`, but not `\(x < y\)`. According to the [trichotomy of the order relation for natural numbers][bookofproofs$1552], we must have otherwise `\(x = y\)` or `\(x > y\)`. If `\(x = y\)`, it would follow from the [cancellation law for multiplying natural numbers][bookofproofs$1440] that  `\(xz = yz\)`, which is a [contradiction][bookofproofs$744] to the assumption `\(x z < y z\)`. If `\(x > y\)`, then it would exist a natural number `\(v\neq 0\)` with `\(x=y+v\)`. Then we would get `\((y+v)\cdot z < y z\)`, or equivalently (applying the distributivity law for natural numbers) `\(yz+vz < yz\)`. This is again a [contradiction][bookofproofs$744], since `\(yz+vz > yz\)`.Thus, we must have `\(x < y\)`.

#### `\((1a)\)` Proof of `\(x < y\Longleftrightarrow  zx < zx\)` 

Follows from `\((1)\)` and the [commutativity of multiplying natural numbers][bookofproofs$1435].
#### `\((2)\)` Proof of `\(x > y\Longleftrightarrow x z > y z\)` and of `\(x > y\Longleftrightarrow z x > z x\)`

The proof is analogous to the proof of `\((1)\)` and `\((1a)\)`, for symmetry reasons. 


#### `\((3)\)` Proof of `\(x \le y\Longleftrightarrow x z \le y z\)` and of `\(x \le y\Longleftrightarrow z x \le z y\)` 

In the "`\( < \)`" case, the proof is identical to the proof `\((1)\)` or  `\((1a)\)`, for symmetry reasons. For the "`\( = \)`" case, the proof is identical to the proof of the [cancellation law for multiplying natural numbers][bookofproofs$1440].


#### `\((4)\)` Proof of `\(x \ge y\Longleftrightarrow x z \ge y z\)` and of `\(x \ge y\Longleftrightarrow z x \ge z y\)` 

The proof is analogous to the proof of `\((3)\)`, for symmetry reasons.
