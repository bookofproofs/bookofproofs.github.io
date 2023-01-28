layout: proof
categories: branches,algebra
nodeid: bookofproofs$834
orderid: 50
parentid: bookofproofs$833
title: 
description:  Proof of KERNEL AND IMAGE OF A GROUP HOMOMORPHISM ARE SUBGROUPS &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$696
keywords: image,kernel,subgroup,subgroups,group homomorphism,image of homomorphism is a subgroup,image of a group homomorphism is a subgroup,image of a homomorphism is a subgroup,image of a homomorphism,kernel and image of homomorphism,image of a group homomorphism,proof
contributors: bookofproofs

---


---

* Given a group homomorphism `\(f:(G,\ast)\mapsto (H,\cdot)\)`, we first show that `\(\ker(f)\)` is a [subgroup][bookofproofs$554] of `\(G\)`.
   * Note that from the [properties of a group homomorphism][bookofproofs$680], it follows that `\(f(e_G)=e_H.\)`
   * Thus, the [kernel][bookofproofs$809] `\(\ker(f)\)` is not empty. 
   * Therefore assume that `\(x,y\in \ker(f)\)`, i.e. `\(f(x)=f(y)=e_H\)`. 
   * It follows `$f(x\ast y^{-1})=f(x)\cdot f(y^{-1})=e_H\cdot (f(y))^{-1}=e_H\cdot (e_H)^{-1}=e_H.$`
   * We have found that `\(x\ast y^{-1}\in ker(f)\)`, which is a [subgroup criterion][bookofproofs$811] 
   * Thus, `\(\ker(f)\)` is a [subgroup][bookofproofs$554] of `\(G\)`.
* We now show analogously that `\(\operatorname{im}(f)\)` is a [subgroup][bookofproofs$554] of `\(H\)`. 
   * Again from `\(e_H=f(e_G)\)` it follows that the [image][bookofproofs$809] `\(\operatorname{im}(f)\)` is not empty. 
   * Therefore assume that `\(a,b\in im(f)\)`, i.e. that there exist some `\(x,y\in G\)` with `\(f(x)=a\)` and `\(f(y)=b\)`. 
   * It follows that `$a\cdot b^{-1}=f(x)\cdot (f(y))^{-1}=f(x)\cdot f(y^{-1})=f(x\ast y^{-1}).$`
   * We have found that `\(a\cdot b^{-1}\in H\)` is the image of `\(x\ast y^{-1}\in G\)`, which is a [subgroup criterion][bookofproofs$811] 
   * Thus, `\(\operatorname{im}(f)\)` is a [subgroup][bookofproofs$554] of `\(H\)`.
