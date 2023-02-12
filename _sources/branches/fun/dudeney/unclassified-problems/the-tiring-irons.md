layout: problem
categories: branches,fun,dudeney,unclassified-problems
nodeid: bookofproofs$7697
orderid: 3
parentid: bookofproofs$7651
title: The Tiring Irons
description: THE TIRING IRONS &#9733; bring your math skills to the graduate level &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$6929
keywords: problems,unclassified,solution
contributors: @H-Dudeney,bookofproofs

---


---

![q417a](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/dudeney/q417a.png?raw=true)

The illustration represents one of the most ancient of all mechanical puzzles. Its origin is unknown. Cardan, the mathematician, wrote about it in 1550, and Wallis in 1693; while it is said still to be found in obscure English villages (sometimes deposited in strange places, such as a church belfry), made of iron, and appropriately called "tiring-irons," and to be used by the Norwegians to-day as a lock for boxes and bags. In the toyshops, it is sometimes called the "Chinese rings," though there seems to be no authority for the description, and it more frequently goes by the unsatisfactory name of "the puzzling rings." The French call it "Baguenaudier."

The puzzle will be seen to consist of a simple loop of wire fixed in a handle to be held in the left hand, and a certain number of rings secured by wires which pass through holes in the bar and are kept there by their blunted ends. The wires work freely in the bar, but cannot come apart from it, nor can the wires be removed from the rings. The general puzzle is to detach the loop completely from all the rings, and then to put them all on again.

Now, it will be seen at a glance that the first ring (to the right) can be taken off at any time by sliding it over the end and dropping it through the loop; or it may be put on by reversing the operation. With this exception, the only ring that can ever be removed is the one that happens to be a contiguous second on the loop at the right-hand end. Thus, with all the rings on, the second can be dropped at once; with the first ring down, you cannot drop the second, but may remove the third; with the first three rings down, you cannot drop the fourth, but may remove the fifth; and so on. It will be found that the first and second rings can be dropped together or put on together, but to prevent confusion we will throughout disallow this exceptional double move, and say that only one ring may be put on or removed at a time.

We can thus take off one ring in `$1$` move; two rings in `$2$` moves; three rings in `$5$` moves; four rings in `$10$` moves; five rings in `$21$` moves; and if we keep on doubling (and adding one where the number of rings is odd) we may easily ascertain the number of moves for completely removing any number of rings. To get off all the seven rings requires 85 moves. Let us look at the five moves made in removing the first three rings, the circles above the line standing for rings on the loop and those under for rings off the loop.

Drop the first ring; drop the third; put up the first; drop the second; and drop the first — `$5$` moves, as shown clearly in the diagrams. The dark circles show at each stage, from the starting position to the finish, which rings it is possible to drop. After move `$2$` it will be noticed that no ring can be dropped until one has been put on because the first and second rings from the right now on the loop are not together. After the fifth move, if we wish to remove all seven rings we must now drop the fifth. But before we can then remove the fourth it is necessary to put on the first three and remove the first two. We shall then have `$7, 6, 4, 3$` on the loop, and may, therefore, drop the fourth. When we have put on `$2$` and `$1$` and removed `$3, 2, 1,$` we may drop the seventh ring. The next operation then will be to get `$6,$` `$5, 4, 3, 2, 1$` on the loop and remove `$4, 3, 2, 1,$` when `$6$` will come off; then get `$5, 4, 3, 2, 1$` on the loop, and remove `$3, 2, 1,$` when `$5$` will come off; then get `$4, 3, 2, 1$` on the loop and remove `$2, 1,$` when `$4$` will come off; then get `$3, 2, 1$` on the loop and remove `$1,$` when `$3$` will come off; then get `$2, 1$` on the loop, when `$2$` will come off; and `$1$` will fall through on the 85th move, leaving the loop quite free. The reader should now be able to understand the puzzle, whether or not he has it in his hand in a practical form.

![q417b](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/dudeney/q417b.png?raw=true)

The particular problem I propose is simply this. Suppose there are altogether fourteen rings on the tiring-irons, and we proceed to take them all off in the correct way so as not to waste any moves. What will be the position of the rings after the `$9,999$`th move has been made?
