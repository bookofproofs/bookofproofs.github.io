layout: explanation
categories: branches,set-theory
nodeid: bookofproofs$8632
orderid: 1100
parentid: bookofproofs$112
title: Building the Successors of Ordinal Numbers
description: BUILDING THE SUCCESSORS OF ORDINAL NUMBERS ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$656
keywords: building the successors of ordinal numbers
contributors: bookofproofs

---


---

### Finite Ordinal Numbers

Given an ordinal `$\alpha$`, we can use the formula to build the [successor of an ordinal number][bookofproofs$774] to create a fascinating [chain][bookofproofs$7998] of ordered ordinals.

We start with finite ordinals, i.e. the [natural numbers][bookofproofs$718].
`$$\begin{array}{rcl}0&:=&\{\emptyset\}\\
1&:=&0\cup\{0\}\\
2&:=&1\cup\{1\}\\
&\vdots&\\
\end{array}$$`

This way, we will come up with the set of all finite ordinals (i.e. natural numbers), which we want to denote by `$$\omega=\{0,1,2,\ldots\}.$$` 


![ordinal1](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/ordinal1.png?raw=true)


### Countably Infinite Ordinal Numbers
 `$\omega$` can be perceived as the [supremum][bookofproofs$7995] of all finite natural numbers `$$\omega=\sup\{k\mid k\in\mathbb N\}.$$` `$\omega$` has [infinitely many][bookofproofs$985] elements, however only [countably many][bookofproofs$772] infinitely many. Moreover, `$\omega$` is the first [limit ordinal][bookofproofs$780], since it has no direct predecessor, although it is greater than all of its predecessors. 

Now, we can continue to create the successor of `$\omega$` by setting 

`$$\begin{array}{rcl}\omega+1&:=&\omega\cup\{\omega\}\\
\omega+2&:=&\omega+1\cup\{\omega+1\}\\
&\vdots&\\
\end{array}$$`

We can continue this process to create again an [infinite][bookofproofs$985], but [countable][bookofproofs$772] number of consecutive successors, until we reach the set `$$\omega+\omega=2\omega:=\{0,1,2,3,4,\ldots,\omega,\omega+1,\omega+2,\omega+3,\omega+4,\ldots\},$$` which is the second [limit ordinal][bookofproofs$780] without a direct predecessor. 


![ordinal1](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/ordinal1.png?raw=true)


![ordinal2](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/ordinal2.png?raw=true)


But wait, we can continue the process of finding new limit ordinals `$k\omega$`, `$k\in\mathbb \omega$` infinitely (but only countably many) times once again to get a new limit ordinal, for which there is no direct predecessor, 

`$$\omega\cdot\omega=\omega^2:=\sup\{k\omega\mid k\in\omega\}$$` 


![ordinal1](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/ordinal1.png?raw=true)


![ordinal2](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/ordinal2.png?raw=true)


![ordinal3](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/ordinal3.png?raw=true)


We can continue the process of building consecutive ordinal numbers even further. Now, starting with `$\omega^2+1:=\omega^2\cup\{\omega^2\},$` leading to the limit ordinals `$\omega+k\omega$`, for all `$k\in\omega.$` It is now clear that the supremum of all theses sets is the set `$2\omega^2.$` It should be also clear, how this process can be continued until we reach further limit ordinals `$$\begin{array}{rcl}\omega\omega^2&=&\omega^3,\\ \omega\omega^3&=&\omega^4,\\\omega\omega^4&=&\omega^5,\\ &\vdots\end{array}.$$` 

### Uncountably Infinite Ordinal Numbers

Now, we have to hold on. The new limit ordinal would be `$\omega ^\omega,$` which is defined as the following [supremum][bookofproofs$7995]: 

`$$\omega^\omega=\sup\{\omega^k\mid k\in\omega\}.$$` 

The special thing about this `$\omega ^\omega$` is that it is the first limit ordinal which has [uncountably many][bookofproofs$772] elements, although all of its predecessors have only countably many elements! The proof of this claim is similar to the proof that the [set of real numbers is uncountable][bookofproofs$6661], using a diagonal argument. 

The counting of ordinals we have done so far up to `$\omega^\omega$` was a **transfinite** one. Each time we have created a new limit ordinal, we have conducted mentally a transition to a new infinite limit. It is, however hard to imagine and even to visualize the transfinite counting process up to `$\omega^\omega.$` Note that above we only provided figures up to `$\omega^2.$` The unimaginable transfinite counting process up to `$\omega^\omega$` can be formulated as follows:

> In each of the countably infinitely many steps, we have counted a countably infinite set countably infinitely many times.

But this process can be continued even further, ad infinitum. The next limit numbers are (these are just a few examples) `$$\begin{align}
\omega^\omega +1, \ldots, \omega^\omega +k,\ldots, \omega^\omega +k\omega,\ldots,\nonumber\\
\omega^\omega +k\omega^2,\ldots,k\omega^\omega,\ldots,\omega^{\omega +k},\ldots,\nonumber\\
\omega^{k\omega},\ldots,\omega^{\omega^{\omega}},\ldots,\omega^{\omega^{\omega^{\omega}}},\ldots,\omega^{\omega^{\omega^{\omega^{\omega}}}},\ldots\nonumber\\
\end{align}$$`

Now, let us denote by `$\omega^{\uparrow k}$` the ordinal number, in which `$k$` times we reach a new exponent power, i.e. `$\omega^\omega=\omega^{\uparrow 1},$` `$\omega^{\omega^{\omega}}=\omega^{\uparrow 2},$` `$\omega^{\omega^{\omega^{\omega}}}=\omega^{\uparrow 3},$` etc.  These all are only countably many new limit numbers with uncountably many elements.  Therefore, a new interesting question arises: Is there a transfinite number such that it is the limit number `$$\Omega:=\sup\{\omega^{\uparrow k}\mid k\in\omega\}?$$`

It turns out that there is no such ordinal number `$\Omega,$` its existence would cause a [contradiction][bookofproofs$744], which became known as the [Burali-Forti paradox][bookofproofs$779].