layout: definition
categories: branches,algebra
nodeid: bookofproofs$8659
orderid: 3
parentid: bookofproofs$210
title: Absolute Values and Non-Archimedean Absolute Values of Fields
description: ABSOLUTE VALUE AND NON-ARCHIMEDEAN ABSOLUTE VALUES OF FIELDS ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$8311
keywords: absolute value in fields,absolute value,valuation of fields,valuations,absolute values,trivial absolute value,trivial valuation,non-archimedean,non-archimedean absolute value,non-archimedean absolute values
contributors: bookofproofs

---


---

Let `$(F,\oplus,\odot)$` be a [field][bookofproofs$557] An **absolute value** `$|\cdot|:F\to \mathbb R$` is a [real-valued][bookofproofs$1105] [function][bookofproofs$592] fulfilling the following properties:

1. `$|x|\ge 0$` for all `$x\in F.$`
1. `$|x|=0$` if and only if `$x=0\in F.$`
1. `$|x\odot y|=|x|\cdot |y|$` for all `$x,y\in F.$`
1. `$|x\oplus y|\le |x|+|y|$` for all `$x,y\in F$`  **triangle inequality**).

An absolute value, in which the 4th axiom is replaced by

#4. `$|x\oplus y|\le \max(|x|,|y|)$`

(i.e. the [maximum][bookofproofs$6602] of the absolute values), is called *non-archimedean* (or a **valuation** of `$F$`).

### Notes

* The absolute value can be defined for all fields, not only for ordered fields. This is because an absolute value is simply a function fulfilling some properties which do not require the domain `$F$` to be an ordered field.
* In some special literature, you will find definitions of absolute values that require the field `$F$` to be ordered. This is the case in definitions like this `$$|x|:=\begin{cases}x&\text{if }x \ge 0,\\-x&\text{else }x < 0.\end{cases}$$` You should be aware that this is only a special case definition applicable for only some common fields like the field of [real numbers][bookofproofs$1105] `$(\mathbb R, +,\cdot).$` It would be not applicable for any unordered field. For instance, the unordered field of complex numbers `$(\mathbb C, +,\cdot)$` requires another definition of an absolute value.
* The definition of an absolute value given here is applicable for all kinds of fields.
