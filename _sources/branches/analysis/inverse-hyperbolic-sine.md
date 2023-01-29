layout: proposition
categories: branches,analysis
nodeid: bookofproofs$6722
orderid: 50
parentid: bookofproofs$415
title: Inverse Hyperbolic Sine
description: INVERSE HYPERBOLIC SINE &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$581
keywords: hyperbolic,inverse,sine
contributors: bookofproofs

---


---

The [hyperbolic sine][bookofproofs$6688] `$\mathbb R\to\mathbb R,~x\to\sinh(x)$` is [invertible][bookofproofs$1381] for all [real numbers][bookofproofs$1105] `$x\in\mathbb R.$` Its inverse function is called the **inverse hyperbolic sine** `$$\operatorname{arsinh}:\mathbb R\to\mathbb R,$$` and can be calculated using the formula
`$$\operatorname{arsinh}(x)=\ln\left(x+\sqrt{1+x^2}\right).$$`

The following graph visualizes the inverse hyperbolic sine function:

<div style ='float:left'>
	<div id="box" class="jxgbox" style="width:500px; height:500px;"></div>
</div>
<div style ='clear:both'></div> 
 
§§§1

---

§§§1

<script type="text/javascript">


var brd = JXG.JSXGraph.initBoard('box', {boundingbox: [-5, 5, 5, -5], axis:true});

var f = brd.create('functiongraph',[function(x){ 
	return Math.log(x+Math.sqrt(1+x*x)); 
}]);

</script>

