layout: example
categories: branches,logic
nodeid: bookofproofs$7846
orderid: 50
parentid: bookofproofs$710
title: Examples of Propositions With a More Complex Syntax
description: EXAMPLES OF PROPOSITIONS WITH A MORE COMPLEX SYNTAX &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$593,bookofproofs$7838
keywords: complex,examples,more,propositions,syntax
contributors: bookofproofs

---


---

We  have introduced a special case for the [syntax of `$PL0$`][bookofproofs$1307] as propositions corresponding to Boolean terms. Let us recall the examples of Boolean terms we have considered as `$PL0$` so far:

* `$x$`,
* `$(x)$`,
* `$\neg a$`,
* `\((\neg(\neg y))\)`,
* `\(((x\Rightarrow(y\vee(1\wedge(\neg w))))\wedge 0)\)`, 
* `\(((a\Leftrightarrow b)\vee(0\Rightarrow y))\)`

However, the [Law of Excluded Middle][bookofproofs$710] also holds for any kind of more complex syntax, in which we allow the two-valued interpretation of `$PL0$`.

Let us first discuss some less formal example - the example of spoken human language (like English).

* Interrogative statements like [Are you his uncle?" or imperative statements like "Report to the colonel's office!" are syntactically correct statements of English language but are not "propositions][bookofproofs$710], because no truth value can be assigned to them. 
* The truth value of a proposition can depend on the person making the judgment or on the time and circumstances in which the statement was made. For instance, "I'm cold" would mean something completely different when a child in winter says it, or when Socrates (who drank a poison by his hand) says it in the moment of his death. 
* "He enjoys mathematics." is not a proposition, since the pronoun "he" prevents us from being able to decide whether the sentence is true or false.
* "Socrates was a man" is a proposition, since we can decide that the sentence is true.

Now, let us discuss some more formal examples - the example invoking the formal language of equations:

* "`$1=0$`" is a proposition since we assign the truth value "false" to it.
* "`$1=1+0$`" is a proposition since we assign the truth value "true" to it.
* "`$x+2=5$`" is not a proposition because the value of `$x$` is not defined. If we said "`$x+2=5$`" where "`$x=2$`", then it would be a proposition, since we can state that it is false.
