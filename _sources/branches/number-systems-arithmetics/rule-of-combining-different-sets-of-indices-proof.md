layout: proof
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1120
orderid: 50
parentid: bookofproofs$1119
title: 
description:  Proof of RULE OF COMBINING DIFFERENT SETS OF INDICES &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$1112
keywords: combining,different,indices,rule,sets,proof
contributors: bookofproofs

---


---

It is required for the sets of [integers][bookofproofs$844] `\(K\)` and `\(L\)` to be [finite][bookofproofs$985], which makes sure that the sums to be added are well-defined.

Using the [Iverson-notation][bookofproofs$261] of sums, which allows to obtain the values `\(0\)` or `\(1\)` from logical statements in the middle of a formula, we can write the sums as

`\[\begin{array}{rcl}
\sum_{k\in K} a_k + \sum_{k\in L} a_k &=& \sum_{k} a_k[k\in K] + \sum_{k} a_k[k\in L]\\
&=&\sum_{k} a_k([k\in K] + [k\in L]),
\end{array}\]`

where the last step was obtained by applying the [associative rule][bookofproofs$1114]. Now, the sum of logical statements `\([k\in K] + [k\in L]\)` can only have the following values:

`\[[k\in K] + [k\in L]=\cases{
0,\quad\text{if }k\not\in (K \cup L)\\
1,\quad\text{if }k\in (K \cup L) \wedge k\not\in (K \cap L)\\
2,\quad\text{if }k\in (K \cap L)
}
\]`

Therefore, we can continue our calculations by 

`\[\begin{array}{rcl}
\sum_{k} a_k([k\in K] + [k\in L])&=&\underbrace{0}_{\text{case 0}}+\underbrace{\sum_k a_k[K\cup L]-\sum_k a_k[K\cap L]}_{\text{case 1}}+\underbrace{2\sum_k a_k[K\cap L]}_{\text{case 2}}\\
&=&\sum_k a_k[K\cup L]+\sum_k a_k[K\cap L]\\
&=&\sum_{k\in K\cup L} a_k+\sum_{k\in K\cap L}a_k,
\end{array}
\]`

which completes the proof.
