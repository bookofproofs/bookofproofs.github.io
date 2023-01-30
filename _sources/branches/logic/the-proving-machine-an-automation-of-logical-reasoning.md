layout: chapter
categories: branches,logic
nodeid: bookofproofs$7875
orderid: 700
parentid: bookofproofs$26
title: The Proving Machine - an Automation of Logical Reasoning
description: THE PROVING MACHINE - AN AUTOMATION OF LOGICAL REASONING ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: 
keywords: automation of logical reasoning,proving machine
contributors: bookofproofs

---


---

The ultimate goal of the formal concepts we have introduced so far is to develop a formal system, in which it is possible to draw logical conclusions from assumptions. Humans can do so but our logical system should be capable to derive logical arguments more or less automatically, e.g. by an imaginary computer, which we will call in this section the __Proving Machine__ (__PM__). We will summarize all concepts introduced so far and check, whether we have all components necessary to get our __PM__ working.

1. First of all, our __PM__ is given an [alphabet][bookofproofs$708] of finitely many letters `$\Sigma.$` We assume that it cconcatenate the letters to strings `$s$`. In principle, the __PM__ can create infinitely many different strings `$s$` out of the alphabet `$\Sigma.$` We denote this infinite set `$\Sigma^*.$`
1. Next, from all the infinitely many strings `$s\in\Sigma^*,$` we choose only some strings and call this subset `$L\subset \Sigma^*$` a [language][bookofproofs$7842]. You can think of `$L$` as the set of all (finitely or infinitely many) words, which the __PM__ should ever be able to use.
1. To enable our __PM__ to decide, whether a given string `$s \in\Sigma^*$` belongs to a language `$L$`, we have to restrict the language to some [grammar][bookofproofs$709]. In other words, we restrict the language `$L$` to be a [formal language][bookofproofs$94]. The syntax can be compared to a computer program that enables the __PM__ to accept only strings `$s$` belonging to the language `$L$` as its input. It should reject any other input.
1. Besides, we want the __PM__ to give us answers about a set `$U$` of mathematical objects we want to study. We call `$U$` the [domain of discourse][bookofproofs$6219] `$U$` is completely independent of the language `$L.$` However, we have chosen the alphabet `$\Sigma$` and the syntax in a way that the resulting language `$L$` is powerful enough to let the __PM__ give us answers about `$U.$`
1. _"Giving us answers about `$U$` in a formal language `$L$`"_ means in fact that the __PM__ should be able to prove statements formulated in `$L$` about `$U$`. Ideally, given a statement `$s\in L$` as input, the __PM__ should return us "true", if the statement is true or "false" if the statement is false. Also, if the __PM__ is not able to decide if a statement is true or false, it should return us "undefined". For this purpose, we have provided the __PM__ with two other computer programs, one we denote by `$I$`  which interprets a given string `$s$`. Once `$s$` is interpreted, the second program `$[[]]_I$`, called the "truth function" of [interpretation][bookofproofs$7874] gives us the answer, whether the interpreted string is true or false.

Are we done? You might say, in principle, yes, we are. We have constructed a __PM__, which can interpret any syntactically correct string `$s\in L,$` which we might feed it with. We might even feed it with strings representing statements about all yet unproven conjectures stated about mathematical objects in the domain of our discourse `$U$`, and the __PM__ will give us the awaited answers "true", "false" or "undefined". So are we are done with building our __PM__? Not quite.

Note that the interpretation `$I$` and its truth function `$[[]]_I$` must be very complex computer programs that somehow tell the __PM__ how to "think logically." Thus, we only have shifted the problem to another level, creating black boxes - the functions `$I$` and `$[[]]_I$`. Enabling the __PM__ to give us all the awaited answers about `$U$` means that we have to tell it __a priori__ which answers are correct and which not. 

Therefore, we will still need some tuning of the __PM__ to get it working. Maybe we need even more components? These components are [axioms][bookofproofs$7876], [rules of inference][bookofproofs$7877], and the [derivability property][bookofproofs$7883].