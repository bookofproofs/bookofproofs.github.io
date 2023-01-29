layout: proof
categories: branches,set-theory
nodeid: bookofproofs$6855
orderid: 50
parentid: bookofproofs$6854
title: 
description: PROOF OF EQUALITY OF SETS Proof of DE MORGAN'S LAWS SETS &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$6823
keywords: de morgan laws,de morgan's laws,de morgan rules,de morgan's rules,proof
contributors: bookofproofs

---


---

* Suppose that `$A$` and `$B$` are [sets][bookofproofs$550].
* We want to show that for the [set intersection][bookofproofs$6828] "`$\cap$`", [set union][bookofproofs$6827] "`$\cup$`" and [set complent][bookofproofs$6829] "`$^C$`", the laws `$(A\cap B)^C=(A^C)\cup (B^C)$` and `$(A\cup B)^C=(A^C)\cap (B^C)$` hold.

### Part 1: `$(A\cap B)^C=(A^C)\cup (B^C)$`

#### We first show `$(A\cap B)^C\subseteq (A^C)\cup (B^C)$`

* Let `$x\in (A\cap B)^C$`. 
* According to the [definition of complent][bookofproofs$6829], we have `$x\not\in (A\cap B)$`.
* According to the [definition of set intersection][bookofproofs$6828], if `$x\in (A\cap B)$`, then `$x\in A \wedge x\in B$`, which is [negated][bookofproofs$714], i.e. `$\neg (x\in A \wedge x\in B).$`
* According to the [De Morgan's laws for logic][bookofproofs$6852], this means that `$x\not\in A\vee x\not\in B.$`
* According to the [definition of complent][bookofproofs$6829], we get `$x\in A^C\vee x\in B^C.$`
* According to the [definition of union][bookofproofs$6827], we get `$x\in (A^C)\cup (B^C).$`
* It follows from the definition of [subsets][bookofproofs$552] `$(A\cap B)^C\subseteq (A^C)\cup (B^C).$`

#### We now show `$(A^C)\cup (B^C)\subseteq (A\cap B)^C$`

* Let `$x\in (A^C)\cup (B^C)$`. 
* According to the [definition of union][bookofproofs$6827], we get `$x\in (A^C)\vee x\in (B^C).$`
* According to the [definition of complent][bookofproofs$6829], we have `$x\not\in A\vee x\not\in B$`.
* According to the [De Morgan's laws for logic][bookofproofs$6852], this means that `$\neg(x\in A\wedge x\in B).$`
* According to the [definition of set intersection][bookofproofs$6828], we get `$\neg (x\in (A\cap B)).$`
* According to the [definition of negation][bookofproofs$714], this is equivalent to `$x\not\in (A\cap B).$`
* By the [definition of complent][bookofproofs$6829], we get `$x\in(A\cap B)^C.$`
* It follows from the definition of [subsets][bookofproofs$552] `$(A^C)\cup (B^C)\subseteq (A\cap B)^C.$`

#### Conclusion 

* From both steps of Part 1 and the [equality of sets][bookofproofs$6841] it follows that `$(A\cap B)^C=(A^C)\cup (B^C).$`

### Part 2: `$(A\cup B)^C=(A^C)\cap (B^C)$`

#### We first show `$(A\cup B)^C\subseteq (A^C)\cap (B^C)$`

* Let `$x\in (A\cup B)^C$`. 
* According to the [definition of complent][bookofproofs$6829], we have `$x\not\in (A\cup B)$`.
* According to the [definition of set union][bookofproofs$6827], if `$x\in (A\cup B)$`, then `$x\in A \vee x\in B$`, which is [negated][bookofproofs$714], i.e. `$\neg (x\in A \vee x\in B).$`
* According to the [De Morgan's laws for logic][bookofproofs$6852], this means that `$x\not\in A\wedge x\not\in B.$`
* According to the [definition of complent][bookofproofs$6829], we get `$x\in A^C\wedge x\in B^C.$`
* According to the [definition of intersection][bookofproofs$6828], we get `$x\in (A^C)\cap (B^C).$`
* It follows from the definition of [subsets][bookofproofs$552] `$(A\cup B)^C\subseteq (A^C)\cap (B^C).$`

#### We now show `$(A^C)\cap (B^C)\subseteq (A\cup B)^C$`

* Let `$x\in (A^C)\cap (B^C)$`. 
* According to the [definition of intersection][bookofproofs$6828], we get `$x\in (A^C)\wedge x\in (B^C).$`
* According to the [definition of complent][bookofproofs$6829], we have `$x\not\in A\wedge x\not\in B$`.
* According to the [De Morgan's laws for logic][bookofproofs$6852], this means that `$\neg(x\in A\vee  x\in B).$`
* According to the [definition of set union][bookofproofs$6827], we get `$\neg (x\in (A\cup B)).$`
* According to the [definition of negation][bookofproofs$714], this is equivalent to `$x\not\in (A\cup B).$`
* By the [definition of complent][bookofproofs$6829], we get `$x\in(A\cup B)^C.$`
* It follows from the definition of [subsets][bookofproofs$552] `$(A^C)\cap (B^C)\subseteq (A\cup B)^C.$`

#### Conclusion 

* From both steps of Part 2 and the [equality of sets][bookofproofs$6841] it follows that `$(A\cup B)^C=(A^C)\cap (B^C).$`
