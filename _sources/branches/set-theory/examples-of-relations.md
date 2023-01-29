layout: example
categories: branches,set-theory
nodeid: bookofproofs$578
orderid: 50
parentid: bookofproofs$571
title: Examples of Relations
description: EXAMPLES OF RELATIONS ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: 
keywords: examples of relations
contributors: bookofproofs

---


---

### Relations defined between elements of the same set

* Let `$P$` be the set of all people. The **silbing relation** `\(S\subset P\times P\)` is the subset of all pairs `$(p_1,p_2)$` of persons such that `$S=\{(p_1,p_2):a \text{ is a sibling of } b\}.$`
* Let `$C$` be the set of all cities in a country. We define the (ternary) relation `$R\subset C\times C\times C$`  as the subset of all tripples of cities `$(c_1,c_2,c_3)$` such that there is a railway connection between `$c_1$` to `$c_3$` via `$c_2.$`
* Let `$\mathbb N$` be the set of [natural numbers][bookofproofs$664]. We define the order relation `$"\ge"\subset \mathbb N\times \mathbb N$` as all pairs of natural numbers `$(a,b)$` such that `$a-b\in\mathbb N.$` In this case we write `$a\ge b$`.
* Let `$T$` be the set of all triangles in a plane. We define the congruency relation `$=$` between these triangles as all pairs of triangles `$(t_1,t_2)$` such that `$t_1$` can exactly cover `$t_2$` by moving or rotating it in the plane. In this case we write `$t_1=t_2$` and say that these triangles are congruent.
* Order relation of integers `$$R_3=\{(x,y)\in\mathbb Z\times \mathbb Z\mid x \le y\}.$$`
* Multiples of `$4$` `$$R_4=\{(x,y)\in\mathbb Z\times \mathbb Z\mid y=4x\}.$$`
* Let `$U$` be the set of all users of a social network. The "is a follower of" relation is defined `$$R_5=\{(u,v)\in U\times U\mid u\text{ is a follower of }v\}.$$`
* A relation can also be defined for only one set: Let `$U$` be the set of all users of a social network. The "is a bot" relation is defined `$$R_6=\{(u)\in U\mid u\text{ is a robot }\}.$$`
* ...

### Relations defined between elements of different sets

* Let `$P$` be the set of all people. The relation of all people `$P$` who have the same child is `$$R_1=\{(a,b)\in P\times P\mid a,b\text{ are the parents of the same child}\}.$$`
* Let `$U$` be the set of all Internet users and `$V$` be the set of all visitors of a specific website. `$$R_2=\{(u,v)\in U\times V\mid u\text{ is female},v\text{ visited the website in the last 2 days}\}.$$`
* Let `$L$` be the set of all lectures and `$T$` be the set of all lecturers in a university. We define a binary relation `$C\subset L\times T$` as consisting of all pairs of a lecture `$\lambda\in L$` and a lecturer `$l\in T$` such that the lecturer `$l$` gives the lecture `$\lambda.$`
* Let `$S$` be the set of all students of the same university. We define another relation `$B\subset S\times L$` such that a student `$s\in S$` attends the lecture `$l\in L$`.
* Let `$C$` be the set of all countries in the world and let `$\mathbb R$` be the [set of real numbers][bookofproofs$1105]. If we map each country `$c$` to its area `$a$` (measured in square kilometers), be define a binary relation of pairs `$(c,a)\in C\times\mathbb R.$`
