layout: proof
categories: branches,analysis
nodeid: bookofproofs$1734
orderid: 50
parentid: bookofproofs$1253
title: 
description: Proof of DISTANCE OF COMPLEX NUMBERS MAKES COMPLEX NUMBERS A METRIC SPACE. ★ master graduate maths ✔ visit BookOfProofs now!
references: bookofproofs$581
keywords: distance of complex numbers,complex metric space,triangle inequality,proof
contributors: bookofproofs

---


---

For any elements `$z,z_1,z_2\in\mathbb C$` of the [field of complex numbers][bookofproofs$1690] `$(\mathbb C, + ,\cdot)$` with `$z=z_1=:(a,b)$` and `$z_2=(c,d)$` ($a,b,c,d\in\mathbb R$):

### Ad `$(1)$`

* By the definition of [absolute value of complex numbers][bookofproofs$1247], `$|z|=\sqrt{a^2+b^2}=0$` 
* if and only if `$\sqrt{a^2+b^2}=0,$` 
* if and only if `$a=0$` and `$b=0,$`
* if and only if `$x=(0,0).$`

### Ad `$(2)$`  

* By the definition of [subtraction of complex numbers][bookofproofs$1701], we get `$|z_1-z_2|=\sqrt{(a-c)^2+(b-d)^2}$`
* `$=\sqrt{(c-a)^2+(d-b)^2}$` because `$x^2=(-x)^2$` for all real numbers,
* `$=|z_2-z_1|$` by definition.

### Ad `$(3)$`

* Note that for every complex number `$z$` we have that its [real part][bookofproofs$216] is smaller or equal[^1] than its absolute value `$\Re(z)\le |z|.$`
* Given the [complex conjugate][bookofproofs$1245] `$z_2^*$`, we get therefore the inequality `$$\Re(z_1z_2^*)\le |z_1z_2^*|=|z_1||z_2^*|=|z_1||z_2|.$$`
* Therefore, `$$\begin{array}{rcl}|z_1+z_2|^2&=&(z_1+z_2)(z_1^*+z_2^*)\\&=&z_1z_1^*+z_1z_2^*+z_2z_2^*+z_2z_2^*\\&=&|z_1|^2+2\Re(z_1z_2^*)+|z_2|^2\\&\le&|z_1|^2+2|z_1||z_2|+|z_2|^2\\&=&(|z_1|+|z_2|)^2\end{array}$$`
* Taking the [square root][bookofproofs$1161] on both sides of the inequality yields the _triangle inequality_ `$$|z_1+z_2|\le |z_1|+|z_2|.$$`

[^1]: This is not only algebraically, but also geometrically clear if you think of a complex number as a point in the [complex plane][bookofproofs$216] with two coordinates - the real part, and the imaginary part.
