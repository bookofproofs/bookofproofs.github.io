layout: proposition
categories: branches,analysis
nodeid: bookofproofs$6749
orderid: 1000
parentid: bookofproofs$346
title: Inverse Tangent of a Real Variable
description: INVERSE TANGENT OF A REAL VARIABLE ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$581
keywords: inverse tangent,inverse tangents
contributors: bookofproofs

---


---

The [tangent of a real variable][bookofproofs$6746] `$\mathbb R\to\mathbb R,~x\to \tan(x)$`, is [invertible][bookofproofs$1381] on all [real intervals][bookofproofs$1153] `$x\in[-\pi/2+k\pi,\pi/2+k\pi],$` where `$\pi$` denotes the [$\pi$ constant][bookofproofs$6738], and `$k\in\mathbb Z$` denotes an [integer][bookofproofs$844].
Its inverse function `$\arctan$`, called the **inverse tangent**, is [continuous][bookofproofs$1260], [strictly monotonically increasing][bookofproofs$282], and defined by
`\[\arctan:\mathbb R\to\mathbb R.\]`

Since the above proposition holds for all `$k\in\mathbb Z$`, the special case `$k=0$` is called the **principal branch** of `$\arctan$`. The inverse tangent has a graph shown in the following figure:

<div id="box-E21620" class="jxgbox centered" style="max-width:500px; height:500px;"></div>
 
§§§1

---

§§§1

<script type="text/javascript">


var brd = JXG.JSXGraph.initBoard('box-E21620', {boundingbox: [-20, 2.5, 20, -2.5], axis:true});


var p = brd.create('point',[0,Math.PI/2], {name:'π/2',size:1});
var p0 = brd.create('point',[0,-Math.PI/2], {name:'-π/2',size:1});
var p1 = brd.create('point',[1,Math.PI/2], {name:'',size:0});
var p2 = brd.create('point',[-1,-Math.PI/2], {name:'',size:0});
var l1 = brd.create('line',[p,p1], {straightFirst:false, strokeWidth:1, dash:2});
var l2 = brd.create('line',[p0,p2], {straightFirst:false, strokeWidth:1, dash:2});

var f = brd.create('functiongraph',[function(x){ 
	return Math.atan(x); 
}]);

</script>

