layout: algorithm
categories: branches,theoretical-computer-science, computability
nodeid: bookofproofs$1194
orderid: 500
parentid: bookofproofs$1188
title: No-Operation Command (NOP)
description: NO-OPERATION COMMAND NOP &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$1086
keywords: command,nop,operation
contributors: bookofproofs

---
In a [unit-cost random access machine][bookofproofs$1179], the no-operation (NOP) command can be simulated using [basic `\(L O O P\)` commands][bookofproofs$1180]:

---

class UCRAM():
    # unit-cost random access machine with 3 registers
    r_i = 0

    def NOP(self):
        self.r_i = self.r_i + 1 #  LOOP register i
        self.r_i = self.r_i - 1  # LOOP register i


1. Usage for NOP
1. creating a unit-cost access machine with registers initially set
ucram = UCRAM()
print(ucram.r_i)

ucram.NOP()  #  no operation
print(ucram.r_i)


1. will output
1. 0
1. 0
