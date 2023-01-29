layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$8604
orderid: 50
parentid: bookofproofs$8603
title: 
description: PROOF OF COMPLEX NUMBERS CANNOT BE ORDERED ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: 
keywords: complex numbers cannot be ordered,proof
contributors: bookofproofs

---


---

We provide a proof by [contradiction][bookofproofs$744].
* Assume, the [field of complex numbers][bookofproofs$1690] `$(\mathbb C,+,\cdot)$` is an [ordered field][bookofproofs$6193], i.e. there is a [linear order][bookofproofs$6191] „`\(\geq \)`“ on `\(\mathbb C\)`, which fulfills the two properties:
   * from `\(z_1\geq z_1\)` it follows `\(z_1+z_3\geq z_1+z_1\)` (for arbitrary `\(z_1,z_2,z_3\in \mathbb C\)`), and
   * from `\(z_1\geq 0\)` and `\(z_2\geq 0\)` it follows `\(z_1\cdot z_2\geq 0\)` (for `\(z_1,z_2\in F\)`).
* It suffices to show that the two complex numbers, the [imaginary unit][bookofproofs$1160] `$i\in\mathbb C$` and the [complex zero][bookofproofs$1662] `$0\in\mathbb C,$` cannot be ordered to fulfill the second property. 
   * Case `$i \ge 0.$`
      * Then `$i\cdot i\ge 0\cdot i=0,$` or `$-1 \ge 0$` which is a contradiction in the [embedded real numbers][bookofproofs$1243] as a special case of complex numbers.
   * Case `$i < 0.$`
      * Then `$(-i)\cdot (-i) > 0,$` or `$-1 > 0$` which is again a contradiction.
