layout: definition
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1657
orderid: 200
parentid: bookofproofs$216
title: Addition of Complex Numbers
description: ADDITION OF COMPLEX NUMBERS ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$581
keywords: addition of complex numbers,adding complex numbers,add complex numbers,sum of complex numbers
contributors: bookofproofs

---


---

According to the [definition of complex numbers][bookofproofs$216], we can consider the complex numbers `\(x,y\in\mathbb C\)` as ordered pairs of some real numbers `\(a,b,c,d\in\mathbb R\)`, i.e. `\(x=(a,b)\)` and `\(y=(c,d)\)`.

The **addition of complex numbers** "`\(+\)`" is defined based on the [addition of the real numbers][bookofproofs$1514] of the corresponding ordered pairs, as follows:

`\[x+y:=(a,b)+(c,d):=(a+c,b+d),\]`

Note that this kind of addition operation always produces a new ordered pair of real numbers `\((a+c,b+d)\)`, which is a new complex number, called the **sum of the complex numbers** `\(x\)` and `\(y\)`. Thus, the set of complex numbers `\(\mathbb C\)` is closed under this kind of addition operation.

The addition of two complex numbers can be interpreted as the addition of two vectors in the complex plain, which can be constructed using a parallelogram. In the following figure, you can drag the complex numbers `\(x\)` and `\(y\)` and see, how their position changes the position of the respective sum `\(x+y\)`:


<div id="boxE20715" class="jxgbox centered" style="max-width:500px; height:500px;"></div>
<div style ='clear:both'></div> 
 
§§§1

---

§§§1

<script type="text/javascript">
board = JXG.JSXGraph.initBoard('boxE20715', {boundingbox: [-6, 6, 6, -6], axis: true});
 
var org = board.create('point', [0,0], {style:10,visible:true,fixed:true,name:' '});
var x = board.create('point', [2,2], {style:5,color:'blue',name:'x'});
var y = board.create('point', [-1,-3], {style:5,color:'blue',name:'y'});
var xy = board.create('point', 
    ["X(x)+X(y)","Y(x)+Y(y)"], {style:7,color:'green',name:'x+y'});
var ax =board.create('arrow', [org,x], {strokeColor:'blue'});
var ay =board.create('arrow', [org,y], {strokeColor:'blue'});
var axy =board.create('arrow', [org,xy], {strokeColor:'red'});
var ax2 =board.create('arrow', [x,xy], {strokeColor:'blue',strokeWidth:1,dash:1});
var ay2 =board.create('arrow', [y,xy], {strokeColor:'blue',strokeWidth:1,dash:1})
</script>

