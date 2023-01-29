layout: proposition
categories: branches,analysis
nodeid: bookofproofs$6720
orderid: 1400
parentid: bookofproofs$8673
title: Infinitesimal Exponential Growth is the Growth of the Identity Function
description: INFINITESIMAL EXPONENTIAL GROWTH IS THE GROWTH OF THE IDENTITY FUNCTION ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$581
keywords: exponential growth,infinitesimal
contributors: bookofproofs

---


---

The [exponential function][bookofproofs$281] growth at `$0$` is the same as the growth of the [identify function][bookofproofs$6680], formally
`$$ \lim_{x\to 0,~x\neq 0}\frac{e^x-1}{x}=1.$$`

The following figure visualizes the behavior of both functions at `$0$` (for a better comparison, instead of the identity function `$f(x)=x$`, the function `$f(x)=x+1$` was drawn together with the function `$g(x)=\exp(x)$`:


<div id="boxE20297" class="jxgbox centered" style="width:500px; height:500px;"></div>
<div style ='clear:both'></div> 
 
§§§1

---

§§§1

<script type="text/javascript">


var brd = JXG.JSXGraph.initBoard('boxE20297', {boundingbox: [-1.5, 2.5, 1.5, -0.5], axis:true});

var f = brd.create('functiongraph',[function(x){ 
	return Math.exp(x); 
}]);

var f = brd.create('functiongraph',[function(x){ 
	return x+1; 
}]);


</script>

