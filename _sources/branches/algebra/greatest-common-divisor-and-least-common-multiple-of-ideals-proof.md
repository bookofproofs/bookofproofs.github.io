layout: proof
categories: branches,algebra
nodeid: bookofproofs$1070
orderid: 0
parentid: bookofproofs$1069
title: 
description: PROOF OF GREATEST COMMON DIVISOR AND LEAST COMMON MULTIPLE OF IDEALS &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$696
keywords: common,divisor,greatest,greatest common divisor,ideals,least,least common multiple,multiple,proof
contributors: bookofproofs

---


---

### We will first show that the set  `\(I + J\)` is an ideal of the ring `\(R\)`. 

According to the [definition of ideals][bookofproofs$1062], if `\(I\lhd R\)` and `\(J\lhd R\)`  are ideals by hypothesis, then `\((I, + )\)` and `\((J, + )\)` are subgroups of the additive group  `\((R,+ )\)`. According to the [definition of the set][bookofproofs$1068] `\(I+J\)` and for an `\(i_1,i_2\in I\)` and `\(j_1,j_2\in J\)` we therefore have for each element `\((i_1+j_1)+(i_2+j_2)\)` contained in `\(I+J\)` that also the element `\((i_1+j_1) - (i_2+j_2)\)` is contained in `\(I+J\)`. Thus, it is verified by the [first subgroup criterion][bookofproofs$811], that the set `\((I + J, + )\)` is a subgroup of the additive group `\((R,+)\)`. Moreover, if `\(r\in R\)` and `\(i+j\in I+J\)`, then we have 
`\[r(i+j)=ri+rj\in I+J.\]` Therefore, `\(I + J\)` is an ideal of the ring `\(R\)`. 

### Now, we will show that `\(I+J\)` is the greatest [ideal dividing][bookofproofs$1065] `\(I\)` and `\(J\)`. 

First of all, we observe that `\(I+J\)` divides both, `\(I\)` and `\(J\)`, since `\(I+J\supseteq I\)` and `\(I+J\supseteq J\)`. Now, for any other ideal `\(K\lhd R\)` dividing both, `\(I\)` and `\(J\)` we have either `\(I+J\supseteq K\)` or `\(K\supseteq I+ J\)`. In the case `\(I+J=K\)` there is nothing to show. Suppose `\(I+J\supset K\)`. Then, there would exist an `\(x\in I+J\)` with `\(x\not\in K\)`. But this [contradicts][bookofproofs$744] `\(K\supseteq I\owns x\)`, (analogously `\(K\supseteq J\owns x\)`), since `\(K\)` divides both ideals by assumption. Thus, we must have `\(K\supseteq I + J\)`. This demonstrates that for any other ideal `\(K\)` dividing both, `\(I\)` and `\(J\)`, it also divides `\(I+J\)`. This means that `\(I + J\)` is the __greatest common divisor__, or `\(I+J=gcd(I,J)\)`.

### Next, we show that the set  `\(I \cap J\)` is an ideal of the ring `\(R\)`.

Since `\((I, + )\)` and `\((J, + )\)` are subgroups of the additive group  `\((R,+ )\)`, also `\((I\cap J, + ) \)` is a subgroup by [second subgroup criterion][bookofproofs$811].  Moreover, if `\(r\in R\)` and `\(x\in I\cap J\)`, then `\(x\in I\)` and `\(x\in J\)`, so `\(rx\in I\)` and `\(rx\in J\)` since `\(I\)` and `\(J\)` are ideals. But this means that `\(rx\in I\cap J\)`. Therefore, `\(I \cap J\)` is an ideal of the ring `\(R\)`.

### Last, we show that the set `\(I \cap J\)` is a least common multiple of the ideals `\(I\)` and `\(J\)`.

First of all, we observe that `\(I\supseteq I\cap J\)` and `\(J\supseteq I\cap J\)`, thus `\(I\cap J\)` is a multiple of both ideals (in other words both ideals divide `\(I\cap J\)` simultaneously). For any other ideal `\(K\lhd R\)` being the multiple of both ideals (`\(I\supseteq K\)` and `\(J\supseteq K\)`) we have either `\(I\cap J\supseteq K\)` or `\(K\supseteq I\cap J\)`. In the case `\(I\cap J=K\)` there is nothing to show. Suppose `\(K\supset I\cap J\)`. Then, there would exist an `\(x\in K\)` with `\(x\not\in I\cap J\)`. This [contradicts][bookofproofs$744] `\(x\in I\cap J\)`, since `\(I\subseteq K\owns x\)` and `\(J\subseteq K\owns x\)` simultaneously. Thus, we must have `\(I\cap J\supseteq K\)`. This demonstrates that for any other ideal `\(K\)` being a multiple of both, `\(I\)` and `\(J\)`, it is also a multiple of `\(I\cap J\)`. This means that `\(I\cap J\)` is the __least common multiple__, or `\(I\cap J=lcm(I,J)\)`.
