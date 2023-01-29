layout: proposition
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1675
orderid: 300
parentid: bookofproofs$1668
title: Existence of Inverse Complex Numbers With Respect to Multiplication
description: EXISTENCE OF INVERSE COMPLEX NUMBERS WITH RESPECT TO MULTIPLICATION ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$581
keywords: complex multiplication,inverse
contributors: bookofproofs

---


---

For each `\(x\in\mathbb C\)`, `\(x\neq 0\)`, there exists a number `\(x^{-1}\in\mathbb C\)` with `\(x\cdot x^{-1}=1\)`.

In particular, the inverse of `$x\neq 0$` can be calculated using the formula
`$$\frac 1x=\frac{\Re(x)-\Im(x)}{|x|^2}$$`

In the following interactive figure, you can experiment with the value of `\(x\)` (i.e. its position in the complex plane) and see, how it influences the value of `\(x^{-1}\)`, the inverse complex number with respect to multiplication:


<div id="boxE22644" class="jxgbox centered" style="max-width:500px; height:500px;"></div>
 
§§§1

---

§§§1

<script type="text/javascript">
board = JXG.JSXGraph.initBoard('boxE22644', {boundingbox: [-3, 3, 3, -3], axis: true});
 
var org = board.create('point', [0,0], {style:10,visible:true,fixed:true,name:' '});
var x = board.create('point', [1,1], {style:5,color:'blue',name:'x'});
var mx = board.create('point', ["X(x)/(X(x)*X(x)+Y(x)*Y(x))","-Y(x)/(X(x)*X(x)+Y(x)*Y(x))"], {style:5,color:'green',name:'x^{-1}'});
var ax =board.create('arrow', [org,x], {strokeColor:'blue',strokeWidth:1,dash:1});
var amx =board.create('arrow', [org,mx], {strokeColor:'blue',strokeWidth:1,dash:1});
</script>

