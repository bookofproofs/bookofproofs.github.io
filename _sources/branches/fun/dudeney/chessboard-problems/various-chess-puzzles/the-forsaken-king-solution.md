layout: solution
categories: branches,fun,dudeney,chessboard-problems,various-chess-puzzles
nodeid: bookofproofs$7341
orderid: 0
parentid: bookofproofs$7340
title: 
description: SOLUTION OF THE FORSAKEN KING &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$6929
keywords: forsaken,king solution
contributors: bookofproofs

---


---

In the original Dudeney's Book from the beginning of the 20th century, the following cases are given, in which the black King is mated in only 6 moves. 

> Play as follows:—
White.	Black.
1. P to K 4th	1. Any move
2. Q to Kt 4th	2. Any move except on KB file (a)
3. Q to Kt 7th	3. K moves to royal row
4. B to Kt 5th	4. Any move
5. Mate in two moves
	If 3. K other than to royal row
4. P to Q 4th	4. Any move
5. Mate in two moves
	(a) If 2. Any move on KB file
3. Q to Q 7th	3. K moves to royal row
4. P to Q Kt 3rd	4. Any move
5. Mate in two moves
	If 3. K other than to royal row
4. P to Q 4th	4. Any move
5. Mate in two moves
Of course, by "royal row" is meant the row on which the king originally stands at the beginning of a game. Though, if Black plays badly, he may, in certain positions, be mated in fewer moves, the above provides for every variation he can possibly bring about.

Unfortunately, the solution is wrong. Modern Chess Engines prove that the shortest number of moves needed to mate the Black King starting from the original position is seven if Black tries to make it as hard for White as possible to win.

The solution (found by the Fritz Chess Engine) is:

1. e2-e4 Ke8-e7
1. Qd1-h5 Ke7-e6
1. Qh5-e8+ Ke6-f6
1. Bf1-c4 Kf6-g5
1. d2-d3+ Kg5-g4
1. h2-h3+ Kg4-h4
1. Sg1-f3#


![dudeneychess](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/dudeney/dudeneychess.png?raw=true)
