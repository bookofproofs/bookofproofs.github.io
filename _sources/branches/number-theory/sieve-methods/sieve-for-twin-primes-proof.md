layout: proof
categories: branches,number-theory,sieve-methods
nodeid: bookofproofs$1018
orderid: 50
parentid: bookofproofs$6403
title: 
description: Proof of SIEVE FOR TWIN PRIMES, SIEVE FOR TWIN PRIMES, TWIN PRIME SEQUENCE ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now! ★ graduate maths ✔ step by step ✚ by the
references: bookofproofs$6913
keywords: twin primes sieve,twin primes sequence,proof
contributors: bookofproofs

---


---

By hypothesis, `$n\ge 1$` is an [integer][bookofproofs$844] and let `$f_s:=\left\lfloor\frac {s+1}6\right\rfloor$` using the [floor][bookofproofs$280] function.

### "`$\Rightarrow$`"

* Let the integer `$a_n:=36n^2-1$` be the product of two [twin primes][bookofproofs$233] `$p=6n-1$` and `$q=6n+1.$`
* According to the [fundamental theorem of arithmetics][bookofproofs$8094], since `$36n^2-1=(6n-1)(6n+1),$` we have `$p=6n-1$` and `$q=6n+1.$`
* Assume, there exists a [prime number][bookofproofs$473] `$s$` with `$5\le s\le\sqrt q$` and `$n$` [congruent][bookofproofs$8153] to `$n\equiv +f_s\mod s$` or `$n\equiv -f_s\mod s.$`
   * By assumption, either `$s\mid n-f_s$` or `$s\mid n+f_s.$`  
   * Therefore, by defintion of [divisibility][bookofproofs$700] there exist integers `$a,b$` such that either `$as=n-f_s$` or `$bs=n+f_s.$`
   * Therefore, either `$6as=6n-6f_s$` or `$6bs=6n+6f_s.$`
   * Therefore, either `$6as+(6f_s-1)=p$` or `$6bs-(6f_s-1)=q.$`
   * Note[^1] that by definition of `$f_s$`, `$s=6f_s-1.$`
   * Therefore, either `$s(6a+1)=p$` or `$s(6b-1)=q.$`
   * Therefore, either `$s\mid p$` or `$s\mid q.$`
   * Since `$p,q$` are prime, we have either `$s=p$` or `$s=q.$`
   * This [contradicts][bookofproofs$744] `$s\le\sqrt{p+2}=\sqrt{q}.$`
* Therefore, the assumption must be wrong and we have `$n\not\equiv \pm f_s\mod s$` for all primes `$s$` with `$5\le s\le\sqrt{q}.$`

### "`$\Leftarrow$`"

* Let `$n\not\equiv \pm f_s\mod s$` for all primes `$s$` with `$5\le s\le\sqrt{q}.$`
* Therefore, analogosly to  "`$\Rightarrow$`", there do not exist any integers `$a,b$` satisfying either `$s(6a+1)=6n-1=:p$` or `$s(6b-1)=6n+1=:q.$`
* Therefore, `$s\not\mid p$` and `$s\not\mid q$` for all primes `$s$` with `$5\le s \le\sqrt q.$`
* Since, by construction of `$p,q$`, `$pq=36n^2-1$`, even `$s\not\mid p$` and `$s\not\mid q$` for all primes `$s$` with `$2\le s \le\sqrt q,$` (otherwise we would have `$2\mid 36n^2-1$` or `$3\mid 36n^2-1,$` which is not the case).
* Therefore, `$p,q$` are [prime numbers][bookofproofs$473].
* Since `$p=q-2,$` they are [twin primes][bookofproofs$233].

[^1]: `$s$` has either the form `$6\nu-1$` or `$6\nu+1$` for some `$\nu\ge 1.$` If `$s=6\nu-1$` then `$6f_s-1=6\left\lfloor\frac{6\nu-1+1}{6}\right\rfloor-1=6\nu-1=s$`. If `$s=6\nu+1$` then `$6f_s-1=6\left\lfloor\frac{6\nu+1+1}{6}\right\rfloor-1=6\lfloor\nu+\frac 13\rfloor-1=6\nu-1=s.$` In both cases, `$s=6f_s-1.$`
