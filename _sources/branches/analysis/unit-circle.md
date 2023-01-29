layout: lemma
categories: branches,analysis
nodeid: bookofproofs$1749
orderid: 100
parentid: bookofproofs$201
title: Unit Circle
description: UNIT CIRCLE ★ bring your math skills to the graduate level ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$581
keywords: unit circle,unit circles
contributors: bookofproofs

---


---

Let `\(x\in\mathbb R\)` be any [real number][bookofproofs$1105] and let `\(z\)` be the [complex number][bookofproofs$1698], for which `\(x\)` is the [imaginary part][bookofproofs$1698], i.e. `\(x=\Im(z)\Longleftrightarrow z:=ix\)`. 

The [distance][bookofproofs$1247] of the [complex exponential function][bookofproofs$312] from the point of origin is equal `\(1\)`, formally


`\[|\exp(ix)|=1\quad\quad\text{for all }x\in\mathbb R.\]`

Geometrically, the complex numbers `\(\exp(ix)\)` form a figure called the **unit circle**:


<div id="boxE22025" class="jxgbox centered" style="max-width:500px; height:500px"></div>
<div id="boxE22025R" class="jxgbox centered" style="max-width:500px; height:100px;"></div>

### Fun questions
* For which values of `\(x\)` does `\(\exp(ix)\)` reach the complex number `\(i\)`?
* For which values of `\(x\)` does `\(\exp(ix)\)` reach the complex number `\(1\)`?

§§§1

---

§§§1

<script type="text/javascript">
var brd1 = JXG.JSXGraph.initBoard('boxE22025R', {boundingbox: [-10, 1.5, 10, -1.5], axis:true});
var brd = JXG.JSXGraph.initBoard('boxE22025', {boundingbox: [-1.5, 1.5, 1.5, -1.5], axis:true});

var xr = brd1.create('line',[[-9,0],[9,0]],{visible:false});
var x = brd1.create('glider',[-9,0,xr],{visible:true, name:'x'});


 x.on('drag', function(){ transform(x);});
var ax = brd.create('line',[[0,0],[1,0]],{visible:false});
var ay = brd.create('line',[[0,0],[0,1]],{visible:false});
 
var p0 = brd.create('point',[0,0],{fixed:true,visible:false});
var p1 = brd.create('point',[1,0],{name:'',visible:false,fixed:true});
var c = brd.create('circle',[p0,p1],{dash:2,strokeWidth:1,strokeOpacity:0.6});


var p2 = brd.create('point',[Math.cos(x.X()),Math.sin(x.X())],{name:'exp(ix)',fixed:true,size:1, strokeColor:'green'});

var p3 = brd.create('point',[function(){return p2.X();},0.0],{visible:false,name:'',withLabel:false});

 



function transform(x) {
 p2.setPosition(JXG.COORDS_BY_USER,[Math.cos(x.X()),Math.sin(x.X())]);

brd.update();
}


</script>

