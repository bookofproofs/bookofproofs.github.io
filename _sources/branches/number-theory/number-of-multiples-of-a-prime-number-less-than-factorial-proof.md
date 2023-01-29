layout: proof
categories: branches,number-theory
nodeid: bookofproofs$8120
orderid: 50
parentid: bookofproofs$8111
title: 
description:  Proof of NUMBER OF MULTIPLES OF A PRIME NUMBER LESS THAN FACTORIAL &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$701,bookofproofs$1272
keywords: factorial,less,multiples,number,prime,than,proof
contributors: bookofproofs

---


---

In the following proof, `$p\in\mathbb P$` is a given [prime number][bookofproofs$473], `$n > 0$` a given [natural number][bookofproofs$718] and `$n !$` its [factorial][bookofproofs$1005].
* First of all, note that the above [infinite series][bookofproofs$1109] `$( * )$` is, in fact, [convergent][bookofproofs$175], because for all `$m$` with `$m > \frac{\log n}{\log p}$`, ($\log$ beging the [natural logarithm][bookofproofs$1421]), we have:
   * `$p^m > n$` and `$0 <  \frac n{p^m} < 1.$`
   * and thus the [floor function][bookofproofs$280] `$\left\lfloor\frac n{p^m}\right\rfloor=0.$`
   * Therefore, we can write the infinite series as a finite sum:
`$$\sum_{m=1}^\infty\left\lfloor\frac n{p^m}\right\rfloor=\sum_{1\le m\le \frac{\log n}{\log p}}\left\lfloor\frac n{p^m}\right\rfloor.$$`
* Also note that `$( * * )$` is correct for `$n=1$`, since we have `$n!=1$` and `$( * * )$` is an empty product, which also equals `$1.$` 
* Moreover, if `$ p > n$` then there are no [multiples][bookofproofs$700] `$kp$` of `$p$` less than `$n$` and the sum `$( * )$` equals `$0$`, which in the product `$( * * )$` means the factor `$1,$` not contributing to the product any more.
* So let `$n > 1.$`
   * We can replace the [natural number][bookofproofs$718] `$n$` by the [floor function][bookofproofs$280] of any [positive real number][bookofproofs$1107] `$x > 0$` and get by applying the [sum of von Mangoldt function over divisors][bookofproofs$8118]:
`$$\log(\lfloor x \rfloor!)=\sum_{n=1}^{\lfloor x \rfloor}\log (n)=\sum_{n=1}^{\lfloor x \rfloor}\sum_{d\mid n}\Lambda(d)=\sum_{d=1}^{\lfloor x \rfloor}\Lambda(d)\left\lfloor \frac xd \right\rfloor.\quad (\dagger) $$`
   * The last step is because the [number of multiples of `$d$` with `$d\le  x$`][bookofproofs$8107] is given by `$\left\lfloor \frac xd \right\rfloor$` and exactly this is the number of `$d\le \lfloor x \rfloor,$` for which `$\Lambda(d) > 0$` when `$d\le n$` and `$n$` runs through the numbers `$1,2,\ldots,\lfloor x \rfloor.$`[^1] 
   * By the definition of the [von Mangoldt function][bookofproofs$702] it follows from `$(\dagger)$` with the [natural logarithm][bookofproofs$1421] that 
`$$\begin{array}{rcl}\sum_{d=1}^{\lfloor x \rfloor}\Lambda(d)\left\lfloor \frac xd \right\rfloor&=&\sum_{p \le x}\log(p)\left\lfloor \frac xp \right\rfloor+\sum_{p \le x}\log(p)\left\lfloor \frac x{p^2} \right\rfloor+\sum_{p \le x}\log(p)\left\lfloor \frac x{p^3} \right\rfloor+\ldots\\
&=&\sum_{p \le x}\log(p)\sum_{m=1}^\infty\left\lfloor \frac x{p^m} \right\rfloor.\end{array}$$`
   * Taking the [exponential function][bookofproofs$281] of this result gives us
`$$\lfloor x\rfloor!=\prod_{p\in\mathbb P}p^{\sum_{m=1}^\infty\left\lfloor\frac {\lfloor x\rfloor}{p^m}\right\rfloor}$$`
* This proves the result `$( * * )$` for `$x=n.$`

[^1]: This type of changing the order of two sums is typical for number-theoretic reasoning and a little bit tricky. The reader is invited to try out some simple cases, for instance, `$x=2.5$` and `$x=4.3$` in this particular case.
