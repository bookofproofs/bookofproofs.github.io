layout: proposition
categories: branches,analysis
nodeid: bookofproofs$457
orderid: 2000
parentid: bookofproofs$166
title: Gamma Function
description: GAMMA FUNCTION ★ bring your math skills to the graduate level ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$581,bookofproofs$586
keywords: gamma function,gamma functions,gamma
contributors: bookofproofs

---


---

The [improper integral][bookofproofs$8343] `$\int_0^\infty \exp(-t)t^{x-1}dt$` is convergent if and only if `$x > 0.$` For a given `$x>0$`, we call this limit the **Gamma function** `$\Gamma(x)$` and set `$$\Gamma(x):=\int_0^\infty \exp(-t)t^{x-1}dt,$$` where `$\exp$` denotes the real [exponential function][bookofproofs$281].
§§§1

---

§§§1
<div class='sage'>plot(gamma, (-5, 7), detect_poles=True).show(ymin=-70, ymax=70)</div>
