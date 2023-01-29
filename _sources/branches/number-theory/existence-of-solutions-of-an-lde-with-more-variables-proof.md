layout: proof
categories: branches,number-theory
nodeid: bookofproofs$3528
orderid: 50
parentid: bookofproofs$8179
title: By Induction
description:  Proof of EXISTENCE OF SOLUTIONS OF AN LDE WITH MORE VARIABLES &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$1272
keywords: existence,lde,more,solutions,variables,proof
contributors: bookofproofs

---


---

By hypothesis, `$m > 0$` is a given [positive integer][bookofproofs$1075] `$a_1,\ldots,a_r,b$` are given [integers][bookofproofs$844].
### "`$\Rightarrow$`"

* Assume, the LDE (linear [Diophantine equation][bookofproofs$8158]) with `$r$` variables `$a_1x_1+\ldots+a_rx_r=b$` is solvable.
   * Let `$d:=\gcd(a_1,\ldots,a_r)$` be the [greatest common divisor of the `$r$` numbers][bookofproofs$8122] of `$a_1,\ldots,a_r.$` 
   * From the [divisibility law no. 9][bookofproofs$508], it follows by [induction][bookofproofs$657] that `$d\mid (a_1x_1+\ldots+a_rx_r)$`.
   * Since `$a_1x_1+\ldots+a_rx_r=b,$` it follows that `$d$` is also a [divisor][bookofproofs$700] of `$b.$`

### "`$\Leftarrow$`"

* Now, assume that `$d\mid b.$`
   * Case `$r=1$`: All except one coefficient `$a_i$` equal zero, without loss of generality `$a_1\neq 0$` i.e. `$a_1x_1+0x_2+\ldots+0x_r=b.$`
      * Then, obviously, `$d=\gcd(a_1,0,\ldots,0)=a_i\mid b$` and we have that the equation is solvable.
   * Case `$r=2$`: All except two coefficients `$a_i$` equal zero, without loss of generality `$a_1\neq 0,a_2\neq 0$` i.e. `$a_1x_1+a_2x_2+0x_3+\ldots+0x_r=b.$`
      * Note that from the [existence and number of solutions of an LDE with one variable][bookofproofs$8178], it follows that the [linear Diophantine equation of congrences][bookofproofs$8159] `$(a_1x_1)(a_2)\equiv b(a_2)$` is solvable for the module `$a_2$` if and only if `$\gcd(a_1,a_2)\mid b.$`
      * With this solution, we can also solve[^1] the above equation `$a_1x_1+a_2x_2=b.$`
   * Case `$r > 2$`: 
      * Assume, the claim is correct for the cases `$2,\ldots,r-1$` (base case). By [induction][bookofproofs$657]: 
      * Set `$a:=\gcd(a_1,\ldots,a_{r-1}),$` then we have `$\gcd(a,a_r)=d$` by definition of the [greatest common divisor of more than two numbers][bookofproofs$8122].
      * According to the case `$r=2,$` the equation `$ax+a_rx_r=b$` is solvable, for some suitable integers `$x, x_r.$`
      * Since `$a\mid ax$` we have also that the equation `$a_1x_1+\ldots+a_{r-1}x_{r-1}=ax$` is solvable, for some suitable integers `$x_1,\ldots,x_{r-1},$` by the base case.
      * Therefore, the equation `$a_1x_1+\ldots+a_rx_r=b$` is solvable for some suitable integers `$x_1,\ldots,x_{r}.$`


[^1]: Take for `$x_1$` any integer representing the congruence class `$x(a_2)$` solving the congruence `$(a_1x_1)(a_2)\equiv b(a_2)$` and solve the equation for `$a_1x_1+a_2x_2=b$` for `$x_2.$`
