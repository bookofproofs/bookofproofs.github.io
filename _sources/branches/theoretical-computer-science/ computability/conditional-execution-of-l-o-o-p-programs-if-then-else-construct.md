layout: algorithm
categories: branches,theoretical-computer-science, computability
nodeid: bookofproofs$1190
orderid: 100
parentid: bookofproofs$1188
title: Conditional execution of `\(L O O P\)` programs - IF-THEN-ELSE construct
description: CONDITIONAL EXECUTION OF LOOP PROGRAMS - IF-THEN-ELSE CONSTRUCT &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$1086
keywords: conditional,construct,else,execution,programs,then
contributors: bookofproofs

---
In a [unit-cost random access machine][bookofproofs$1179], the IF-THEN-construct can be simulated using  [basic `\(L O O P\)` commands][bookofproofs$1180] as well as the [algorithm for `\(r_i:=c\)` ][bookofproofs$1187]  and the [algorithm for the NOP operation][bookofproofs$1194].
---

class UCRAM():
    # unit-cost random access machine with 3 registers
    r_i = 0
    r_m = 0
    r_n = 0

    def set_r_m_to_1(self):
        # set r_m=0 with loop r_m do
        while True:
            if self.r_m &gt; 0:
                self.r_m = self.r_m - 1 #  LOOP register n
                self.NOP() #  DO nothing
            else:
                break
        # set register m to 1 by incrementing it once
        self.r_m = self.r_m + 1

    def set_r_n_to_1(self):
        # set r_n=0 with loop r_n do
        while True:
            if self.r_n &gt; 0:
                self.r_n = self.r_n - 1 #  LOOP register n
                self.NOP() #  DO nothing
            else:
                break
        # set register n to 1 by incrementing it once
        self.r_n = self.r_n + 1

    def LOOP_r_i_DO_decrement_r_n(self):
        while True:
            if self.r_i &gt; 0:
                self.r_i = self.r_i - 1 #  LOOP register i
                if self.r_n &gt; 0:
                    self.r_n = self.r_n - 1  # DO decrement register n
            else:
                break

    def LOOP_r_n_DO_decrement_r_m(self):
        while True:
            if self.r_n &gt; 0:
                self.r_n = self.r_n - 1 #  LOOP register n
                if self.r_m &gt; 0:
                    self.r_m = self.r_m - 1  # DO decrement register m
            else:
                break

    def LOOP_r_n_DO_P1(self):
        while True:
            if self.r_n &gt; 0:
                self.r_n = self.r_n - 1 #  LOOP register n
                # DO P1 and DO decrement register m
                self.P1()
                if self.r_m &gt; 0:
                    self.r_m = self.r_m - 1
            else:
                break

    def LOOP_r_m_DO_P2(self):
        while True:
            if self.r_m &gt; 0:
                self.r_m = self.r_m - 1  # LOOP register m
                self.P2()
            else:
                break

    def P1(self):
        print("executing P1")

    def P2(self):
        print("executing P2")

    def IF_ri_THEN_P1_ELSE_P2_END(self):
        self.set_r_m_to_1()
        self.set_r_n_to_1()
        self.LOOP_r_i_DO_decrement_r_n()
        self.LOOP_r_n_DO_P1()
        self.LOOP_r_n_DO_decrement_r_m()
        self.LOOP_r_m_DO_P2()


1. Usage of simulating an IF r_i==0 THEN P1 ELSE P2 END construct
1. creating a unit-cost access machine
ucram = UCRAM()
ucram.r_i = 100
ucram.IF_ri_THEN_P1_ELSE_P2_END()
ucram.r_i = 0
ucram.IF_ri_THEN_P1_ELSE_P2_END()


1. will output
1. executing P2
1. executing P2
