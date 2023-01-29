layout: example
categories: branches,theoretical-computer-science, computability
nodeid: bookofproofs$1188
orderid: 50
parentid: bookofproofs$1180
title: Simulating More Complex Commands Using Basic `\(L O O P\)` Commands
description: SIMULATING MORE COMPLEX COMMANDS USING BASIC \L O O P\ COMMANDS &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$1086
keywords: basic,commands,complex,more,simulating,using
contributors: bookofproofs

---


---

The basic syntax and semantics of a  [`\(L O O P\)` program][bookofproofs$1180] is very plain and simple: It is only possible to increment and decrement a register and repeat a `\(L O O P\)` program a number of times. However, using these basic commands, it is possible to simulate a lot of more complex commands, among others:

> the [assignment of a constant value to a register][bookofproofs$1187],
`\[\mathtt{r_i:=c;}\]`

> [setting the value of a register to the value of another register plus/minus a constant][bookofproofs$1189],
`\[\mathtt{r_i:=r_j\pm c;}\]`

> checking if a register equals `\(0\)` and, based of this comparison, a conditional execution of a `\(L O O P\)` program ([if-then-else construct][bookofproofs$1190]), 
`\[\mathtt{IF~r_i=0~THEN~P_1~ELSE~P_2~END;}\]`

> checking if a register is greater then a constant value and, based of this comparison, a conditional execution of a `\(L O O P\)` program ([if-then construct][bookofproofs$1191]), 
`\[\mathtt{IF~r_i > c~THEN~P~END;}\]`

> [the no-operation command (NOP command)][bookofproofs$1194],
`\[\mathtt{NOP;}\]`

> [addition (or subtraction) of two registers][bookofproofs$1192],
`\[\mathtt{r_i:=r_j\pm r_k;}\]`

> [multiplication of two registers][bookofproofs$1193],
`\[\mathtt{r_i:=r_j\ast r_k;}\]`

> [division with quotient and remainder][bookofproofs$1195],
`\[\begin{array}{l}
\mathtt{r_q:=r_j~DIV~r_k;}\\
\mathtt{r_r:=r_j~MOD~r_k;}
\end{array}\]`

> and many more...
