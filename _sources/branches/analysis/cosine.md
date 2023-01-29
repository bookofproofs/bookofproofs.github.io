layout: definition
categories: branches,analysis
nodeid: bookofproofs$1745
orderid: 50
parentid: bookofproofs$346
title: Cosine of a Real Variable
description: COSINE OF A REAL VARIABLE ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$581
keywords: cosine,real cosine,cosine function
contributors: bookofproofs

---


---

Let `\(x\in\mathbb R\)` be any [real number][bookofproofs$1105] and let `\(z\)` be [the complex number][bookofproofs$1698] obtained from `\(x\)` by multiplying it with the [imaginary unit][bookofproofs$1698], i.e. `\(z:=ix\)`. 

The **cosine** of `\(x\)` is a [function][bookofproofs$592] `\(f:\mathbb R\mapsto\mathbb R\)`, which is defined as the [real part][bookofproofs$1248] of the [complex exponential function][bookofproofs$312].
`\[\cos(x):=\Re(\exp(ix)).\]`

Geometrically, the cosine is a projection of the complex number `\(\exp(ix)\)`, which is on the [unit circle][bookofproofs$1749], to the real axis. The behavior of the cosine function can be studied in the following interactive figure (with a draggable value of `\(x\)`):

Cosine graph of `$\cos(x)$`

<div id="boxR1745" class="jxgbox centered" style="max-width:500px; height:500px;"></div>

Projection of `$\exp(ix)$` happening in the complex plane

<div id="boxE20041" class="jxgbox centered" style="max-width:500px; height:500px;"></div>
§§§1

---

§§§1

<script type="text/javascript">
var brd1 = JXG.JSXGraph.initBoard('boxR1745', {boundingbox: [-10, 1.5, 10, -1.5], axis:true});
var brd = JXG.JSXGraph.initBoard('boxE20041', {boundingbox: [-1.5, 1.5, 1.5, -1.5], axis:true});

var xr = brd1.create('line',[[-9,0],[9,0]],{visible:false});
var x = brd1.create('glider',[-9,0,xr],{visible:true, name:'x'});
var y = brd1.create('point',[x.X(),Math.cos(x.X())],{size:1,name:'',strokeColor:'green'});

var x1 = brd1.create('segment',[x,y],{visible:true, straightFirst:false,straightLast:false,strokeColor:'red'});
 x.on('drag', function(){ transform(x);});
var f = brd1.create('functiongraph',[function(x){ 
	return Math.cos(x); 
}]);
var ax = brd.create('line',[[0,0],[1,0]],{visible:false});
var ay = brd.create('line',[[0,0],[0,1]],{visible:false});
 
var p0 = brd.create('point',[0,0],{fixed:true,visible:false});
var p1 = brd.create('point',[1,0],{name:'',visible:false,fixed:true});
var c = brd.create('circle',[p0,p1],{dash:2,strokeWidth:1,strokeOpacity:0.6});


var p2 = brd.create('point',[Math.cos(x.X()),Math.sin(x.X())],{name:'exp(ix)',fixed:true,size:1, strokeColor:'green'});

var p3 = brd.create('point',[function(){return p2.X();},0.0],{name:'cos(x)=Re(exp(ix))',fixed:true,size:1});
var p4 = brd.create('point',[0.0,function(){return p2.Y();}],{visible:false,name:'',withLabel:false});
 
brd.create('line',[p3,p0 ],{straightFirst:false,straightLast:false,strokeColor:'red'});     // cos
brd.create('segment',[p2,p3 ],{strokeColor:'blue',strokeWidth:1,dash:1});     // projection

brd1.create('text',[
        function(){return x.X()+0.3;},
        function(){return y.Y()*0.5;},
        'cos'],{});

function transform(x) {
 p2.setPosition(JXG.COORDS_BY_USER,[Math.cos(x.X()),Math.sin(x.X())]);
y.setPosition(JXG.COORDS_BY_USER,[x.X(),Math.cos(x.X())]);
brd.update();
}


</script>

