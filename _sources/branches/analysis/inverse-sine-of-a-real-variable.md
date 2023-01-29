layout: proposition
categories: branches,analysis
nodeid: bookofproofs$6748
orderid: 900
parentid: bookofproofs$346
title: Inverse Sine of a Real Variable
description: INVERSE SINE OF A REAL VARIABLE ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$581
keywords: inverse,inverse sine,real,sine,variable
contributors: bookofproofs

---


---

The [sine of a real variable][bookofproofs$1746] `$\mathbb R\to\mathbb R,~x\to \sin(x)$`, is [invertible][bookofproofs$1381] on all [real intervals][bookofproofs$1153] `$x\in[-\pi/2+k\pi,\pi/2+k\pi],$` where `$\pi$` denotes the [$\pi$ constant][bookofproofs$6738], and `$k\in\mathbb Z$` denotes an [integer][bookofproofs$844].
Its inverse function `$\arcsin$`, called the **inverse sine**, is [continuous][bookofproofs$1260], [strictly monotonically increasing][bookofproofs$282], and defined by
`\[\arcsin:[-1,1]\to\mathbb R.\]`

Since the above proposition holds for all `$k\in\mathbb Z$`, the special case `$k=0$` is called the **principal branch** of `$\arcsin$`. The inverse sine has a graph shown in the following figure:


<div id="boxE20211" class="jxgbox centered" style="max-width:500px; height:500px;"></div>
<div style ='clear:both'></div> 
 
§§§1

---

§§§1

<script type="text/javascript">


var brd = JXG.JSXGraph.initBoard('boxE20211', {boundingbox: [-1.1, 2, 1.1, -2], axis:true});


var p = brd.create('point',[0,Math.PI/2], {name:'π/2',size:1});
var p0 = brd.create('point',[0,-Math.PI/2], {name:'-π/2',size:1});
var p1 = brd.create('point',[-1,0], {size:1, name:''});
var p2 = brd.create('point',[1,0], {size:1, name:''});
var p3 = brd.create('point',[1,Math.PI/2], {size:1, name:''});
var p4 = brd.create('point',[-1,-Math.PI/2], {size:1, name:''});
var l1 = brd.create('line',[p2,p3], {straightFirst:false, straightLast:false, strokeWidth:1, dash:2});
var l2 = brd.create('line',[p,p3], {straightFirst:false, straightLast:false, strokeWidth:1, dash:2});
var l3 = brd.create('line',[p1,p4], {straightFirst:false, straightLast:false, strokeWidth:1, dash:2});
var l4 = brd.create('line',[p0,p4], {straightFirst:false, straightLast:false, strokeWidth:1, dash:2});

var f = brd.create('functiongraph',[function(x){ 
	return Math.asin(x); 
}]);

</script>

