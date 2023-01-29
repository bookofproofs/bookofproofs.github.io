layout: definition
categories: branches,set-theory
nodeid: bookofproofs$8034
orderid: 100
parentid: bookofproofs$716
title: Singleton
description: SINGLETON &#9733; bring your math skills to the graduate level &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$656,bookofproofs$983
keywords: singleton
contributors: bookofproofs

---
We have just shown how the [axiom of power set][bookofproofs$716] ensures the existence and uniqueness of the [power set][bookofproofs$6831]. The following diagram illustrates the power set `$\mathcal P(X)$` for a set `$X$` containing three elements:


![singleton1](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/singleton1.png?raw=true)


Using the [axiom of separation][bookofproofs$675], we can now separate a subset of `$\mathcal P(X)$` containing exactly `$X$` as its single element:


![singleton2](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/singleton2.png?raw=true)


Moreover, the resulting set is unique by the [axiom of extensionality][bookofproofs$551]. This motivates the following definition:

---

For every set `$X$` the set `$\{X\}$` is well-defined and is called the **singleton** of `$X.$` Formally, using the [power set][bookofproofs$6831], we have `$$\{X\}:=\{z\in\mathcal P(X)\mid z=X\}.$$`
