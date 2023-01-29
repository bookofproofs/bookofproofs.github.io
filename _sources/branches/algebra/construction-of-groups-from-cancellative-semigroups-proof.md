layout: proof
categories: branches,algebra
nodeid: bookofproofs$840
orderid: 50
parentid: bookofproofs$839
title: 
description:  Proof of CONSTRUCTION OF GROUPS FROM COMMUTATIVE AND CANCELLATIVE SEMIGROUPS &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$696
keywords: construction,cancellative semigroup,group,proof
contributors: bookofproofs

---


---

### Uniqueness

* Assume, two [groups][bookofproofs$671] `\((G_1,\ast)\)` and `\((G_2,\circ)\)` fulfil both properties (1) and (2).
* Because of the property (2), `\((G_1,\ast)\)` is a [subgroup][bookofproofs$554] of `\((G_2,\ast)\)` and vice versa. 
* Therefore, both groups are, in fact, the same groups.

### Existence

Our proof will be comprised of 4 steps:

* Step 1: Construct `\((G,\ast)\)` as a non-empty set with a binary operation "`\(\ast\)`"
   * By assumption, `\((H,\circ)\)` is a [commutative][bookofproofs$672] and [cancellative][bookofproofs$837] [semigroup][bookofproofs$660].
   * As a first step, we define an [equivalence relation][bookofproofs$574] on the [cartesian product][bookofproofs$748] `\(H\times H=\{(a,b)~|~a,b\in H\}\)` as follows:
`\[(a,b)\sim (c,d)\Leftrightarrow a\circ d=b\circ c~~~(a,b,c,d\in H).\]`
   * Please note that this is indeed an equivalence relation, since it is reflexive, symmetric and transitive:
      * The _reflexivity_ of "`\(\sim\)`" follows from the commutativity of `\(H\)`: `$(a,b)\sim(a,b)\Leftrightarrow a\circ b=b\circ a.$`
      * Also the _symmetry_ of "`\(\sim\)`" follows from the commutativity of `\(H\)`:`\[\begin{array}{ccl}
(a,b)\sim (c,d)&\Leftrightarrow&a\circ d=b\circ c\\
&\Leftrightarrow&c\circ b=d\circ a\\
&\Leftrightarrow&(c,d)\sim (a,b).
\end{array}\]`
      * The _transitivity_ of  "`\(\sim\)`" follows from `\(H\)` being cancellative and commutative:
         * Assume for `\(a,b,c,d,e,f\in H\)`:
`\[\begin{array}{ccc}
(a,b)\sim (c,d)&\Leftrightarrow&a\circ d=b\circ c\\
(c,d)\sim (e,f)&\Leftrightarrow&c\circ f=d\circ e.\\
\end{array}\]`
         * After multiplying both sides of both equations, rearranging the variables and cancelling we get
`\[\begin{array}{ccc}
(a\circ d)\circ (c\circ f)&=&(b\circ c)\circ (d\circ e)\\
a\circ d\circ c\circ f&=&b\circ c\circ d\circ e\\
(a\circ f)\circ \cancel{(d\circ c)}&=&(b\circ e)\circ \cancel{(d\circ c)}\\
&(a,b)&\sim&(e,f).&
\end{array}\]`
   * We have just shown that `\(\sim\)` is an equivalence relation. 
   * Therefore, each ordered pair `\((a,b)\)` represents its own equivalence class `\([a,b]\subseteq H\times H\)` and we can set `$G:=( H\times H)/\sim$` as the set of all these equivalence classes. 
   * However, because the relation `\(\sim\)` is symmetric and transitive, each equivalence class `\([a,b]\)` _does not(!)_ depend on the special choice of its representative `\((a,b)\)`. 
   * Therefore, we can define the operation `\(\ast\)` on `\(G\)` using _any_ representatives, e.g. the representatives `\((a,b)\)` and `\((c,d)\)` as we do in the following `$[a,b]\ast[c,d]:=[a\circ c,b\circ d].$`
   * Please note that `\(G\)` does contain equivalence classes suitable to define the above binary operation `$\ast,$` since `\(H\)` is not empty and so `\(G\)` is. 
   * Therefore, we have succeeded to define a non-empty set with a binary operation `\((G,\ast)\)`.
* Step 2: Demonstrate that `\((G,\ast)\)` is a [commutative group][bookofproofs$553].
   * We will show that the operation `\(\ast\)` is associative and commutative and that `\(G\)` contains a unique identity as well as each of its elements has a unique inverse. 
   * By construction, the operation `\(\ast\)` is associative:
