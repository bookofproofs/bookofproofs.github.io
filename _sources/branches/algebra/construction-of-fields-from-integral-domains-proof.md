layout: proof
categories: branches,algebra
nodeid: bookofproofs$889
orderid: 50
parentid: bookofproofs$888
title: 
description:  Proof of CONSTRUCTION OF FIELDS FROM INTEGRAL DOMAINS &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$696
keywords: construction,domains,fields,integral,proof
contributors: bookofproofs

---


---

#### Uniqueness

If `\((F_1, + , \cdot)\)` and `\((F_2,\ast, \circ)\)` where two different [fields][bookofproofs$557] fulfilling both properties (1) and (2), then because of the property (2), `\((F_1,+, \cdot)\)` would be a [subfield][bookofproofs$887] of `\((F_2,\ast, \circ)\)` and vice versa. Therefore, both fields must be the same.

#### Existence

To improve the readability, in our proof we write `\(ab\)` instead of `\(a\cdot b\)`. Our proof will be comprised of 4 steps:

### Step 1: Construct `\((F, \ast , \circ)\)` as a non-empty set with two binary operations: addition "`\( \ast \)`" and multiplication "`\( \circ \)`"

By assumption, `\((R, +, \cdot)\)` is an [integral domain][bookofproofs$821]. As a first step, we define an [equivalence relation][bookofproofs$574] on the [cartesian product][bookofproofs$748] `\(R\times (R\setminus\{0\})=\{(a,b)~|~a\in R,b\in R\setminus\{0\}\}\)` as follows:

`$$(a,b)\sim (c,d)\Leftrightarrow ad=bc,~~~~~~(a,c\in R;~b,d\in R\setminus\{0\}).$$`

Please note that this is indeed an equivalence relation, since it is reflexive, symmetric and transitive:
* The __reflexivity__ of "`\(\sim\)`" follows from the commutativity of multiplication in the integral domain `\((R, + , \cdot)\)`: `$$(a,b)\sim(a,b)\Leftrightarrow ab=ba,~~~~~~(a\in R;~b\in R\setminus\{0\}).$$`
* Also the __symmetry__ of "`\(\sim\)`" follows from the commutativity of multiplication in the integral domain `\((R, + , \cdot)\)`: 
`$$\begin{array}{ccl}
(a,b)\sim (c,d) &\Leftrightarrow& ad=bc\\
&\Leftrightarrow &cb=da\\
&\Leftrightarrow& (c,d)\sim (a,b),~~~~~~(a,c\in R;~b,d\in R\setminus\{0\}).
\end{array}$$`
* The __transitivity__ of  "`\(\sim\)`" follows from `\(R\)` being an integral domain: 
   * Assume for `\(a,c,e\in R;~b,d,f\in R\setminus\{0\}\)`:
\begin{align}\label{eq:889a}\begin{array}{ccc}
(a,b)\sim (c,d)&\Leftrightarrow&ad=bc\\
(c,d)\sim (e,f)&\Leftrightarrow&cf=de.\\
\end{array}\end{align}
   * After multiplying both sides of both equations, we can first rearrange the variables, because the multiplication is commutative in any integral domain, and get
\begin{align}\label{eq:889b}\begin{array}{ccc}
(ad)(cf)&=&(bc)(de)\\
adcf&=&bcde\\
(af)(dc)&=&(be)(dc)\\
\end{array}\end{align}
   * Now, if `\(c\neq 0\)`, then `\(d\in R\setminus\{0\}\)` means that also `\(d\neq 0\)`. Therefore we have `\(dc\neq 0\)`, because in `\(R\)` the element `\(0\)` is the only zero divisor. This means that we can cancel `\((dc)\)` in the equation \eqref{eq:889b}, resulting in
`$$\begin{array}{ccc}
(af)\cancel{(dc)}&=&(be)\cancel{(dc)}\\
&(a,b)\sim(e,f).&
\end{array}$$`
   * On the other hand, if `\(c=0\)`, then it follows from \eqref{eq:889a} and from `\(b,d,f\in R\setminus\{0\}\)`, and from the fact that `\(F\)` has no zero divisors except of `\(0\)` that we must have `\(a=e=0\)`, which means that `\((a,b)\sim(c,d)\)` degrades to `\((0,b)\sim(0,d)\Leftrightarrow 0\cdot d=b\cdot 0\Leftrightarrow 0=0\)`, and analogously  `\((c,d)\sim(e,f)\)` degrades to `\((0,d)\sim(0,f)\Leftrightarrow 0\cdot f=d\cdot 0\Leftrightarrow 0=0\)`, which again means `\((a,b)\sim(e,f)\)`. 
   * Therefore, "`\(\sim\)`" is transitive.


