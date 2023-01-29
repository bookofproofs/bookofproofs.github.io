layout: proof
categories: branches,analysis
nodeid: bookofproofs$1627
orderid: 50
parentid: bookofproofs$1626
title: 
description:  Proof of GENERAL POWERS OF POSITIVE NUMBERS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$581,bookofproofs$696
keywords: general powers of positive numbers,general powers,general power,proof
contributors: bookofproofs

---


---

We have already proven that [rational exponents, the power function is identical to the exponential function of general base][bookofproofs$1622], i.e. 
`\[a^x=\exp_a(x),\quad\quad x\in\mathbb Q.\]`
Now, we will prove that the expression `\(a^x\)` makes perfectly sense and this equation also holds[^1], if we allow `\(x\)` to be a general real number. 
According to the [definition of real numbers][bookofproofs$1105], a real number `\(x\)` is a class of all rational Cauchy sequences, which equal each other except a difference, which is a rational Cauchy sequence converging to zero, formally `\[x\in\mathbb R\Longleftrightarrow x=(x_n)_{n\in\mathbb N}+I\]`
where `\((x_n)_{n\in\mathbb N}\)` is a [rational Cauchy sequence][bookofproofs$1485] representing the real number `\(x\)`, and

`\[I:=\{(i_n)_{n\in\mathbb N}~|~i_n\in\mathbb Q,\lim i_n=0\}\]`
is the set of all rational sequences, which converge to `\(0\)`. Now, we have 

`\[\begin{array}{rcll}
a^x&=&\lim_{n\to\infty}a^{x_n+i_n}&\text{due to the definition of real numbers}\\
&=&\lim_{n\to\infty}\exp_a(x_n+i_n)&\text{definition of rational powers of positive numbers}\\
&=&\lim_{n\to\infty}\exp_a(x_n)\cdot \exp_a(i_n)&\text{functional equation of exponential function of general base}\\
&=&\exp_a(x)\cdot \exp_a(0)&\text{continuity of exponential function of general base}\\
&=&\exp_a(x)\cdot \exp(0\cdot \ln(a))&\text{definition of exponential function of general base}\\
&=&\exp_a(x)\cdot \exp(0)&\text{multiplication by }0\\
&=&\exp_a(x)\cdot 1&\text{proposition stating that} \exp(0)=1\\
&=&\exp_a(x)&\text{multiplication by }1\\
\end{array}\]`

Above, we have used, among others, the following propositions:
* [functional equation of exponential function of general base][bookofproofs$1612],
* [continuity of exponential function of general base][bookofproofs$1610], and the
* [proposition stating that][bookofproofs$1423] `\(\exp(0)=1\)`.




[^1]: E.g. a general power `\(3^\pi\)` makes perfectly sense, although it makes no sense to say that we "multiply `\(\pi\)` copies of `\(3\)` together".
