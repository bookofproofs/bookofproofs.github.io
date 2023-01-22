layout: proof
categories: branches,algebra
nodeid: bookofproofs$1100
orderid: 0
parentid: bookofproofs$274
title: 
description:  Proof of FACTOR RINGS, GENERALIZATION OF CONGRUENCE CLASSES &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$696
keywords: factor rings,factor ring,proof
contributors: bookofproofs

---


---

We will show the lemma in five steps, by proving the existence of an additive group `\((R/I,\oplus)\)`, introducing a multiplication operation "`\(\odot\)`",  and proving the ring properties of the resulting algebraic structure `\((R/I,\oplus,\odot)\)`. 

### `\((1)\)` Existence of the additive group `\((R/I,\oplus)\)`

By hypothesis, `\(I\lhd R\)` is an [ideal][bookofproofs$1062] of the [ring][bookofproofs$683] `\( ( R, + ,\cdot )\)`. Thus, by definition of any ideal, `\( ( I, + )\)` is a subgroup of the additive group `\((R, + )\)`. Moreover, since `\( ( R, + ,\cdot )\)` is a ring, the group `\((R,+)\)` and its subgroup `\((I , + )\)` are commutative. Therefore, `\((I , + )\)` is a [normal subgroup][bookofproofs$273] of `\((R , + )\)`. According to the corresponding lemma, there exists an (here additive) [factor group][bookofproofs$191] `\((R/I ,\oplus)\)`, while the addition "`\(\oplus\)`" is defined by 

`\[(r_1 + I)\oplus(r_2+I):=(r_1 +  r_2)+I\quad\quad(r_1,r_2\in R).\]`

According to this lemma, the operation "`\(\oplus\)`" is well-defined, because it does not depend on the particular choice of representatives `\(r_1,r_2\)`. Also, the elements of `\((R/I ,\oplus)\)` are residue classes `\(r+I~(r\in R)\)`, its identity element is `\(I\)`. The inverse of an element `\((r + I)\in R/I \)` is `\( (-r + I)\in R/I \)`.

### `\((2)\)` the factor group `\((R/I,\oplus)\)` is Abelian

This follows immediately from the commutativity of the group `\((R, + )\)` and the definition 

`\[(r_1 + I)\oplus(r_2+I)=(r_1 +  r_2)+I=(r_2 +  r_1)+I=(r_2 + I)\oplus(r_1+I).\]`

### `\((3)\)` In `\(R/I\)`, we can also define a multiplication "`\(\odot\)`" by `\((r_1 + I)\odot(r_2+I):=(r_1 \cdot  r_2)+I\)`, which does not depend on the representatives `\(r_1,r_2\in R\)`.

To realize it, suppose `\(r_1,s_1\in R\)` are two different representatives of the residue class `\(r_1 + I\)` in `\(R/I\)` and `\(r_2,s_2\in R\)` are two different representatives of the residue class `\(r_2 + I\)` in `\(R/I\)`. We have to show that
`\[(r_1 \cdot  r_2)+I=(s_1 \cdot  s_2)+I.\]` 
By our assumption
`\[\begin{array}{ccl}
s_1=r_1+i_1\quad (i_1\in I),\\
s_2=r_2+i_2\quad (i_2\in I).\\
\end{array}\]`
Therefore 
`\[(s_1\cdot s_2) + I=((r_1+i_1)\cdot(r_2+i_2))+ I=(r_1\cdot r_2+\underbrace{r_1\cdot i_2+i_1\cdot r_2+i_1\cdot i_2}_{\in I,\text{ since }I\text{ is an ideal }})+ I=(r_1\cdot r_2)+ I.\]`

Thus, the multiplication defined like this does not depend on the representatives `\(r_1,r_2\in R\)`.

### `\((4)\)` The algebraic structure `\((R/I,\odot)\)` is a semigroup, i.e. the multiplication "`\(\odot\)`" is associative.

The associativity follows for any `\((r_1 + I),(r_2 + I),(r_3 + I)\in R/I\)` from 

`\[\begin{array}{ccl}
(r_1+I)\odot((r_2+I)\odot(r_3+I))&=&(r_1+I)\odot((r_2\cdot r_3)+I)\\
&=&(r_1\cdot(r_2\cdot r_3))+I\\
&=&((r_1\cdot r_2)\cdot r_3)+I\quad\quad("\cdot"\text{ is associative!})\\
&=&((r_1\cdot r_2)+I)\odot (r_3+I)\\
&=&((r_1+I)\odot(r_2+I))\odot (r_3+I)\\
\end{array}\]`

Note, that if `\((R,\cdot)\)` is a monoid, so is `\((R/I,\odot)\)`. For if `\(1\)` is the identity element of `\((R,\cdot)\)`, then the identity element of `\((R/I,\odot)\)` is `\((1 + I)\)`, since for any `\(r+I\in R/I\)`

`\[\begin{array}{ccl}
(r+I)\odot(1+I) = (r\cdot 1)+I=r+I,\\
(1+I)\odot(r+I) = (1\cdot r)+I=r+I.\\
\end{array}\]`

Therefore, `\(R/I\)` is an unit ring, if and only if `\(R\)` is.

### `\((5)\)` The distributivity laws hold for "`\(\oplus\)`" and "`\(\odot\)`".

For any `\((r_1 + I),(r_2 + I),(r_3 + I)\in R/I\)` we have:

`\[\begin{array}{ccl}
(r_1 + I)\odot((r_2 + I)\oplus(r_3 + I)) &=&(r_1 + I)\odot((r_2 + r_3) + I)\\
&=&(r_1 \cdot(r_2 + r_3)) + I\\
&=&((r_1 \cdot r_2) + (r_1 \cdot r_3)) + I\\
&=&((r_1 \cdot r_2)+I)\oplus((r_1 \cdot r_3) + I)\\
&=&((r_1+I) \odot (r_2+I))\oplus((r_1+I) \odot (r_3 + I))
\end{array}\]`
and
`\[\begin{array}{ccl}
((r_1 + I)\oplus(r_2 + I))\odot(r_3 + I) &=&((r_1 + r_2)+ I)\odot(r_3 + I)\\
&=&((r_1+r_2)\cdot r_3) + I\\
&=&((r_1 \cdot r_3) + (r_2 \cdot r_3)) + I\\
&=&((r_1 \cdot r_3)+I)\oplus((r_2 \cdot r_3) + I)\\
&=&((r_1+I) \odot (r_3+I))\oplus((r_2+I) \odot (r_3 + I)).
\end{array}\]`

We have proven the resulting algebraic structure `\((R/I,\oplus,\odot)\)` to be a ring, es required.
