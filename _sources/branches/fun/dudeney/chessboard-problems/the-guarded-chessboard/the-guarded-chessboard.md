layout: section
categories: branches,fun,dudeney,chessboard-problems,the-guarded-chessboard
nodeid: bookofproofs$7217
orderid: 2
parentid: bookofproofs$7214
title: The Guarded Chessboard
description: THE GUARDED CHESSBOARD &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$6929
keywords: chessboard,guarded
contributors: bookofproofs
issues: malformed-tables

---


---

On an ordinary chessboard, `$8$` by `$8$`, every square can be guarded—that is, either occupied or attacked—by `$5$` queens, the fewest possible. There are exactly `$91$` fundamentally different arrangements in which no queen attacks another queen. If every queen must attack (or be protected by) another queen, there are at fewest `$41$` arrangements, and I have recorded some `$150$` ways in which some of the queens are attacked and some not, but this last case is very difficult to enumerate exactly.

On an ordinary chessboard, every square can be guarded by `$8$` rooks (the fewest possible) in `$40,320$` ways, if no rook may attack another rook, but it is not known how many of these are fundamentally different. (See solution to No. 295, "The Eight Rooks.") I have not enumerated the ways in which every rook shall be protected by another rook.

On an ordinary chessboard, every square can be guarded by `$8$` bishops (the fewest possible), if no bishop may attack another bishop. Ten bishops are necessary if every bishop is to be protected. (See Nos. 297 and 298, "Bishops unguarded" and "Bishops guarded.")

On an ordinary chessboard, every square can be guarded by `$12$` knights if all but `$4$` are unprotected. But if every knight must be protected, `$14$` are necessary. (See No. 319, "The Knight-Guards.")

Dealing with the queen on `$n^2$` boards generally, where n is less than `$8$`, the following results will be of interest:—

* `$1$` queen guards `$2^2$` board in `$1$` fundamental way.
* `$1$` queen guards `$3^2$` board in `$1$` fundamental way.
* `$2$` queens guard `$4^2$` board in `$3$` fundamental ways (protected).
* `$3$` queens guard `$4^2$` board in `$2$` fundamental ways (not protected).
* `$3$` queens guard `$5^2$` board in `$37$` fundamental ways (protected).
* `$3$` queens guard `$5^2$` board in `$2$` fundamental ways (not protected).
* `$3$` queens guard `$6^2$` board in `$1$` fundamental way (protected).
* `$4$` queens guard `$6^2$` board in `$17$` fundamental ways (not protected).
* `$4$` queens guard `$7^2$` board in `$5$` fundamental ways (protected).
* `$4$` queens guard `$7^2$` board in `$1$` fundamental way (not protected).

### Non-Attacking Chessboard Arrangements

We know that n queens may always be placed on a square board of `$n^2$` squares (if `$n$` be greater than `$3$`) without any queen attacking another queen. But no general formula for enumerating the number of different ways in which it may be done has yet been discovered; probably it is undiscoverable. The known results are as follows:—

* Where `$n = 4$` there is `$1$` fundamental solution and `$2$` in all.
* Where `$n = 5$` there are `$2$` fundamental solutions and `$10$` in all.
* Where `$n = 6$` there is `$1$` fundamental solution and `$4$` in all.
* Where `$n = 7$` there are `$6$` fundamental solutions and `$40$` in all.
* Where `$n = 8$` there are `$12$` fundamental solutions and `$92$` in all.
* Where `$n = 9$` there are `$46$` fundamental solutions.
* Where `$n = 10$` there are `$92$` fundamental solutions.
* Where `$n = 11$` there are `$341$` fundamental solutions.

Obviously, `$n$` rooks may be placed without an attack on an `$n^2$`  board in `$n!$` ways, but how many of these are fundamentally different I have only worked out in the four cases where `$n$` equals `$2$`, `$3$`, `$4$`, and `$5.$` The answers here are respectively `$1$`, `$2$`, `$7,$` and `$23.$` (See [The Four Lions][bookofproofs$7228])

We can place `$2n-2$` bishops on an `$n^2$` board in `$2^n$` ways. (See No. 299, "Bishops in Convocation.") For boards containing `$2,$` `$3,$` `$4,$` `$5,$` `$6,$` `$7,$` `$8$` squares, on a side there are respectively `$1,$` `$2,$` `$3,$` `$6,$` `$10,$` `$20,$` `$36$` fundamentally different arrangements. Where `$n$` is [odd][bookofproofs$2318] there are `$2^{\sqrt{n-1}}$` such arrangements, each giving `$4$` by reversals and reflections, and `$2^{n-3} - 2^{\sqrt{n-3}}$` giving `$8$`. Where `$n$` is [even][bookofproofs$2317] there are `$2^{\sqrt{n-2}}$`, each giving `$4$` by reversals and reflections, and `$2^{n-3} - 2^{\sqrt{n-4}}$`, each giving `$8.$`

We can place `$\frac 12(n^2+1)$` knights on an `$n^2$` board without attack, when `$n$` is odd, in `$1$` fundamental way; and `$\frac {n^2}2$` knights on an `$n^2$` board, when `$n$` is even, in `$1$` fundamental way. In the first case we place all the knights in the same color as the central square; in the second case, we place them all on black, or all on white, squares.

### The Two Pieces Problem

On a board of `$n^2$` squares, two queens, two rooks, two bishops, or two knights can always be placed, irrespective of attack or not, in `$\frac 12(n^4 - n^2)$` ways. The following formulæ will show in how many of these ways the two pieces may be placed under attack and without:—


 | With Attack | Without Attack
:------------- |:------------- |:-------------
<. `$2$` Queens| `$\frac{5n^3 - 6n^2 + n}3$`| `$\frac{3n^4 - 10n^3 + 9n^2 - 2n}6$`
<. `$2$` Rooks| `$n^3 - n^2$`| `$\frac{n^4 - 2n^3 + n^2}2$`
<. `$2$` Bishops|  `$\frac{4n^3 - 6n^2 + 2n}6$`| `$\frac{3n^4 - 4n^3 + 3n^2 - 2n}6$`
<. `$2$` Knights| `$4n^2 - 12n + 8$`| `$\frac{n^4 - 9n^2 + 24n}2$`

(See [Lion-Hunting][bookofproofs$7250])
