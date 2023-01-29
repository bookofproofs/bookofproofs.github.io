layout: proof
categories: branches,analysis
nodeid: bookofproofs$8400
orderid: 50
parentid: bookofproofs$8399
title: 
description: PROOF OF CALCULATIONS WITH UNIFORMLY CONVERGENT FUNCTIONS &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: 
keywords: calculations with uniformly convergent functions,proof
contributors: bookofproofs

---


---

By hypothesis, `$\mathbb F$` is either the [field of real numbers][bookofproofs$1640] or the [field of complex numbers][bookofproofs$1690], let `$D\subset \mathbb F.$` Let  `$f_n,g_n,f,g:D\to\mathbb F$` be [functions][bookofproofs$592], `$\alpha_n,\alpha\in\mathbb F,$` and let `$f_n\to f,$` `$g_n\to g$` are [uniformly convergent][bookofproofs$8382], and `$(\alpha_n)_{n\in\mathbb N}$` be a [sequence][bookofproofs$1249] with the limit `$\alpha_n\to \alpha.$`

* Ad `$f_n+g_n\to f+g$`
   * Using the [supremum norm][bookofproofs$8392], and applying the [triangle inequality][bookofproofs$588], we get `$||(f_n+g_n)-(f+g)||_\infty\le ||f_n-f||_\infty +||g_n-g||_\infty.$`
   * By assumption, `$f_n\to f$` and `$g_n\to g$`. 
   * Therefore, using the criterion [supremum norm and uniform convergence][bookofproofs$8393], from the assumption and the above inequality it follows `$$\lim_{n\to\infty}||(f_n+g_n)-(f+g)||_\infty=0,$$` in other words `$f_n+g_n$` is [uniformly convergent][bookofproofs$8382] to `$f+g$` on `$D.$`
* Ad `$\alpha f_n\to \alpha f$`
   * Similarly, `$||\alpha f_n-\alpha f||_\infty\le |\alpha|\cdot ||f_n-f||_\infty.$`
   * Again, using the criterion [supremum norm and uniform convergence][bookofproofs$8393], from `$f_n\to f$` and the above inequality oit follows 
`$$\lim_{n\to\infty}||(\alpha f_n-\alpha f)||_\infty=0.$$` 
   * Thus `$\alpha f_n\to \alpha f$` on `$D.$`

Now, assume that `$f_n,g_n$` are [bounded][bookofproofs$302] and that the [sequence][bookofproofs$1249] `$\alpha_n$` is [convergent][bookofproofs$1700] to `$\alpha.$`

* We will first show that `$f,g$` are bounded. 
   * By assumption `$f_n,g_n$` are [bounded][bookofproofs$302] for all `$n\in\mathbb N.$` 
   * By definition of bounded, there is a [positive real number][bookofproofs$1107] `$B > 0$` such that `$|f_n(x)| < B,$` `$|g_n(x)| < B$` for all `$n\in\mathbb N$` and all `$x\in D.$`  
   * By definition of [supremum norms][bookofproofs$8392], this yieds
      * `$||f||_\infty < B$` and
      * `$||g||_\infty < B.$`
   * Define `$\phi_n,\psi:D\to\mathbb N$` by `$f_n=\phi_n+f$` and `$g_n=\psi_n+g$` for all `$n\in\mathbb N.$`
   * From the triangle inequality, it follows for the [supremum norms][bookofproofs$8392] `$||f_n||_\infty\le ||\phi_n||_\infty + ||f||_\infty$` and `$||g_n||_\infty\le ||\psi_n||_\infty + ||g||_\infty.$`
   * Note that since `$f_n\to f$` and `$g_n\to g$` [uniformly][bookofproofs$8382], we have `$\phi_n\to 0$` and `$\psi\to 0$` uniformly.
   * Therefore, 
      * `$||f_n||_\infty\le 1 + ||f||_\infty$` and 
      * `$||g_n||_\infty\le 1 + ||g||_\infty.$`
   * On the other hand, from the uniform convergence and the [reverse triangle inequality][bookofproofs$6637] it follows for `$\epsilon = 1$` there is an index `$N\in\mathbb N$` such that for all `$x\in D$` and `$n\ge N$` 
      * `$|f(x)|-|f_n(x)|\le \left||f(x)|-|f_n(x)|\right|\le |f(x)-f_n(x)| < 1$` and
      * `$|g(x)|-|g_n(x)|\le \left||g(x)|-|g_n(x)|\right|\le |g(x)-g_n(x)| < 1.$` 
   * This yields for all `$x\in D$` and `$n\ge N$` 
      * `$|f(x)| < 1 + |f_n(x)|\le 1+||f_n||_\infty < 1+ B$` and 
      * `$|g(x)| < 1 + |g_n(x)|\le 1+||g_n||_\infty < 1+ B$`.
   * It follows that `$f,g$` are bounded on `$D.$`
* Ad `$f_ng_n\to fg$` 
   * Note that `$f_ng_n-fg=(f_n-f)g_n+(g_n-g)f.$`
   * Therefore, `$$\begin{array}{rcl}||f_ng_n-fg||_\infty&=&||(f_n-f)g_n+(g_n-g)f||_\infty\\
&\le&||(f_n-f)g_n||_\infty+||(g_n-g)f||_\infty\\
&\le&||(f_n-f)||_\infty||g_n||_\infty+||(g_n-g)||_\infty||f||_\infty\\
&\le&||(f_n-f)||_\infty B+||(g_n-g)||_\infty B.\\
\end{array}$$`
   * since `$f_n\to f$` and `$g_n\to g$` [uniformly][bookofproofs$8382], we have `$f_ng_n\to fg$` uniformly.
* Ad `$\alpha_n f_n\to \alpha f$`
   * This follows from `$f_ng_n\to fg$` as a special case for the [constant functions][bookofproofs$6342] `$g_n(x)=:\alpha_n$` for all `$x\in D.$`
