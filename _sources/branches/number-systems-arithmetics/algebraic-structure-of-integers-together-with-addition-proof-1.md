layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1656
orderid: 100
parentid: bookofproofs$1654
title: 
description:  Proof of ALGEBRAIC STRUCTURE OF INTEGERS TOGETHER WITH ADDITION &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$696
keywords: algebraic structure of integers together with addition,algebraic structure of integers,additive structure of integers,proof
contributors: bookofproofs

---


---

A proof of this proposition is a direct application of the theorem [construction of groups from commutative cancellative semigroups][bookofproofs$839] `\(( * )\)`, in which we will construct the group `\((\mathbb Z, +)\)` from the semigroup `\((\mathbb N, +)\)`.

We first have to check, if all preconditions necessary to apply the above-mentioned theorem are fulfilled. We do this by showing that `\((\mathbb N, +)\)` is a commutative and a cancellative semigroup. Please note that this follows immediately from the [corresponding proposition][bookofproofs$841] stating that `\((\mathbb N, +)\)` is, in fact, a special case of a commutative and cancellative monoid. Since [by definition][bookofproofs$659] every monoid is also a semigroup, all preconditions to apply theorem `\(( * )\)` are fulfilled.

### Application of the theorem `\(( * )\)` to construct the group `\((\mathbb Z, +)\)` from the semigroup `\((\mathbb N, +)\)`

In the proof of the theorem `\(( * )\)`, a group `\((G,\ast)\)` is constructed from a semigroup `\((H,\circ)\)` as the set of all [equivalence classes][bookofproofs$7990] `\([a,b]\)`, which are represented by ordered pairs `\((a,b)\in H\times H\)`. In this proof, the operation `\(\ast\)` is defined as 
`\[[a,b]\ast[c,d]:=[a\circ c,b\circ d].\]`
In our special case, `\((H,\circ)=(\mathbb N, + )\)`, and the operation `\(\ast\)` is given by  
`\[[a,b]\ast[c,d]=[a,b] + [c,d]:=[a + c,b + d],\]`
in which, for simplicity reasons and in accordance with usual notation of addition of integers, we replace the operation `\(\ast\)` (general case) by `\( +\)` (special case). 

Furthermore, according to the proof of `\(( * )\)`, the semigroup `\((\mathbb N, + )\)` is isomorphic to a proper subset `\(S\subset G\)` with (using our new notation)
`\[S:=\{[a+h,h]~|~a\in\mathbb N\}.\]`
Please note, that because `\((\mathbb N, + )\)` is cancellative and a monoid, we can even write
`\[S=\{[a+h,h]~|~a\in\mathbb N\}=\{[a+\cancel h,\cancel h]~|~a\in\mathbb N\}=\{[a+0,0]~|~a\in\mathbb N\}=\{[a,0]~|~a\in\mathbb N\}.\]`
Thus, we have just identified all natural numbers `\(a\in\mathbb N\)` with the equivalence classes `\([a,0]\in G\)` , represented by the ordered pair `\((a,0)\in\mathbb N\times \mathbb N\)`. 

We also learn from the proof of theorem `\(( * )\)` that for each `\([a,0]\in G\)` there is a unique inverse element `\([0,a]\in G\)`, i.e. an element fulfilling the equation
`\[[a,0]+[0,a]=[a+0,0+a]=[a,a]=[\cancel a,\cancel a]=[0,0],\]`
applying the cancellation and monoid properties of `\(\mathbb N\)` once again and showing us that `\([0,0]\)` is the identity element of the group `\(G\)`.

Altogether, we can now introduce the set of integers `\((\mathbb Z, + )\)` as follows:

`\[\begin{array}{ccc}
a\in \mathbb Z&\Longleftrightarrow&[a,0]\in G~\forall a\in\mathbb N, a\neq 0\\ 
- a\in \mathbb Z&\Longleftrightarrow&[0,a]\in G~\forall a\in\mathbb N, a\neq 0\\ 
0\in \mathbb Z&\Longleftrightarrow&[0,0]\in G,~0\in\mathbb N.
\end{array}~~~~~~~(**)\]`
For simplicity reasons, we write `\(a-b\)` instead of `\(a + (-b)\)`. 

Finally, we have to prove that there are no other elements in `\(\mathbb Z\)`, instead of those listed in the three cases `\(( * *)\)`. We can do so by demonstrating that any equivalence class `\([a,b]\in G\)` with __both__ `\(a\neq 0\)` __and__  `\(b\neq 0\)` can be identified with one of the integers already defined in `\(( * *)\)`. Assume `\(a -b\in\mathbb N\)`. Then we can identify `\([a,b]\in G\)` with
`\[[a,b]=[a-b,b-b]=[a-b,0],\]`
which shows us that the equivalence class `\([a,b]\)` is independent of the representative, since we have replaced the representative `\((a,b)\in\mathbb N\times\mathbb N\)` by another representative `\((a-b,0)\in\mathbb N\times\mathbb N\)`. In a similar way, we can identify `\([a,b]\)` with `\([0,b-a]\)`, if we assume `\(b -a\in\mathbb N\)`. This completes the proof.
