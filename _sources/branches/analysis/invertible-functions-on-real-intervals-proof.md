layout: proof
categories: branches,analysis
nodeid: bookofproofs$1382
orderid: 50
parentid: bookofproofs$1381
title: 
description:  Proof of INVERTIBLE FUNCTIONS ON REAL INTERVALS &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$581
keywords: functions,intervals,invertible,real,proof
contributors: bookofproofs

---


---

The proof involves three steps:

### `\((1)\)` Showing that `\(f\)` is [invertible][bookofproofs$407].
By hypothesis, `\([a,b]\)` is a [closed real interval][bookofproofs$1153] and `\(f:[a,b]\to\mathbb R\)` is a [strictly monotonically increasing][bookofproofs$282]  real function. (The proof is analogue for strictly monotonically decreasing functions). Therefore, for an `\(x\)` with `\(a < x < b\)` we have `\(A:=f(a) < f(x) < B:=f(b)\)`. Therefore, `\(f\)` is a function mapping the closed interval `\([a,b]\)` to the closed interval `\([A,B]\)`. Because from `\( x < x'\)` it follows that `\(f(x) < f(x')\)`, this function is [injective][bookofproofs$769]. Because `\(f\)` is a [continuous real function][bookofproofs$1260], it follows from the [intermediate value theorem][bookofproofs$1259] that `\(f\)` takes any value between `\(A\)` and `\(B\)`. Thus, `\(f\)` is also [surjective][bookofproofs$770]. Because `\(f\)` is both, injective and surjective, it is [bijective][bookofproofs$771]. As a bijective function, an inverse function `\(f^{-1}\)` must exist, thus `\(f\)` is invertible.

### `\((2)\)` Demonstrating that the inverse function `\(f^{-1}\)` is [strictly monotonically increasing][bookofproofs$282].
According to `\((1)\)`, it follows from `\( x < x'\)` that `\(f(x) < f(x')\)`. Analogously, we can conclude from `\(f(x) < f(x') \)` that `\(f^{-1}\circ f(x)= x < f^{-1}\circ f(x')=x'\)`.  (The proof is analogue for strictly monotonically decreasing functions).

### `\((3)\)` Proving that the inverse function `\(f^{-1}\)` is [continuous][bookofproofs$1260].
The proof will be [by contradiction][bookofproofs$744]. Suppose, `\(y\in[A,B]\)` and `\((y_n)_{n\in\mathbb N}\)` is [real sequence][bookofproofs$875] with `\(y_n\in[A,B]\)` and `\(\lim_{n\to\infty} y_n=y\)`, but `\(\lim_{n\to\infty} f^{-1}(y_n)\neq f^{-1}(y)\)`. We will show that this cannot be true, i.e. it must be `\(\lim_{n\to\infty} f^{-1}(y_n)=f^{-1}(y)\)`, which is equivalent to `\(f^{-1}\)` being continuous.

`\(\lim_{n\to\infty} f^{-1}(y_n)\neq f^{-1}(y)\)` would imply that there exists an `\(\epsilon > 0\)` with `\[|f^{-1}(y_n)-f^{-1}(y)| \ge \epsilon\]` for infinitely many `\(n\)`. Therefore there exists a [subsequence][bookofproofs$1151] `\((y_{n_k})_{k\in\mathbb N}\)` with 
`\[|f^{-1}(y_{n_k})-f^{-1}(y)| \ge \epsilon\]` 
for all `\(k\in\mathbb N\)`. Because by definition `\(a < f^{-1}(y_{n_k})_{k\in\mathbb N} < b\)`, the sequence `\((f^{-1}(y_{n_k}))_{k\in\mathbb N}\)` is [bounded][bookofproofs$1136], thus it contains another subsequence,  which is convergent due to the [theorem of Bolzano-Weierstrass][bookofproofs$1152].
Let's call this other subsequence `\((f^{-1}(y_{n_j}))_{j\in\mathbb N}\)` and let's assume `\(\lim_{j\to\infty} f^{-1}(y_{n_j})=c\)`. Note that, since [convergence preserves upper and lower bounds][bookofproofs$1145], it must follow from 
`\[|f^{-1}(y_{n_j})-f^{-1}(y)| \ge \epsilon\]`
for all `\(j\in\mathbb N\)` that 
`\[|c-f^{-1}(y)| \ge \epsilon\quad\quad( * ).\]`
Now, note that `\(f(f^{-1}(y_{n_j}))=y_{n_j}\)` and that from the continuity of `\(f\)` it follows 
`\[y=\lim_{n\to\infty}y_n=\lim_{j\to\infty}f(f^{-1}(y_{n_j}))=f(\lim_{j\to\infty}f^{-1}(y_{n_j}))=f( c).\]`
This would mean that `\(f^{-1}(y)=f^{-1}(f( c))=c\)`, which is a contradiction to `\( ( * )\)`. Thus, our assumption must be wrong and `\(f^{-1}\)` must be continuous.
