layout: proof
categories: branches,set-theory
nodeid: bookofproofs$8057
orderid: 50
parentid: bookofproofs$8056
title: 
description:  Proof of ANY SET IS SUBSET OF SOME TRANSITIVE SET - ITS TRANSITIVE HULL &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$8055
keywords: any,hull,its,set,some,subset,transitive,proof
contributors: bookofproofs


---


---

* For a given [set][bookofproofs$550] `$X,$`  construct a set `$Y$` as follows: `$$Y:=\bigcup\{ y_n \mid n\in\mathbb N  \}$$` with the elements `$y_n$` being sets recursively defined by `$y_0:=X,$` `$y_{n+1}:=\bigcup y_n.$`[^1]  
* `$X$` is [subset][bookofproofs$552] of `$Y$` by construction, since `$X=y_0\subset Y.$`
* It remains to be shown that `$Y$` is [transitive][bookofproofs$720]:
   * Let `$w\in Y.$`
   * It follows that `$w\in y_n$` for some `$n\in\mathbb N.$`
   * Let `$u\in w$`. 
   * It follows `$u\in \bigcup y_n.$`
   * By definition `$u\in y_{n+1},$` and `$u\in Y.$`
   * Therefore `$w\subseteq Y.$`
   * This means that `$Y$` is transitive.

[^1]: For the `$\bigcup$` notation see "axiom of union":https://www.bookofproofs.org/branches/axiom-of-union-ernst/.
