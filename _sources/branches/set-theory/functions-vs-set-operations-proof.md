layout: proof
categories: branches,set-theory
nodeid: bookofproofs$8003
orderid: 50
parentid: bookofproofs$294
title: 
description:  Proof of BEHAVIOR OF FUNCTIONS WITH SET OPERATIONS &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$979,bookofproofs$1038
keywords: functions,operations,set,proof
contributors: bookofproofs


---


---

In the following, `$A,B$` denote [sets][bookofproofs$550], between which a [function][bookofproofs$592] `$f:A\mapsto B$` be defined.

### Ad `$(1)$` 


`$y\in f[X\cup Y]$` | `$\Leftrightarrow$` | <. `$\exists x:(x\in X\cup Y\wedge y=f(x))$` | definition of [image][bookofproofs$592].
:------------- |:------------- |:------------- |:-------------
| `$\Leftrightarrow$`|<. `$\exists x:((x\in X\vee x\in  Y)\wedge y=f(x))$`| definition of [set union][bookofproofs$6827].
| `$\Leftrightarrow$`|<. `$(\exists x:(x\in X \wedge y=f(x)))\vee (\exists x:(x\in Y \wedge y=f(x)))$`| definition of [set union][bookofproofs$6827].
| `$\Leftrightarrow$`|<. `$\exists y:y\in f[X]\vee y\in f[Y]$`| definition of [image][bookofproofs$592].
| `$\Leftrightarrow$`|<. `$\exists y:y\in f[X]\cup f[Y]$`| definition of [set union][bookofproofs$6827].
Altogether, it follows `$f[X\cup Y]=f[X]\cup f[Y]$` for all [subsets][bookofproofs$552] of `$X,Y\subseteq A.$`

### Ad `$(2)$` 

 `$y\in f[X\cap Y]$`| `$\Leftrightarrow$`|<. `$\exists x:(x\in X\cap Y\wedge y=f(x))$`| definition of [image][bookofproofs$592].
| `$\Rightarrow$`|<. `$\exists x_1,x_2:((x_1\in X\wedge x_2\in  Y)\wedge y=f(x_1)=f(x_2))$`| definition of [set intersection][bookofproofs$6828] and because `$f$` is generally not [injective][bookofproofs$769], (thus `$x_1=x_2$` cannot be assumed).
| `$\Leftrightarrow$`|<. `$(\exists x_1:(x_1\in X \wedge y=f(x_1)))\wedge (\exists x_2:(x_2\in Y \wedge y=f(x_2)))$`| definition of [set intersection][bookofproofs$6828].
| `$\Leftrightarrow$`|<. `$\exists y:y\in f[X]\wedge y\in f[Y]$`| definition of [image][bookofproofs$592].
| `$\Leftrightarrow$`|<. `$\exists y:y\in f[X]\cap f[Y]$`| definition of [set intersection][bookofproofs$6828].
Altogether, it follows `$f[X\cap Y]\subseteq f[X]\cap f[Y]$` for all `$X,Y\subseteq A.$` Please note the difference in the second argument and in the outcome of the argumentation. 

### Ad `$(3)$` 

 `$x\in f^{-1}[X\cup Y]$`| `$\Leftrightarrow$`|<. `$\exists x:f(x)\in X\cup Y$`| definition of [inverse image][bookofproofs$592].
| `$\Leftrightarrow$`|<. `$\exists x:f(x)\in X \vee f(x)\in Y$`| definition of [set union][bookofproofs$6827].
| `$\Leftrightarrow$`|<. `$\exists x:x\in f^{-1}[X]\vee x\in f^{-1}[Y]$`| definition of [inverse image][bookofproofs$592].
| `$\Leftrightarrow$`|<. `$\exists x:x\in f^{-1}[X]\cup f^{-1}[Y]$`| definition of [set union][bookofproofs$6827].
Altogether, it follows `$f^{-1}[X\cup Y]=f^{-1}[X]\cup f^{-1}[Y]$` for all `$X,Y\subseteq B.$`

