layout: proof
categories: branches,analysis
nodeid: bookofproofs$1396
orderid: 50
parentid: bookofproofs$1390
title: 
description:  Proof of CAUCHY PRODUCT OF ABSOLUTELY CONVERGENT SERIES &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: 
keywords: cauchy product,absolutely convergent series,absolutely convergent,cauchy product of series,proof
contributors: bookofproofs

---


---

We begin the proof with a number of definitions: We set 


`\[\begin{array}{c}
A:=\sum_{n=0}^\infty a_n,\quad A_n:=\sum_{k=0}^n a_k\\
B:=\sum_{n=0}^\infty b_n,\quad B_n:=\sum_{k=0}^n b_k\\
c_n:=\sum_{k=0}^n a_{n-k}b_k,\quad C_n:=\sum_{k=0}^n c_k\\
D_n:=\left(\sum_{k=0}^n a_k\right)\left(\sum_{k=0}^n b_k\right)=A_n\cdot B_n\\
D_n^*:=\left(\sum_{k=0}^n |a_k|\right)\left(\sum_{k=0}^n |b_k|\right).
\end{array}\]`

The proof is in two steps:


### `\( (1) \)` We will first show that `\(\lim_{n\to\infty} C_n=A\cdot B\)`.

By hypothesis, `\(A\)` and `\(B\)` are [absolutely convergent series][bookofproofs$198], which by definition means that `\(\sum_{n=0}^\infty |a_n|\)` and `\(\sum_{n=0}^\infty |b_n|\)` are [convergent series][bookofproofs$175]. Due to the rule of the [product of convergent sequences][bookofproofs$1135], it follows that the [real sequences][bookofproofs$875] `\((D_n^*)_{n\in\mathbb N}\)` is a [convergent sequence][bookofproofs$141]. This in turn means by definition that for a fixed `\(\epsilon > 0\)` there is an index `\(m\in\mathbb N\)` with
`\[|D_n^*- D_m^*| < \epsilon\]`

 for all `$n\ge m$`  and, in particular, for all `$n > 2m.$` Note that if `\( n > 2m \)`, then[^1] 
`\[\begin{array}{rcl}
D_n^* - D_m^*&=&\sum_{\substack{0\le i\le n \\ 0\le j\le n}} |a_i||b_j|-\sum_{\substack{0\le i\le m \\ 0\le j\le m}} |a_i||b_j|\\
&=&\sum_{i,j} |a_i||b_j|[0\le i\le n\wedge   0\le j\le n]-\sum_{i,j}|a_i||b_j|[0\le i\le m\wedge   0\le j\le m]\\
&=&\sum_{i,j} |a_i||b_j|[m < i \le n\wedge   m < j\le n].\quad\quad ( * )
\end{array}\]`

We will use this as an interim result.

Now, observe that first: 
`\[D_n=\left(\sum_{k=0}^n a_k\right)\left(\sum_{k=0}^n b_k\right)=\sum_{\substack{0\le i\le n \\ 0\le j\le n}} a_ib_j=\sum_{i,j} a_ib_j[0\le i\le n\wedge 0\le j\le n]\]`
and that second
`\[C_n=\sum_{k=0}^n c_k=\sum_{k=0}^n \sum_{j=0}^k a_{k-j}b_j=\sum_{k=0}^n \sum_{i+j=k} a_ib_j=\sum_{i+j\le n} a_ib_j=\sum_{i,j} a_ib_j[i+j\le n]\]`
and that third, according to the [triangle inequality][bookofproofs$588] and the [properties of the absolute value][bookofproofs$619].
`\[\begin{array}{rcl}
|D_n - C_n|&=&\left|\sum_{i,j} a_ib_j[0\le i\le n\wedge   0\le j\le n] - \sum_{i,j} a_ib_j[i+j\le n]\right|\\
&=&\left|\sum_{i,j} a_ib_j[0\le i\le n\wedge   0\le j\le n\wedge  i+j > n]\right|\\
&\le &\sum_{i,j} |a_i||b_j|[0\le i\le n\wedge   0\le j\le n\wedge  i+j > n]\quad\quad ( * * )
\end{array}\]`
This is our second interim result.

