layout: proof
categories: branches,number-theory
nodeid: bookofproofs$3550
orderid: 50
parentid: bookofproofs$8216
title: 
description: PROOF OF PROPERTIES OF THE JACOBI SYMBOL &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$1272,bookofproofs$8187
keywords: jacobi,properties,symbol,jacobi symbol,jacobi symbol properties,proof
contributors: bookofproofs

---


---

By hypothesis, `$n,m$` are [odd][bookofproofs$8130] [positive integers][bookofproofs$1075], while `$a,b$` are any [integers][bookofproofs$844]. Moreover, in the following, we assume that `$n=p_1\cdots p_r$` and `$m=q_1\cdots q_s$` are the [factorizations][bookofproofs$803]  of `$n$` and `$m,$` in which we allow the prime numbers `$p_i$` to repeat, as `$i$` runs through the values `$1,\ldots,r.$` The same holds for the prime numbers `$q_j$` for `$j=1,\ldots, s.$` This will keep the formulae below clearer and simpler, but please keep this in mind when reading the proof below.

### Ad 1 

(Generalization of [Legendre symbols of equal residues][bookofproofs$8199])

* Let the [congruence][bookofproofs$8153] `$a(n)\equiv b(n)$` be fulfilled.
* From [congruence modulo a divisor][bookofproofs$8171], it follows that `$a(p_i)\equiv b(p_i)$` for every [prime][bookofproofs$473] [dividing][bookofproofs$700] `$n.$` 
* According to [Legendre symbols of equal residues][bookofproofs$8199], it follows that `$\left(\frac{a}{p_i}\right)=\left(\frac{b}{p_i}\right)$` for each [Legendre symbol][bookofproofs$8198].
* By the definition of the [Jacobi symbol][bookofproofs$8214], it follows that  `$\left(\frac{a}{n}\right)=\left(\frac{b}{n}\right).$`

### Ad 2

(Generalization of the [multiplicativity of the Legendre symbol][bookofproofs$8202])

* For every [prime][bookofproofs$473] `$p_i$` [dividing][bookofproofs$700] `$n$` it follows from the [multiplicativity of the Legendre symbol][bookofproofs$8202] that `$\left(\frac{ab}{p_i}\right)=\left(\frac{a}{p_i}\right)\cdot \left(\frac{b}{p_i}\right).$`
* By the definition of the [Jacobi symbol][bookofproofs$8214], it follows that  `$\left(\frac{ab}{n}\right)=\left(\frac{a}{n}\right)\cdot \left(\frac{b}{n}\right).$`

### Ad 3

* Case 1) `$a$` is [co-prime][bookofproofs$8093] to `$n$` and `$m.$`
   * By the definition of the [Jacobi symbol][bookofproofs$8214], it follows `$$\left(\frac{a}{n}\right)\cdot \left(\frac{a}{m}\right)=\prod_{i=1}^r\left(\frac{a}{p_i}\right)\cdot \prod_{j=1}^s\left(\frac{a}{q_j}\right)=\left(\frac{a}{nm}\right),$$` since if a prime `$p$` divides both numbers `$n$` and `$m$` at once, then its multiplicities sum up in both products, otherwise the multiplicities remain the same if a prime either divides the number `$n$` or the number `$m.$`
* Case 2) `$a$` is not co-prime to `$n$` or not co-prime to `$m$`.
   * Therefore, `$a$` is not co-prime to `$nm$`, and we have `$\left(\frac{a}{nm}\right)=0.$`
   * But then, either `$\left(\frac{a}{n}\right)=0,$` or `$\left(\frac{a}{m}\right)=0,$` or both. 
   * Therefore, again `$\left(\frac{a}{n}\right)\cdot \left(\frac{a}{m}\right)=\left(\frac{a}{nm}\right).$`

### Ad 4

(Generalization of the [quadratic reciprocity law][bookofproofs$8205])

