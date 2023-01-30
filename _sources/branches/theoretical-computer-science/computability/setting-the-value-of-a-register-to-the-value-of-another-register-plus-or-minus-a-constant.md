layout: algorithm
categories: branches,theoretical-computer-science, computability
nodeid: bookofproofs$1189
orderid: 50
parentid: bookofproofs$1188
title: Setting the value of a register to the value of another register plus or minus a constant
description: SETTING THE VALUE OF A REGISTER TO THE VALUE OF ANOTHER REGISTER PLUS OR MINUS A CONSTANT &#9733; master graduate maths &#10004; visit BookOfProofs now!
references: bookofproofs$1086
keywords: another,constant,minus,plus,register,setting,value
contributors: bookofproofs

---
In a [unit-cost random access machine][bookofproofs$1179], the value of a register `\(r_i\)` can be set to the value of another register `\(r_j\)` plus/minus a constant `\(c\in\mathbb N\)` using [basic `\(L O O P\)` commands][bookofproofs$1180] as well as the [algorithm for `\(r_i:=\pm c\)` ][bookofproofs$1187] and the [algorithm for the NOP operation][bookofproofs$1194].
### Implementing a unit-cost random access machine capable to represent negative numbers and to subtract constans
 
Although the unit-cost random access machine is not able to store negative numbers in its registers, it is not much more complicated to calculate the difference of a registers `\(r_j\)` and a positive constant, because negative integers can be represented by pairs of natural numbers, as shown in the [definition of integers][bookofproofs$844]. Thus, it is possible to build a unit-cost random access machine, which is able to store negative numbers using more auxiliary registers representing integers as pairs of natural numbers and implementing an appropriate [subtraction operation][bookofproofs$1585] on these pairs.

---

class UCRAM():
    # unit-cost random access machine with 3 registers
    r_i = 0
    r_j = 0
    r_n = 0


    def LOOP_r_j_DO_increment_r_i(self):
        while True:
            if self.r_j &gt; 0:
                self.r_j = self.r_j - 1 #  LOOP register j
                self.r_i = self.r_i + 1 #  DO increment register i
            else:
                break

    def set_r_n_to_10(self):
        # set r_n=0 with loop r_n do
        while True:
            if self.r_n &gt; 0:
                self.r_n = self.r_n - 1 #  LOOP register n
                self.NOP() #  DO nothing
            else:
                break
        # set register to 10 by incrementing it 10 times
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

    def LOOP_r_n_DO_increment_r_i(self):
        while True:
            if self.r_n &gt; 0:
                self.r_n = self.r_n - 1 #  LOOP register n
                self.r_i = self.r_i + 1 #  DO decrement register j
            else:
                break

    def NOP(self):
        self.r_i = self.r_i + 1 #  LOOP register i
        self.r_i = self.r_i - 1  # LOOP register i

    def add_ri_plus_rj_plus_constant(self):
        # setting r_i:=r_j
        self.LOOP_r_j_DO_increment_r_i()
        # setting r_i:=r_j + 10
        self.LOOP_r_n_DO_increment_r_i()


1. Usage for adding the r_i = r_j + const
1. creating a unit-cost access machine with registers initially set
ucram = UCRAM()
ucram.r_j = 7 # assumed initial value for r_j
ucram.r_i = 0
# ucram.r_n // r_n will be used as auxiliary register and is undefined

# set constant to be added
ucram.set_r_n_to_10()
print(ucram.r_i, ucram.r_j, ucram.r_n)

ucram.add_ri_plus_rj_plus_constant()
print(ucram.r_i, ucram.r_j, ucram.r_n)


1. will output
1. 0 7 0
1. 0 7 10
1. 0 7 10
