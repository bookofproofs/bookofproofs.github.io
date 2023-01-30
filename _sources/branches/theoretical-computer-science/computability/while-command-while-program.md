layout: definition
categories: branches,theoretical-computer-science, computability
nodeid: bookofproofs$1181
orderid: 300
parentid: bookofproofs$1179
title: WHILE Command, WHILE Program
description: WHILE COMMAND, WHILE PROGRAM &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$1086
keywords: command,program,terminates,while,while command,while program
contributors: bookofproofs

---


---

Let `\(M\)` be a [unit-cost random access machine][bookofproofs$1179] with the registers `\(r_1,\ldots, r_n\)`. 

#### `\((1)\)` The syntax of a WHILE command and a WHILE program

The [syntax][bookofproofs$709] of a **WHILE command** and a **WHILE program** is defined [by induction][bookofproofs$657].
> Base case 
* `\(\mathtt{r_i:=r_i + 1}\)` is both, a WHILE command and WHILE program for all `\(r_i\)`.
* `\(\mathtt{r_i:=r_i - 1}\)` is both, a WHILE command and WHILE program for all `\(r_i\)`.

> Induction step: Let `\(P_1,P_2\)` be two WHILE programs. Then
* `\(\mathtt{P_1;P_2}\)` is a WHILE program.
* `\(\mathtt{WHILE~r_i\neq 0~DO~P_1~END}\)` is both, a WHILE command and a WHILE program  for all `\(r_i\)`.

A WHILE program **terminates**, if there are no more WHILE commands / WHILE programs left to be executed. 

#### `\((2)\)` The semantics of a WHILE command and a WHILE program

The [semantics][bookofproofs$710] of the WHILE commands and a WHILE programs described above is as follows:

* `\(\mathtt{r_i:=r_i + 1}\)` means that `\(M\)` increments the natural number, which is contained in the register `\(r_i\)`.
* If `\(r_i > 0\)`, `\(\mathtt{r_i:=r_i - 1}\)` means that `\(M\)` decrements the natural number contained in the register `\(r_i\)`. 
* If `\(r_i=0\)`,   `\(\mathtt{r_i:=r_i - 1}\)` means that `\(M\)` does not change the register `\(r_i\)` at all.
* `\(\mathtt{P_1;P_2}\)` means that `\(M\)` executes the program `\(\mathtt {P_1}\)`. After the termination of this program, `\(M\)` continues with the execution of the program `\(\mathtt {P_2}\)`.  
* `\(\mathtt{WHILE~r_i\neq 0~DO~P~END}\)` means that `\(M\)` compares the value of the register `\(r_i\)` with `\(0\)`. If `\(r_i=0\)`, the program terminates. Otherwise, `\(M\)` executes the program `\(\mathtt P\)`.
