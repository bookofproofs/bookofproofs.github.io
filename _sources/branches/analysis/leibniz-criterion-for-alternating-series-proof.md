layout: proof
categories: branches,analysis
nodeid: bookofproofs$1267
orderid: 50
parentid: bookofproofs$1266
title: 
description: Proof of CRITERION FOR ALTERNATING INFINITE SERIES LEIBNIZ ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$581
keywords: alternating series,alternating series criterion,criterion for alternating series,alternating infinite series,leibniz criterion,leibniz criterion series,proof
contributors: bookofproofs

---


---

* Let `$(a_n)_{n\in\mathbb N}$` being a [monotonically decreasing real series][bookofproofs$1155], which is convergent to `\(0\)`, i.e. with `\(\lim_{n\to\infty} a_n=0\)`. 
* Define the [partial sums][bookofproofs$1109] `$s_k:=\sum_{n=0}^k (-1)^n a_n.$` 
* Then, for the partial sums `\(s_k\)` with [even][bookofproofs$8130] indices we have that `$s_{2k+2}-s_{2k}=-a_{2k+1}+a_{2k+2}\le 0.$`
* Therefore, `$s_0\ge s_2\ge s_4\ge \ldots \ge s_{2k}\ge s_{2k+2}\ge\ldots.$`
* Since `\(s_{2k}\ge s_1=a_0-a_1\)` for all `\(k\)`,  the [subsequence][bookofproofs$1151] `\((s_{2k})_{k\in\mathbb N}\)` is [monotonically decreasing][bookofproofs$1155] and [bounded][bookofproofs$1136].
* Analogously, for the partial sums `\(s_k\)` with [odd][bookofproofs$8130] indices `$s_{2k+3}-s_{2k+1}=a_{2k+2}-a_{2k+3}\ge 0.$`
* Therefore, `$s_1\le s_3\le s_5\le \ldots \le s_{2k+1}\le s_{2k+3}\le\ldots.$`
* Since `\(s_{2k+1}\le s_0=a_0\)` for all `\(k\)`, the [subsequence][bookofproofs$1151] `\((s_{2k+1})_{k\in\mathbb N}\)` is [monotonically increasing][bookofproofs$1155] and [bounded][bookofproofs$1136].
* Therefore, according to the [monotone convergence theorem][bookofproofs$197], both sequences converge to some limits `$$\lim_{k\to\infty} s_{2k}=L\quad\text{and}\quad\lim_{k\to\infty} s_{2k+1}=U.\quad\quad( * )$$`
* In fact, `\(L=U\)`, since `$L-U=\lim_{k\to\infty}(s_{2k}-s_{2k+1})=\lim_{k\to\infty} a_{2k+1}=0.$`
* It remains to be shown that the common limit of the subsequences `\((s_{2k})_{k\in\mathbb N}\)` and `\((s_{2k+1})_{k\in\mathbb N}\)` is also a limit of the sequence `\((s_{k})_{k\in\mathbb N}\)` itself. 
   * Choose `\(\epsilon > 0\)` arbitrarily small, but fixed. 
   * Then, from `\( ( * ) \)`, it follows that there exist some indices `\(N_1(\epsilon),N_2(\epsilon)\in\mathbb N\)` with `$|s_{2k} - L| < \epsilon$` for all `$k\ge N_1(\epsilon),$` and `$|s_{2k+1}-U| < \epsilon$` for all `$k\ge N_2(\epsilon).$` 
   * It follows `$|s_{k} - L| < \epsilon$`  for all `$k\ge \max(N_1(\epsilon),N_2(\epsilon)).$` 
* This proves that the alternating series `$\sum_{n=0}^\infty (-1)^n a_n$` is [convergent][bookofproofs$175].