layout: proposition
categories: branches,analysis
nodeid: bookofproofs$6733
orderid: 1500
parentid: bookofproofs$8673
title: Infinitesimal Growth of Sine is the Growth of the Identity Function
description: INFINITESIMAL GROWTH OF SINE IS THE GROWTH OF THE IDENTITY FUNCTION &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$581
keywords: function,growth,identity,infinitesimal,sine
contributors: bookofproofs

---


---

The [sine function][bookofproofs$1746] has the same growth at `$0$` as the growth of the [identify function][bookofproofs$6680], formally
`$$ \lim_{x\to 0,~x\neq 0}\frac{\sin(x)}{x}=1.$$`

The following figure visualizes the behavior of both functions at `$0$`, function `$f(x)=x$` is drawn together with the function `$g(x)=\sin(x)$`:


<div style ='float:left'>
	<div id="box" class="jxgbox" style="width:500px; height:500px;"></div>
</div>
<div style ='clear:both'></div> 
 
§§§1

---

§§§1

<script type="text/javascript">


var brd = JXG.JSXGraph.initBoard('box', {boundingbox: [-1.5, 1.5, 1.5, -1.5], axis:true});

var f = brd.create('functiongraph',[function(x){ 
	return Math.sin(x); 
}]);

var f = brd.create('functiongraph',[function(x){ 
	return x; 
}]);


</script>

