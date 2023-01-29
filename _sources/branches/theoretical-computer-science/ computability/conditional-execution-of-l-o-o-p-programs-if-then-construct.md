layout: algorithm
categories: branches,theoretical-computer-science, computability
nodeid: bookofproofs$1191
orderid: 200
parentid: bookofproofs$1188
title: Conditional execution of `\(L O O P\)` programs - IF-THEN construct
description: CONDITIONAL EXECUTION OF LOOP PROGRAMS - IF-THEN CONSTRUCT &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$1086
keywords: conditional,construct,execution,programs,then
contributors: bookofproofs

---
In a [unit-cost random access machine][bookofproofs$1179], the IF-THEN-construct can be simulated using [IF-THEN-ELSE-construct][bookofproofs$1190] and the [algorithm for the NOP operation][bookofproofs$1194].
---

class UCRAM():
    # unit-cost random access machine with 3 registers
    r_i = 0
    r_m = 0
    r_n = 0

    def set_rm_to_0(self):
        # set r_m=0 with loop r_m do
        while True:
            if self.r_m &gt; 0:
                self.r_m = self.r_m - 1 #  LOOP register m
                self.NOP() #  DO nothing
            else:
                break

    def NOP(self):
        self.r_i = self.r_i + 1 #  LOOP register i
        self.r_i = self.r_i - 1  # LOOP register i


    def set_rm_to_1(self):
        self.set_rm_to_0()
        # set register m to 1 by incrementing it once
        self.r_m = self.r_m + 1

    def set_rn_to_1(self):
        # set r_n=0 with loop r_n do
        while True:
            if self.r_n &gt; 0:
                self.r_n = self.r_n - 1 #  LOOP register n
                self.NOP() #  DO nothing
            else:
                break
        # set register m to 1 by incrementing it once
        self.r_n = self.r_n + 1

    def set_ri_minus_rn(self):
        while True:
            if self.r_n &gt; 0:
                self.r_n = self.r_n - 1 #  LOOP register n
                if self.r_i &gt; 0:
                    self.r_i = self.r_i - 1  # DO decrement register i
            else:
                break

    def LOOP_ri_DO_set_rm_to_1(self):
        while True:
            if self.r_i &gt; 0:
                self.r_i = self.r_i - 1 #  LOOP register i
                # DO set rm to 1
                self.set_rm_to_1()
            else:
                break

    def LOOP_rm_DO_P1(self):
        while True:
            if self.r_m &gt; 0:
                self.r_m = self.r_m - 1  # LOOP register m
                self.P1()
            else:
                break


    def P1(self):
        print("executing P1")

    def IF_ri_greter_c_THEN_P1_END(self):
        self.set_ri_minus_rn()
        self.set_rm_to_0()
        self.LOOP_ri_DO_set_rm_to_1()
        self.LOOP_rm_DO_P1()


1. Usage of simulating an IF r_i==0 THEN P1 ELSE P2 END construct
1. creating a unit-cost access machine
ucram = UCRAM()
ucram.r_i = 6
ucram.r_n = 6
ucram.IF_ri_greter_c_THEN_P1_END()
# will output nothing

ucram.r_i = 8
ucram.r_n = 6
ucram.IF_ri_greter_c_THEN_P1_END()
1. will output
1. will output