We have just shown that the relation "`\(\sim\)`" constitutes an equivalence relation. Therefore, each ordered pair `\((a,b)\)` represents its own equivalence class `\(\lbrack a,b\rbrack \subseteq R\times (R\setminus\{0\})\)` and we can set 
`$$F:=(R\times (R\setminus\{0\}))/\sim$$`
as the set of all these equivalence classes. However, because the relation `\(\sim\)` is symmetric and transitive, each equivalence class `\(\lbrack a,b\rbrack \)` __does not(!)__ depend on the special choice of its representative `\((a,b)\)`. Therefore, we can define two new binary operations `\(\ast\)`, `\(\circ\)` on `\(F\)` using __any__ representatives, e.g. the representatives `\((a,b)\)` and `\((c,d)\)` as we do in the following: 
`$$\begin{array}{ccl}
\lbrack a,b\rbrack \ast\lbrack c,d\rbrack &:=&\lbrack ad + cb,~bd\rbrack ,\\
\lbrack a,b\rbrack \circ\lbrack c,d\rbrack &:=&\lbrack ac,~bd\rbrack .\\
\end{array}$$`



Please note that `\(F\)` does contain equivalence classes suitable to define the above binary operations `\(\ast\)`, `\(\circ\)`. Because `\((R, + ,\cdot)\)` is an integral domain, it contains the element `\(0\)`, but also at least one other element `\(x\in R\)` with `\(x\neq 0\)`. Therefore, `\(F\)` is also not empty (i.e. it contains at least the two equivalence classes `\(\lbrack 0,x\rbrack \)` and `\(\lbrack x,x\rbrack \)` represented by `\((0,x)\)` and `\((x,x)\)`). Thus, we have succeeded to define a non-empty set with two binary operations `\((F,\ast,\circ)\)`.

### Step 2: Demonstrate that `\((F,\ast,\circ)\)` is a field

We will show the [defining properties of a field][bookofproofs$557], namely: 
1. `\((F,\ast)\)` is a commutative group with `\(\lbrack 0,x\rbrack \)` as neutral element (of addition "`\(\ast\)`")
1. `\(F^*:=(F \setminus \{\lbrack 0,x\rbrack \},\circ)\)` is a commutative group with `\(\lbrack x,x\rbrack \)` as neutral element (identity of multiplication "`\(\circ\)`")
1. The distributivity law holds for all `\(\lbrack a,b\rbrack ,\lbrack c,d\rbrack ,\lbrack e,f\rbrack \in F\)`.

Ad 1):
As mentioned in the last note on Step 1, `\(\lbrack 0,x\rbrack \in F\)`, so `\((F,\ast)\)` is not empty.

> a) The operation `\(\ast\)` is associative, because for all `\(\lbrack a,b\rbrack ,\lbrack c,d\rbrack ,\lbrack e,f\rbrack \in F\)` we have
`$$
\begin{array}{ccl}
(\lbrack a,b\rbrack \ast\lbrack c,d\rbrack )\ast \lbrack e,f\rbrack &=&\lbrack ad + cb,bd\rbrack \ast\lbrack e,f\rbrack \\
&=&\lbrack (ad + cb)f + ebd,bdf\rbrack \\
&=&\lbrack adf + cfb + edb,bdf\rbrack \\
&=&\lbrack adf + (cf + ed)b,bdf\rbrack \\
&=&\lbrack a,b\rbrack \ast\lbrack cf + ed,df\rbrack =\lbrack a,b\rbrack \ast(\lbrack c,d\rbrack \ast\lbrack e,f\rbrack ).\\
\end{array}$$`



> b) The operation `\(\ast\)` is commutative, because for all `\(\lbrack a,b\rbrack ,\lbrack c,d\rbrack \in F\)` we have
`$$
\begin{array}{ccl}
\lbrack a,b\rbrack \ast\lbrack c,d\rbrack &=&\lbrack ad + cb,bd\rbrack \\
&=&\lbrack cb + ad,db\rbrack =\lbrack c,d\rbrack \ast\lbrack a,b\rbrack .\\
\end{array}$$`

