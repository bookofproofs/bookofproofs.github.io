layout: proof
categories: branches,analysis
nodeid: bookofproofs$3560
orderid: 50
parentid: bookofproofs$6745
title: 
description: PROOF OF MORE INSIGHT TO EULER'S IDENTITY &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: 
keywords: geralized euler's identity,general case of euler's identity,proof
contributors: bookofproofs

---


---

* Let `$x=k\pi$` be a [real number][bookofproofs$1105] by some [integer][bookofproofs$844] `$k\in\mathbb Z$` and the [number pi][bookofproofs$6738] `$\pi.$`
* By [representing the real sine by complex function][bookofproofs$1788], we have `$$\sin\left(\frac x2\right)=\frac{1}{2i}\left(\exp\left(i\frac{x}{2}\right)-\exp\left(-i\frac{x}{2}\right)\right)=\frac{\exp\left(-i\frac x2\right)}{2i}(\exp(ix)-1).$$`
* Therefore, `$\exp(ix)=1$` if and only if `$\sin\left(\frac x2\right)=0.$`  
* By [zeros of sine][bookofproofs$6743], it follows 
`$$\sin\left(\frac x2\right)=0\Longleftrightarrow \frac x2= m\pi\Longleftrightarrow x=2m\pi,\quad m\in\mathbb Z.$$`
* Therefore, `$\exp(ix)=1$` if and only if `$k=2m$` is [even][bookofproofs$8130].
* By [representing the real cosine by complex function][bookofproofs$1786], we have `$$\cos\left(\frac x2\right)=\frac{1}{2}\left(\exp\left(i\frac{x}{2}\right)+\exp\left(-i\frac{x}{2}\right)\right)=\frac{\exp\left(-i\frac x2\right)}{2}(\exp(ix)+1).$$`
* Therefore, `$\exp(ix)=-1$` if and only if `$\cos\left(\frac x2\right)=0.$`  
* By [zeros of cosine][bookofproofs$6743], it follows 
`$$\cos\left(\frac x2\right)=0\Longleftrightarrow \frac x2= \left(m+\frac 12\right)\pi=x=(2m+1)\pi,\quad m\in\mathbb Z.$$`
* Therefore, `$\exp(ix)=-1$` if and only if `$k=2m+1$` is [odd][bookofproofs$8130].