`\[\begin{array}{rcl}([a,b]\ast[c,d])\ast[e,f]&=&([a\circ c,b\circ d])\ast[e,f]\\
&=&[a\circ c\circ e,b\circ d\circ f]\\
&=&[a,b]\ast([c\circ e,d\circ f])\\
&=&[a,b]\ast([c,d]\ast [e,f]).\end{array}\]`
   * By construction, the operation `\(\ast\)` is commutative:
`\[\begin{array}{rcl}[a,b]\ast[c,d]&=&[a\circ c,b\circ d]\\
&=&[c\circ a,d\circ b]\\
&=&[c,d]\ast[a,b].\end{array}\]`
   * Because `\(H\)` is cancellative, it follows for any `\((h,h)\in H\times H\)` that the equivalence class `\([h,h]\)` is an identity element of `\((G,\ast\)`):
`\[\begin{array}{rcl}[a,b]\ast[h,h]&=&[a\circ \cancel h,b\circ \cancel h]\\
&=&[\cancel h\circ a,\cancel h\circ b]\\
&=&[h,h]\ast[a,b]\\
&=&[a,b].\end{array}\]`
Please note that the identity `\([h,h]\)` is unique because, as an equivalence class, it does not dependent on the special choice of the representative `\((h,h)\)`.
   * Because `\(\circ\)` is commutative by assumption, for any `\([a,b]\in (G,\ast)\)`, the equivalence class `\([a,b]\)` is the unique inverse:
`\[\begin{array}{rcl}[a,b] \ast[b,a]&=&[a\circ b, b\circ a]\\
&=&[a\circ b, a\circ b]\\
&=&[h,h].\end{array}\]`
* Step 3: Demonstrate that `\((G,\ast)\)` fulfills property (1)
   * We shall show that there is a subset `\(S\subseteq G\)`, which is a [semigroup isomorphic][bookofproofs$838] to `\(H\)`, i.e. where `\((S,\ast)\simeq (H,\circ)\)`. 
   * We will do so by constructing the subset `\(S\subseteq G\)` and finding a bijective homomorphism `\(f:H\mapsto S\)`.
   * For the identity element `\([h,h]\in G\)`, consider the subset `$S:=\{[a\circ h,h]~|~a\in H\},$` and set `\[f:\begin{cases}H&\mapsto S\\a&\mapsto [a\circ h,h].\end{cases}\]`
   * Then `\(f\)` surjective by definition and it is injective since we can conclude that 
`\[\begin{array}{ccl}
f(a)=f(b)&\Leftrightarrow&[a\circ h,h]=[b\circ h,h]\\
&\Rightarrow&(a\circ h,h)\sim(b\circ h,h)\\
&\Rightarrow&(a\circ h)\circ h=h\circ (b\circ h)\\
&\Rightarrow&a\circ \cancel{h^2}=b\circ \cancel{h^2}\\
&\Rightarrow&a=b\\
\end{array}.\]`
Since `\(f\)` is both, surjective and injective, it is [bijective][bookofproofs$771].
   * `\(f\)` is also a [homomorphism][bookofproofs$401], since we have
`\[\begin{array}{ccl}
f(a\circ b)&=&[(a\circ b)\circ h,h]\\
&=&[(a\circ b)\circ h,h]\ast[h,h]\\
&=&[a\circ b\circ h\circ h,h\circ h]\\
&=&[(a\circ h)\circ (b\circ h),h\circ h]\\
&=&[a\circ h,h]\ast[b\circ h,h]\\
&=&f(a)\ast f(b).
\end{array}\]`
* Altogether, in steps 1 to 3, we have shown the isomorphism `\((S,\ast)\simeq (H,\circ)\)`.
* Step 4: Demonstrate that `\((G,\ast)\)` fulfills property (2)
   * We shall show that `\((G,\ast)\)` is minimal with the property (1). 
   * By construction of `\(S\subseteq G\)`, `\(G\)` contains all elements of the form `\([a\circ h,h]\)` for all `\(a\in H\)`. 
   * Because `\(G\)` is a group, it must also contain the inverse elements `\([h,a\circ h]\)` for all `\(a\in H\)`. 
   * Because `\((G,\ast)\)` is closed under `\(\ast\)`, we also have for all `$a,b\in H$`:
`\[\begin{array}{rcl}[a\circ h,h]\ast[h,b\circ h]&=&[a\circ \cancel{h\circ h},b\circ \cancel{h\circ h}]\\
&=&[a,b]\end{array}.\]`
   * This demonstrates that we cannot reduce `\(G\)` any further, e.g. by taking away any single equivalence class `\([a,b]\)`. 
   * Therefore `\(G\)` is minimal with the property (1).
