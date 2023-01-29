layout: definition
categories: branches,analysis
nodeid: bookofproofs$6688
orderid: 100
parentid: bookofproofs$406
title: Hyperbolic Sine
description: HYPERBOLIC SINE &#9733; bring your math skills to the graduate level &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$581
keywords: hyperbolic,hyperbolic sine function,sine
contributors: bookofproofs

---


---

The real **hyperbolic sine function** is a [function][bookofproofs$592] defined using the [real exponential function][bookofproofs$281] by the formula

`\[\sinh(x):=\frac 12(\exp(x)-\exp(-x))\]`

for all `\(x\in\mathbb R\)`. Note that `$\cosh$` can be interpreted as the "half the difference" of `$\exp(x)$` and `$\exp(-x)$`.

The following graph visualizes the hyperbolic sine function:

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
	return Math.sinh(x); 
}]);

</script>

