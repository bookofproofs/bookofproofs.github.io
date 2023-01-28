layout: proof
categories: branches,algebra
nodeid: bookofproofs$7954
orderid: 50
parentid: bookofproofs$7953
title: 
description:  Proof of ELEMENTARY GAUSSIAN OPERATIONS DO NOT CHANGE THE SOLUTIONS OF AN SLE &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$7937
keywords: change,elementary,gaussian,not,operations,sle,solutions,proof
contributors: bookofproofs

---


---

* Let an [SLE][bookofproofs$1044]  be given in the form of an [extended coefficient matrix][bookofproofs$7941] `$A|\gamma.$`
* We want to prove that the [elementary Gaussian operations][bookofproofs$7952] do not change the [set][bookofproofs$550] `$S$` of the solutions of the SLE.
   * Exchanging the rows of `$A|\gamma.$`
      * This elementary Gaussian operation does not change `$S$` because the exchanged rows just change the order of the equations listed in the SLE and the order of the equations does not influence the simultaneous solution of the whole SLE.
   * Exchanging the columns of `$A$`
      * This elementary Gaussian operation corresponds to a renaming of the unknowns in each of the equations in the whole SLE. Certainly, the solutions `$S$` do not change if we rename the unknowns.
   * Multiplying a row of `$A|\gamma$` by a number `$c\neq 0.$`
      * This elementary Gaussian operation transforms an equation 
`$$\alpha_{i1}x_1+\alpha_{i2}x_2+\ldots+\alpha_{in}x_n=\gamma_i$$`
into
`$$c\alpha_{i1}x_1+c\alpha_{i2}x_2+\ldots+c\alpha_{in}x_n=c\gamma_i.$$`
Clearly, since both sides of the equation are multiplied by the same number `$c\neq 0$`, any existing replacement of the unknowns solving the first equation will also solve the second equation and vice versa. Therefore, the set `$S$` of the simultaneous solutions of the whole SLE does not change in this case, either.
   * Adding a multiple of one row of `$A|\gamma$` to another row of `$A|\gamma$` 
      * This elementary Gaussian operation transforms two equations 
`$$\begin{array}{rcl}\alpha_{i1}x_1+\alpha_{i2}x_2+\ldots+\alpha_{in}x_n&=&\gamma_i\\
\alpha_{j1}x_1+\alpha_{j2}x_2+\ldots+\alpha_{jn}x_n&=&\gamma_j\end{array}\quad\quad( * )$$`
into
`$$\begin{array}{rcl}(\alpha_{i1}+c\alpha_{j1})x_1+(\alpha_{i2}+c\alpha_{j2})x_2+\ldots+(\alpha_{in}+c\alpha_{jn})x_n&=&\gamma_i+c\gamma_j\\
\alpha_{j1}x_1+\alpha_{j2}x_2+\ldots+\alpha_{jn}x_n&=&\gamma_j\end{array}\quad\quad( * * )$$`
It follows from the [distributivity property of the field][bookofproofs$557] `$F$` that any simultaneous solution `$(s_1,\ldots,s_n)$` of `$( * )$` is also a solution of `$( * * ).$` If, conversely, `$(s_1,\ldots,s_n)$` is a solution of `$( * * )$`, then we can transform the first equation into the original form `$( * )$` by adding the `$-c$`-th mutliple of the `$j$`-th row, and `$(s_1,\ldots,s_n)$` will remain the simultaneous solution of the new two equations `$( * ).$` Therefore, this type of elementary Gaussian operation does not change the set `$S$` of solutions to SLE, either.
* In summary, all four elementary Gaussian operations do not change the solution set `$S$` of any given SLE.
