layout: proof
categories: branches,set-theory
nodeid: bookofproofs$989
orderid: 50
parentid: bookofproofs$988
title: 
description:  Proof of FINITE CARDINAL NUMBERS AND SET OPERATIONS &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$983
keywords: cardinal,finite,numbers,operations,set,proof
contributors: bookofproofs

---


---

Let `\(X, Y, U\)` and `\(W\)` be [finite sets][bookofproofs$985].
### (1) 

We want to show that from `\(|X|=|Y|, |U|=|W|\)` and `\(X\cap U=\emptyset, Y\cap W=\emptyset\)` it follows for [set unions][bookofproofs$552] that `\(|X\cup U|=|Y\cup W|=|X|+|U|=|Y|+|W|\)`.

* From the hypothesis `\(|X|=|Y|, |U|=|W|\)` it follows from [rules of comparing cardinal numbers][bookofproofs$984] that there are [bijective][bookofproofs$771] maps `\(f:X\mapsto Y\)` and `\(g:U\mapsto W\)`. 
* The hypothesis `\(X\cap U=\emptyset\)` means that from `\(a\in X\cup U\)` it follows that either `\(a\in X\)` or `\(a\in U\)` (but not both). 
* Thus, we can define a map `\(h:\)`.
`\[h:=\begin{cases}
X\cup U & \mapsto   Y\cup W\\
a & \mapsto   f(a)   \Leftrightarrow  a\in X\\
a & \mapsto   g(a) \Leftrightarrow  a\in U\\
\end{cases}\]`
* The hypothesis `\(Y\cap W=\emptyset\)` means that from `\(h(a)\in Y\cup W\)` it follows that either `\(h(a)\in Y\)` or `\(h(a)\in W\)` (but not both), so `\(|X\cup U|=|X|+|U|\)` and `\(|Y\cup W|=|Y|+|W|\)`. 
* Moreover, `\(h\)` is bijective, because `\(f\)` and `\(g\)` are bijective. 
* Thus, `\(|X\cup U|=|Y\cup W|\)`. 

### (2) 
 
We want to show that from `\(|X|=|Y|\)` and `\(|U|=|W|\)` it follows for the [Cartesian products][bookofproofs$748] that `\(|X\times U|=|Y\times W|=|X|\cdot|U|=|Y|\cdot|W|\)`
* As in (1) from `\(|X|=|Y|, |U|=|W|\)` it follows that there are bijective maps `\(f:X\mapsto Y\)` and `\(g:U\mapsto W\)`. 
* We define a new map
`\[h:\begin{cases}
X\times U&\mapsto  Y\times W\\
(a,b)&\mapsto  (f(a),g(b))
\end{cases}\]`
* For a fixed cardinal number `\(|X|\)` we prove [by induction][bookofproofs$657] on the cardinal number `\(|U|=n\in\mathbb N\)`. 
   * For `\(n=0\)` we have `\(U=\emptyset\)` and `\(W=g(U)=g(\emptyset)=\emptyset\)`. Therefore `\(h(X\times \emptyset)=h(\emptyset)=f(\emptyset)=\emptyset\)`. Thus it follows trivially that `\(h\)` is bijective as `\(f\)`. 
   * Thus `\(|X\times\emptyset|=|Y\times\emptyset|=|X|\cdot|\emptyset|=|Y|\cdot|\emptyset|=0\)`, as required.
   * Let the claim 
`\[(|X|=|Y|\wedge |U_0|=|W_0|)\Rightarrow|X\times U_0|=|Y\times W_0|=|X|\cdot|U_0|=|Y|\cdot|W_0|\]`
 be proven for all `\(U_0,W_0\)` with `\(|U_0|=|W_0|=n_0\ge 0\)`. 
   * We observe that `\(|X|=|X \times \{U_0\}|\)`, since the set `\(\{U_0\}\)` has only one element[^1].  
   * For the set `\(U=U_0 \cup \{U_0\}\)` we have then
`\[X\times U=X\times(U_0 \cup \{U_0\})=(X\times U_0) \cup (X\times \{U_0\}).\]`
   * Taking the cardinal numbers on both sides we find
`\[|X\times U|=|(X\times U_0) \cup (X\times \{U_0\})|=|(X\times U_0)| + |(X\times \{U_0\})|,\]`
where the last equation follows from (1) and the fact that `\((X\times U_0) \cap (X\times \{U_0\})=\emptyset\)`.[^2] 
   * Therefore we have
`\[|X\times U|=|X|\cdot|U_0|+|X|\cdot|\{U_0\}|=|X|\cdot n_0+|X|\cdot 1=|X|\cdot(n_0+1)=|X|\cdot(|U_0|+1)=|Y|\cdot(|W_0|+1)=|Y\times W|\]`
* The claim can analogously be proven by induction for a fixed [cardinal number][bookofproofs$980] `\(|U|\)` on the cardinal number `\(|X|=n\in\mathbb N\)`.

[^1]: We also could have used `\(\{\emptyset\}\)` or any other set with only one element. 

[^2]: Note: There is no pair `\((a,b)\)` for which both  `\((a,b)\in (X\times \{U_0\})\)` and `\((a,b)\in (X\times U_0)\)` can be true simultaneously, otherwise `\(b\)` would equal a set `\(U_0\)` which contains itself `\(\{U_0\}\)`, which is forbidden by the [axiom of foundation][bookofproofs$717].