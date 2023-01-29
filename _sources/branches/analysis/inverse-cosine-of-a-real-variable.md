layout: proposition
categories: branches,analysis
nodeid: bookofproofs$6747
orderid: 800
parentid: bookofproofs$346
title: Inverse Cosine of a Real Variable
description: INVERSE COSINE OF A REAL VARIABLE &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$581
keywords: cosine,inverse,inverse cosine,real,variable
contributors: bookofproofs

---


---

The [cosine of a real variable][bookofproofs$1745] `$\mathbb R\to\mathbb R,~x\to \cos(x)$`, is [invertible][bookofproofs$1381] on all [real intervals][bookofproofs$1153]  `$x\in[k,(k+1)\pi],$` where `$\pi$` denotes the [$\pi$ constant][bookofproofs$6738], and `$k\in\mathbb Z$` denotes an [integer][bookofproofs$844].
Its inverse function `$\arccos$`, called the **inverse cosine**, is [continuous][bookofproofs$1260], [strictly monotonically decreasing][bookofproofs$282], and defined by
`\[\arccos:[-1,1]\to\mathbb R.\]`

Since the above proposition holds for all `$k\in\mathbb Z$`, the special case `$k=0$` is called the **principal branch** of `$\arccos$`. The inverse cosine has a graph shown in the following figure:

<div style ='float:left'>
	<div id="box" class="jxgbox" style="width:500px; height:500px;"></div>
</div>
<div style ='clear:both'></div> 
 
§§§1

---

§§§1

<script type="text/javascript">


var brd = JXG.JSXGraph.initBoard('box', {boundingbox: [-1.1, 4, 1.1, -0.5], axis:true});


var p = brd.create('point',[0,Math.PI], {name:'π',size:1});
var p1 = brd.create('point',[-1,0], {size:1, name:''});
var p2 = brd.create('point',[1,0], {size:1, name:''});
var p3 = brd.create('point',[-1,Math.PI], {size:1, name:''});
var l1 = brd.create('line',[p1,p3], {straightFirst:false, straightLast:false, strokeWidth:1, dash:2});
var l2 = brd.create('line',[p,p3], {straightFirst:false, straightLast:false, strokeWidth:1, dash:2});

var f = brd.create('functiongraph',[function(x){ 
	return Math.acos(x); 
}]);

</script>

