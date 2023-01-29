layout: definition
categories: branches,logic
nodeid: bookofproofs$7880
orderid: 500
parentid: bookofproofs$26
title: Satisfaction Relation, Model, Tautology, Contradiction
description: SATISFACTION RELATION, MODEL, TAUTOLOGY, CONTRADICTION ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: 
keywords: contradiction,model,relation,satisfaction,tautology,satisfaction relation
contributors: bookofproofs

---


---

Let `\(L\subseteq (\Sigma^*,\cdot) \)` be a [formal language][bookofproofs$94] with [strings][bookofproofs$708] `$s\in L$` formed according to a [syntax][bookofproofs$709] and let inside a [domain of discourse][bookofproofs$6219] `$U,$` a [semantics][bookofproofs$7874] `$I(U,L)$`, and the valuation `$[[]]_I$` be given. 

### Tautology

We say that the [interpretation][bookofproofs$7874]  `$I(U,L)$` **satisfies**  **models**, is  **a model of**) an [interpretable][bookofproofs$7874] string `$s\in L$`, denoted by `$$I\models s,$$` if and only if the corresponding [valuation][bookofproofs$7874] is true, i.e.`$$[[s]]_I=1.$$`
If `$I\models s$` for all possible interpretations `$I$`, then we write `$\models s$` and say that `$s$` is **valid**. Alternatively, we call `$s$` a **tautology**.

### Contradiction

We say that the [interpretation][bookofproofs$7874]  `$I(U,L)$` **does not satisfy**  **does not model**) an [interpretable][bookofproofs$7874] string `$s\in L$`, denoted by `$$I\not{\models} s,$$` if and only if the corresponding [valuation][bookofproofs$7874] is false, i.e.`$$[[s]]_I=0.$$`
If `$I\not {\models} s$` for all possible interpretations `$I$`, then we write `$\not{\models} s$` and say that `$s$` is **invalid**. Alternatively, we call `$s$` a **contradiction**.
