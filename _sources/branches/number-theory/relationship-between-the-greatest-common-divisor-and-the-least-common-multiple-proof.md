layout: proof
categories: branches,number-theory
nodeid: bookofproofs$1282
orderid: 50
parentid: bookofproofs$1281
title: 
description:  Proof of RELATIONSHIP BETWEEN THE GREATEST COMMON DIVISOR AND THE LEAST COMMON MULTIPLE &#9733; master graduate maths &#10004; visit BookOfProofs now!
references: bookofproofs$1272
keywords: between,common,divisor,greatest,least,multiple,relationship,proof
contributors: bookofproofs

---


---

* Let `\(a > 0\)`, `\(b > 0\)` be [natural numbers][bookofproofs$718].
* Since `\(ab\)` is a [common multiple][bookofproofs$1276] of `\(a\)` and `\(b\)`, it follows from the proposition about the [least common multiple][bookofproofs$1276] that `$\operatorname{lcm}(a,b)\mid ab.$`
* We set `$$d:=\frac{ab}{\operatorname{lcm}(a,b)},\quad\quad( * )$$` and will show that `\(d\)` is the [greatest common divisor][bookofproofs$1280] of `\(a\)` and `\(b\)`, i.e. `$d=\gcd(a,b).$`
   * From the [definition of multiplication of rational numbers][bookofproofs$1033] it follows that we can transform the equation `\(( * )\)` into 
`\[\frac{a}{d}=\frac{\operatorname{lcm}(a,b)}{b},~\frac{b}{d}=\frac{\operatorname{lcm}(a,b)}{a}.\]`
   * Since `\(a\)` and `\(b\)` divide `\(\operatorname{lcm}(a,b)\)` , the fractions `\(\frac{a}{d}\)` and `\(\frac{b}{d}\)` are, in fact, [integers][bookofproofs$844].
   * Therefore, `\(d\)` is a [common divisor][bookofproofs$1280] of `\(a\)` and `\(b\)`. 
   * It remains to be shown that `$d$` is the [greatest common divisor][bookofproofs$1280] of `\(a\)` and `\(b\)`. 
      * Let `\(f\)` be any common divisor of `\(a\)` and `\(b\)`. 
      * Because `$a\mid a\frac bf$` and `$b\mid b\frac af,$` the number `\(\frac{ab}f\)` is a [common multiple][bookofproofs$1276] of `\(a\)` and `\(b\)`.
      * It follows from the [proposition about the least common multiple][bookofproofs$1276] that `\(\operatorname{lcm}(a,b)\)` divides `\(\frac{ab}f\)`. 
      * Since `\(\operatorname{lcm}(a,b)=\frac{ab}d\)` (see above), we have that
`\[\frac{ab}d|\frac{ab}f.\]`
      * This means that the rational number 
`\[\frac{\frac{ab}f}{\frac{ab}d}=\frac df\]`
is in fact an integer. 
      * Since `\(f\)` was _an arbitrarily chosen_ common divisor of both, `\(a\)` and `\(b\)`, and since it divides the common divisor `\(d\)`, the latter number `\(d\)` must be the greatest common divisor.
      * It follows that `$d=\gcd(a,b).$`
