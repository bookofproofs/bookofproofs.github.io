layout: part
categories: branches,logic
nodeid: bookofproofs$184
orderid: 700
parentid: bookofproofs$25
title: Methods of Mathematical Proving
description: METHODS OF MATHEMATICAL PROVING ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$6823
keywords: methods of mathematical proving,mathematical proofs
contributors: bookofproofs


---


---

This part is dedicated to the methods developed over centuries to prove mathematical statements. Mathematical proofs are the strength of mathematics because they help us to replace our experience or heuristics by doubtless certainty.

Mathematical **proofs** are based on the axiomatic method - in each mathematical discipline, there is a small number of facts, called **axioms** (or **postulates** or **principles**), considered as absolutely certain truths which do not have to be proved. Beginning from these axioms (sometimes complemented by definitions), one proves [statements][bookofproofs$710] using logical reasoning. A statement is known as a **theorem**, **lemma**, **corollary**, **proposition**, or **law**.

Based on the proven theorems, one proves new theorems, and so forth. The axiomatic method is - like a snowball - very powerful!

Mathematicians know from experience that before you want to begin a logical investigation, you better start with
*definitions*, which are some "clear" descriptions of objects you are about to study. It is important to know what is meant by "clear" in this context. Some definitions come together with theorems (i.e. they have to be proven). This is the case when you introduce some objects with their **defining property**, for which have it is at a first sight not obvious that the property ever occurs. In this case, you have to first prove its **existence**. Another prerequisite of a "clear" definition is that the defining property has to be chosen in a way, which allows to use it to uniquely identify the objects under your study. Otherwise, you could run into problems in studying the objects because they have you have been not consistent about how you should be treating these new objects.


### Criticism

The axiomatic method is very powerful as it allows to construct a complex theory from simple and (sometimes) easy to understand basic facts, called axioms. It has been very successful since about 300 B.C.E when the Greek mathematician Euclid used it for the first (historically attested) time in his famous [Elements][bookofproofs$621]. The axiomatic method has continued to be very successful over centuries and it still works very well today.

However, there are two substantial theoretical limits, known as the [Gödel's Incompleteness Theorems][bookofproofs$270]. They basically state that:

1. If we have a consistent (i.e. lacking any contradictions) theory derived from an axiom system `\(\Sigma\)`, there will always be statements, which can be formulated in this theory, which cannot be proved or disproved using this theory[^1].
2. It is impossible by means of the theory itself to prove its consistency. In other words, it is also impossible to ensure that there are no contradictions in a theory derived from its axiomatic system.

Another difficulty with the axiomatic method is that it seems to be hard (if not impossible?) to establish an axiomatic system `\(\Sigma\)` without implicitly using other axioms `\(a\notin\Sigma\)`. For instance, even the above-mentioned Gödel's Incompleteness Theorems, proving the limits to mathematical reasoning, implicitly use axioms being part of the theory they deal with - they imply that each statement has either to be true or false - known as the [axiom of excluded middle][bookofproofs$705]. Probably you will ask, why this is a problem? The problem is that since you cannot be sure that you have made all axioms you have used explicit (e.g. by completing the list of axioms you started with), you also cannot be sure that you prove statements about these axioms, i.e. making statements about the theory inside the theory. As an example, the above-mentioned Gödel's Incompleteness Theorems use the axiom of excluded middle and at the same time prove the impossibility of proving or disproving something (nothing in between is possible, according to the used axiom). Whenever a theory makes statements about itself, a logical contradiction known as [Russell's Paradox][bookofproofs$7987] is close behind.

Moreover, the above-mentioned axiom of excluded middle is only an idealization of our real-life experience (just think about statements like "I love you" or "It is 10 o'clock"). 
In addition, there are other logical systems (e.g. the [fuzzy logic][bookofproofs$157]), which successfully do without the law of excluded middle and are still consistent.

Another difficulty is the following: Let `\(T\)` be a theorem, which can be proved without contradictions in two different ways. In general, both proofs will use different axiomatic systems `\(\Sigma_1\)` and `\(\Sigma_2\)`. Now suppose, that you have a corollary `\(C\)` following from `\(T\)` (`\(T\Rightarrow C\)`). What is then the axiomatic system `\(\Sigma^*\)` necessary to prove `\(C\)`? Probably, you will say the union `\(\Sigma_1 \cup \Sigma_2\)`. However, is it possible that in this union we come up with two axioms `\(a_1\in \Sigma_1\)` and `\(a_2\in \Sigma_2\)` with `\(a_1=\neg a_2\)`?

The final difficulty is a technical one. There is no valid unified approach applying the axiomatic method in the mathematical literature. Each mathematical textbook will use its own axiomatic system (if any) and base its theorems on a different set of proofs, implicitly using non-stated axioms (see problems mentioned above). What is unique about BookofProofs is that it tries to create an overarching axiomatic system for all branches of mathematics. It will be an ongoing work in progress since mathematics is a dynamic and still developing scientific discipline.

[^1] A good later demonstration of this limit was the proof that the _continuum hypothesis_ is not provable using the current axiomatic system of set theory.