layout: section
categories: branches,logic
nodeid: bookofproofs$7899
orderid: 50
parentid: bookofproofs$7898
title: Examples of Propositions With Different Syntactic Forms but the Same Boolean Function
description: EXAMPLES OF PROPOSITIONS WITH DIFFERENT SYNTACTIC FORMS BUT THE SAME BOOLEAN FUNCTION &#9733; master graduate maths &#10004; visit BookOfProofs now!
references: bookofproofs$711,bookofproofs$7895
keywords: boolean,but,different,examples,forms,function,propositions,same,syntactic
contributors: bookofproofs


---


---

### Example 1

If `$x$` is a [Boolean variable][bookofproofs$1307] then the [disjunctions][bookofproofs$713].
Different Syntax | Same Semantics for a given [interpretation][bookofproofs$710] `$I$` | Same Boolean functions
:------------- |:------------- |:-------------
$x\neq$  |$I\models x\Leftrightarrow$ |$f_x=$
$x\vee x\neq$ |$I\models x\vee x\Leftrightarrow$ |$f_{x\vee x}=$
$x\vee x\vee x\neq$ |$I\models x\vee x\vee x\Leftrightarrow$ |$f_{x\vee x\vee x}=$ 
$x\vee x\vee x\vee x\neq$ |$I\models x\vee x\vee x\vee x\Leftrightarrow$ |$f_{x\vee x\vee x\vee x}=$ 
$\ldots$|$\ldots$|$\ldots$

are syntactically different [Boolean terms][bookofproofs$1307] (propositions), but they still have the same [semantics][bookofproofs$7871]. Therefore, by [definition of Boolean functions][bookofproofs$1316], they constitute the same Boolean function.

### Example 2

The same Boolean function might even be represented by propositions containing more than one variable. Let `$x$` and `$y$` be Boolean variables, Consider the propositions `$\phi=x$` and `$\psi=(x\wedge y)\vee y$`. These propositions have the same [truth tables][bookofproofs$7868], depending on the [semantics][bookofproofs$7871] of `$x$` and `$y$`:

 `$[[x]]_I$`| `$[[y]]_I$`| `$[[\phi]]_I$`| `$[[\psi]]_I$`
 `$1$`| `$1$`| `$1$`| `$1$`
 `$0$`| `$1$`| `$0$`| `$0$`
 `$1$`| `$0$`| `$1$`| `$1$`
 `$0$`| `$0$`| `$0$`| `$0$`

Therefore, the functions `$f_\phi$` and `$f_\psi$` are, in fact, the same Boolean function.
