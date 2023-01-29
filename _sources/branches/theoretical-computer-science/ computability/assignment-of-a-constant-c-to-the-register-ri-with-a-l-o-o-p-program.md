layout: algorithm
categories: branches,theoretical-computer-science, computability
nodeid: bookofproofs$1187
orderid: 700
parentid: bookofproofs$1188
title: Assignment of a Constant `\(c\)` to the Register `\(r_i\)` with a `\(L O O P\)`-Program
description: ASSIGNMENT OF A CONSTANT C TO THE REGISTER R_I WITH A LOOP-PROGRAM &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$1086
keywords: assignment,constant,program,register
contributors: bookofproofs

---
In a [unit-cost random access machine][bookofproofs$1179], the assignment of a constant `\(c\in\mathbb N\)` to a register `\(r_i\)` can be  simulated using [basic `\(L O O P\)` commands][bookofproofs$1180] only:

---

class UCRAM():
    # unit-cost random access machine with 3 registers
    r_i = 0
    r_j = 0
    r_n = 0


    def set_r_n_to_5(self):
        # set r_n=0 with loop r_n do
        while True:
            if self.r_n &gt; 0:
                self.r_n = self.r_n - 1 # LOOP register n
                self.NOP() # DO nothing
            else:
                break
        # set register to 5 by incrementing it 5 times
        self.r_n = self.r_n + 1
        self.r_n = self.r_n + 1
        self.r_n = self.r_n + 1
        self.r_n = self.r_n + 1
        self.r_n = self.r_n + 1

    def NOP(self):
        self.r_i = self.r_i + 1 #  LOOP register i
        self.r_i = self.r_i - 1  # LOOP register i


1. Usage for adding the r_i = const
1. creating a unit-cost access machine with registers initially set
ucram = UCRAM()
1. ucram.r_n // r_n is undefined
1. ucram.r_i // r_i is undefined
1. ucram.r_j // r_j is undefined


# setting r_n:=constant (here 5)
ucram.set_r_n_to_5()
print(ucram.r_i, ucram.r_j, ucram.r_n)


1. will output
1. will output
