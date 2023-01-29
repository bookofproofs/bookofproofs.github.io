layout: definition
categories: branches,analysis
nodeid: bookofproofs$6687
orderid: 50
parentid: bookofproofs$406
title: Hyperbolic Cosine
description: HYPERBOLIC COSINE &#9733; bring your math skills to the graduate level &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$581
keywords: cosine,hyperbolic,hyperbolic cosine function
contributors: bookofproofs

---


---

The real **hyperbolic cosine function** is a [function][bookofproofs$592] defined using the [real exponential function][bookofproofs$281] by the formula

`\[\cosh(x):=\frac 12(\exp(x)+\exp(-x))\]`

for all `\(x\in\mathbb R\)`. Note that `$\cosh$` can be interpreted as the "average" of `$\exp(x)$` and `$\exp(-x)$`.

The following graph visualizes the hyperbolic cosine function:

<div style ='float:left'>
	<div id="box" class="jxgbox" style="width:500px; height:500px;"></div>
</div>
<div style ='clear:both'></div> 
 
§§§1

---

§§§1

<script type="text/javascript">


var brd = JXG.JSXGraph.initBoard('box', {boundingbox: [-10, 10, 10, -10], axis:true});

var f = brd.create('functiongraph',[function(x){ 
	return Math.cosh(x); 
}]);

</script>

