layout: definition
categories: branches,analysis
nodeid: bookofproofs$6746
orderid: 200
parentid: bookofproofs$346
title: Tangent of a Real Variable
description: TANGENT OF A REAL VARIABLE ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$581
keywords: tangent,tangent function
contributors: bookofproofs

---


---

Let `\(x\in\mathbb R\)` be any [real number][bookofproofs$1105]. The **tangent** of `\(x\)` is a [function][bookofproofs$592] `\(\tan:\mathbb R\mapsto\mathbb R\)` defined as the ratio of the [sine][bookofproofs$1746] and [cosine][bookofproofs$1745] of `$x$`, formally, 

`$$\tan(x):=\frac{\sin(x)}{\cos(x)}.$$`

The tangent function has is demonstrated in the following figure:


<div id="box-E21619" class="jxgbox centered" style="max-width:500px; height:500px;"></div>
 
§§§1

---

§§§1

<script type="text/javascript">


var brd = JXG.JSXGraph.initBoard('box-E21619', {boundingbox: [-7.1, 20, 7.1, -20], axis:true});


var p = brd.create('point',[Math.PI/2,0], {name:'π/2',size:1});
var p1 = brd.create('point',[-Math.PI/2,0], {name:'-π/2',size:1});
var p2 = brd.create('point',[3*Math.PI/2,0], {name:'3π/2',size:1});
var p3 = brd.create('point',[-3*Math.PI/2,0], {name:'-3π/2',size:1});

var f = brd.create('functiongraph',[function(x){ 
	return Math.tan(x); 
}]);

</script>

