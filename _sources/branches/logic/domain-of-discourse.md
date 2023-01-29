layout: definition
categories: branches,logic
nodeid: bookofproofs$6219
orderid: 200
parentid: bookofproofs$7873
title: Domain of Discourse
description: DOMAIN OF DISCOURSE ★ bring your math skills to the graduate level ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: 
keywords: discourse,domain,domain of discourse,universe,universe of discourse
contributors: bookofproofs

---
After defining what [truth values][bookofproofs$707] are, we will next explain, in which context it makes sense to assign a truth value to a [string][bookofproofs$708] of a given [formal language][bookofproofs$7842]. Imagine, we want to assign a truth value to the following English sentence: 

> "The equation `$x+4 = 2$` has always a solution." 

Remember, that we are now at the model level of our study and this sentence is up to now a string of some formal language without any meaning. If we want to construct a logical calculus, in which we can assign a truth value to this string, we have to pay attention to the context, in which we do so. Otherwise, our assignment might be ambiguous. For instance, if the context is [integers][bookofproofs$844], and our logical calculus is laying out the corresponding theory, then our logical calculus should be able to assign the value __true__ to this string because the integer `\(x = -2\)` is a solution. But if the context is [natural numbers][bookofproofs$718], then the string is __false__, since there is no such natural number `$x$`, for which `$x+4=2$`. 
 
The context, in which we are studying the logic of given strings is known as the __domain of discourse__. Now, we will define it formally:

---

A **domain of discourse** (also called **universe of discourse** or just **universe**) is a non-empty [universal set][bookofproofs$7984] `$U$`, in which we study a given [formal language][bookofproofs$94] `\(L\subseteq (\Sigma^*,\cdot) \)` over an [alphabet][bookofproofs$708] `\(\Sigma\)`.
