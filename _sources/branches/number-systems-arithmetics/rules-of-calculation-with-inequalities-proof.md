layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$595
orderid: 50
parentid: bookofproofs$594
title: 
description: Proof of RULES OF CALCULATION WITH INEQUALITIES ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: 
keywords: inequality rules,calculations involving inequalities,rules of calculations with inequalities,inequalities,inequality,proof
contributors: bookofproofs

---


---

*Proof of Rule 1)* For any `\(x\neq 0\)` it is `\(x \cdot x >0\)`.
This is a consequence from the rules of [multiplying positive and negative real numbers][bookofproofs$1598].
*Proof of Rule 2)* `\(1 > 0 \)`.
From the [uniqueness of 1][bookofproofs$48] and the [uniqueness of 0][bookofproofs$43], it follows that `\(1 \neq 0\)`. Therefore, according to the [definition of order relation][bookofproofs$1107], it must be either `\(1 > 0\)` or `\(-1 > 0\)`. Since `\(1\cdot 1 =1\)` , it must be `\(1 > 0 \)`, according to the rule Rule 1). 

*Proof of Rule 3)*  From `\(x > y\)` it follows that `\(x+a > y+a\)` for any `\(a\in\mathbb R\)`. 
(The rule is analogously valid and proven for any inequalities with "`\( < \)`" in between).
`\(x > y\)` means, by definition, that `\(x - y > 0\)`. Therefore, it is `\(x - y + a - a > 0\)`, and so it follows that `\(x + a  - (y + a) > 0\)`, and finally that `\(x + a > y + a \)`.  

*Proof of Rule 4)*  If `\(x > y\)` and `\(a > b\)`, then it follows that `\(x+a > y+b\)`.
(The rule is analogously valid and proven for any inequalities with "`\( < \)`" in between).
By definition, it is `\( x - y > 0 \)` and `\( a - b > 0 \)`. From the [definition of order relation][bookofproofs$1107], it follows that `\( (x - y) + (a -b) > 0\)`, which by definition results in `\(x + a > y + b\)`.

*Proof of Rule 5)* Transitivity of the "`\( < \)`" (analogously the "`\( > \)`" relation)
If `\(x < y\)` and `\(y < z\)`, then by definition it is `\(0 < y - x\)` and `\(0 < z - y\)`. From the [definition of order relation][bookofproofs$1107], it follows that `\( 0 < y - x + z - y= z - x\)`, which by definition results in `\(x < z\)`.

*Proof of Rule 6)* The inequality `\(x > y\)` does not change, if it is multiplied by any number `\(a > 0\)`, i.e. it is `\(ax > ay\)`. 
(The rule is analogously valid and proven for an inequalities with "`\( < \)`" in between). 
By definition, it is `\(x -y  > 0\)`. From the [definition of order relation][bookofproofs$1107], it follows that `\( a(x-y)  = ax - ay > 0\)`, which, by definition, results in `\(ax > ay\)`.

*Proof of Rule 7)* The inequality `\(x > y\)` changes, if it is multiplied by any number `\(a < 0\)`, i.e. it is `\(ax < ay\)`. (The rule is analogously valid and proven for an inequality with "`\( < \)`" in between, which then changes into "`\( > \)`"). By definition, it is `\(x - y  > 0\)` and `\(-a > 0\)`. From the [definition of order relation][bookofproofs$1107], it follows that `\( (-a)(x-y)  = -ax + ay > 0\)`, which, by definition, results in `\(ay > ax\)`, and finally in `\(ax < ay\)`.

*Proof of Rule 8)*  If `\(x > 0\)`, then `\(x^{-1} > 0\)`.
It is `\(x^{-1}=x^{-1}\cdot 1=x^{-1}\cdot(x^{-1}\cdot x) =(x^{-1}\cdot x^{-1})\cdot x\)`, which is greater then `\(0\)`, following the precondition, the Rule 1) and the [definition of order relation][bookofproofs$1107].

*Proof of Rule 9)*  If `\(x < 0\)`, then `\(x^{-1} < 0\)`.
It is `\(x^{-1}=x^{-1}\cdot 1=x^{-1}\cdot(x^{-1}\cdot x) =(x^{-1}\cdot x^{-1})\cdot x\)`, which is smaller then `\(0\)`, following the precondition, the Rule 1) and the Rule 7).

*Proof of Rule 10)* If `\(y > x > 0\)`, then `\(x^{-1} > y^{-1} \)`.
(The rule is analogously valid and proven for the inequality `\(0 < x < y\)`, resulting in `\(y^{-1} < x^{-1}\)`).
According to the precondition `\(x\)` and `\(y\)` are both positive. Therefore, it follows from the [definition of order relation][bookofproofs$1107] that `\(xy > 0\)`, and according to Rule 8) `\((xy)^{-1} > 0\)`. Multiplying the inequality `\(y > x\)` by the number `\((xy)^{-1}\)` does not change the inequality by Rule 6), therefore `\(y(xy)^{-1} > x (xy)^{-1}\)`. This is equivalent to `\(x^{-1} > y^{-1}\)`.

*Proof of Rule 11)* If `\(0 \le x < y\)` and `\(0 \le a < b\)`  then `\(ax < by\)`.
(The rule is analogously valid and proven for `\(by > ax\)`, following from `\(y > x \ge 0\)` and `\(b > a \ge 0\)`).
The argument is valid, if `\(x=0\)` or `\(a=0\)`, since then `\(0 < by\)` follows from the [definition of order relation][bookofproofs$1107]. So assume `\(0 < x < y\)` and `\(0 < a < b\)`. In this case we have `\(ax < ay\)` and `\(ay < by\)`, following in both cases from the Rule 6. The argument follows now from the transitivity (Rule 5)).
