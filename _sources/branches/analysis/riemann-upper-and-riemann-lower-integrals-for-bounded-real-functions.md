layout: proposition
categories: branches,analysis
nodeid: bookofproofs$1761
orderid: 200
parentid: bookofproofs$474
title: Riemann Upper and Riemann Lower Integrals for Bounded Real Functions
description: RIEMANN UPPER AND RIEMANN LOWER INTEGRALS FOR BOUNDED REAL FUNCTIONS ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$581
keywords: bounded,functions,integrals,lower,real,riemann,riemann lower integral,riemann upper integral,upper
contributors: bookofproofs

---


---

Let `\([a,b]\)` be a [closed real interval][bookofproofs$1153] and let `\(f:[a,b]\mapsto\mathbb R\)` be an arbitrary [bounded function][bookofproofs$302].
Then the following integrals exist and are well-defined:

### Riemann Upper Integral

The **Riemann upper integral** of `\(f\)` over the interval `\([a,b]\)` is the [infimum][bookofproofs$1755] of all possible [Riemann Integrals for step functions][bookofproofs$1752] `\(\phi\)` such that their values are bounded below by the respective values of `\(f\)`, formally:

`\[\int_{a}^{b~*}f(x)dx:=\inf\left\{\int_{a}^b\phi(x)dx:~~\phi(x)\ge f(x)\text{ for all }x\in[a,b]\text{ and }\phi\text{ is a step function over }[a,b]\right\}.\]`

### Riemann Lower Integral

The **Riemann lower integral** of `\(f\)` over the interval `\([a,b]\)` is the [supremum][bookofproofs$1754] of all possible [Riemann Integrals for step functions][bookofproofs$1752] `\(\phi\)` such that their values are bounded above by the respective values of `\(f\)`, formally:

`\[\int_{a~*}^bf(x)dx:=\sup\left\{\int_{a}^b\phi(x)dx:~~\phi(x)\le f(x)\text{ for all }x\in[a,b]\text{ and }\phi\text{ is a step function over }[a,b]\right\}.\]`


In the following interactive figure, an example bounded function on the closed interval `\([-3,3]\)` is generated. You can drag the red points to change the function. The slider to the right changes the step functions of the upper (red) and lower (green) Riemann integrals of the corresponding step functions. The infimum and supremum of the upper and lower integrals of step functions are reached, if the step length goes to zero (i.e. number of steps in the closed interval goes to infinity).

<div id="E20174box" class="jxgbox centered" style="max-width:500px; height:500px;"></div>
<div id="E20174box1" class="jxgbox centered" style="max-width:400px; height:100px;"></div>
<div style ='clear:both'></div> 
 
§§§1

---

§§§1

<script type="text/javascript">
var brd1 = JXG.JSXGraph.initBoard('E20174box1', {boundingbox: [0, 0, 12, -10], showNavigation:false, showCopyright: false, axis:false});
var n = brd1.create('slider',[[1,-5],[9,-5],[1,5,300]], {name:'steps', snapWidth:1});

var val=n.Value();

var brd = JXG.JSXGraph.initBoard('E20174box', {boundingbox:[-3,5,3,-3],axis:true,showCopyright: false});

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

brd.create('text',[-2.9,-2,function(){ return 'Integral of upper step function='+(JXG.Math.Numerics.riemannsum(f,val,'upper',-3,3)).toFixed(1); }]);

brd.create('text',[-2.9,-2.5,function(){ return 'Integral of lower step function='+(JXG.Math.Numerics.riemannsum(f,val,'lower',-3,3)).toFixed(1); }]);

n.on('drag',function(){ 
val=this.Value();
brd.update();});

</script>

