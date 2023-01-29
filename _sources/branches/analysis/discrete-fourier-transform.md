layout: chapter
categories: branches,analysis
nodeid: bookofproofs$382
orderid: 800
parentid: bookofproofs$58
title: Discrete Fourier Transform (DFT)
description: DISCRETE FOURIER TRANSFORM ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: 
keywords: discrete fourier transform,dfs,fast fourier transform,fft,finite fourier transform,signal,fourier
contributors: bookofproofs

---


---

The basis for the _discrete Fourier transform_ (DFT), also sometimes called _finite Fourier transform_ or _fast Fourier transform_ (FFT), are the properties of the n-th [roots of unity][bookofproofs$6752]. The DFT can be used to study any sequence of (real) numbers, which is the result of a sample of measurements of an unknown physical phenomenon, e.g. a _signal_.

The sequence is assumed to be [periodical][bookofproofs$8318] with a period `$n$`, if `$n$` the number of measured values in the sample of a given "si. The theory of DFT, which will be described in this chapter, shows that this assumption does not really matter for the usefulness of DFT for sampling methods, i.e. even if the signal, in reality, is not periodical.

There are many ways to derive equivalent formulae for the DFT. The different formulae found in literature might differ from those introduced in this chapter by the sign of exponents, or the norming factor `$\frac 1n$` of the so-called _Fourier coefficients_, but all of these formulae are equivalent forms of DFT and can be transformed to the forms introduced and derived in this chapter.
