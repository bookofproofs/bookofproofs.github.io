layout: proof
categories: branches,geometry,analytic-geometry
nodeid: bookofproofs$7963
orderid: 50
parentid: bookofproofs$7962
title: 
description:  Proof of EQUIVALENCE OF DIFFERENT DESCRIPTIONS OF A STRAIGHT LINE USING TWO VECTORS &#9733; master graduate maths &#10004; visit BookOfProofs now!
references: 
keywords: descriptions,different,equivalence,line,straight,two,using,vectors,proof
contributors: bookofproofs

---


---

* Let `$A,B,C,D$` be points in of an `$n$`-dimensional [number space][bookofproofs$7959] `$\mathbb R^n$` with `$A\neq B$` and `$C\neq D,$` and the origin `$O\in\mathbb R^n.$` 
* "`$\Rightarrow$`": Assume, `$L_2:=\{Q\in \mathbb R^n:\; \overrightarrow{OQ}=\overrightarrow{OC}+t\cdot \overrightarrow{CD}\}$` is a [straight line][bookofproofs$7961], which equals the straight line `$L_1:=\{P\in \mathbb R^n:\; \overrightarrow{OP}=\overrightarrow{OA}+s\cdot \overrightarrow{AB}\}.$`
   * Let `$C\in L_2.$`
   * Since `$L_2=L_1$`, we have trivially then `$C\in L_1.$`
   * This means that `$\overrightarrow{OC}=\overrightarrow{OA}+s_0\cdot \overrightarrow{AB}$` for some `$s_0\in\mathbb R.$` 
   * Moreover, there is an `$s_1\in\mathbb R$` with `$\overrightarrow{OC}+\overrightarrow{CD}=\overrightarrow{OA}+s_1\cdot \overrightarrow{AB}.$`
   * Subtracting the first equation from the second gives us `$\overrightarrow{CD}=(s_1-s_0)\cdot \overrightarrow{AB}.$` 
   * Set `$c:=(s_1-s_0).$`  We have `$c\neq 0$` (otherwise we would have `$\overrightarrow{OC}=\overrightarrow{OC}+\overrightarrow{CD},$` which would mean `$\overrightarrow {CD}=\overrightarrow{OO},$` or `$C=D,$` but this case has been excluded.
*  "`$\Leftarrow$`": Now, assume that  `$C\in L_1$` and `$\overrightarrow{CD}=c\cdot  \overrightarrow{AB}$` with `$0\neq c\in \mathbb R.$`
   * Since `$C\in L_1,$` then `$\overrightarrow{OC}=\overrightarrow{OA}+s_0\cdot \overrightarrow{AB}$` for some `$s_0\in\mathbb R.$` 
   * By assumption, `$c\cdot  \overrightarrow{AB}=\overrightarrow{CD}$` for a `$c\in \mathbb R$` with `$c\neq 0.$`
   * Any point `$Q\in L_2$` with `$ \overrightarrow{OQ}=\overrightarrow{OC}+t\cdot \overrightarrow{CD}$` for `$t\in\mathbb R$` can be, therefore, written as `$ \overrightarrow{OQ}=\overrightarrow{OA}+s_0 \overrightarrow{AB}+tc\cdot \overrightarrow{AB}=\overrightarrow{OA}+(s_0+tc)\cdot \overrightarrow{AB}.$`
   * Since `$c\neq 0$`, the real number `$s_0+tc$` runs through all real numbers `$\mathbb R$` as `$t$` does.
   * Therefore, `$Q$` runs through all points of the straight line `$L_1,$` as `$t$` runs through all real numbers `$\mathbb R.$` 
   * Therefore, `$L_2=L_1$`.
