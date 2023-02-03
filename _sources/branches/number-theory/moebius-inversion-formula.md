layout: theorem
categories: branches,number-theory
nodeid: bookofproofs$8149
orderid: 400
parentid: bookofproofs$8141
title: Möbius Inversion Formula
description: MöBIUS INVERSION FORMULA &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$701,bookofproofs$1272
keywords: formula,inversion,moebius,mobius inversion formula proof,mobius inversion formula,inversion formula,mobius inversion,moebius inversion formula
contributors: bookofproofs


---
The _Möbius inversion formula_ is a useful tool allowing to calculate sums of [arithmetic functions][bookofproofs$232]. 
It was developed by [August Möbius](https://mathshistory.st-andrews.ac.uk/Biographies/Mobius/) (1790 – 1868).

---

Let `$\alpha:\mathbb N\to \mathbb C$` be an arbitrary [arithmetic function][bookofproofs$232] and let `$\beta:\mathbb N\to\mathbb C$` be another arithmetic function given by `$$\beta(n):=\sum_{d\mid n}\alpha(d).$$`
Then, using the [Möbius function][bookofproofs$8116], we can reverse the equation and provide a formula for `$\alpha:$`

`$$\alpha(n)=\sum_{d\mid n}\mu(d)\beta\left(\frac nd\right).$$`
