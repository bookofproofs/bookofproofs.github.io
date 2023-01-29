layout: proof
categories: branches,topology
nodeid: bookofproofs$6586
orderid: 50
parentid: bookofproofs$6585
title: 
description:  Proof of CHARACTERIZATION OF CLOSED SETS BY LIMITS OF SEQUENCES &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$582
keywords: characterization,closed,limits,sequences,sets,proof
contributors: bookofproofs

---


---

Let `$X$` be a [metric space][bookofproofs$617] and let `\(A \)` be its [subset][bookofproofs$552].
### "$\Rightarrow$"

* Let `$A$` be [closed][bookofproofs$852].
* Take any [convergent sequence][bookofproofs$148] `$(x_k)_{k\in\mathbb N}$` with `$x_k\in A$`  for all `$k\in\mathbb N$` with `$\lim_{k\to\infty} x_k=x$`.
* Assume, `$x\not\in A$`.
   * Because `\(X\setminus A\)` is [open][bookofproofs$852],  `\(X\setminus A\)` is a [neighborhood][bookofproofs$849] of `\(x\)`.
   * By the [definition of convergence][bookofproofs$148] there is a `\(N\in\mathbb N\)` such that `\(x_k\in X\setminus A\)` for all `\(k\ge N\)`.
   * This [contradicts][bookofproofs$744] `$x_k\in A$`  for all `$k\in\mathbb N$`.

### "$\Leftarrow$"

* Let  `$x\in A$` for any [convergent sequence][bookofproofs$148] `$(x_k)_{k\in\mathbb N}$` with `$x_k\in A$`  for all `$k\in\mathbb N$` with `$\lim_{k\to\infty} x_k=x$`. Further let `\(x\in A\)`.
* We have to show that `$A$` is [closed][bookofproofs$852].
* Assume, `$A$` is [open][bookofproofs$852].
   * Then `\(A\)` is a [neighborhood][bookofproofs$849] of `\(x\)`.
   * Therefore there is an `\(\epsilon > 0\)` such that the [open ball][bookofproofs$849] `\(B(x,\epsilon)\)` is contained in `\(A\)`.
   * Since `$(x_k)_{k\in\mathbb N}$` was an arbitrary sequence, we can choose it in a way that `\(x\)` is contained in the [boundary][bookofproofs$1202] `\(\delta A\)`.
   * But then, for all `\(\epsilon > 0\)`, the open ball `\(B(x,\epsilon)\)` will have points in common with `\(A\)` and with `\(X\setminus A\)`.
   * This contradicts `$A$` being open.
