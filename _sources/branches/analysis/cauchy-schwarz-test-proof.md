layout: proof
categories: branches,analysis
nodeid: bookofproofs$8362
orderid: 50
parentid: bookofproofs$8361
title: 
description: PROOF OF CAUCHY-SCHWARZ TEST &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$586
keywords: cauchy-schwarz test,proof
contributors: bookofproofs

---


---

* By hypothesis, the "squared" [infinite series][bookofproofs$1109] `$\sum_{n=0}^\infty a_n^2$` and `$\sum_{n=0}^\infty b_n^2$` are both [convergent][bookofproofs$175], say to the limits `$\alpha$` and `$\beta.$`
* By the [Cauchy-Schwarz inequality][bookofproofs$6791] and the [triangle inequality][bookofproofs$588] we have for the [partial sums][bookofproofs$1109] the relation `$$\left|\sum_{n=0}^N a_n b_n\right|\le \sum_{n=0}^N |a_n b_n|\le \left(\sum_{n=0}^N a_n^2 \right)^{\frac 12}\left(\sum_{n=0}^N b_n^2 \right)^{\frac 12}$$` for all `$N\ge 0.$`
* Because [convergence preserves order relation][bookofproofs$1144], we have that the sequence `$(s_N)_{N\in\mathbb N}$` of partial sums `$s_N:=\sum_{n=0}^N |a_n b_n|$` is [bounded from above][bookofproofs$1136] and by definition, [monotonically increasing][bookofproofs$1155].
* Since [every bounded monotone sequence is convergent][bookofproofs$197], so is `$(s_N)_{N\in\mathbb N}$`, and thus the series `$\sum_{n=0}^\infty |a_n b_n|$` is [convergent][bookofproofs$175].
* It follows that `$\sum_{n=0}^\infty a_n b_n$` [absolutely convergent][bookofproofs$198].