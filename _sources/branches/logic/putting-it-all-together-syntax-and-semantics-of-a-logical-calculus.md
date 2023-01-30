layout: chapter
categories: branches,logic
nodeid: bookofproofs$7884
orderid: 50
parentid: bookofproofs$113
title: Putting it All Together - Syntax and Semantics of a Logical Calculus
description: SYNTAX AND SEMANTICS OF A LOGICAL CALCULUS ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$656,bookofproofs$7878
keywords: syntax and semantics of a logical calculus
contributors: bookofproofs

---


---

The goal of the [basic concepts][bookofproofs$26] introduced so far was to link the syntactical and the semantic levels of a formal language. The following figure demonstrates these two levels:


![syntaxsemantics](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/syntaxsemantics.png?raw=true)


The advantage of the [derivability property][bookofproofs$7883] "`$\vdash$`" is that it is defined in a way capable for automation. 
Even a machine, (we have called the [proving machine][bookofproofs$7875] __PM__) would be able to derive one [string][bookofproofs$708] from another formally (i.e. in a [formal language][bookofproofs$94] `$L$`), 
according to its [syntax][bookofproofs$709] and the defined [rules of inference][bookofproofs$7877].

The disadvantage of the derivability property "`$\vdash$`" is that it only operates on strings without any meaning. 
But we want to construct a [logical calculus][bookofproofs$7882] to be able to derive true statements about a universe `$U$`,
we call the [domain of discourse][bookofproofs$6219]. This is where interpretation `$I(U,L)$` comes into play with its [valuation][bookofproofs$7874] function `$[[]]_I$`. 

Ideally, our logical calculus should fulfill some desirable properties:

* From `$\vdash g$` we should always be able to conclude `$\models g$`, i.e.  whenever we are able to [derive][bookofproofs$7883] a formula `$g$` __syntactically__, it should also follow __semantically__ - i.e. be a [valid][bookofproofs$7880] statement about our universe. 
* From  `$\models g$` we should always be able to conclude `$\vdash g$`, i.e. every valid statement `$g$` should be also derivable.
* If we are able to derive `$g$`, we should never be able to derive its negation `$\neg g$`.
* If we are not able to derive the negation `$\neg g$`, we should always be able to derive `$g$`.

Now, we will introduce these desirable properties of a logical calculus as formal definitions.
