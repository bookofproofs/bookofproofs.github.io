layout: proof
categories: branches,theoretical-computer-science, semi-numerical-algorithms
nodeid: bookofproofs$2882
orderid: 50
parentid: bookofproofs$8224
title: 
description:  Proof of CALCULATION OF INVERSES MODULO A NUMBER PYTHON &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$1357,bookofproofs$8187
keywords: calculation,inverses,modulo,number,python,invmod python,python invmod,inverse modulo python,proof
contributors: bookofproofs

---


---

* The algorithm uses [gcdext][bookofproofs$8223] to calculate the numbers `$x,y$` with `$ax+by=\gcd(a,b).$`
* If `$\gcd(a,b)=1$`, the value of `$x$` is an integer fulfilling `$ax\equiv 1\mod b.$`
* Otherwise, an exception is thrown, since a [multiplicative inverse][bookofproofs$670] does not exist.
* In the last step, if `$x < 0,$` `$\operatorname{invmod}$` choses a positive representative of the same [congruence class][bookofproofs$8154] modulo `$b$` in the time `$\mathcal O(1).$`
* Altogether, the runtime is the same as in the [gcdext][bookofproofs$8223] algorithm, i.e. `$\mathcal O(b).$`
