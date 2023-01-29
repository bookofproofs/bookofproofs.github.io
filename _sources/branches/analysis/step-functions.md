layout: definition
categories: branches,analysis
nodeid: bookofproofs$1751
orderid: 400
parentid: bookofproofs$166
title: Step Functions
description: STEP FUNCTIONS ★ bring your math skills to the graduate level ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: 
keywords: step function,step functions
contributors: bookofproofs

---


---

Let `\([a,b]\)` be a [closed real interval][bookofproofs$1153]. A [function][bookofproofs$592] `\(f:[a,b]\mapsto\mathbb R\)` is called a **step function over the interval** `\([a,b]\)` (or a **staircase function over this interval**), if there exist [real numbers][bookofproofs$1105] `\(x_i\)` such that

`\[a=x_0 < x_1 < \ldots < x_{n-1} < x_n=b\]`

and on any open interval `\((x_{i-1},x_{i})\)`, `\(i=1,\ldots,n\)`, the function `\(f\)` is [constant][bookofproofs$1371]. The numbers `\(x_0,\ldots,x_n\)` are called a **partition** of the real interval `\([a,b]\)`.


In the following figure, you can generate different partitions and different step functions for the interval `\([-9,9]\)`:

<div id="E20179box" class="jxgbox centered" style="max-width:500px; height:500px;"></div>
<div id="E20179box1" class="jxgbox centered" style="max-width:400px; height:100px;"></div>
<div style ='clear:both'></div> 
 
§§§1

---

§§§1

<script type="text/javascript">
var brd1 = JXG.JSXGraph.initBoard('E20179box1', {boundingbox: [0, 0, 12, -10], showNavigation:false, showCopyright: false, axis:false});
var a0 = brd1.create('slider',[[1,-5],[9,-5],[0,0,10]], {name:'random step height', value:3, snapWidth:1});

var brd = JXG.JSXGraph.initBoard('E20179box', {boundingbox: [-10, 20, 10, -20], axis:true});

var xw=new Array();
var yw=new Array();


var f = brd.create('functiongraph',[function(x){ 
if (lt(x,-9)) return 0;
else if (gt(x,9)) return 0; 
else 
for (var i=1; lt(i,10); i++) {
if (lt(x,xw[i-1])) return yw[i-1];
}
  return yw[i];
}]);
    
function update(v) {
xw=[];yw=[];
xw[^0]=-9;
yw[^0]=Math.random()*10-5;
for (var i=1; lt(i,11); i++) {
 xw.push(xw[xw.length-1]+Math.random()*4);
 yw.push(yw[yw.length-1]+Math.random()*v-v/2);
}
}

a0.on('drag',function(){ 
update(a0.Value());
brd.update();});

update(a0.Value());
</script>

