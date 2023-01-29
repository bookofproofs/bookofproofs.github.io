layout: definition
categories: branches,logic
nodeid: bookofproofs$7874
orderid: 300
parentid: bookofproofs$7873
title: Interpretation of Strings of a Formal Language and Their Truth Function
description: INTERPRETATION OF STRINGS OF A FORMAL LANGUAGE AND THEIR TRUTH FUNCTION &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: 
keywords: interpretation,truth function,interpretations,truth functions,interpret
contributors: bookofproofs


---
Now, we are ready to explain, what it means to logically _interpret_ a [word][bookofproofs$708] of a [formal language][bookofproofs$94]. We are able to provide a first strict definition of the concept of logical _interpretation_. Later, when we will be discussing special types of logic, including the [propositional logic][bookofproofs$66], the [first-order][bookofproofs$186] and [higher-order predicate logics][bookofproofs$207], we will need some customized definitions of _interpretations_, more precisely serving specific purposes of each case.

For the time being, it is sufficient to understand that an _interpretation_ inside a logical system is a rule assigning truth values to the strings of the underlying formal language.

---

Let `\(L\subseteq (\Sigma^*,\cdot) \)` be a [formal language][bookofproofs$94] in a given [domain of discourse][bookofproofs$6219] `$U$`. The **interpretation** `$I$` is an appropriate [partial function][bookofproofs$592]  `$I: L\subset \to \mathbb B$`, `$s\to I(s)$`,  depending on `$L$` and `$U$`. 

In other words, given such an appropriate `$I$`, for any string `$s\in L$`, the value of the function `$I(s)$` can take one of three values:

`$$I(s):=\cases{1,&\text{if }s\text{ is interpreted as being “true”,}\\ 
0,&\text{if }s\text{ is interpreted as being “false”,}\\ 
undefined,&\text{if }s\text{ neither can be interpreted as being “true” or “false”.}}$$`


### Insights worth mentioning

* Please note that, in general, not all strings `$s\in L$` can be interpreted, even though they are syntactically correct. In this case, they either have no meaning or do have a meaning but no truth value can be assigned to them. We will learn examples of such strings later on.
* Note also that the __truth__ of strings is always a matter of the choice of the specific function `$I$`. It means that logical systems do not support any kind of "absolute, objective interpretation". For instance, the same string `$s$` can be true in one interpretation, false in another or no interpretation might be possible in yet another interpretation.
