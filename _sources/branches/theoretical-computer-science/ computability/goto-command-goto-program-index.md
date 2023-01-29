layout: definition
categories: branches,theoretical-computer-science, computability
nodeid: bookofproofs$1182
orderid: 400
parentid: bookofproofs$1179
title: GOTO Command, GOTO Program, Index
description: GOTO COMMAND, GOTO PROGRAM, INDEX &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$1086
keywords: command,goto,goto command,goto program,index,program,terminates
contributors: bookofproofs

---


---

Let `\(M\)` be a [unit-cost random access machine][bookofproofs$1179] with the registers `\(r_1,\ldots, r_n\)`. 

#### `\((1)\)` The syntax of a GOTO command and a GOTO program

The [syntax][bookofproofs$709] of a **GOTO command** is defined by:

* An **index** is a natural number `\(j > 0\)`. 
* For all registers `\(r_i\)` and all indices `\(j\)`: 
   * `\(\mathtt{r_i:=r_i + 1}\)` is a GOTO command,
   * `\(\mathtt{r_i:=r_i - 1}\)` is a GOTO command,
   * `\(\mathtt{ I F~r_i=0~G O T O~j} \)` is a GOTO command. 

The syntax of a **GOTO program** is defined by:

* `\(\mathtt{j : C}\)` is a GOTO program, if `\(\mathtt{C}\)` is a GOTO command,
* `\(\mathtt{P_1;P_2}\)` is a GOTO program, if `\(\mathtt{P_1,P_2}\)` are two GOTO programs. 

A GOTO program **terminates**, if there are no more GOTO commands / GOTO programs left to be executed. 

Without any loss of generality, all program lines can be numbered by consecutive indices `\(j=1,2,\ldots \)`.
 
#### `\((2)\)` The semantics of a GOTO command and a GOTO program

The [semantics][bookofproofs$710] of the GOTO commands and a GOTO programs described above is as follows:

* `\(\mathtt{r_i:=r_i + 1}\)` means that `\(M\)` increments the natural number, which is contained in the register `\(r_i\)`.
* If `\(r_i > 0\)`, `\(\mathtt{r_i:=r_i - 1}\)` means that `\(M\)` decrements the natural number contained in the register `\(r_i\)`. 
* If `\(r_i=0\)`,   `\(\mathtt{r_i:=r_i - 1}\)` means that `\(M\)` does not change the register `\(r_i\)` at all.
* `\(\mathtt{P_1;P_2}\)` means that `\(M\)` executes the program `\(\mathtt {P_1}\)`. After the termination of this program, `\(M\)` continues with the execution of the program `\(\mathtt {P_2}\)`.  
* `\(\mathtt{j : P}\)` means that `\(M\)` executes the program `\(P\)`.
* `\(\mathtt{ I F~r_i=0~G O T O~j} \)` means that `\(M\)` compares the value of the register `\(r_i\)` with `\(0\)`. If `\(r_i\neq 0\)`, then `\(M\)` ignores the command and continues to execute the program with the next index to the index of the current program. Otherwise (i.e. if `\(r_i=0\)`), `\(M\)` continues to execute the program with the next index `\(j\)`.
