layout: chapter
categories: branches,geometry,projective-geometry
nodeid: bookofproofs$7972
orderid: 100
parentid: bookofproofs$110
title: An Introduction to the Principle of Duality in Projective Geometry
description: AN INTRODUCTION TO THE PRINCIPLE OF DUALITY IN PROJECTIVE GEOMETRY &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: 
keywords: duality,geometry,introduction,principle,principle of duality,projective,duality (projective geometry),duality projective geometry,projective duality,projective geometry duality,duality geometry,duality in geometry
contributors: bookofproofs


---


---

The determination of a point by two [concurrent straight lines][bookofproofs$7970] is a kind of symmetric with the determination of a straight line by two [collinear points][bookofproofs$7968]. In projective geometry, we shall find this symmetry very often and are going to establish a principle, called the **principle of duality**. In fact, later on we will establish (and prove) two kinds of principles of duality - a two-dimensional (planar) principle of duality, and a three-dimensional principle of duality. These principles mean the following:

* In the __planar principle of duality__ every theorem remains true and every definition keeps making sense, if we exchange the words "straight line" and "point". Possibly, also other exchanges can be necessary, e.g. replacing the words "collinear" by "concurrent", "meets" by "joins", etc.
* Similarly, in the __three-dimensional principle of duality__  every theorem remains true and every definition keeps making sense, if we exchange the words "planes", "straight lines" and "points" by "points", "straight lines" and "planes", respectively.

The principles of duality and their symmetry provide projective geometry with a beauty of its own. They also make the theory very effective - for instance, proving `$10$` theorems in projective geometry means, in fact, proving `$20$` theorems - including the dual ones.  Despite of this effectiveness, for the rest of the text to follow, we will always provide both theorems / proofs / definitions, etc. at once, whenever it is possible to "dualize" them. For this purpose, we will find it convenient to write them in two columns. For instance, the definitions of collinear points and concurrent straight lines could have already been written at once in two columns as follows:


Definition: Collinear Points | Dual Definition: Concurrent Straight Lines
:------------- |:-------------
 Different points which are incident to a straight line are said to be collinear.| Different straight lines which are incident to a point are said to be concurrent.
<div id='box-E15135' class='jxgbox centered' style='max-width:300px; height:250px;'></div>|<div id='box-E15135b' class='jxgbox centered' style='max-width:300px; height:250px;'></div>


§§§1

§§§2

---

§§§1

<script>
board = JXG.JSXGraph.initBoard('box-E15135b', {boundingbox: [-6, 6, 6, -6], axis: false, showCopyright:false});

var A1 = board.create('point', [0,0],{name:'K'});
var D1 = board.create('point', [2,0],{size:0, name:'a'});
var lineD1 =board.create('line', [D1,A1], {attractors: [A1], attractorDistance:0.2, snatchDistance: 20});
var D2 = board.create('point', [2,1],{size:0, name:'b'});
var lineD2 =board.create('line', [D2,A1], {attractors: [A1], attractorDistance:0.2, snatchDistance: 20});
var D3 = board.create('point', [-2,1],{size:0, name:'c'});
var lineD3 =board.create('line', [D3,A1], {attractors: [A1], attractorDistance:0.2, snatchDistance: 20});
var D4 = board.create('point', [-2,2],{size:0, name:'d'});
var lineD4 =board.create('line', [D4,A1], {attractors: [A1], attractorDistance:0.2, snatchDistance: 20});
</script>


§§§2

<script>
board = JXG.JSXGraph.initBoard('box-E15135', {boundingbox: [-6, 6, 6, -6], axis: false, showCopyright:false});

var A1 = board.create('point', [5,0],{name:'k', size:0});
var D1 = board.create('point', [-1,0],{visible:false});
var line =board.create('line', [D1,A1],{name:'l'});

var A = board.create('point', [1,0], {name:'A', attractors: [line], attractorDistance:0.2, snatchDistance: 20});
var B = board.create('point', [0.5,0], {name:'B', attractors: [line], attractorDistance:0.2, snatchDistance: 20});
var C = board.create('point', [-1.5,0], {name:'C', attractors: [line], attractorDistance:0.2, snatchDistance: 20});
var D = board.create('point', [-2.5,0], {name:'D', attractors: [line], attractorDistance:0.2, snatchDistance: 20});
</script>

