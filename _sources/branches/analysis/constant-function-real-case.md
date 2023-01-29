layout: definition
categories: branches,analysis
nodeid: bookofproofs$1371
orderid: 50
parentid: bookofproofs$166
title: Constant Function Real Case
description: CONSTANT FUNCTION REAL CASE &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$581
keywords: case,constant,constant function,function,real
contributors: bookofproofs

---


---

Let `\(a\)` be [real number][bookofproofs$1105] and  A **constant function** is a [function][bookofproofs$592] defined by 

`\[f(x):=c\]`

for all `\(x\in\mathbb R\)`. 

In the following interactive figure, you can drag the slider to manipulate the value of the constant `\(c\)` and see the behavior of resulting constant function. The initial value is (when the Reset button is pressed) is `\(c=0\)`.


	<div id="box15723" class="jxgbox centered" style="max-width:500px; height:500px;"></div>

	<div id="box15724" class="jxgbox centered" style="max-width:500px; height:100px;"></div>

 
§§§1

---

§§§1

<script type="text/javascript">
var brd1 = JXG.JSXGraph.initBoard('box15724', {boundingbox: [2, 0, 20, -8], showNavigation:false, showCopyright: false, axis:false});
var a = brd1.create('slider',[[3,-3],[15,-3],[-19,0,19]], {name:'c'});
var button1 = brd1.create('button', [3, -5, 'Reset', function() {
	a.moveTo([9,-3]);
	brd.update();
}], {});

var brd = JXG.JSXGraph.initBoard('box15723', {boundingbox: [-10, 20, 10, -20], axis:true});

var f = brd.create('functiongraph',[function(x){ 
  return a.Value(); 
}]);
    

a.on('drag',function(){ brd.update();});
</script>