> c) The equivalence class `\(\lbrack 0,x\rbrack \)`, represented by `\((0,x)\)` with `\(0\in R;~x\in R\setminus\{0\}\)` is the neutral element of the operation `\(\ast\)`.
`$$
\begin{array}{ccl}
\lbrack a,b\rbrack \ast\lbrack 0,x\rbrack &=&\lbrack ax + 0\cdot b,bx\rbrack =\lbrack ax,bx\rbrack \\
&\Leftrightarrow&ax=xb\\
&\Leftrightarrow&a\cancel x=\cancel xb~~~~~~~~~\text{ note that we can cancel by }x\neq 0!\\
&\Leftrightarrow&a\cdot 1=1\cdot b\\
&\Leftrightarrow&\lbrack a\cdot 1,b\cdot 1\rbrack =\lbrack a,b\rbrack \\
\end{array}$$`

> d) Each equivalence class `\(\lbrack a,b\rbrack \in(F,\ast)\)` has an (additive) inverse element `\(\lbrack - a,b\rbrack \in(F,\ast)\)`.
`$$\lbrack a,b\rbrack \ast\lbrack  - a,b\rbrack =\lbrack ab - ba,bb\rbrack =\lbrack 0,bb\rbrack =\lbrack 0,x\rbrack ,$$`
because `\((0,bb)\sim(0,x)\)`.



Ad 2):
As mentioned in the last note on Step 1, `\(\lbrack x,x\rbrack \in F \setminus \{\lbrack 0,x\rbrack \}\)`, so `\((F \setminus \{\lbrack 0,x\rbrack \},\circ)\)` is not empty.

> a) The operation `\(\circ\)` is associative, because for all `\(\lbrack a,b\rbrack ,\lbrack c,d\rbrack ,\lbrack e,f\rbrack \in F \setminus \{\lbrack 0,x\rbrack \}\)` we have
`$$
\begin{array}{ccl}
(\lbrack a,b\rbrack \circ\lbrack c,d\rbrack )\circ \lbrack e,f\rbrack &=&\lbrack ac,bd\rbrack \circ\lbrack e,f\rbrack \\
&=&\lbrack (ac)e,(bd)f\rbrack \\
&=&\lbrack (a(ce),b(df)\rbrack \\
&=&\lbrack a,b\rbrack \circ\lbrack ce,df\rbrack \\
&=&\lbrack a,b\rbrack \circ(\lbrack c,d\rbrack \circ\lbrack e,f\rbrack ).\\
\end{array}$$`

> b) The operation `\(\circ\)` is commutative, because for all `\(\lbrack a,b\rbrack ,\lbrack c,d\rbrack \in F \setminus \{\lbrack 0,x\rbrack \}\)` we have
`$$
\begin{array}{ccl}
\lbrack a,b\rbrack \circ\lbrack c,d\rbrack &=&\lbrack ac,bd\rbrack \\
&=&\lbrack ca,db\rbrack =\lbrack c,d\rbrack \circ\lbrack a,b\rbrack .\\
\end{array}$$`

> c) The equivalence class `\(\lbrack x,x\rbrack \)`, represented by `\((x,x)\)` with `\(x\in R\setminus\{0\}\)` is the neutral element of the operation `\(\circ\)`.
`$$
\begin{array}{ccl}
\lbrack a,b\rbrack \circ\lbrack x,x\rbrack &=&\lbrack ax,bx\rbrack \\
&\Leftrightarrow&ax=xb\\
&\Leftrightarrow&a\cancel x=\cancel xb~~~~~~~~~\text{ note that we can cancel by }x\neq 0!\\
&\Leftrightarrow&a\cdot 1=1\cdot b\\
&\Leftrightarrow&\lbrack a\cdot 1,b\cdot 1\rbrack =\lbrack a,b\rbrack \\
\end{array}$$`



> d) Each equivalence class `\(\lbrack a,b\rbrack \in(F \setminus \{\lbrack 0,x\rbrack \},\circ)\)` has a (multiplicative) inverse element `\(\lbrack b,a\rbrack \in(F \setminus \{\lbrack 0,x\rbrack \},\circ)\)`.
`$$\lbrack a,b\rbrack \circ\lbrack b,a\rbrack =\lbrack ab,ba\rbrack =\lbrack x,x\rbrack ,$$`
because `\((ab,ba)\sim(x,x)\)`.

