layout: lemma
categories: branches,analysis
nodeid: bookofproofs$6619
orderid: 100
parentid: bookofproofs$6611
title: Approximability of Continuous Real Functions On Closed Intervals By Step Functions
description: APPROXIMABILITY OF CONTINUOUS REAL FUNCTIONS ON CLOSED INTERVALS BY STEP FUNCTIONS &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$581
keywords: approximability,closed,continuous,functions,intervals,real,step
contributors: bookofproofs

---


---

Let `$[a,b]$` be a [closed real interval][bookofproofs$1153], `$\mathbb R$` be the [set of real numbers][bookofproofs$1105] and `\(f:[a,b]\mapsto \mathbb R\)` a [continuous function][bookofproofs$219]. Then for every `\(\epsilon > 0\)` there exist some [step functions][bookofproofs$1751] `\(\phi:[a,b]\mapsto\mathbb R\)` and `\(\psi:[a,b]\mapsto\mathbb R\)` with

> `$(i)$` `$\phi(x) \le f(x)\le \psi(x)$` for all `$x\in[a,b],$` and

> `$(ii)$` `$|\phi(x)-\psi(x)|\le\epsilon$` for all `$x\in[a,b].$`

### Example

The following interactive figure demonstrates the idea of this lemma for the close interval `$[-3,3]$`, some continuous function `$f$` and the step function `\(\phi\)` green and `\(\psi\)` red.  You can drag the red points to change the curvature of the function and use the slider to change the number of steps of the step functions.

<div style ='float:left'>
	<div id="box" class="jxgbox" style="width:500px; height:500px;"></div>
</div>
<div>
	<div id="box1" class="jxgbox" style="width:400px; height:100px;"></div>
</div>
<div style ='clear:both'></div> 
 
§§§1

---

§§§1

<script type="text/javascript">
var brd1 = JXG.JSXGraph.initBoard('box1', {boundingbox: [0, 0, 12, -10], showNavigation:false, showCopyright: false, axis:false});
var n = brd1.create('slider',[[1,-5],[9,-5],[1,5,300]], {name:'steps', snapWidth:1});

var val=n.Value();

var brd = JXG.JSXGraph.initBoard('box', {boundingbox:[-3,5,3,-3],axis:true,showCopyright: false});

var p = [];
p.push(brd.create('point',[-2.7,2.95]));
p.push(brd.create('point',[-1,3.57]));
p.push(brd.create('point',[0,3.62]));
p.push(brd.create('point',[1,3.59]));
p.push(brd.create('point',[2.7,2.21]));
 
var f = JXG.Math.Numerics.lagrangePolynomial(p);

var plot = brd.create('functiongraph',[f,-3,3]);
 
var up = brd.create('riemannsum',[f,function(){ return val;}, 'upper',-3,3],{fillColor:'#ff0000', fillOpacity:0.3});
var lo = brd.create('riemannsum',[f,function(){ return val;}, 'lower',-3,3],{fillColor:'#00ff00', fillOpacity:0.3});


n.on('drag',function(){ 
val=this.Value();
brd.update();});

</script>

