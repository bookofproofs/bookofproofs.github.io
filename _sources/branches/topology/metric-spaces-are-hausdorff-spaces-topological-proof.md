layout: proof
categories: branches,topology
nodeid: bookofproofs$851
orderid: 50
parentid: bookofproofs$850
title: 
description: TOPOLOGICAL PROOF PROOF OF METRIC SPACES ARE HAUSDORFF SPACES &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$582
keywords: hausdorff spaces,hausdorff space,metric spaces are hausdorff spaces,hausdorff,proof
contributors: bookofproofs

---


---

Set `\(\epsilon:=\frac 12 d(x,y)\)`. Because by assumption `\(x\neq y\)` , we have `\(d(x,y)>0\)`. The open balls 

`\[U:=B(x,\epsilon),~~~~~~~~~~~~V:=B(y,\epsilon)\]`
are [by definition][bookofproofs$849] neighborhoods of `\(x\)` and `\(y\)`. We shall show that `\(U\cap V= \emptyset\)`.

Assume that `\(U\cap V\neq \emptyset\)` and let `\(z\in U\cap V\)` be a point in both neighbourhoods. Then it would follow that 

`\[2\epsilon=d(x,y)\le d(x,z)+d(z,y) < \epsilon+\epsilon,\]`

which is a [contradiction][bookofproofs$744]. Therefore we have indeed `\(U\cap V= \emptyset\)`, which means that the [metric space][bookofproofs$617] `\((X,d)\)` is a [Hausdorff space][bookofproofs$6199].