Now, once again since `\(A\)` and `\(B\)` are absolutely convergent series, [they are in particular convergent][bookofproofs$1268]. Therefore, the [real sequences][bookofproofs$875] of their partial sums `\((A_n)_{n\in\mathbb N}\)` and `\((B_n)_{n\in\mathbb N}\)`  are [convergent sequences][bookofproofs$141] with `\(\lim A_n=A\)` and `\(\lim B_n=B\)`. Like in the reasoning above, due to the rule of the [product of convergent sequences][bookofproofs$1135], we have
`\[\lim_{n\rightarrow\infty} D_n=\lim_{n\rightarrow\infty} (A_n \cdot B_n)=\lim_{n\rightarrow\infty} A_n \cdot \lim_{n\rightarrow\infty} B_n=A\cdot B.\]`
Thus, it suffices to demonstrate that 
`\[\lim_{n\to\infty} (D_n - C_n)=0.\]`
But this will follow immediately, if we can show that for a given `\(\epsilon > 0\)` and all `\(n > 2m\)` the set of possible index pairs  `\(\{(i,j)\}\)` in the sum  `\( ( * * ) \)` is included in the set of index pairs `\(\{(i,j)\}\)`, which are possible  in the sum  `\( ( * ) \)`. If this is the case, the inequality
`\[|D_n - C_n| \le |D_n^*- D_m^*| < \epsilon\text{ for all }n\ge 2m\]`
will be true. But the set of possible index pairs  `\(\{(i,j)\}\)` in the sum  `\( ( * * ) \)` is indeed included in the set of index pairs `\(\{(i,j)\}\)`, which are possible  in the sum  `\( ( * ) \)`, like demonstrated in the following figure


![cauchyproductproof](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/cauchyproductproof.jpg?raw=true)


This is a pure geometric argument, since for `\(n > 2m\)` the hatched area is totally included in the blue area. Therefore, we have `\(\lim_{n\to\infty} (D_n - C_n)=0,\)` and `\(\lim_{n\to\infty} C_n=A\cdot B\)`.

### `\( (2) \)` It remains to be shown  `\(\sum_{n\to\infty} c_n\)` is absolutely convergent.

We have to show that `\(\sum_{n\to\infty}|c_n|\)` is convergent. It has already been shown that the real sequence `\((D_n^*)_{n\in\mathbb N}\)` is a [convergent sequence][bookofproofs$141]. Moreover, we have in the Iverson notation

`\[D_n^*=\sum_{i,j} |a_i||b_j|[0\le i\le n\wedge   0\le j\le n].\quad\quad ( \times )\]`

On the other hand, it follows from the triangle inequality that 
`\[\sum_{k=0}^n |c_k|=\sum_{k=0}^n \left|\sum_{j=0}^k a_{k-j}b_j\right|\le \sum_{k=0}^n \sum_{i+j=k} |a_i||b_j|=\sum_{i,j} |a_i||b_j|[i+j\le n]\quad\quad ( \times\times )\]`

Following a similar geometric argument as above, the set of of possible index pairs  `\(\{(i,j)\}\)` in the sum  `\( ( \times\times ) \)` is included in the set of index pairs `\(\{(i,j)\}\)`, which are possible  in the sum  `\( ( \times ) \)` - see following figure


![cauchyproductproof1](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/cauchyproductproof1.jpg?raw=true)


Therefore, we have 

`\[\sum_{k=0}^n |c_k|\le D_n^*\]`
and it follows from the [majorant criterion][bookofproofs$1270] that `\(\sum_{n\to\infty}|c_n|\)` is convergent.

[^1]: In the following text, the [Iverson notation for sum][bookofproofs$261] is used, which turns out to be very helpful in sum manipulation steps.
