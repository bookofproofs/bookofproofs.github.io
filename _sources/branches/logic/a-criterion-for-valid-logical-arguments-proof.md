layout: proof
categories: branches,logic
nodeid: bookofproofs$7916
orderid: 50
parentid: bookofproofs$7915
title: 
description:  Proof of A CRITERION FOR VALID LOGICAL ARGUMENTS &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$6823,bookofproofs$7838
keywords: a criterion for valid logical arguments,proof
contributors: bookofproofs

---


---

[If and only if" means that we have to show both implications "$\Rightarrow$" and "$\Leftarrow$" of the above lemma. Assume, our "logical argument][bookofproofs$7913], which we will call "$\phi$" below, consist of the premises `$p_1,\ldots,p_n$` and the conclusion `$q$`.


### "$\Rightarrow$"

* Suppose that `$\phi$` is a [valid logical argument][bookofproofs$7913].
* Then, by definition a valid logical argument, the conclusion `$q$` is true whenever all the premises  `$p_1,\ldots,p_n$` are simultaneously true, i.e. `$$\text{ if }([[p_1]]_I=1\text{ and },\ldots,\text{ and }[[p_n]]_I=1),\text{ then } [[q]]_I=1$$` for all interpretations `$I$`.
* It follows from the [truth table of the conjunction][bookofproofs$712] that `$x=p_1\wedge,\ldots,\wedge p_n$` will be valued true: `$[[x]]_I=1.$`
* Furthermore, it follows from the [truth table of the implication][bookofproofs$1304] that if any other proposition `$y$` is valued true `$[[y]]_I=1,$`  then the implication `$x\Rightarrow y$` is also valued true:  `$[[x\Rightarrow y]]_I=1.$`
* In our case, `$x\Rightarrow q$` and `$q$` is true by assumtion. Therefore, the proposition `$x\Rightarrow q$` is always valued true.
* Thus, `$(p_1\wedge\ldots\wedge p_n)\Rightarrow q$` is a [tautology][bookofproofs$7880].
### "$\Leftarrow$"

* Conversely, suppose that `$(p_1\wedge\ldots\wedge p_n)\Rightarrow q$` is a [tautology][bookofproofs$7880], but the `$\phi$` is [fallacy][bookofproofs$7913].
* This would mean that `$q$` is false, even though  the premises `$p_1,\ldots,p_n$` are all true.
* With the above notation this means that `$q$` is false, even though `$x=(p_1\wedge\ldots\wedge p_n)$` is true.
* From the truth table of implication, it follows that `$x\Rightarrow q$` is false.
* But in this case, `$(p_1\wedge\ldots\wedge p_n)\Rightarrow q$` cannot be a [tautology][bookofproofs$7880], which is a [contradiction][bookofproofs$744].
* Therefore, `$\phi$` is not a [fallacy][bookofproofs$7913], but it must be a [valid logical argument][bookofproofs$7913].
