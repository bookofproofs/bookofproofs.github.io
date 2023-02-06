layout: part
categories: branches,combinatorics
nodeid: bookofproofs$8298
orderid: 50
parentid: bookofproofs$82
title: Historical Development of Combinatorics
description: HISTORICAL DEVELOPMENT OF COMBINATORICS ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$8297
keywords: historical development of combinatorics
contributors: bookofproofs


---


---

The earliest developments of mathematics which can be connected to combinatorics are relatively old. In 2200 BC, a Chinese legend mentions the _magic square_ discovered on a turtle shell `$$\pmatrix{4&9&2\\3&5&7\\8&1&6},$$` in which the sums of all columns, rows, and diagonals equals `$15.$` Many other magic squares have been developed by the _Pythagoreans_ between 500 and 400 BC in their mystical philosophy. 

It is a common technique for many combinatoric problems to transform the problem into a sequence of natural numbers and to define this sequence _recursively_. The first known recursive definition of a sequence of natural numbers in the _rabbit problem_ published 1202 by [Leonardo Fibonacci][bookofproofs$Fibonacci] (1170 - 1250) in his famous book [Liber abaci](https://archive.org/details/LiberAbaci), which was also important for the propagation of the _positional decimal system_ including the digit `$0$` in European mathematics. The rabbit problem was to determine the number of couples of rabbits in one year, starting with one couple and assuming that each couple of rabbits will bear another couple of descendants in `$2$` months. The answer to this problem is the [Fibonacci number sequence][bookofproofs$498] with the recursive formula `$$f_0=1,\quad f_{n+2}=f_{n+1}+f_n$$` beginning of which is given in the following table:


Month | `$0$` | `$1$` | `$2$` | `$3$` | `$4$` | `$5$` | `$6$` | ... | `$n$`
:------------- |:------------- |:------------- |:------------- |:------------- |:------------- |:------------- |:------------- |:------------- |:-------------
 Couples| `$1$`| `$1$`| `$2$`| `$3$`| `$5$`| `$8$`| `$13$`| ...| `$f_n$`

In 1494, [Luca Pacioli][bookofproofs$Pacioli] (1445 - 1517) published a book [Suma de arithmetica geometria proportioni proportionalita](https://archive.org/details/summadearithmeti00paci/page/n4), which, among others, contained also problems related to modern combinatorics: the identity `$$\sum_{k=1}^n k^3=\left(\sum_{k=1}^n k\right)^2,$$` as well as problems related to [probability theory][bookofproofs$73].
Magical squares had also been studied in Europe by 
[Adam Ries][bookofproofs$Ries] (1492 - 1559) and his pupil 
Michael Stiftel, who developed some rules for the creation of magic squares. In his book [Arithmetica integra](https://archive.org/details/bub_gb_fndPsRv08R0C/page/n6) published in 1544, Stiftel also described many combinatorial problems, including the [recursive formula for binomial coefficients][bookofproofs$994].
[Niccolò Tartaglia][bookofproofs$Tartaglia] (1500 - 1557) was the inventor of a formula for solving cubic equations, but this rule was plagiarised by 
[Girolamo Cardano](https://mathshistory.st-andrews.ac.uk/Biographies/Cardan/) (1501 - 1576) and became, therefore, known as the _Cardano formula_. Cardano also studied the triangle and square numbers and discovered the rule

`$$\sum_{k=1}^{n-1}k+\sum_{k=1}^{n}k=n^2.$$`

Tartaglia himself probably plagiarized Stiftel's recursive formula for binomial coefficients, since he knew _Arithmetica integra_. But Tartaglia also solved himself other combinatorial problems,  including the problem of [summing arithmetical progression][bookofproofs$1117] and related sums with coefficients of higher degrees. For instance, he solved the problem of the number of different results when throwing `$8$` dice onto the table. The answer he found was:

`$$1+8+36+120+330+792=1287.$$`

[Francesco Maurolico][bookofproofs$Maurolico] (1494 - 1575) used for the first time the [proving principle by induction][bookofproofs$657], which became one of the most important proving techniques in combinatorics.

The first systematical study of combinatorics can be found in the results of the French mathematicians [Blaise Pascal](https://mathshistory.st-andrews.ac.uk/Biographies/Pascal/) (1623 - 1662) and [Pierre de Fermat][bookofproofs$Fermat]  (1601 - 1665). Pascal re-discovered the binomial coefficients independently from Stiftel and ordered them in his famous [Pascal's triangle][bookofproofs$1409]. Pascal was able to recognize that the numbers in his triangles can be interpreted as the number of possibilities to choose `$k$` objects out of `$n$` objects and he also used Maurolico's _proving principle of induction_ as a technique to prove many of his results. Pascal and Fermat corresponded with each other and in their correspondence, they laid the foundations of probability theory which remained closely connected to combinatorics.

In his [Dissertatio de arte combinatoria](https://archive.org/details/ita-bnc-mag-00000844-001/page/n11) published in the year 1666, [Gottfried Wilhelm von Leibniz][bookofproofs$Leibniz] (1646 - 1716) used the word _combinatorics_ for the first time. Leibniz published this work without any knowledge of the Pascal's triangle and it contained many new combinatorial results, including insights for the number of [permutations][bookofproofs$188] `$P_n:=n !.$`  In his "Dissertatio" and also later, in the years 1680 and 1700, Leibniz deduced some combinatorial results, including
* A recursive formula for permutations `${P_n^2}{P_{n-1}}=P_{n+1}-P_n,$`
* the permutation number `$P_n$` is a [divisor][bookofproofs$700] of the number `$(m+1)(m+2)\cdots(m+n)$` for every `$m\ge 0.$`

Leibniz was also the first to recognize that calculations involving [infinite series][bookofproofs$1109] and [polynomials][bookofproofs$199] have - with respect to their coefficients - many parallels to combinatorial results. In particular, he replaced the contemporary notation of sums, e.g. `$\alpha+\beta x + \gamma x^2+\cdots,$` by the _indexed notation_ `$a_0+a_1x+a_2x^2+\cdots a_nx^n,$` and was able to find formulas for coefficients when two such sums are being multiplied with each other. E.g. he found a formula for the coefficients `$$c_n:=\sum_{k=0}^n a_{n-k}b_k$$` when multiplying two polynomials with each other and which was also used later in the [Cauchy product of infinite series][bookofproofs$1390].
The work [Ars conjectandi](https://archive.org/details/wahrscheinlichke00bernuoft) published 1713 posthumous by [Jacob Bernoulli](https://mathshistory.st-andrews.ac.uk/Biographies/Bernoulli_Jacob/) (1654 - 1705) is important for both, the probability theory and combinatorics. In this book, the terms "permutation" and "combination" were used for the first time in history. Using identities for binomial coefficients, Bernoulli was able to derive, in particular, the following combinatorial formulae:

`$$\sum_{k=1}^n k^2=\frac{n^3}{3}+\frac{n^2}{2}+\frac n6,\quad\sum_{k=1}^n k^3=\frac{n^4}{4}+\frac{n^3}{2}+\frac{n^2}{4},$$`
and he continued to derive similar formulae up to the sum of `$10$`-th powers. He was also able to find a general formula for the sum of the `$m$`-th powers:

`$$\sum_{k=1}^n k^m=\frac{n^{m+1}}{m+1}+\frac{n^m}{2}+\sum_{k=2}^m \frac{B_k}{k!}m^{\underline{k-1}}n^{m-k+1},$$`
where `$B_k$` are the so-called **Bernoully numbers**, and `$m^{\underline{k-1}}$` are the [falling factorials][bookofproofs$1399]. The Bernoulli numbers have themselves an interesting recursive formula `$$B_0=1,\sum_{k=0}^{n-1} B_k=0,\quad n\ge 2.$$` For instance, the first Bernoulli numbers are 

`$$B_0=1,B_1=-\frac 12,B_2=\frac 16,B_3=0,B_4=-\frac1{30},\ldots.$$` 

In the meanwhile, one has found many applications of Bernoulli numbers in combinatorics, [analysis][bookofproofs$47] and [number theory][bookofproofs$62].
Combinatorics has not only connections to [arithmetics][bookofproofs$195], [analysis][bookofproofs$47], and [probability theory][bookofproofs$73], but also to [geometry][bookofproofs$75]. The first combinatorial problems in geometry were studied by [Leonhard Euler](https://mathshistory.st-andrews.ac.uk/Biographies/Euler/) (1707 - 1783). In particular, his famous _Königsberg problem_, which led to a [corresponding theorem][bookofproofs$6385] and the development of [graph theory][bookofproofs$68] as a separate mathematical discipline, which was called so later in 1878 by 
[James Sylvester](https://mathshistory.st-andrews.ac.uk/Biographies/Sylvester/) (1814 - 1897).

Jacob Bernoulli, [Gottfried Wilhelm von Leibniz][bookofproofs$Leibniz] (1646 - 1716), and also [Abraham de Moivre](https://mathshistory.st-andrews.ac.uk/Biographies/De_Moivre/) (1667 - 1754) studied the [multinomial theorem][bookofproofs$1822] and the properties its [multinomial coefficients][bookofproofs$1819]. At the end of these studies in the year 1796, 
a work with the exuberant title ["Der polynomische Lehrsatz, das wichtigste Theorem der ganzen Analysis"](https://reader.digitale-sammlungen.de/de/fs1/object/display/bsb10082292_00001.html) (engl. "The Multinomial Theorem - the Most Important Theorem of Calculus") was published by 
[Carl Hindenburg](https://mathshistory.st-andrews.ac.uk/Biographies/Hindenburg/) (1741 - 1808). 

In 19th century, combinatorics developed further, becoming a source of many interdisciplinary links between different branches of mathematics mentioned above already: analysis, probability theory, arithmetics, and graph theory. With this respect, this development is remarkable, because traditionally, combinatorics was born out of problem-solving of brain teasers and other seemingly superfluous gimmicks. 

The interdisciplinary character of combinatorics has been maintained in the 20th century and continues so currently, in the 21th century. In particular, the development of computers opened the way to solving problems which were untractable previously. Currently, combinatorics has many applications in mathematics and beyond, including optimization theory, physics, economy, logistics, and computer science.
