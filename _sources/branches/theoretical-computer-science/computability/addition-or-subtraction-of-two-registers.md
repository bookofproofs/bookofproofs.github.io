layout: algorithm
categories: branches,theoretical-computer-science, computability
nodeid: bookofproofs$1192
orderid: 300
parentid: bookofproofs$1188
title: Addition (or Subtraction) of Two Registers
description: ADDITION OR SUBTRACTION OF TWO REGISTERS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$1086
keywords: addition,registers,subtraction,two,register addition
contributors: bookofproofs

---
In a [unit-cost random access machine][bookofproofs$1179], the value of a register `\(r_i\)` can be set to the sum of other two registers `\(r_j\)` and `\(r_n\)` using [basic `\(L O O P\)` commands][bookofproofs$1180] as well as the [algorithm for `\(r_i:=r_j\pm c\)` ][bookofproofs$1189] and the [algorithm for the NOP operation][bookofproofs$1194].
### Implementing a unit-cost random access machine capable to represent negative numbers and to subtract registers
 
Although the unit-cost random access machine is not able to store negative numbers in its registers, it is not much more complicated to calculate the difference of two registers `\(r_j\)` and `\(r_n\)`, because negative integers can be represented by pairs of natural numbers, as shown in the [definition of integers][bookofproofs$844]. Thus, it is possible to build a unit-cost random access machine, which is able to store negative numbers using more auxiliary registers representing integers as pairs of natural numbers and implementing an appropriate [subtraction operation][bookofproofs$1585] on these pairs.

---

class UCRAM():
    # unit-cost random access machine with 3 registers
    r_i = 0
    r_j = 0
    r_n = 0

    def set_ri_to_0(self):
        while True:
            if self.r_i &gt; 0:
                self.r_i = self.r_i - 1 #  LOOP register i
                self.NOP()  #  DO nothing
            else:
                break

    def LOOP_rj_DO_increment_r_i(self):
        while True:
            if self.r_j &gt; 0:
                self.r_j = self.r_j - 1 #  LOOP register j
                self.r_i = self.r_i + 1 #  DO increment register i
            else:
                break

    def LOOP_rn_DO_increment_ri(self):
        while True:
            if self.r_n &gt; 0:
                self.r_n = self.r_n - 1 #  LOOP register n
                self.r_i = self.r_i + 1 #  DO increment register i
            else:
                break

    def add_rn_rj_and_store_result_to_ri(self):
        self.set_ri_to_0()
        self.LOOP_rj_DO_increment_r_i()
        self.LOOP_rn_DO_increment_ri()

    def NOP(self):
        self.r_i = self.r_i + 1 #  LOOP register i
        self.r_i = self.r_i - 1  # LOOP register i


1. Usage for adding the r_i = r_j + r_n
1. creating a unit-cost access machine with registers initially set
ucram = UCRAM()
ucram.r_j = 7 # assumed initial value for r_j
ucram.r_n = 123 # assumed initial value for r_n

print(ucram.r_i, ucram.r_j, ucram.r_n)

# setting r_i:= r_n + r_j
ucram.add_rn_rj_and_store_result_to_ri()
# setting r_i:=r_j
print(ucram.r_i, ucram.r_j, ucram.r_n)


1. will output
1. 0 7 123
1. 0 7 123
