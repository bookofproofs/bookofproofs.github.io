layout: definition
categories: branches,geometry,projective-geometry
nodeid: bookofproofs$7970
orderid: 200
parentid: bookofproofs$7967
title: Concurrent Straight Lines
description: CONCURRENT STRAIGHT LINES &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: 
keywords: concurrent,lines,straight
contributors: bookofproofs

---


---

Different [straight lines][bookofproofs$645] which [passes through][bookofproofs$7969] the same [point][bookofproofs$631] are said to be **concurrent**. We also say that concurrent straight lines `$l_1,l_2,\ldots$` **meet at** the point `$A$` and write `$$P=l_1\cdot l_2\cdot\ldots.$$` 

We agree that the order of the lines in this dot "`$\cdot$`" notation does not play any role, e.g. `$m\cdot l$` and `$l\cdot m$` for two straight lines `$m$` and `$l$` denote the same point. 
Please note the difference of notation of concurrent lines and [collinear points][bookofproofs$7968], where we do not use the dot "`$\cdot$`".

### Example

The following figure shows an example of four coincident straight lines passing a point `$A=k\cdot l\cdot m\cdot n.$`

<div id='box-E15135b' class='jxgbox centered' style='max-width:500px; height:500px;'></div>
§§§1

---

§§§1

<script>
board = JXG.JSXGraph.initBoard('box-E15135b', {boundingbox: [-6, 6, 6, -6], axis: false, showCopyright:false});

var A1 = board.create('point', [0,0],{name:'A'});
var D1 = board.create('point', [2,0],{size:0, name:'l'});
var lineD1 =board.create('line', [D1,A1], {attractors: [A1], attractorDistance:0.2, snatchDistance: 20});
var D2 = board.create('point', [2,1],{size:0, name:'k'});
var lineD2 =board.create('line', [D2,A1], {attractors: [A1], attractorDistance:0.2, snatchDistance: 20});
var D3 = board.create('point', [-2,1],{size:0, name:'m'});
var lineD3 =board.create('line', [D3,A1], {attractors: [A1], attractorDistance:0.2, snatchDistance: 20});
var D4 = board.create('point', [-2,2],{size:0, name:'n'});
var lineD4 =board.create('line', [D4,A1], {attractors: [A1], attractorDistance:0.2, snatchDistance: 20});
</script>

