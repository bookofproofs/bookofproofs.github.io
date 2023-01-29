layout: definition
categories: branches,analysis
nodeid: bookofproofs$1377
orderid: 600
parentid: bookofproofs$166
title: Linear Function
description: LINEAR FUNCTION ★ bring your math skills to the graduate level ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: 
keywords: linear function
contributors: bookofproofs

---


---

A **linear function** is a [polynomial][bookofproofs$199] of degree `\(1\)` or `\(0\)`, i.e. a function `\(f:\mathbb R\to\mathbb R\)` of the form 
`\[f(x):=a_1x+a_0,\quad\quad a_0,a_1\in\mathbb R.\]`

In the following interactive figure, you can drag the sliders to manipulate the values of the coefficients `\(a_0,a_1\)` and see the behavior of resulting linear function. The initial values are(when the Reset button is pressed) are set to `\(0\)`. 


<div id="boxE20838" class="centered jxgbox" style="max-width:500px; height:500px;"></div>
<div id="boxE208381" class="centered jxgbox" style="max-width:400px; height:100px;"></div>

§§§1

---

§§§1

<script type="text/javascript">
var brd1 = JXG.JSXGraph.initBoard('boxE208381', {boundingbox: [2, 0, 20, -20], showNavigation:false, showCopyright: false, axis:false});
var a1 = brd1.create('slider',[[3,-5],[15,-5],[-10,0,10]], {name:'a_1'});
var a0 = brd1.create('slider',[[3,-9],[15,-9],[-19,0,19]], {name:'a_0'});
var button1 = brd1.create('button', [3, -15, 'Reset', function() {
	a1.moveTo([9,-5]);
	a0.moveTo([9,-9]);
	brd.update();
}], {});

var brd = JXG.JSXGraph.initBoard('boxE20838', {boundingbox: [-10, 20, 10, -20], axis:true});

var f = brd.create('functiongraph',[function(x){ 
	return a1.Value()*x + a0.Value(); 
}]);
    
a1.on('drag',function(){ brd.update();});
a0.on('drag',function(){ brd.update();});
</script>

