layout: solution
categories: branches,fun,dudeney,unclassified-problems
nodeid: bookofproofs$7725
orderid: 0
parentid: bookofproofs$7697
title: 
description: SOLUTION OF THE TIRING IRONS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$6929
keywords: problems,unclassified,solution,tiring-irons,solution
contributors: bookofproofs
issues: malformed-tables

---


---

I will give my complete working on the solution, so that readers may see how easy it is when you know how to proceed. And first of all, as there is an even number of rings, I will say that they may all be taken off in one-third of `$(2^{n + 1} - 2)$` moves; and since `$n$` in our case is `$14,$` all the rings may be taken off in `$10,922$` moves. Then I say `$$10,922- 9,999 = 923,$$` and proceed to find the position when only `$923$` out of the `$10,922$` moves remain to be made. Here is the curious method of doing this. It is based on the binary scale method used by Monsieur L. Gros, for an account of which see W.W. Rouse Ball's __Mathematical Recreations.__

Divide `$923$` by `$2,$` and we get `$461$` and the remainder `$1;$` divide `$461$` by `$2,$` and we get `$230$` and the remainder `$1;$` divide `$230$` by `$2,$` and we get `$115$` and the remainder nought. Keep on dividing by `$2$` in this way as long as possible, and all the remainders will be found to be `$1,$` `$1,$` `$1,$` `$0,$` `$0,$` `$1,$` `$1,$` `$0,$` `$1,$` `$1,$` the last remainder being to the left and the first remainder to the right. As there are fourteen rings and only ten figures, we place the difference, in the form of four noughts, in brackets to the left, and bracket all those figures that repeat a figure on their left. Then we get the following arrangement: `$(0 0 0 0)$` `$1$` `$(1 1)$` `$0$` `$(0)$` `$1$` `$(1)$` `$0 1$` `$(1). $`This is the correct answer to the puzzle, for if we now place rings below the line to represent the figures in brackets and rings on the line for the other figures, we get the solution in the required form, as below:—

![a417](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/dudeney/a417.png?raw=true)

This is the exact position of the rings after the `$9,999$`th move has been made, and the reader will find that the method shown will solve any similar question, no matter how many rings are on the tiring-irons. But in working the inverse process, where you are required to ascertain the number of moves necessary in order to reach a given position of the rings, the rule will require a little modification, because it does not necessarily follow that the position is one that is actually reached in course of taking off all the rings on the irons, as the reader will presently see. I will here state that where the total number of rings is odd the number of moves required to take them all off is one-third of `$(2^{n + 1}- 1)$`.

* With `$n$` rings (where `$n$` is odd) there are `$2^n$` positions counting all on and all off. In `$\frac{1}{3}(2^{n+1} + 2)$` positions they are all removed. The number of positions not used is `$\frac{1}{3}(2^n- 2).$`
* With `$n$` rings (where `$n$` is even) there are `$2^n$` positions counting all on and all off. In `$(2^{n + 1} + 1)$` positions they are all removed. The number of positions not used is here `$\frac{1}{3}(2^n- 1).$`

It will be convenient to tabulate a few cases.


No. of Rings | Total Positions | Positions used | Positions not used
:------------- |:------------- |:------------- |:-------------
 `$1$`| `$2$`| `$2$`| `$0$`
 `$3$`| `$8$`| `$6$`| `$2$`
 `$5$`| `$32$`| `$22$`| `$10$`
 `$7$`| `$128$`| `$86$`| `$42$`
 `$9$`| `$512$`| `$342$`| `$170$`
 `$2$`| `$4$`| `$3$`| `$1$`
 `$4$`| `$16$`| `$11$`| `$5$`
 `$6$`| `$64$`| `$43$`| `$21$`
 `$8$`| `$256$`| `$171$`| `$85$`
 `$10$`| `$1024$`| `$683$`| `$341$`

Note first that the number of positions used is one more than the number of moves required to take all the rings off because we are including "all on" which is a position but not a move. Then note that the number of positions not used is the same as the number of moves used to take off a set that has one ring fewer. For example, it takes `$85$` moves to remove `$7$` rings, and the `$42$` positions not used are exactly the number of moves required to take off a set of `$6$` rings. The fact is that if there are `$7$` rings and you take off the first `$6,$` and then wish to remove the `$7$`th ring, there is no course open to you but to reverse all those `$42$` moves that never ought to have been made. In other words, you must replace all the `$7$` rings on the loop and start afresh! You ought first to have taken off `$5$` rings, to do which you should have taken off `$3$` rings, and previously to that `$1$` ring. To take off `$6$` you first remove `$2$` and then `$4$` rings.
