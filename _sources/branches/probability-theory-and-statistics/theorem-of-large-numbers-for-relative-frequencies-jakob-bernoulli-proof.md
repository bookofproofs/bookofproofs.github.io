layout: proof
categories: branches,probability-theory-and-statistics
nodeid: bookofproofs$1848
orderid: 50
parentid: bookofproofs$1838
title: 
description:  Proof of THEOREM OF LARGE NUMBERS FOR RELATIVE FREQUENCIES &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$856
keywords: bernoulli,frequencies,jakob,large,numbers,relative,theorem,proof
contributors: bookofproofs

---


---

For a [natural number][bookofproofs$718] `\(n\ge 1\)`, let `\(f_n(A)\)` be the [absolute frequency][bookofproofs$1837], in which the [event][bookofproofs$857] `\(A\)` could occur, if we repeat the [Bernoulli experiment][bookofproofs$1812] `\(n\)` times. We can interpret `\(f_n\)` as a [random variable][bookofproofs$1813] counting the number `\(k\)` of the realizations of `\(A\)` with `\(0\le f_n(A)=k\le n\)`. With this interpretation, it follows from the [binomial distribution][bookofproofs$450] that the [probability mass function][bookofproofs$1824] of `\(f_n\)` is given by 

`\[p(f_n=k)=\binom nk P^k(1-P)^{n-k}\quad\quad(k=0,1,\ldots n),\quad\quad( * )\]`

where `\(P:=p(A)\)` denotes the [probability][bookofproofs$858] of the [event][bookofproofs$857] `\(A\)`. Similarly, the [relative frequency][bookofproofs$1837] `\(F_n(A):=f_n(A)/n\)` can be interpreted as a random variable `\(F_n\)` with the possible realizations `\(0\le F_n\le n/n=1\)`. The probability mass function of `\(F_n\)` does not change   
`\[p\left(F_n=\frac kn\right)=\binom nk P^k(1-P)^{n-k}\quad\quad(k=0,1,\ldots n),\]`
because `\[F_n=\frac kn\Longleftrightarrow f_n=k.\quad\quad(* *)\]`

Let `\(\epsilon > 0\)` be an arbitrarily small [real number][bookofproofs$1105]. Note that the events `\((F_n < P - \epsilon)\)` and `\((F_n > P + \epsilon)\)` in each Bernoulli experiment repeated `\(n\)` times are [mutually exclusive][bookofproofs$859]. From the [definition of probability][bookofproofs$858] and the [definition of absolute value][bookofproofs$583] it follows that

`\[p(|F_n-P| > \epsilon)=p(F_n < P-\epsilon) + p(F_n > P+\epsilon).\]`

Because of `\(( * * )\)` and `\(( * )\)` , we can conclude further that


`\[\begin{array}{rcl}
p(|F_n-P| > \epsilon)&=&p(f_n < n(P-\epsilon)) + p(f_n > n(P+\epsilon))\\
&=&\sum_{k < n(P-\epsilon)}p(f_n=k)+\sum_{k > n(P+\epsilon)}p(f_n=k)\\
&=&\sum_{k < n(P-\epsilon)}\binom nk P^k(1-P)^{n-k}+\sum_{k > n(P+\epsilon)}\binom nk P^k(1-P)^{n-k}.
\end{array}\quad\quad ( * * * )\]` 

Applying the [distributivity law for real numbers][bookofproofs$520] and the [rules of calculation with inequations][bookofproofs$594], we observe that the summation indices `\(k\)` of both sums on the right side of `\(( * * * ) \)` fulfill a common property `\( ( \times ) \)` 

`\[\left.\begin{array}{rclcr}
k < n(P-\epsilon)&\Rightarrow& k < nP-n\epsilon&\Rightarrow& n\epsilon < nP-k\\
k > n(P+\epsilon)&\Rightarrow& k > nP+n\epsilon&\Rightarrow& k - nP > n\epsilon
\end{array}\right\}\Rightarrow(n\epsilon)^2 < (nP-k)^2\quad\quad ( \times )\]` 

