layout: proof
categories: branches,analysis
nodeid: bookofproofs$1631
orderid: 50
parentid: bookofproofs$1630
title: 
description:  Proof of FUNCTIONAL EQUATION OF THE EXPONENTIAL FUNCTION OF GENERAL BASE REVISED &#9733; master graduate maths &#10004; visit BookOfProofs now!
references: bookofproofs$581
keywords: base,equation,exponential,function,functional,general,revised,proof
contributors: bookofproofs

---


---

Assume that `\(f:\mathbb R\to \mathbb R\)` obeys the functional equation `\(f(x+y)=f(x)\cdot f(y)\)` for all `\(x,y\in\mathbb R\)`. Because of the functional equation, we must have `\[f(1)=f\left(\frac 12\right)^2.\]` Therefore, in any case `\(f(1)\ge 0\)`. 
https://www.bookofproofs.org/branches/functional-equation-of-the-exponential-function-of-general-base-revised/proof/#
Suppose `\(f(1)=0\)`. Then, `\(f\)` is a [constant function][bookofproofs$1371] and equals `\(0\)`, since:

`\[\begin{array}{rcll}
f(x)&=&f(x+0)&\text{existence of real zero}\\
f(x)&=&f(x+(-1)+1)&\text{existence of inverse real numbers with respect to addition}\\
&=&f((x-1)+1)&\text{associativity of addition}\\
&=&f(x-1)\cdot f(1)&\text{by assumed functional equation}\\
&=&f(x-1)\cdot 0&\text{by assumption }f(1)=0\\
&=&0&\text{existence of real zero}\\
\end{array}\]`

Above, we have used the [existence of real zero][bookofproofs$34], the [existence of inverse real numbers with respect to addition][bookofproofs$35], and the [associativity law of adding real numbers][bookofproofs$31].
Now, suppose `\(f(1) > 0\)`. Set `\(a:=f(1)\)`. Then, it follows from the [uniqueness of 1][bookofproofs$48] and from  `\(a=f(1 + 0)=f(1)\cdot f(0)=a\cdot f(0)\)` that `\(f(0)=1\)`.

Next, we will prove that 

> `\((i)\)` `\(f(n)=a^n\)` for all natural numbers `\(n\in \mathbb  N\)` 

> `\((ii)\)` `\(f(n)=a^n\)` for all integers `\(n\in \mathbb  Z\)` 

> `\((iii)\)` `\(f\left(\frac pq\right)=\sqrt[q]a^p\)` for all rational numbers `\(\frac pq\in \mathbb  Q\)` 

> `\((iv)\)` `\(f(x)=a^x\)` for all real numbers `\(x\in \mathbb R\)`, if `\(f\)` in addition is a [continuous real function][bookofproofs$219].
### ad `\((i)\)`

By [induction][bookofproofs$657], for the base case `\(n=1\)`, `\(f(1)=a\)`, and for the induction step `\(f(n+1)=f(n)\cdot f(1)=a^n\cdot a=a^{n+1}.\)`

### ad `\((ii)\)`

From the functional equation, it follows 
`\[1=0=f(n+(-n))=f(n)\cdot f(-n)\]`
and therefore `\[f(-n)=\frac 1{f(n)}=\frac 1{a^n}=a^{-n}.\]`

### ad `\((iii)\)`

From `\(a^p=f(p)=f\left(q\cdot \frac pq\right)=\left(f\left(\frac pq\right)\right)^q\)`, it follows `\(\sqrt[q]a^p=f\left(\frac pq\right)\)`.

### ad `\((iv)\)`

Let `\(x\)` be a [real number][bookofproofs$1105], i.e. `\(x\)` is a class of all rational Cauchy sequences, which equal each other except a difference, which is a rational Cauchy sequence converging to zero, formally `\[x\in\mathbb R\Longleftrightarrow x=(x_n)_{n\in\mathbb N}+I\]`
where `\((x_n)_{n\in\mathbb N}\)` is a [rational Cauchy sequence][bookofproofs$1485] representing the real number `\(x\)`, and

`\[I:=\{(i_n)_{n\in\mathbb N}~|~i_n\in\mathbb Q,\lim i_n=0\}\]`
is the set of all rational sequences, which converge to `\(0\)`. Now, we have 

`\[\begin{array}{rcll}
a^x&=&\lim_{n\to\infty}a^{x_n+i_n}&\text{due to the definition of real numbers}\\
&=&\lim_{n\to\infty}f(x_n+i_n)&\text{follows from }( i i i )\\
&=&\lim_{n\to\infty}f(x_n)\cdot f(i_n)&\text{by the assumed functional equation}\\
&=&f(x)\cdot f(0)&\text{continuity of }f\\
&=&f(x)\cdot 1&\text{according to }f(0)=1\\
&=&f(x)&\text{multiplication by }1.
\end{array}\]`

Above, we have used, in addition, the [existence of the real number 1][bookofproofs$40].
Finally, it remains to be shown that `\(f(x)=\exp_a(x)\)` for all `\(x\in\mathbb R\)` and all [positive real numbers][bookofproofs$1107] `\(a > 0\)`. This follows immediately from `\((iv)\)` and the [proposition about general powers of positive numbers][bookofproofs$1626].