layout: algorithm
categories: branches,theoretical-computer-science, computability
nodeid: bookofproofs$1193
orderid: 400
parentid: bookofproofs$1188
title: Multiplication of Two Registers
description: MULTIPLICATION OF TWO REGISTERS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$1086
keywords: multiplication,registers,two
contributors: bookofproofs

---
In a [unit-cost random access machine][bookofproofs$1179], the value of a register `\(r_i\)` can be set to the product of other two registers `\(r_j\)` and `\(r_n\)` using [basic `\(L O O P\)` commands][bookofproofs$1180] as well as the [algorithm for `\(r_i:=0\)` ][bookofproofs$1187], and the [algorithm for `\(r_i:=r_j\pm r_n\)` ][bookofproofs$1192].
### Implementing a unit-cost random access machine capable to represent negative numbers
 
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

    def set_rn_to_11(self):
        # reset register n to 0
        while True:
            if self.r_n &gt; 0:
                self.r_n = self.r_n - 1 #  LOOP register n
                self.NOP()  #  DO nothing
            else:
                break
        self.r_n = self.r_n + 1  # set register n to the value 11
        self.r_n = self.r_n + 1
        self.r_n = self.r_n + 1
        self.r_n = self.r_n + 1
        self.r_n = self.r_n + 1
        self.r_n = self.r_n + 1
        self.r_n = self.r_n + 1
        self.r_n = self.r_n + 1
        self.r_n = self.r_n + 1
        self.r_n = self.r_n + 1
        self.r_n = self.r_n + 1

    def set_rj_to_7(self):
        # reset register j to 0
        while True:
            if self.r_j &gt; 0:
                self.r_j = self.r_j - 1 #  LOOP register n
                self.NOP()  #  DO nothing
            else:
                break
        self.r_j = self.r_j + 1  # set register j to the value 7
        self.r_j = self.r_j + 1
        self.r_j = self.r_j + 1
        self.r_j = self.r_j + 1
        self.r_j = self.r_j + 1
        self.r_j = self.r_j + 1
        self.r_j = self.r_j + 1

    def LOOP_rj_DO_increment_ri(self):
        while True:
            if self.r_j &gt; 0:
                self.r_j = self.r_j - 1 #  LOOP register j
                self.r_i = self.r_i + 1 #  DO increment register i
            else:
                break

    def add_rj_to_ri(self):
        self.LOOP_rj_DO_increment_ri()

    def NOP(self):
        self.r_i = self.r_i + 1 #  LOOP register i
        self.r_i = self.r_i - 1  # LOOP register i

    def multiply_rj_times_rn_and_store_result_in_ri(self):
        self.set_ri_to_0()
        while True:
            if self.r_n &gt; 0:
                self.r_n = self.r_n - 1  # LOOP register n
                self.set_rj_to_7()
                self.add_rj_to_ri()  # DO add registers r_i and r_j
            else:
                break


1. Usage for adding the r_i = r_j * r_n
1. creating a unit-cost access machine with registers initially set
ucram = UCRAM()
ucram.set_rj_to_7()
ucram.set_rn_to_11()
print(ucram.r_i, ucram.r_j, ucram.r_n)
ucram.multiply_rj_times_rn_and_store_result_in_ri()
print(ucram.r_i, ucram.r_j, ucram.r_n)


1. will output
1. 0 7 11
1. 0 7 11