By multiplying the respective left and right sides of the equation `\( ( * * * ) \)` by the inequation `\( ( \times ) \)`, we get the inequation

`\[\begin{array}{rcl}
(n\epsilon)^2p(|F_n-P| > \epsilon)& < &\sum_{k < n(P-\epsilon)}(nP-k)^2\binom nk P^k(1-P)^{n-k}+\sum_{k > n(P+\epsilon)}(nP-k)^2\binom nk P^k(1-P)^{n-k}.
\end{array}\]` 

Because `\(p(f_n=k)=0\)` for all `\(k < 0\)` and all `\(k > n\)`, we get finally the inequation

`\[\begin{array}{rcl}
(n\epsilon)^2p(|F_n-P| > \epsilon)& < &\sum_{k =0}^n(nP-k)^2\binom nk P^k(1-P)^{n-k}\\
&=&\sum_{k =0}^n(n^2P^2 - 2nPk +k^2)\binom nk P^k(1-P)^{n-k}\\
&=&\underbrace{n^2P^2\sum_{k =0}^n\binom nk P^k(1-P)^{n-k}}_{=:S_1}-\underbrace{2nP\sum_{k =0}^nk\binom nk P^k(1-P)^{n-k}}_{=:S_2}+\underbrace{\sum_{k =0}^nk^2\binom nk P^k(1-P)^{n-k}}_{=:S_3}\\
\end{array}\quad\quad ( \times\times )\]` 

Applying the [sum of binomial coefficients (i) ][bookofproofs$1841] for all `\(n\ge 0\)`, we obtain the result:

`\[S_1=n^2P^2\sum_{k =0}^n\binom nk P^k(1-P)^{n-k}=n^2P^2\cdot 1=n^2P^2.\]`

Similarly, applying the [sum of binomial coefficients (ii) ][bookofproofs$1843] for all for all `\(n\ge 1\)`, we obtain the result:

`\[S_2=-2nP\sum_{k =0}^nk\binom nk P^k(1-P)^{n-k}=-2nP\cdot nP=-2n^2P^2.\]`

For the third sum, applying the [sum of binomial coefficients (iii) ][bookofproofs$1845], we get for `\(n\ge 0\)`:

`\[S_3=\sum_{k =0}^nk^2\binom nk P^k(1-P)^{n-k}=nP(1-P)+n^2P^2.\]`


Thus, it follows from `\((\times\times)\)` and because the  `\(P(1-P)\)` for `\(P\in[0,1]\)` has its maximum at `\(\frac 12\)`:

`\[\begin{array}{rcll}
(n\epsilon)^2p(|F_n-P| > \epsilon)& < &nP(1-P)\\
&\Longleftrightarrow&\\
p(|F_n-P| > \epsilon)& < &\frac{P(1-P)}{n\epsilon^2}&\text{for a fixed }\epsilon > 0\text{ and all }n\ge 1\\
&\Longleftrightarrow&\\
p(|F_n-P| > \epsilon)& < &\frac{1}{4n\epsilon^2}&\text{for a fixed }\epsilon > 0\text{ and all }n\ge 1.\\
\end{array}\quad\quad ( \times\times\times )\]` 

It follows 

`\[\lim_{n\to\infty}p(|F_n(A)-P| > \epsilon)=0\quad\quad\text{for every fixed }\epsilon > 0.\]`

The [probability of the complement event][bookofproofs$861] is given by 

`\[\lim_{n\to\infty}p(|F_n(A)-P|\le \epsilon)=1\quad\quad\text{for every fixed }\epsilon > 0.\]`

Therefore, it is almost certain that the sequence members `\(F_n\)` will approximate the probability `\(P\)` with virtually any accuracy, if `\(n\)` is large enough.
