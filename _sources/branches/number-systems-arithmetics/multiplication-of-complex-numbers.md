layout: definition
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1668
orderid: 400
parentid: bookofproofs$216
title: Multiplication of Complex Numbers
description: MULTIPLICATION OF COMPLEX NUMBERS ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$696
keywords: multiplication of complex numbers,multiplying complex numbers,product of complex numbers,product,products
contributors: bookofproofs

---


---

According to the [definition of complex numbers][bookofproofs$216], we can consider the complex numbers `\(x,y\in\mathbb C\)` as ordered pairs of some real numbers `\(a,b,c,d\in\mathbb R\)`, i.e. `\(x=(a,b)\)` and `\(y=(c,d)\)`.

The **multiplication of complex numbers** "`\(\cdot\)`" is defined based on the [addition][bookofproofs$1514], [subtraction][bookofproofs$1588], and [multiplication of real numbers][bookofproofs$1532] in the corresponding ordered pairs:

`\[x\cdot y:=(a,b)\cdot (c,d):=(ac-bd,ad+bc),\]`

Note that this kind of multiplication operation always produces a new ordered pair of real numbers `\((ac-bd,ad+bc)\)`, which is a new complex number, called the **product of the complex numbers** `\(x\)` and `\(y\)`. Thus, the set of complex numbers `\(\mathbb C\)` is closed under this kind of multiplication operation.

The multiplication of two complex numbers (points in the complex plane) `\(x\)` and `\(y\)` can be interpreted/constructed as follows:

1. Connect `\(x\)` and `\(y\)` with the origin of the complex plane.
1. Measure the angles of the segments with respect to the positive horizontal axis. 
1. Measure the lengths of the segments.
1. Add the two angles.
1. Multiply the two lengths.
1. The point `\(x\cdot y\)` lies on the segment with the length gained in step 5 with an angle to the positive horizontal axis gained in step 4.

In the following figure, you can drag the complex numbers `\(x\)` and `\(y\)` and see, how the position of `\(x\cdot y\)` changes with the position of the respective factors `\(x\)` and `\(y\)`:

<div id="boxE20716" class="jxgbox centered" style="max-width:500px; height:500px;"></div>

### Fun questions:

* Why is the product of two negative real numbers positive?
* Can you find point `\(x\)` in the complex plain, for which `\(x=\sqrt{-1}\)`? (See also [imaginary unit][bookofproofs$1160])


§§§1

---

§§§1

<script type="text/javascript">
board = JXG.JSXGraph.initBoard('boxE20716', {boundingbox: [-4, 4, 6, -3], axis: true});
 
var org = board.create('point', [0,0], {style:10,visible:true,fixed:true,name:' '});
var x = board.create('point', [2,1], {style:5,color:'blue',name:'x'});
var y = board.create('point', [2,-1], {style:5,color:'blue',name:'y'});
var xy = board.create('point', 
    ["X(x)*X(y)-Y(x)*Y(y)","X(x)*Y(y)+Y(x)*X(y)"], {style:7,color:'green',name:'x*y'});
var ax =board.create('arrow', [org,x], {strokeColor:'blue'});
var ay =board.create('arrow', [org,y], {strokeColor:'blue'});
var axy =board.create('arrow', [org,xy], {strokeColor:'red'});
var ax2 =board.create('arrow', [x,xy], {strokeColor:'blue',strokeWidth:1,dash:1});
var ay2 =board.create('arrow', [y,xy], {strokeColor:'blue',strokeWidth:1,dash:1})
</script>

