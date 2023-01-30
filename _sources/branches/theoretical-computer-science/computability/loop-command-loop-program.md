layout: definition
categories: branches,theoretical-computer-science, computability
nodeid: bookofproofs$1180
orderid: 200
parentid: bookofproofs$1179
title: LOOP Command, LOOP Program
description: LOOP COMMAND, LOOP PROGRAM &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$1086
keywords: command,loop,loop command,loop program,program,terminates
contributors: bookofproofs

---


---

Let `\(M\)` be a [unit-cost random access machine][bookofproofs$1179] with the registers `\(r_1,\ldots, r_n\)`. 

#### `\((1)\)` The syntax of a LOOP command and a LOOP program

The [syntax][bookofproofs$709] of a **LOOP command** and a **LOOP program** is defined [by induction][bookofproofs$657].
> Base case 
* `\(\mathtt{r_i:=r_i + 1}\)` is both, a LOOP command and LOOP program for all `\(r_i\)`.
* `\(\mathtt{r_i:=r_i - 1}\)` is both, a LOOP command and LOOP program for all `\(r_i\)`.

> Induction step: Let `\(P_1,P_2\)` be two LOOP programs. Then
* `\(\mathtt{P_1;P_2}\)` is a LOOP program.
* `\(\mathtt{LOOP~r_i~DO~P_1~END}\)` is both, a LOOP command and a LOOP program  for all `\(r_i\)`.

A LOOP program **terminates**, if there are no more LOOP commands / LOOP programs left to be executed. 

#### `\((2)\)` The semantics of a LOOP command and a LOOP program

The [semantics][bookofproofs$710] of the LOOP commands and a LOOP programs described above is as follows:

* `\(\mathtt{r_i:=r_i + 1}\)` means that `\(M\)` increments the natural number, which is contained in the register `\(r_i\)`.
* If `\(r_i > 0\)`, `\(\mathtt{r_i:=r_i - 1}\)` means that `\(M\)` decrements the natural number contained in the register `\(r_i\)`. 
* If `\(r_i=0\)`,   `\(\mathtt{r_i:=r_i - 1}\)` means that `\(M\)` does not change the register `\(r_i\)` at all.
* `\(\mathtt{P_1;P_2}\)` means that `\(M\)` executes the program `\(\mathtt {P_1}\)`. After the termination of this program, `\(M\)` continues with the execution of the program `\(\mathtt {P_2}\)`.  
* `\(\mathtt{LOOP~r_i~DO~P~END}\)` means that `\(M\)` executes the program `\(\mathtt P\)` exactly `\(n\)` times, where `\(n\)` is the natural number stored in the register `\(r_i\)`.
