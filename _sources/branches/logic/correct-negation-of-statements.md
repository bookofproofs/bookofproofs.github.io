layout: explanation
categories: branches,logic
nodeid: bookofproofs$6878
orderid: 600
parentid: bookofproofs$184
title: Correct Negation of Statements
description: CORRECT NEGATION OF STATEMENTS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$6823
keywords: correct,example 1,example 2,example 3,example 4,negated example 1,negated example 2,negated example 3,negated example 4,negation,statements
contributors: bookofproofs

---


---

When proving mathematical theorems, one has quite often to [negate][bookofproofs$714] different kind of [propositions][bookofproofs$710]. The logic of negating propositions is not hard to follow and depends on the type of proposition to negate. The following list gives some examples of propositions types and provides rules to follow when negating them. 

### Negating Conditional Propositions

A [conditional proposition][bookofproofs$1304] is a proposition of the type `$P\Rightarrow Q$`, where `$P,Q$` are themselves propositions. 

> **Example 1**: `$P:=$`"It is raining", `$Q:=$`"The roads are wet.", `$P\Rightarrow Q:$`"If it is raining, then the roads are wet."

> **Example 2**: `$P:=$`"$a$ is even", `$Q:=$`"$a\cdot b$ is even for all `$b\in\mathbb N$`", `$P\Rightarrow Q:$`"If `$a$` is even, then `$a\cdot b$` is even for all `$b\in\mathbb N$`."

The correct negation of such statements is proven [here][bookofproofs$6876] and follows these steps:

1. Negate `$Q$` (i.e. get `$\neg Q$`).
1. Conjugate `$P$` and the negated `$\neq Q$`, i.e. build `$P\wedge \neq Q$`.

> **Negated example 1**: `$P:=$`"It is raining", `$\neg Q:=$`"The roads are dry.", `$\neg (P\Rightarrow Q)=(P\wedge \neg Q):$`"It is raining and the roads are dry."

> **Negated example 2**: `$P:=$`"$a$ is even", `$\neg Q:=$`"there exists a `$b\in\mathbb N$`, for which `$a\cdot b$` is odd"[^1], `$\neg (P\Rightarrow Q)=(P\wedge \neg Q):$`"$a$ is even and there exists a `$b\in\mathbb N$`, for which `$a\cdot b$` is odd."

### Negating Existential and Universal Quantifiers

Many statements use the [existential and universal quantifiers][bookofproofs$6221] `$\exists$` ("there exists") and `$\forall$` ("for all"). For instance, consider the following examples:

> **Example 3**: `$P:=$`"All cars have their own maximal velocity, but you can find a suitable trailer which can be pulled by them."

> **Example 4**: `$P:=$`"There exists a real number `$y$` such that for all `$\epsilon > 0$` there exists `$\delta > 0$` such that for every `$x$` with `$0 < |x-a| < \delta$` implies `$|f(x)-y| < \epsilon.$`"

The correct negation of such statements follows these rules:

1. The negation of "for every `$y$`, `$P(y)$`" says that `$P(y)$` is true for every possible value of `$y$`. The negation of it must be that it is false that every value of `$y$` makes `$P(y)$` true, so there must be at least one `$y$` which makes `$P(y)$` a false statement. In other words, to negate a universal quantifier, change it to an existential quantifier and negate the statement that follows, formally `$$\neg(\forall y:\;P(y))=(\exists y:\;\neg P(y)).$$`
1. The negation of "there exists `$y$`, `$P(y)$`" says there is a value of `$y$` which makes `$P(y)$` a true statement. The negation of it must be that it is false that there is any value of `$y$` which makes `$P(y)$` true, so all values of `$y$` must make `$P(y)$` a false statement. In other words, to negate an existential quantifier, change it to a universal quantifier and negate the statement that follows, formally `$$\neg(\exists y:\;P(y))=(\forall y:\;\neg P(y)).$$`

> **Negated example 3**: `$\neg P:=$`"There is at least one car with a maximal velocity, such that, whatever trailer you take, you cannot pull it by the car."

> **Negated example 4**: `$\neg P:=$`"For all real numbers `$y$` there exists `$\epsilon > 0$` such that for all `$\delta > 0$` there exists `$x$` with `$0 < |x-a| < \delta$` and `$|f(x)-y| \ge \epsilon.$`"[^2]


[^1]: Not that the quantifier "for all `$b\in\mathbb N$`" has also to be negated - see examples 3 and 4.

[^1]: Note the negation of the implication "$0 < |x-a| < \delta$ implies `$|f(x)-y| \ge \epsilon$`", as explained  in examples 1 and 2.
