layout: proposition
categories: branches,analysis
nodeid: bookofproofs$1752
orderid: 50
parentid: bookofproofs$474
title: Riemann Integral for Step Functions
description: RIEMANN INTEGRAL FOR STEP FUNCTIONS ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$581
keywords: functions,integral,riemann,riemann integral of the step function
contributors: bookofproofs

---


---

Let `\(\phi\in T[a,b]\)` be a [step function][bookofproofs$6796] with respect to the partition `\(a=x_0 < x_1 < \ldots < x_{n-1} < x_n=b\)`, i.e. let `\(\phi\)` take some constant values `\(c_i\)` on the open intervals `\((x_{i-1},x_i)\)`  `\[\phi (x)=c_i\quad\quad\text{for all } x\in(x_{i-1},x_i),\quad i=1,\ldots,n.\]`
The **Riemann integral of the step function** is defined as the [sum][bookofproofs$261].
`\[\int_a^b\phi(x)dx:=\sum_{i=1}^nc_i(x_i-x_{i-1}).\]`

The Riemann integral of the step function is well-defined, i.e. its definition does not depend on the specific choice of the partition `\(a=x_0 < x_1 < \ldots < x_{n-1} < x_n=b\)`.


The Riemann integral can be interpreted as the area between the `\(x\)`-axis and the step function. The area is counted positive, if it is above the `\(x\)`-axis (green) and negative if it is below the `\(x\)`-axis (red):

<div id="E20165box" class="jxgbox centered" style="max-width:500px; height:500px;"></div>
<div id="E20165box1" class="jxgbox centered" style="max-width:400px; height:100px;"></div>

<div style ='clear:both'></div> 
 
§§§1

---

§§§1

<script type="text/javascript">
var brd1 = JXG.JSXGraph.initBoard('E20165box1', {boundingbox: [0, 0, 12, -10], showNavigation:false, showCopyright: false, axis:false});
var a0 = brd1.create('slider',[[1,-5],[9,-5],[0,5,10]], {name:'random step height', value:3, snapWidth:1});

var brd = JXG.JSXGraph.initBoard('E20165box', {boundingbox: [-10, 20, 10, -20], axis:true});

var xw=new Array();
var yw=new Array();

    

var allBoardObjects=new Array();

function update(v) {
  xw=[];yw=[];
  xw[^0]=-9;
  yw[^0]=Math.random()*v;
  do {
    var newX=xw[xw.length-1]+Math.random()*4;
    if (gt(newX,9)) newX=9;
    xw.push(newX);
    var sign;
    if (gt(Math.random(),0.5)) {
      sign=1;
    } else {
      sign=-1;
    }
    var y=sign*Math.random()*v;
    if (gt(y,v) && gt(v,0)) y=v;
    if (lt(y,v) && lt(v,0)) y=v;
    yw.push(y);
  } while (lt(newX,9));
  // remove all objects from board
  while (allBoardObjects.length > 0) { brd.removeObject(allBoardObjects.pop()); }
  for (i=1; lt(i,xw.length); i++) {
    var rectangle=new Array();
    var point=brd.create('point', [xw[i-1],0], {visible:false,fixed:true}); allBoardObjects.push(point); rectangle.push(point);
    point=brd.create('point', [xw[i-1],yw[i-1]], {visible:false,fixed:true}); allBoardObjects.push(point); rectangle.push(point);
    point=brd.create('point', [xw[i],yw[i-1]], {visible:false,fixed:true}); allBoardObjects.push(point); rectangle.push(point);
    point=brd.create('point', [xw[i],0], {visible:false,fixed:true}); allBoardObjects.push(point); rectangle.push(point);
    var rect;
    if (lt(yw[i-1],0)) {
       rect = brd.create('polygon',[rectangle[^0],rectangle[^1],rectangle[^2],rectangle[^3]],{hasInnerPoints:true, fillColor:'#ff0000', fillOpacity:0.3});
    } else {
       rect = brd.create('polygon',[rectangle[^0],rectangle[^1],rectangle[^2],rectangle[^3]],{hasInnerPoints:true});
    }
    
    allBoardObjects.push(rect);
  }
}

a0.on('drag',function(){ 
update(a0.Value());
brd.update();});

update(a0.Value());
</script>

