layout: explanation
categories: branches,logic
nodeid: bookofproofs$558
orderid: 400
parentid: bookofproofs$184
title: When is something "well-defined" in mathematics?
description: WHEN IS SOMETHING WELL-DEFINED IN MATHEMATICS? &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$6823
keywords: any,continuous functions,defined,makes it as simple as possible,mathematics,something,well,well-defined,when,would not be valid anymore!
contributors: bookofproofs


---


---

Mathematicians are concerned about using only those objects, which are "well-defined". But what does it actually mean? 

Something is said to be *well-defined*, if its as simply described as possible and its description is definite, i.e. without any ambiguities.

### Example 1 - Definition of a Field

As an example, take the definition of a [field][bookofproofs$557].
#### Why is this definition as simple, as possible?

In any field, besides the distributivity law `\(a\cdot (b+c)=a\cdot b + a\cdot c\)` also "another" distributivity law `\((a+b)\cdot c=a\cdot c + b\cdot c\)` is valid. However, this information is not part of the field's definition, because it follows from the first distributivity law and the commutativity of its two operations `\( + \)` and `\(\cdot\)`, both __being already__ part of the definition. Avoiding this "additional" information in the description of what a field really is helps to keep its definition simple. Avoiding **any** "additional" information  without changing the meaning of the definition actually **makes it as simple as possible**.

#### Why is it definite (non-ambiguous)?

If you read the [above-mentioned definition][bookofproofs$557] carefully, you will find the distributivity law, however you will not find the commutativity of its operations explicitly mentioned in it. This is because it is mentioned indirectly by the unimposing words "abelian":

1. `\((F,+)\)` is an [abelian group][bookofproofs$553].
1. If `\(0\)` is the neutral element of `\((F,+)\)`, then `\(F^*:=(F \setminus \{0\},\cdot)\)` is an [abelian group][bookofproofs$553]If the words "abelian" were dropped from the definition of a field, i.e. if its definition would be formulated like this:

|# `\((F,+)\)` is an [group][bookofproofs$553].
1. If `\(0\)` is the neutral element of `\((F,+)\)`, then `\(F^*:=(F \setminus \{0\},\cdot)\)` is an [group][bookofproofs$553].
1. For all `\(a,b,c\in F\)` the distributivity law holds: `\(a\cdot(b+c)=a\cdot b+a\cdot c\)`.|

then it would be ambiguous, since there are also groups which are not abelian, so the operations `\(+\)` and `\(\cdot\)` would not necessarily be commutative. In an algebraic structure defined like this the "other" distributivity law `\((a+b)\cdot c=a\cdot c + b\cdot c\)` *would not be valid anymore!*


### Example 2 - Definition of Continuity

A central concept of Calculus and Analysis are **continuous functions**. Before we deal with the correct mathematical definition of a continuous function, let's take a look at a first attempt, which would be not a good definition of a limit:

> If `$f$` is a function on an open real interval containing `$a\in\mathbb R,$` then `$f$` is said to be continuous at `$a$` if the values of `$f(x)$` get closer and closer to `$f(a)$` as `$x$` approaches `$a.$`

Might you find this definition quite simple and thus to fulfill already one of the criteria of being "well-defined"?
 Okay, but how about its non-ambiguity? Well, the above definition is not definite. It is for instance not clear what "values of `$f(x)$` get closer and closer to `$y$` or what "as `$x$` approaches `$a.$`" means. Do we want to say "arbitrarily close" or "as close as one likes"? 

Whenever you try to define mathematical objects, watch out for terms, which might be misunderstood by some readers. If you find such terms, your definition is not good enough!

A "well-defined" concept of "continuous functions" can be found [here][bookofproofs$219]. Try to find out by yourself, why and by which means this definition is better than our first attempt above!
