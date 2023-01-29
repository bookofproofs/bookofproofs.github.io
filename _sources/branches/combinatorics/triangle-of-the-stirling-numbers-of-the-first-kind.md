layout: chapter
categories: branches,combinatorics
nodeid: bookofproofs$8430
orderid: 300
parentid: bookofproofs$293
title: Triangle of the Stirling Numbers of the First Kind
description: TRIANGLE OF THE STIRLING NUMBERS OF THE FIRST KIND ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$8404
keywords: triangle of the stirling numbers of the first kind
contributors: bookofproofs


---


---

The [Stirling numbers of the first kind][bookofproofs$8425] `$\left[\begin{array}{c}n\\r\end{array}\right],$` where `$n$` and `$r$` are [natural numbers][bookofproofs$718], are named after "James Stirling":https://www.bookofproofs.org/history/james-stirling (1692 - 1770). According to the "corresponding recursive formula":https://www.bookofproofs.org/branches/recursive-formula-for-the-stirling-number-of-the-first-kind/, they form a triangular scheme, in analogy to the [Pascal's triangle][bookofproofs$1409] for binomial coefficients. For the first `$10$` values of `$n$` this scheme is

`\[\begin{array}{r|rrrrrrrrrr}
n&\left[\begin{array}{c}n\\0\end{array}\right]&\left[\begin{array}{c}n\\1\end{array}\right]&\left[\begin{array}{c}n\\2\end{array}\right]&\left[\begin{array}{c}n\\3\end{array}\right]&\left[\begin{array}{c}n\\4\end{array}\right]&\left[\begin{array}{c}n\\5\end{array}\right]&\left[\begin{array}{c}n\\6\end{array}\right]&\left[\begin{array}{c}n\\7\end{array}\right]&\left[\begin{array}{c}n\\8\end{array}\right]&\left[\begin{array}{c}n\\9\end{array}\right]&\left[\begin{array}{c}n\\10\end{array}\right]\\
\hline
0&1\\
1&&1\\
2&&1&1\\
3&&2&3&1\\
4&&6&11&6&1\\
5&&24&50&35&10&1\\
6&&120&274&225&85&15&1\\
7&&720&1764&1624&735&175&21&1\\
8&&5040&13068&13132&6769&1960&322&28&1\\
9&&40320&109584&118124&67284&22449&4536&546&36&1\\
10&&362880&1026576&1172700&723680&269325&63273&9450&870&45&1\\
\end{array}\]`

Note that empty entries in this table are actually `\(0\)`'s.
