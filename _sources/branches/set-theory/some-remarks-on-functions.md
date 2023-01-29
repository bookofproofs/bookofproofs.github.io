layout: explanation
categories: branches,set-theory
nodeid: bookofproofs$266
orderid: 100
parentid: bookofproofs$64
title: Some Remarks on Functions
description: SOME REMARKS ON FUNCTIONS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: 
keywords: caution,functions,remarks,some
contributors: bookofproofs

---


---

We want to visualize the introduced concepts on an example. The function `$f:A\mapsto B$` maps the elements of the set `$A$` 
into the elements of the set `$B$`. It is [left-total][bookofproofs$1308], since all elements `$x_1,x_2,x_3,x_4` of `$A$` are mapped. 
It is [right-unique][bookofproofs$1308], since every `$x\in A$` has only one value `$f(x)\in B$`. 


![function](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/function.png?raw=true)


As the figure shows, it is not necessary for a function to be [right-total][bookofproofs$1308], since not all elements of `$B$` have to be values of some elements of `$A$`: In the example, `$y_2,y_4$` and `$y_5$` are not contained in the [image][bookofproofs$592] `$f[A]$`. In general, the [image][bookofproofs$592] `$f[A]$` is a  [proper subset][bookofproofs$552] of but not equal `$B$` (in formulae `$f[A]\subset B$` but `$f[A]\neq B$`). 

Moreover, a function is in general, not [left-unique][bookofproofs$1308], i.e. the values in `$B$` have not to be different for different elements in `$A$`. For instance, `$f(x_3)=f(x_4)$`. For this reason, the [fiber][bookofproofs$592] `$f^{-1}(y_r)$` contains two elements `$x_3,x_4\in A.$`. 

*Caution*: The fiber `$f^{-1}$` is not a function, it is only a notation for a special set. There are other mathematical objects with the same notation. Usually, [inverse functions][bookofproofs$407] and the function `\(x\mapsto \frac1{f(x)}\)` which we will learn about later, are also denoted by `$f^{-1}$`. You must be careful not to confuse these concepts.
