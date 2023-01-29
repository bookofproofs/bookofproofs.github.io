layout: proposition
categories: branches,theoretical-physics, special-relativity
nodeid: bookofproofs$6275
orderid: 600
parentid: bookofproofs$642
title: Construction of a Light Clock
description: CONSTRUCTION OF A LIGHT CLOCK &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$6267
keywords: clock,construction,light
contributors: bookofproofs

---


---

In any [inertial reference frame][bookofproofs$6295] `\(\mathcal I\)`, it is (theoretically) possible to construct a **light clock** by placing two mirrors in a vacuum at a fixed distance `\(d\)` and letting a light particle "bounce" between them. The "tick duration" of such a light clock is then given by the formula

`\[\operatorname{tick duration}:=\frac dc\]`

where `\(s\)` denotes the time unit of one [second][bookofproofs$6273], and where `\(c\)` denotes the (constant) speed of light in a vacuum:

`\[c=299.792.458 \frac{\operatorname{m}}{\operatorname{s}}\]`


The following figure demonstrates a model of a light clock:

<div style ='float:left'>
	<div id="box" class="jxgbox" style="width:500px; height:500px;"></div>
</div>

<div style ='clear:both'></div> 
 
§§§1

### Examples


In particular, if `\(d=1m\)`, the tick duration of this clock in `\(\mathcal I\)` is

`\[\frac dc=\frac {1m}c=\frac {1m}{299\,792\,458\frac ms}=\frac {1}{299\,792\,458}s.\]`

For `\(d=299\,792.458\,m\)` the tick duration would be 

`\[\frac dc\approx\frac {299.8\,km}c=\frac {1}{1000}s=1\,ns.\]`

---

§§§1

<script type="text/javascript">
var brd = JXG.JSXGraph.initBoard('box', {boundingbox: [0, 1.1, 10, -.1], showCopyright:false});
var pArr=[];

pArr[^0] = brd.create('point', [4,function(){return 0;}], {visible:false, snapToGrid:true, snapSizeY:1});
pArr[^1] = brd.create('point', [6,0], {visible:false, snapToGrid:true, snapSizeY:1});
pArr[^2] = brd.create('point', [4,1], {visible:false, snapToGrid:true, snapSizeY:1});
pArr[^3] = brd.create('point', [6,1], {visible:false, snapToGrid:true, snapSizeY:1});


var xr1 = brd.create('segment',[pArr[^0],pArr[^1]],{visible:true});
xr1.setLabel("mirror 1");
xr1.setLabelRelativeCoords([0,1]);
var xr2 = brd.create('segment',[pArr[^2],pArr[^3]],{visible:true});
xr2.setLabel("mirror 2");

var gr = brd.create('group',pArr);


var p = brd.create('point', [5, 0.5], {name:''});

var richtung=1;

setInterval(function(){
   var x=pArr[^0].X()+(pArr[^1].X()-pArr[^0].X())/2;
   var y=p.Y();

	if (richtung==1) {
		y=y+0.01;
		if (y > pArr[^2].Y()) {
			richtung = 1 - richtung;
		}
   } else {
       y=y-0.01;
		if (y < pArr[^0].Y()) {
			richtung = 1 - richtung;
		}
   }
   p.moveTo([x,y])
},1);




</script>