### Ad `$(4)$` 

 `$x\in f^{-1}[X\cap Y]$`| `$\Leftrightarrow$`|<. `$\exists x:f(x)\in X\cap Y$`| definition of [inverse image][bookofproofs$592].
| `$\Leftrightarrow$`|<. `$\exists x:f(x)\in X \wedge f(x)\in Y$`| definition of [set intersection][bookofproofs$6828].
| `$\Leftrightarrow$`|<. `$\exists x:x\in f^{-1}[X]\wedge x\in f^{-1}[Y]$`| definition of [inverse image][bookofproofs$592].
| `$\Leftrightarrow$`|<. `$\exists x:x\in f^{-1}[X]\cap f^{-1}[Y]$`| definition of [set intersection][bookofproofs$6828].
Altogether, it follows `$f^{-1}[X\cap Y]=f^{-1}[X]\cap f^{-1}[Y]$` for all `$X,Y\subseteq B.$`

### Ad `$(5)$` 

 `$y\in f[A]\setminus f[X]$`| `$\Leftrightarrow$`|<. `$\exists y:y\in f[A]\wedge y\not\in f[X]$`| definition of [set difference][bookofproofs$6830].
| `$\Rightarrow$`|<. `$(\exists x: x\in A\wedge f(x)=y)\wedge (\not\exists x:x\in X\wedge f(x)=y)$`| definition of [inverse image][bookofproofs$592].
| `$\Leftrightarrow$`|<. `$\exists x:x\in A\setminus X\wedge f(x)=y$`| definition of [set difference][bookofproofs$6830].
| `$\Leftrightarrow$`|<. `$\exists y:y\in f[A\setminus X]$`| definition of [inverse image][bookofproofs$592].
Altogether, it follows `$f[A\setminus X]\supseteq f[A]\setminus f[X]$` for all `$X \subseteq A.$`


### Ad `$(6)$` 

 `$x\in f^{-1}[B\setminus X]$`| `$\Leftrightarrow$`|<. `$\exists x:f(x)\in B\setminus X$`| definition of [inverse image][bookofproofs$592].
| `$\Leftrightarrow$`|<. `$\exists x:f(x)\in B\wedge f(x)\not \in X$`| definition of [set difference][bookofproofs$6830].
| `$\Leftrightarrow$`|<. `$\exists x:x\in A\wedge x\not\in f^{-1}[X]$`| definition of [inverse image][bookofproofs$592].
| `$\Leftrightarrow$`|<. `$\exists x:x\in A\setminus f^{-1}[X]$`| definition of [set difference][bookofproofs$6830].
Altogether, it follows `$f^{-1}[B\setminus X]=A\setminus f^{-1}[X]$` for all `$X\subseteq B.$`


### Ad `$(7)$` 

 `$x\in X$`| `$\Rightarrow$`|<. `$\exists x:f(x)\in f[X]$`| definition of [image][bookofproofs$592].
| `$\Leftrightarrow$`|<. `$\exists x:x\in f^{-1}[X]$`| definition of [inverse image][bookofproofs$592].
Altogether, it follows `$f^{-1}[f[X]]\supseteq X$` for all `$X\subseteq A.$`

### Ad `$(8)$` 

 `$y\in f[f^{-1}[X]]$`| `$\Rightarrow$`|<. `$\exists x:x\in f^{-1}[X]\wedge f(x)=y$`| definition of [image][bookofproofs$592].
| `$\Leftrightarrow$`|<. `$\exists x:f(x)\in X\wedge f(x)=y$`| definition of [inverse image][bookofproofs$592].
| `$\Leftrightarrow$`|<. `$\exists x:y\in X\wedge f(x)=y$`| definition of [function][bookofproofs$592].
Altogether, it follows `$f[f^{-1}[X]]\subseteq X$` for all `$X\subseteq B.$`
