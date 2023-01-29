layout: definition
categories: branches,analysis
nodeid: bookofproofs$1746
orderid: 100
parentid: bookofproofs$346
title: Sine of a Real Variable
description: SINE FUNCTION OF A REAL VARIABLE ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$581
keywords: sine function,real sine,sine
contributors: bookofproofs

---


---

Let `$x\in\mathbb R$` be any [real number][bookofproofs$1105] and let `$z$` be [the complex number][bookofproofs$1698] obtained from `$x$` [by multiplying][bookofproofs$6437] it with the [imaginary unit][bookofproofs$1698], i.e. `$z:=ix$`. 

The **sine** of `$x$` is a [function][bookofproofs$592] `$f:\mathbb R\mapsto\mathbb R,$` which is defined as the [imaginary part][bookofproofs$1698] of the [complex exponential function][bookofproofs$312].
`$$\sin(x):=\Im(\exp(ix)).$$`

Geometrically, the sine is a projection of the complex number `$\exp(ix),$` which is on the [unit circle][bookofproofs$1749], to the imaginary axis. The behavior of the sine function can be studied in the following interactive figure (with a draggable value of `$x$`):

Sine Graph of `$x$`

<div id="boxRE20035" class="jxgbox centered" style="max-width:500px; height:500px;"></div>

Projection of `$\exp(ix)$` happening in the complex plane

<div id="box1746" class="jxgbox centered" style="max-width:500px; height:500px;"></div>

§§§1

---

§§§1

<script type="text/javascript">
var brd1 = JXG.JSXGraph.initBoard('boxRE20035', {boundingbox: [-10, 1.5, 10, -1.5], axis:true});
var brd = JXG.JSXGraph.initBoard('box1746', {boundingbox: [-1.5, 1.5, 1.5, -1.5], axis:true});

var xr = brd1.create('line',[[-9,0],[9,0]],{visible:false});
var x = brd1.create('glider',[-9,0,xr],{visible:true, name:'x'});
var y = brd1.create('point',[x.X(),Math.sin(x.X())],{size:1,name:'',strokeColor:'green'});

var x1 = brd1.create('segment',[x,y],{visible:true, straightFirst:false,straightLast:false,strokeColor:'red'});
 x.on('drag', function(){ transform(x);});
var f = brd1.create('functiongraph',[function(x){ 
	return Math.sin(x); 
}]);
var ax = brd.create('line',[[0,0],[1,0]],{visible:false});
var ay = brd.create('line',[[0,0],[0,1]],{visible:false});
var p0 = brd.create('point',[0,0],{fixed:true,visible:false});
var p1 = brd.create('point',[1,0],{name:'',visible:false,fixed:true});
var c = brd.create('circle',[p0,p1],{dash:2,strokeWidth:1,strokeOpacity:0.6});


var p2 = brd.create('point',[Math.cos(x.X()),Math.sin(x.X())],{name:'exp(ix)',fixed:true,size:1, strokeColor:'green'});
var p3 = brd.create('point',[0.0,function(){return p2.Y();}],{name:'sin(x)=Im(exp(ix))',fixed:true,size:1});
var p4 = brd.create('point',[function(){return p2.X();},0.0],{visible:false,name:'',withLabel:false});
 
brd.create('line',[p0,p3],{straightFirst:false,straightLast:false,strokeColor:'red'});     // sin
brd.create('segment',[p2,p3 ],{strokeColor:'blue',strokeWidth:1,dash:1});     // projection

brd1.create('text',[
        function(){return x.X()+0.3;},
        function(){return y.Y()*0.5;},
        'sin'],{});

function transform(x) {
 p2.setPosition(JXG.COORDS_BY_USER,[Math.cos(x.X()),Math.sin(x.X())]);
y.setPosition(JXG.COORDS_BY_USER,[x.X(),Math.sin(x.X())]);
brd.update();
}

</script>

