layout: proof
categories: branches,algebra
nodeid: bookofproofs$810
orderid: 50
parentid: bookofproofs$809
title: 
description: Proof of KERNEL AND IMAGE OF GROUP HOMOMORPHISM ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$696
keywords: image,kernel,group homomorphism,proof
contributors: bookofproofs

---


---

* By hypothesis, `\((G,\ast)\)` and `\((H,\cdot)\)` are [groups][bookofproofs$671] with the respective [identities][bookofproofs$661] `\(e_G\)` and `\(e_H\)` and `\(f:G\rightarrow H\)` is a [group homomorphism][bookofproofs$679].
* We first show that `\(ker(f)=\{e_G\}\)` `\(\Longleftrightarrow f\)` is [injective][bookofproofs$769].
   * "`$\Rightarrow$`"
      * Assume `\(\ker(f)=\{e_G\}\)`. 
      * This means that the [fiber of `\(e_H\)` under `\(f\)` ][bookofproofs$592] equals `\(\{e_G\}\)`, i.e. `\(f^{-1}(e_H)=e_G\)`. 
      * This means that `\(f(e_G)=e_H\)`. 
      * Because `\(f\)` is a group homomorphism, it follows that 
`\[\begin{array}{cl}
f(x)=f(x\ast e_G)=e_H\cdot x=x\\
f(y)=f(y\ast e_G)=e_H\cdot y=y\\
\end{array}\]`
for any two elements `\(x,y\in H\)`. 
      * Therefore, from `\(f(x)=f(y)\)` it follows that `\(x=y\)`, so `\(f\)` is [injective][bookofproofs$769].
   * "`$\Leftarrow$`"
      * Assume `\(f\)` is injective. 
      * This means that from `\(f(x)=f(y)\)` it follows that `\(x=y\)`. 
      * Because `\(f\)` is a group homomorphism, we have `\(f(x)\cdot(f(y))^{-1}=e_H\)` and it follows further from its [properties][bookofproofs$680] that `\(f(x)\cdot f(y^{-1})=e_H\)`. 
      * Applying the homomorphism property again, we get `\(f(x\ast y^{-1})=e_H\)`. 
      * Now, because `\(x=y\)`, we have `\(f(e_G)=e_H\)`, i.e. `\(f^{-1}(e_H)=e_G\)`, thus `\(ker(f)=\{e_G\}\)`.
* We now show that `\(\operatorname{im}(f)=H\)` `\(\Longleftrightarrow f\)` is surjective. 
   * We just have to apply the [definition of surjectivity][bookofproofs$770].