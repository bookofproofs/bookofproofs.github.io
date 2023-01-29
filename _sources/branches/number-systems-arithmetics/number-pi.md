layout: definition
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$6738
orderid: 200
parentid: bookofproofs$373
title: Number `$\pi$`
description: NUMBER PI ★ bring your math skills to the graduate level ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$581
keywords: pi,number pi
contributors: bookofproofs

---


---

The number `$\pi$` (read **pi**) is defined as twice the the [uniquely defined zero of the cosine function][bookofproofs$6737] in the closed interval `$[0,2].$`

`$$\cos\left(\frac\pi2\right)=0\quad\Longleftrightarrow\quad\frac\pi2=1.570796326\pm 10^{-9}\quad\Longleftrightarrow\quad\pi\approx 3.141592653\pm 10^{-9}.$$`

<div id="box-6738" class="jxgbox centered"  style="max-width:500; width:500px; height:500px;"></div>
<div style ='clear:both'></div> 
 
§§§1

---

§§§1

<script type="text/javascript">


var brd = JXG.JSXGraph.initBoard('box-6738', {boundingbox: [0, 1, 2.1, -1], axis:true});


var p = brd.create('point',[Math.PI/2,0], {name:'π/2',size:1});

var f = brd.create('functiongraph',[function(x){ 
	return Math.cos(x); 
}]);

</script>

