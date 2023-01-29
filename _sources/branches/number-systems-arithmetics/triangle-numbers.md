layout: definition
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1410
orderid: 200
parentid: bookofproofs$405
title: Triangle Numbers
description: TRIANGLE NUMBERS &#9733; bring your math skills to the graduate level &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: 
keywords: numbers,triangle
contributors: bookofproofs


---


---

If we put building bricks into rows, beginning from `\(1\)` brick in the first row, `\(2\)` bricks in the second, and so on, the total number of bricks is the `\(n\)`-th **triangle number** `\(\Delta_n\)`:

|`\[\begin{array}{c}
\fbox x
\end{array}\]`|`\[\begin{array}{cc}
\fbox x\\
\fbox x&\fbox x
\end{array}\]`|`\[\begin{array}{ccc}
\fbox x\\
\fbox x&\fbox x\\
\fbox x&\fbox x&\fbox x
\end{array}\]`|`\[\begin{array}{cccc}
\fbox x\\
\fbox x&\fbox x\\
\fbox x&\fbox x&\fbox x\\
\fbox x&\fbox x&\fbox x&\fbox x
\end{array}\]`|`\[\begin{array}{ccccc}
\fbox x\\
\fbox x&\fbox x\\
\fbox x&\fbox x&\fbox x\\
\fbox x&\fbox x&\fbox x&\fbox x\\
\fbox x&\fbox x&\fbox x&\fbox x&\fbox x
\end{array}\]`|`\(\cdots\)`|

`\(\Delta_1:=1\)` | `\(\Delta_2:=3\)` | `\(\Delta_3:=6\)` | `\(\Delta_4:=10\)` | `\(\Delta_5:=15\)` | `\(\cdots\)`
:------------- |:------------- |:------------- |:------------- |:------------- |:-------------

The general formula for the `\(n\)`-th triangle number is

`\[\Delta_n=\sum_{k=1}^n n=1+2+\cdots+n=\frac {(n+1)n}{2},\]`

which can easily be proven as a special case of the [sum of arithmetic progression][bookofproofs$1117].

The sequence of triangle numbers begins with `\(1\)`, `\(3\)`, `\(6\)`, `\(10\)`, `\(15\)`, `\(21\)`, `\(28\)`, `\(36\)`, ...
