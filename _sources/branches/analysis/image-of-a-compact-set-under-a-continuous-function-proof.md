layout: proof
categories: branches,analysis
nodeid: bookofproofs$6601
orderid: 50
parentid: bookofproofs$143
title: 
description:  Proof of IMAGE OF A COMPACT SET UNDER A CONTINUOUS FUNCTION &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$582
keywords: compact,continuous,function,image,set,under,proof
contributors: bookofproofs

---


---

* Let `\(X,Y\)` be [metric spaces][bookofproofs$617].
* Let `$f:X\mapsto Y$` a [continuous function][bookofproofs$1205].
* Let `\(C\subset X\)` be a [compact][bookofproofs$6575] subset of `$X$`.
* We have to show that the [image][bookofproofs$592] `\(f( C)\subset Y\)` is also compact.
   * Let `$(U_i)_{i\in I}$` be an [open cover][bookofproofs$150] of `$f( C)$`.
   * Because `$f$` is continuous, it follows from the [definition of continuity using open sets][bookofproofs$6195] that the [inverse images][bookofproofs$592] `$V_i:=f^{-1}(U)$` are open in `$X$`.
   * Thus, `$(V_i)_{i\in I}$` be an [open cover][bookofproofs$150] of `$C$`.
   * Since `$C$` is [compact][bookofproofs$6575], there is a [finite subcover][bookofproofs$6575] `$V_{i_1}\cup V_{i_2}\cup \ldots \cup V_{i_n}\supset C$`.
   * It follows that `$U_{i_1}\cup U_{i_2}\cup \ldots \cup U_{i_n}\supset f( C)$`.
   * This means that `$f( C)$` has a [finite subcover][bookofproofs$6575] in `$Y$`.
   * This means that `$f( C)$` is [compact][bookofproofs$6575] in `$Y$`.
