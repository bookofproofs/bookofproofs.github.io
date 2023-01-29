layout: proof
categories: branches,analysis
nodeid: bookofproofs$6621
orderid: 50
parentid: bookofproofs$1766
title: 
description:  Proof of CONTINUOUS REAL FUNCTIONS ON CLOSED INTERVALS ARE RIEMANN-INTEGRABLE &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$581
keywords: continuous functions,integrable functions,proof
contributors: bookofproofs

---


---

* Let `\([a,b]\)` be a [closed real interval][bookofproofs$1153].
* Let `\(f:[a,b]\mapsto\mathbb R\)` be [continuous][bookofproofs$1260].
* We want to show that `$f$` is [Riemann-integrable][bookofproofs$1763].
   * According to the [approximability of continuous real functions on closed intervals by step functions][bookofproofs$6619], there exist for a fixed `\(\epsilon > 0\)` [step functions][bookofproofs$1751] `$\phi,\psi$` with `$$\phi(x)\le f(x)\le \psi(x),\quad\text{ and }\quad |\psi(x)-\phi(x)|\le \frac\epsilon{b-a}$$` for all `$x\in[a,b].$`
   * From the [linearity and monotony of the Riemann integral for step functions][bookofproofs$1759], it follows that `$$\int_a^b\psi(x)dx-\int_a^b\phi(x)dx=\int_a^b(\psi(x)-\phi(x))dx\le \int_a^b\frac\epsilon{b-a}dx=\epsilon.$$`
   * Thus a [sufficient condition for Riemann-integrable functions][bookofproofs$1764] is fulfilled. 
   * Thus, `$f$` is [Riemann-integrable][bookofproofs$1763].