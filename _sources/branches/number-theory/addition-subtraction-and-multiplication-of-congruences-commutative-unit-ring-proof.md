layout: proof
categories: branches,number-theory
nodeid: bookofproofs$2946
orderid: 50
parentid: bookofproofs$8156
title: 
description:  Proof of ADDITION, SUBTRACTION AND MULTIPLICATION OF CONGRUENCES, THE COMMUTATIVE RING $\MATHBB Z_M$ &#9733; master maths &#10004; visit BookOfProofs!
references: bookofproofs$8152,bookofproofs$8189
keywords: addition of residues,multiplication of congruences,add residues,multiply residues,add congruences,multiply congruences,commutative ring of congruences,proof
contributors: bookofproofs

---


---

* We have to show that these operations for the [congruence classes][bookofproofs$8154] modulo a [positive integer][bookofproofs$1075] `$m$` are well-defined, i.e. do not depend on the special choice of the representatives `$a$` and `$b$`.
* Assume, `$a\neq a'$` and `$b\neq b'$` are all [integers][bookofproofs$844] with equal congruence classes `$a\equiv a'(m)$` and `$b\equiv b'(m).$`
* By definition `$m\mid (a-a')$` and `$m\mid (b-b').$`
* Using the [addition][bookofproofs$890] and/or [subtraction][bookofproofs$1585] "`$\pm$`" of integers:
   * I.e. `$m\mid ((a-a')\pm (b-b')).$` 
   * I.e. `$m\mid ((a\pm b)-(a'\pm b').$`
   * I.e. `$m\mid ((a\pm b)$` and `$m\mid (a'\pm b').$`
   * I.e. `$(a\pm b)(m)=(a'\pm b')(m).$`
* Using the [multiplication of integers][bookofproofs$891]:
   * I.e. `$a=a'+km$` and `$b=b'+lm$` for some integers `$k,l.$`
   * I.e. `$ab=a'b'+(a'l+kb'+klm)m$`
   * I.e. `$ab(m)\equiv a'b'(m).$`
* Therefore, the set  `$(\mathbb Z_m,\cdot,+)$` is a [commutative unit ring][bookofproofs$880], (a detailed proof is left for the reader as an exercise) since:
   * `$(\mathbb Z,+)$` is a [commutative group][bookofproofs$553] with the neutral element `$0(m),$` i.e. `$a(m)+0(m)\equiv 0(m)+a(m)\equiv a(m)$` and the inverse elements `$(-a)(m)+a(m)=0(m)$` for all `$a(m)\in\mathbb Z_m.$`
   * `$(\mathbb Z,\cdot)$` is a commutative [semigroup][bookofproofs$660] with the neutral element `$1(m),$` i.e. `$a(m)\cdot 1(m)\equiv 1(m)\cdot a(m)\equiv a(m)$` for all `$a(m)\in\mathbb Z_m.$`
