layout: explanation
categories: branches,set-theory
nodeid: bookofproofs$8004
orderid: 100
parentid: bookofproofs$294
title: How Functions interact with Set Operations
description: HOW FUNCTIONS INTERACT WITH SET OPERATIONS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$979,bookofproofs$1038
keywords: functions,how,interact,operations,set
contributors: bookofproofs

---


---

In the above [lemma][bookofproofs$294], the rules `$2, 5,7$` and `$8$` do not allow equality in the general case. The proof given for the lemma is simple but highly technical and it might be interesting to see a counterexample. Such a counterexample is given below.


![examplesetopsfunction](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/examplesetopsfunction.png?raw=true)


In the figure, a function `$f:A\mapsto A$` is defined and where we set `$X:=\{u\}$` and `$Y:=\{w\}.$` We calculate the above rules to see that, indeed, no equality can be achieved:

* Rule `$2$`: Assume equality `$f[X\cap Y] = f[X]\cap f[Y]$` for all `$X,Y\subseteq A.$` This cannot be true since `$f[A\cap B]=f[\emptyset]=\emptyset$` on the one side of the equation and `$f[X]\cap f[Y]=\{u\}\cap \{u\}=\{u\}$` on the other.
* Rule `$5$`: Assume equality `$f[A\setminus X]= f[A]\setminus f[X]$` for all `$X \subseteq A.$` This cannot be true since `$f[A\setminus X]=f[\{w\}]=\{u\}$`  on the one side of the equation and  `$f[A]\setminus f[X]=\{u\}\setminus\{u\}=\emptyset$` on the other.
* Rule `$7$`: Assume equality `$f^{-1}[f[X]]=X$` for all `$X\subseteq A.$` This cannot be true since `$f^{-1}[f[X]]=f^{-1}[\{u\}]=\{u,w\}=A$`  on the one side of the equation and  `$X\subset A$` (proper [subset][bookofproofs$552]) on the other.
* Rule `$8$`: Assume equality `$f[f^{-1}[X]]=X$` for all `$X\subseteq B.$` This cannot be true since if we choose `$X=\{w\}$`, then `$f[f^{-1}[X]]=f[\emptyset]=\emptyset$` on the one side of the equation and  `$X=\{w\}$` on the other.
