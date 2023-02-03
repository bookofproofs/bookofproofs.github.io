layout: theorem
categories: branches,combinatorics
nodeid: bookofproofs$8314
orderid: 200
parentid: bookofproofs$104
title: Approximation of Factorials Using the Stirling Formula
description: APPROXIMATION OF FACTORIALS USING THE STIRLING FORMULA ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$581
keywords: approximation of factorials,stirling formula
contributors: bookofproofs


---
The calculation of factorials `$n!$` can be quite difficult when `$n$` is large. 
<a href="https://mathshistory.st-andrews.ac.uk/Biographies/Stirling/">James Stirling</a> (1692 - 1770) developed a formula which helps to approximate the factorial. The approximation is quite good - for `$n=10$` the formula generates a value differing from the correct one only by `$1$`%, for `$n=100,$` the error is even `$0.1$`%.

---

The [factorial][bookofproofs$1005] `$n!$` can be [asymptotically approximated][bookofproofs$8313] by the following formula:
`$$n!\sim\sqrt{2\pi n}\left(\frac ne\right)^n,$$` where `$e$` is the [Euler's constant][bookofproofs$1344] `$e\approx 2.71828\ldots$` and `$\pi$` is the [number pi][bookofproofs$6738] `$\pi\approx 3.141592653\ldots.$`

The approximation error is given by the inequation `$$\sqrt{2\pi n}\left(\frac ne\right)^n < n! < \sqrt{2\pi n}\left(\frac ne\right)^n\exp\left(\frac{1}{12(n-1)}\right).$$`
