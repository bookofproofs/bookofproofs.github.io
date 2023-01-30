layout: proof
categories: branches,theoretical-computer-science, computability
nodeid: bookofproofs$1200
orderid: 50
parentid: bookofproofs$1199
title: 
description:  Proof of SIMULATING LOOP PROGRAMS USING WHILE PROGRAMS &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$1086
keywords: loop,programs,simulating,using,while,proof
contributors: bookofproofs

---


---

The only [LOOP command][bookofproofs$1180], which is not already included in the syntax and sematics of a [WHILE program][bookofproofs$1181] is the command

`\[\mathtt{LOOP~r_i~DO~P~END;}\quad\quad ( * )\]`

Therefore, in order to show that all [LOOP-computable functions][bookofproofs$1183] are included in all [WHILE-computable functions][bookofproofs$1184], formally, 

`\[L O O P \subseteq W H I L E,\]`

it is sufficient to find a `\(W H I L E\)` program simulating the LOOP command `\( ( * )\)`. The following program does the trick:

`\[\begin{array}{rll}\hline&\mathbf{\text{Algorithm:}}~\mathsf{\text{Simulation of }}\mathtt{LOOP~r_i~DO~P~END;}\mathsf{\text{ using W H I L E commands}}&\\
\hline
\hline
{\tiny 1}&{\hspace{0em}\mathtt{WHILE~r_i\neq 0~DO} }&//~\text{ simulate }r_n:=r_i\\
{\tiny 2}&{\hspace{2em}\mathtt{r_n:=r_n + 1;}}\\
{\tiny 3}&{\hspace{2em}\mathtt{r_{n+1}:=r_{n+1} + 1;}}\\
{\tiny 4}&{\hspace{2em}\mathtt{r_i:=r_i - 1;}}\\
{\tiny 5}&{\hspace{0em}\mathtt{END;}}\\
{\tiny 6}&{\hspace{0em}\mathtt{WHILE~r_{n+1}\neq 0~DO} }\\
{\tiny 7}&{\hspace{2em}\mathtt{r_i:=r_i + 1;}}\\
{\tiny 8}&{\hspace{2em}\mathtt{r_{n+1}:=r_{n+1} - 1;}}\\
{\tiny 9}&{\hspace{0em}\mathtt{END;}}\\
{\tiny 10}&{\hspace{0em}\mathtt{WHILE~r_n\neq 0~DO} }&//~\text{ simulate }LOOP\text{ command}\\
{\tiny 11}&{\hspace{2em}\mathtt{P;}}\\
{\tiny 12}&{\hspace{2em}\mathtt{r_n:=r_n - 1;}}\\
{\tiny 13}&{\hspace{0em}\mathtt{END;}}\\
\hline\end{array}\]`
