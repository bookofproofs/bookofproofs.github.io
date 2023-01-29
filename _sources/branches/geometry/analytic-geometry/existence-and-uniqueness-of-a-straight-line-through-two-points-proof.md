layout: proof
categories: branches,geometry,analytic-geometry
nodeid: bookofproofs$7965
orderid: 50
parentid: bookofproofs$7964
title: 
description:  Proof of EXISTENCE AND UNIQUENESS OF A STRAIGHT LINE THROUGH TWO POINTS &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: 
keywords: existence,line,points,straight,through,two,uniqueness,proof
contributors: bookofproofs

---


---

* By hypothesis, `$A, B$` are points of an `$n$`-dimensional [number space][bookofproofs$7959] `$\mathbb R^n$` with `$A\neq B.$`
* "Existence":
   * Let `$O$` be the origin of `$\mathbb R^n.$`
   * Then we can [describe a straight line using the vectors][bookofproofs$7961] as the set `$$L:=\{P\in \mathbb R^n:\; \overrightarrow{OP}:=\overrightarrow{OA}+t\cdot \overrightarrow{AB}\}.$$`
   * Obviously, for `$t=0,$` `$A\in L,$` and for `$t=1,$` `$B\in L.$`
   * Thus, there is at least one straight line through `$A$` and `$B.$`
* "Uniqueness":
   * Let `$C, B$` be two points of an `$n$`-dimensional [number space][bookofproofs$7959] `$\mathbb R^n$` with `$C\neq D$`.
   * Assume, `$L':=\{Q\in \mathbb R^n:\; \overrightarrow{OQ}:=\overrightarrow{OC}+t\cdot \overrightarrow{CD}\}$` is a [straight line  described by these points][bookofproofs$7961] containing also the points `$A$` and `$B.$`
   * Thus, since `$A\in L',$` there exists a `$t_A\in\mathbb R$` with `$\overrightarrow{OA}=\overrightarrow{OC}+t_A\cdot\overrightarrow{CD}.$`
   * Similarly, since `$B\in L',$` there exists a `$t_B\in\mathbb R$` with `$\overrightarrow{OB}=\overrightarrow{OC}+t_B\cdot\overrightarrow{CD}.$`
   * The difference of both last equations gives us `$\overrightarrow{AB}=(t_B-t_A)\cdot\overrightarrow{CB}.$`
   * We have `$(t_B-t_A)\neq 0,$` because `$A\neq B$` by hypothesis.
   * Altogether, we have found that `$A\in L'$` and that `$\overrightarrow{AB}=c\cdot\overrightarrow{CB}$` for some constant `$0\neq c\in \mathbb R.$`
   * This means by the [lemma about equivalence of different descriptions of a straight line using two vectors][bookofproofs$7962] that `$L'=L.$`
   * Thus, there is at most one straight line through `$A$` and `$B.$`
