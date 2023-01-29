layout: proposition
categories: branches,analysis
nodeid: bookofproofs$6723
orderid: 100
parentid: bookofproofs$415
title: Inverse Hyperbolic Cosine
description: INVERSE HYPERBOLIC COSINE &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: 
keywords: cosine,hyperbolic,inverse
contributors: bookofproofs

---


---

The [hyperbolic cosine][bookofproofs$6688] `$\mathbb R\to\mathbb R,~x\to\sinh(x)$` is [invertible][bookofproofs$1381] for all [positive real numbers][bookofproofs$1107] `$x\ge 0.$` Its inverse function is called the **inverse hyperbolic cosine** `$$\operatorname{arcosh}:[0,\infty[\to[1,\infty[,$$` and can be calculated using the formula
`$$\operatorname{arcosh}(x)=\ln\left(x+\sqrt{x^2-1}\right).$$`

The following graph visualizes the inverse hyperbolic cosine function:

<div style ='float:left'>
	<div id="box" class="jxgbox" style="width:500px; height:500px;"></div>
</div>
<div style ='clear:both'></div> 
 
§§§1

---

§§§1

<script type="text/javascript">


var brd = JXG.JSXGraph.initBoard('box', {boundingbox: [0, 5, 15, -5], axis:true});

var f = brd.create('functiongraph',[function(x){ 
	return Math.log(x+Math.sqrt(x*x-1)); 
}]);

</script>

