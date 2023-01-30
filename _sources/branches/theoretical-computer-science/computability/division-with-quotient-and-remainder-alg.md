layout: algorithm
categories: branches,theoretical-computer-science, computability
nodeid: bookofproofs$1195
orderid: 600
parentid: bookofproofs$1188
title: Division with Quotient and Remainder (Unit-cost Random Access Machine)
description: DIVISION WITH QUOTIENT AND REMAINDER UNIT-COST RANDOM ACCESS MACHINE &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$1086
keywords: alg,division,quotient,remainder
contributors: bookofproofs

---
In a [unit-cost random access machine][bookofproofs$1179], the division with quotient and remainder operation of two registers `\(r_j\)` and `\(r_k\)` can be simulated using [basic `\(L O O P\)` commands][bookofproofs$1180], the [algorithm for `\(r_i:=c\)` ][bookofproofs$1187], the [algorithm for `\(r_i:=r_j\pm r_k\)` ][bookofproofs$1192], the [algorithm for the NOP-command][bookofproofs$1194], and the [algorithm for the IF-THEN-ELSE-construct ][bookofproofs$1190]:

---

class UCRAM():
    # unit-cost random access machine with 4 registers
    r_q = 0
    r_j = 0
    r_k = 0
    r_r = 0
    r_m = 0
    r_c = 0

    def set_rc_to_0(self):
        # set r_c=0 with loop r_q do
        while True:
            if self.r_c > 0:
                self.r_c = self.r_c - 1 #  LOOP register c
                self.NOP() #  DO nothing
            else:
                break

    def set_rc_to_1(self):
        self.set_rc_to_0()
        self.r_c = self.r_c + 1  # increment register c

    def set_rq_to_0(self):
        # set r_q=0 with loop r_q do
        while True:
            if self.r_q > 0:
                self.r_q = self.r_q - 1 #  LOOP register q
                self.NOP() #  DO nothing
            else:
                break

    def set_rr_to_0(self):
        # set r_r=0 with loop r_r do
        while True:
            if self.r_r > 0:
                self.r_r = self.r_r - 1 #  LOOP register n
                self.NOP() #  DO nothing
            else:
                break

    def set_rm_to_0(self):
        # set r_m=0 with loop r_m do
        while True:
            if self.r_m > 0:
                self.r_m = self.r_m - 1 #  LOOP register m
                self.NOP() #  DO nothing
            else:
                break

    def NOP(self):
        self.r_q = self.r_q + 1
        self.r_q = self.r_q - 1

    def check_if_rr_minus_rk_equals_0_and_flag_this_in_rc(self):
        saved_rr=self.r_r
        saved_rk=self.r_k
        self.set_rm_to_0()
        while True:
            if self.r_k > 0:
                self.r_k = self.r_k - 1  # LOOP register k
                self.r_m = self.r_m + 1  # do increment r_m
            else:
                break
        while True:
            if self.r_r > 0:
                self.r_r = self.r_r - 1  # LOOP register n
                if self.r_m > 0:
                    self.r_m = self.r_m - 1  # do decrement r_m
            else:
                break
        # add r_k and r_r were equal, then r_m is 0
        self.set_rc_to_1() # assume equality
        while True:
            if self.r_m > 0:
                self.r_m = self.r_m - 1  # LOOP register r_m
                self.set_rc_to_0()  # unequal
            else:
                break
        # restore compared registers
        self.r_r = saved_rr
        self.r_k = saved_rk

    def DIV_MOD(self):
        self.set_rq_to_0()
        self.set_rr_to_0()
        self.set_rm_to_0()
        while True:
            if self.r_j > 0:
                self.r_j = self.r_j - 1 #  LOOP register j (dividend)
                self.r_r = self.r_r + 1 # increment auxiliary register n
                self.check_if_rr_minus_rk_equals_0_and_flag_this_in_rc()
                while True:
                    if self.r_c > 0: # if rr was equal than rk
                        self.r_c = self.r_c - 1  # LOOP register j (dividend)
                        self.r_q = self.r_q + 1  # increase quotient
                        self.set_rr_to_0() #  set auxiliary register n to 0
                    else:
                        break
            else:
                break



1. Usage of r_j DIV r_k
1. creating a unit-cost access machine
ucram = UCRAM()
ucram.r_j = 39
ucram.r_k = 6
result=str(ucram.r_j)+"/"+str(ucram.r_k)+" ="
ucram.DIV_MOD()
result +=" quotient: "+str(ucram.r_q)+", remainder: "+str(ucram.r_r)
print(result)

1. will output
1. will output
