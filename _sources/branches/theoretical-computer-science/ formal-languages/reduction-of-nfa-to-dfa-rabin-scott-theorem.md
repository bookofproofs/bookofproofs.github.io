layout: theorem
categories: branches,theoretical-computer-science, formal-languages
nodeid: bookofproofs$8503
orderid: 50
parentid: bookofproofs$8498
title: Reduction of NFA to DFA (Rabin-Scott Theorem)
description: REDUCTION NFA TO DFA, RABIN-SCOTT THEOREM ★ bring your math skills to the graduate level ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$1086,bookofproofs$7895
keywords: rabin-scott theorem
contributors: bookofproofs


---
The [examples of nfa][bookofproofs$8502]":[bookofproofs$8502] give rise to the question, whether the class `$\mathcal L(\operatorname{NFA})$` of all languages accepted by any NFA is bigger than the class `$\mathcal L(\operatorname{DFA})$` of all languages accepted by any DFA, due to the non-determinism of the NFA, as compared to the determinism of the DFA.

This question has been answered by Michael Rabin (1931 - ) and Dana S. Scott (1932 - ) in 1959 in "Finite Automata and Their Decision Problems":http://www.cse.chalmers.se/~coquand/AUTOMATA/rs.pdf.

---

For every [non-deterministic finite automaton][bookofproofs$8501]. NFA there is a [deterministic finite automaton][bookofproofs$8499]. DFA accepting the same [language][bookofproofs$7842].
In other words, the class `$\mathcal L(\operatorname{NFA})$` of all languages accepted by any NFA equals the class `$\mathcal L(\operatorname{DFA})$` of all languages accepted by any DFA, formally

`$$\mathcal L(\operatorname{NFA})=\mathcal L(\operatorname{DFA}).$$`
