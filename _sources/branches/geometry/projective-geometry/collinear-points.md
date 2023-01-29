layout: definition
categories: branches,geometry,projective-geometry
nodeid: bookofproofs$7968
orderid: 100
parentid: bookofproofs$7967
title: Collinear Points
description: COLLINEAR POINTS &#9733; bring your math skills to the graduate level &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: 
keywords: collinear,collinearity,points,collinear points,collinear points definition,collinear definition geometry
contributors: bookofproofs

---


---

The concept of **collinearity** is the same in projective geometry as [already defined for the Euclidean geometry][bookofproofs$649]. Here, we recall this definition and reformulate it for the purposes of the projective geometry[^1]:

Different [points][bookofproofs$631] which are [incident][bookofproofs$7969] to a [straight line][bookofproofs$645] are said to be **collinear**. We also say that a line `$l$` **joins** the points `$A_1,A_2,\ldots$` and write `$$l=A_1A_2\ldots.$$` 

We agree that the order of points in this notation does not play any role, e.g. `$AB$` and `$BA$` for two points `$A$` and `$B$` denote the same line. 

### Example 

The following figure shows an example of four collinear points on a straight line `$l=ABCD.$`

<div id='box-E15135' class='jxgbox centered' style='max-width:500px; height:500px;'></div>
§§§1

[^1]: getting rid of collinear segments and rays, which are not terms of projective geometry

---

§§§1

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

