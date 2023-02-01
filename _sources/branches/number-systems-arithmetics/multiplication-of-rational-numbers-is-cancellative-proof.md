layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1481
orderid: 50
parentid: bookofproofs$1480
title: 
description: Proof of MULTIPLICATION OF RATIONAL NUMBERS IS CANCELLATIVE ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$696
keywords: cancellative,left cancellation property,multiplication,numbers,rational,right cancellation property,proof
contributors: bookofproofs

---


---

* Assume the equation `\(x\cdot z=y\cdot z\)` holds and that `\(z\neq 0\)`[^1]. 
* By [definition of rational numbers][bookofproofs$1033], each rational number `$x,y,z\in\mathbb Q$` is an [equivalence class][bookofproofs$7990] of [ordered pairs][bookofproofs$747] of some [integers][bookofproofs$844] `\(a,b,c,d,e,f\in\mathbb Z\)`, with `\(b\neq 0,d\neq 0,f\neq 0\)`[^2] and `$x=\frac ab,$` `$y=\frac cd,$` and `$z=\frac ef.$`
* It follows by [definition of multiplying rational numbers][bookofproofs$1475] `$$x\cdot z=y\cdot z \Leftrightarrow \frac {ae}{bf}=\frac {ce}{df}.$$`
* Again, by definition of rational numbers `$$\Leftrightarrow (ae)(df)=(ce)(bf).$$`  
* By [associativity law for multiplying integers][bookofproofs$1450] `$$\Leftrightarrow aedf=cebf.$$` 
* By [commutativity law for multiplying integers][bookofproofs$1448] `$$\Leftrightarrow adef=cbef.$$` 
* By [cancellation law for multiplying integers][bookofproofs$1464], where `$ef\neq 0$`, since `$z\neq 0$`, by hypothesis, `$$\Leftrightarrow ad=cb.$$` 
* By definition of rational numbers `$$\Leftrightarrow \frac ab=\frac cd\Leftrightarrow x=y.$$` 
* The above arguments show the right cancellation property.
* Because the [multiplication of rational numbers is commutative][bookofproofs$1478], the left cancellation property follows immediately. 
* Altogether, we have shown that the multiplication of rational numbers is [cancellative][bookofproofs$837]: `$$x\cdot z=y\cdot z\Longleftrightarrow x=y,$$` for all `$x,y,z\in\mathbb Q$` with `$z\neq 0.$`

[^1]: Here, the symbol "`$0$`" denotes the [zero][bookofproofs$1684] defined for rational numbers.

[^2]: Here, the symbol "`$0$`" denotes the [zero][bookofproofs$1682] defined for integers.
