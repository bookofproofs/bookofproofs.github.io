layout: proof
categories: branches,analysis
nodeid: bookofproofs$8359
orderid: 50
parentid: bookofproofs$8358
title: 
description: PROOF OF LIMIT TEST FOR ROOTS OR RATIOS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$586
keywords: limit test for roots,limit test for ratios,proof
contributors: bookofproofs

---


---

* By hypothesis, the [sequence][bookofproofs$875] of [n-th roots][bookofproofs$46] `$(\sqrt[n]{|a_n|})_{n\in\mathbb N},$` or the sequence of ratios `$\left(\frac{|a_{n+1}|}{|a_n|}\right)_{n\in\mathbb N}$` is [convergent][bookofproofs$141] to a limit `$\alpha > 0.$` 
* Case a) `$\lim_{n\to\infty} \sqrt[n]{|a_n|}=\alpha < 1.$`
   * By the [inequality of arithmetic mean][bookofproofs$589], we have `$\alpha < (\alpha+1)/2 < 1.$`
   * Therefore, there is an index `$N$` such that for all `$n > N$` we have `$\sqrt[n]{|a_n|} < q:=(\alpha+1)/2.$`
   * By the [root test][bookofproofs$8352], the [infinite series][bookofproofs$1109]  `$\sum_{n=0}^\infty a_n$` is [convergent][bookofproofs$175].
* Case b) `$\lim_{n\to\infty} \sqrt[n]{|a_n|}=\alpha > 1.$`
   * As for the case a) `$\alpha < 1$`, the root test reveals that `$\sum_{n=0}^\infty a_n$` is [divergent][bookofproofs$217], if `$\alpha > 1.$`
* Cases c) `$\lim_{n\to\infty} \frac{|a_{n+1}|}{|a_n|}=\alpha < 1$` and d) `$\alpha > 1.$`
   * The reasoning is identical as in the cases a) and b), but we have to apply the [ratio test][bookofproofs$1337].