* By hypothesis, `$n$`, and `$m$` are [co-prime][bookofproofs$8093].
* Therefore, all prime numbers `$p_i$` are distinct from the prime numbers `$q_j.$`
* By the definition of the [Jacobi symbol][bookofproofs$8214], we have `$$\left(\frac{n}{m}\right)\cdot \left(\frac{m}{n}\right)=\prod_{j=1}^s\left(\frac{n}{q_j}\right)\cdot \prod_{i=1}^r \left(\frac{m}{p_i}\right)=\prod_{i=1}^r\prod_{j=1}^s\left(\frac{p_i}{q_j}\right)\cdot \left(\frac{q_j}{p_i}\right).$$`
* Applying the [quadratic reciprocity law][bookofproofs$8205] to the right side of the equation, we get `$\left(\frac{n}{m}\right)\cdot \left(\frac{m}{n}\right)=(-1)^U$` with a sum `$$U=\sum_{i=1}^r\sum_{j=1}^s\frac{p_i-1}{2}\frac{q_j-1}{2}.$$`
* By the [generalized distributivity rule][bookofproofs$6629], we get `$$U=\left(\sum_{i=1}^r\frac{p_i-1}{2}\right)\cdot\left(\sum_{j=1}^s\frac{q_j-1}{2}\right).$$`
* For the theorem, it is sufficient to show that `$U\equiv\frac{n-1}2 \frac{m-1}2\mod 2.$`
* We get this result by applying a general rule repeatedly to all primes `$p_i$` and `$q_j$` which are all [odd][bookofproofs$8130]. The rule states that for arbitrary two odd integers `$a,b$` we have `$$\frac{a-1}2 +\frac{b-1}2\equiv \frac{ab-1}2\mod 2.\label{eq:E18802}\tag{1}$$` 
* To complete the proof, we note that `$$ 0\equiv\frac{(a-1)(b-1)}2\equiv \frac{ab-a-b+1}2\equiv\frac{ab-1}2-\left(\frac{a-1}2+\frac{b-1}2\right) \mod 2.$$`

### Ad 5

(Generalization of the [first supplementary law to the quadratic reciprocity law][bookofproofs$8206])

* By the definition of the [Jacobi symbol][bookofproofs$8214], and applying the [first supplementary law to the quadratic reciprocity law][bookofproofs$8206], we get `$$\left(\frac{-1}{n}\right)=\prod_{i=1}^r\left(\frac{-1}{p_i}\right)=\prod_{i=1}^r(-1)^{\frac{p_i-1}{2}}=(-1)^{V},$$` with `$$V:=\sum_{i=1}^r\frac{p_i-1}{2}.$$`
* Since `$n$` is [odd][bookofproofs$8130], we can apply  `$(\ref{eq:E18802})$` repeatedly, and get `$$V\equiv \frac{n-1}{2}\mod 2.$$`

### Ad 6

(Generalization of the [second supplementary law to the quadratic reciprocity law][bookofproofs$8207])

* By the definition of the [Jacobi symbol][bookofproofs$8214], and applying the [second supplementary law to the quadratic reciprocity law][bookofproofs$8207], we get `$$\left(\frac{2}{n}\right)=\prod_{i=1}^r\left(\frac{2}{p_i}\right)=\prod_{i=1}^r(-1)^{\frac{p_i^2-1}{8}}=(-1)^{W},$$` with `$$W:=\sum_{i=1}^r\frac{p_i^2-1}{8}.$$`
* For the theorem, it is sufficient to show that `$W\equiv\frac{n^2-1}8 \mod 2.$`
* We get this result by applying a general rule repeatedly to all primes `$p_i$` which are all [odd][bookofproofs$8130]. The rule states that for arbitrary two odd integers `$a,b$` we have `$$\frac{a^2-1}8 +\frac{b^2-1}8\equiv \frac{(ab)^2-1}8\mod 2.$$` 
* To complete the proof, we note that `$$ 0\equiv\frac{(a^2-1)(b^2-1)}8\equiv \frac{(ab)^2-a^2-b^2+1}8\equiv\frac{(ab)^2-1}8-\left(\frac{a^2-1}8+\frac{b^2-1}8\right) \mod 2.$$`
