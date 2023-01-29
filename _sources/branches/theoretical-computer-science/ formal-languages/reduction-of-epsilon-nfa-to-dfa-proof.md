layout: proof
categories: branches,theoretical-computer-science, formal-languages
nodeid: bookofproofs$8537
orderid: 50
parentid: bookofproofs$8536
title: 
description: PROOF OF REDUCTION OF EPSILON-NFA TO DFA ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$1086,bookofproofs$7895
keywords: reduction of epsilon-nfa to dfa,proof
contributors: bookofproofs

---


---

* First, reduce a given `$\epsilon$`-NFA to an NFA according to theorem about the [reduction of epsilon-nfa to nfa][bookofproofs$8533].
* Now, reduce the resulting NFA to a DFA according to the [Rabin-Scott theorem][bookofproofs$8503].
* This shows the set inclusion `$\mathcal L(\epsilon-\operatorname{NFA})\subseteq\mathcal L(\operatorname{DFA}).$`
* The other set inclusion `$\mathcal L(\operatorname{DFA})\subseteq\mathcal L(\epsilon-\operatorname{NFA})$` is trivial.