Ad 3):
In `\((F,\ast,\circ)\)`, the distributivity law is fulfilled, because for all `\(\lbrack a,b\rbrack ,\lbrack c,d\rbrack ,\lbrack e,f\rbrack \in F\)` we have
`$$
\begin{array}{ccl}
\lbrack a,b\rbrack \circ(\lbrack c,d\rbrack \ast\lbrack e,f\rbrack )&=&\lbrack a,b\rbrack \circ\lbrack cf + de,df\rbrack \\
&=&\lbrack a(cf + de),bdf\rbrack \\
&=&\lbrack acf + ade),bdf\rbrack \\
&=&\lbrack (acf + ade)b,(bdf)b\rbrack ~~~~~~~~~\text{ note that we can multiply by }b\neq 0!\\
&=&\lbrack (ac)(bf) + (ae)(bd),(bd)(bf)\rbrack \\
&=&\lbrack ac,bd\rbrack \ast\lbrack ae,bf\rbrack \\
&=&(\lbrack a,b\rbrack \circ\lbrack c,d\rbrack )\ast(\lbrack a,b\rbrack \circ\lbrack e,f\rbrack ).
\end{array}$$`


### Step 3: Demonstrate that `\((F,\ast,\circ)\)` fulfills property (1)

We shall show that there is a subset `\(S\subseteq F\)`, which is a [ring isomorphic][bookofproofs$885] to `\(R\)`, i.e. where `\((S, \ast, \circ)\simeq (R, +, \cdot)\)`. We will do so by constructing the subset `\(S\subseteq F\)` and finding a bijective homomorphism `\(f:R\mapsto S\)`.
* For the multiplicative identity element `\(\lbrack x,x\rbrack \in F\)`, consider the subset 
`$$S:=\{\lbrack ax,x\rbrack ~|~a\in R\},$$`
and set `$$f:\begin{cases}R&\mapsto S\\a&\mapsto \lbrack ax,x\rbrack .\end{cases}$$`
* Then `\(f\)` surjective by definition and it is injective since we can conclude that 
`$$\begin{array}{ccl}
f(a)=f(b)&\Leftrightarrow&\lbrack ax,x\rbrack =\lbrack bx,x\rbrack \\
&\Rightarrow&(ax,x)\sim(bx,x)\\
&\Rightarrow&(ax)x=x(bx)\\
&\Rightarrow&a\cancel{x^2}=b\cancel{x^2}~~~~~~~~~\text{ note that we can cancel by }x\neq 0!\\
&\Rightarrow&a=b\\
\end{array}.$$`
Since `\(f\)` is both, surjective and injective, it is [bijective][bookofproofs$771].
* `\(f\)` is also a [ring homomorphism][bookofproofs$885], since we have
`$$\begin{array}{ccl}
f(a+b)&=&\lbrack (a + b)x,x\rbrack \\
&=&\lbrack (ax + bx),x\rbrack \\
&=&\lbrack (ax)x + (bx)x,xx\rbrack ~~~~~~~~~\text{ note that we can multiply by }x\neq 0!\\
&=&\lbrack ax,x\rbrack \ast\lbrack bx,x\rbrack \\
&=&f(a)\ast f(b).
\end{array}$$`
On the other hand, we have also
`$$\begin{array}{ccl}
f(ab)&=&\lbrack (ab)x,x\rbrack \\
&=&\lbrack abx,x\rbrack \\
&=&\lbrack abxx,xx\rbrack ~~~~~~~~~\text{ note that we can multiply by }x\neq 0!\\
&=&\lbrack ax,x\rbrack \circ\lbrack bx,x\rbrack \\
&=&f(a)\circ f(b).
\end{array}$$`
Together, we have shown the isomorphism `\((S, \ast, \circ)\simeq (R, +, \cdot)\)`.



### Step 4: Demonstrate that `\((F,\ast,\circ)\)` fulfills property (2)

We shall show that `\((F,\ast,\circ)\)` is minimal with the property (1). By construction of `\(S\subseteq F\)`, `\(F\)` contains all elements of the form `\(\lbrack ax,x\rbrack \)` for all `\(x\in R \setminus \{0\}\)`. Because `\(F\)` is a field, it must also contain the inverse elements `\(\lbrack x,ax\rbrack \)` for all `\(a\in R \setminus \{0\}\)`. Because `\((F,\ast,\circ)\)` is closed under the operation `\(\circ\)`, we also have that

`$$\lbrack ax,x\rbrack \circ\lbrack x,bx\rbrack =\lbrack a \cancel{xx},b\cancel{xx}\rbrack =\lbrack a,b\rbrack ,~~~~~~(a\in R,~b\in R \setminus \{0\}).$$`
This demonstrates that we cannot reduce `\(F\)` further more, e.g. by taking away any single equivalence class `\(\lbrack a,b\rbrack \)`. Therefore `\(F\)` is minimal with the property (1).
