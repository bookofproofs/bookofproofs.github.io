layout: definition
categories: branches,analysis
nodeid: bookofproofs$8551
orderid: 50
parentid: bookofproofs$130
title: Open and Closed Discs
description: OPEN AND CLOSED DISCS ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$6735,bookofproofs$8548
keywords: open disc,closed disc,open discs,closed discs,disc,discs
contributors: bookofproofs

---


---

Let `$z\in\mathbb C$` be a [complex number][bookofproofs$216] and let `$r > 0$` be a [positive real number][bookofproofs$1107]. The [subset][bookofproofs$552] `$D\subset\mathbb C$` of the [complex plane][bookofproofs$216] is called:

* **open disc**, if `$D:=\{\alpha\in\mathbb C\mid |z-\alpha| < r\},$` i.e. if `$D$` constitutes  [open ball][bookofproofs$849] in the complex plane. 
* **closed disc**, if `$D:=\{\alpha\in\mathbb C\mid |z-\alpha| \le r\}.$`

Above, `$|\cdot|$` denotes the [absolute value of complex numbers][bookofproofs$583].
### Example



<div id='box-E21660' class='jxgbox centered' style='max-width:500px; height:500px;'></div>
§§§1

---

§§§1

<script>
board = JXG.JSXGraph.initBoard('box-E21660', {boundingbox: [-2, 6, 6, -2], axis: true});

var p1 = board.createElement('point',[2,2], {name:'z',size: 4, face: 'o'});
var p2 = board.createElement('point',[3,1], {name:'a',size: 4, face: 'o', visible:true, label:{visible:false}});
var l = board.create('line',[p1,p2], 
 {straightFirst:false, straightLast:false, strokeWidth:2, dash:2, label:'r'});
var ci = board.createElement('circle',["z","a"],{fillColor:'#ffff00', fillOpacity:0.3});
</script>

