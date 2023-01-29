layout: solution
categories: branches,number-theory
nodeid: bookofproofs$8212
orderid: 50
parentid: bookofproofs$8211
title: 
description: Solution of CALCULATING QUADRATIC RESIDUES &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$1272
keywords: calculating,quadratic,residues solution
contributors: bookofproofs

---


---

* The [congruence][bookofproofs$8153] `$x^2(p)\equiv 3\equiv(p)$` has a solution, if the [Legendre symbol][bookofproofs$8198] `$\left(\frac 3p\right)=1.$`
* According to the [quadratic reciprocity law][bookofproofs$8205], we have `$$\left(\frac{3}{p}\right)\cdot \left(\frac{p}{3}\right)=(-1)^{\frac{p-1}{2}\frac{3-1}{2}}=(-1)^{\frac{p-1}{2}}.$$`
* We can divide both sides by `$\left(\frac{p}{3}\right)=\pm 1$` and get `$$\left(\frac{3}{p}\right)=\left(\frac{p}{3}\right)\cdot (-1)^{\frac{p-1}{2}}.\label{eq:E18781a}\tag{a}$$`
* First of all, we have `$$(-1)^{\frac{p-1}{2}}=\begin{cases}1&\text{if }p\equiv 1\mod 4,\\-1&\text{if }p\equiv -1\mod 4.\end{cases}\label{eq:E18781b}\tag{b}$$`
* On the other hand, we can apply the [Legendre symbols of equal residues][bookofproofs$8199] rule to deduce, that if `$p(3)\equiv 1(3),$` then `$\left(\frac{p}{3}\right)=\left(\frac{1}{3}\right).$`
* But `$\left(\frac{1}{3}\right)=1,$` which can be verified directly.
* Note that if `$p(3)\not\equiv 1(p)$`, then otherwise we have `$p(3)\equiv 2(3)\equiv-1(3).$` In this case, we can apply the [first supplementary law to the quadratic reciprocity law][bookofproofs$8206] to deduce that `$\left(\frac{-1}{3}\right)=-1.$`
* Altogether, we have `$$\left(\frac{p}{3}\right)=\begin{cases}1&\text{if }p\equiv 1\mod 3,\\-1&\text{if }p\equiv -1\mod 3,\; p > 2.\end{cases}\label{eq:E18781c}\tag{c}$$`
* Combining the results `$(\ref{eq:E18781a}),$` `$(\ref{eq:E18781b}),$` and `$(\ref{eq:E18781c})$` together, we get `$$\left(\frac{3}{p}\right)=\begin{cases}1&\text{if }p\equiv\pm 1\mod 12,\\-1&\text{if }p\equiv \pm 5\mod 12.\\\end{cases}$$`
* Therefore, the [congruence][bookofproofs$8153] `$x^2(p)\equiv 3\equiv(p)$` has a solution, if and only if `$p\equiv\pm 1\mod 12.$`
