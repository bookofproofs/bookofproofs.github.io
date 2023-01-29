layout: definition
categories: branches,geometry,projective-geometry
nodeid: bookofproofs$7973
orderid: 400
parentid: bookofproofs$7967
title: Projectivities, Ranges and Pencils
description: PROJECTIVITIES, RANGES AND PENCILS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: 
keywords: pencil,pencils,projectivities,projectivity,range,ranges
contributors: bookofproofs

---


---

In projective geometry, a **projectivity** [$\overline\wedge$" is a "bijection][bookofproofs$771] (one-to-one-relationship) of [collinear points][bookofproofs$7968] on a [straight line][bookofproofs$645] `$o$` to [concurrent straight lines][bookofproofs$7970] passing through a [point][bookofproofs$631] `$O$` (and vice versa). It is required that `$o$` and `$O$` are not [incident][bookofproofs$7969] and that each of the collinear points lies on the concurrent line it has a bijection with.

If there is a projectivity of the point `$P$` to the straight line `$p$`, then we write `$P\overline\wedge p$` (or `$p\overline\wedge P$`).

The collinear points in a projectivity are called the **range**, the corresponding concurrent lines are called the **pencil** of the projectivity.

### Example

The following interactive figure demonstrates a projectivity of the range `$P_1,P_2$` to the pencil `$p_1,p_2$`, in other words, we have `$P_1\overline\wedge p_1$` and `$P_2\overline\wedge p_2.$`

<div id='box-E15135c' class='jxgbox centered' style='max-width:500px; height:500px;'></div>
§§§1

---

§§§1

<script>
board = JXG.JSXGraph.initBoard('box-E15135c', {boundingbox: [-6, 6, 3, -6], axis:false, showCopyright:false});

var A1 = board.create('point', [0,0],{name:'O'});
var D2 = board.create('point', [-2,-1],{size:0, name:'p_1'});
var linep1 =board.create('line', [D2,A1], {attractors: [A1], attractorDistance:0.2, snatchDistance: 20});
var D4 = board.create('point', [-2,2],{size:0, name:'p_2'});
var linep2 =board.create('line', [D4,A1], {attractors: [A1], attractorDistance:0.2, snatchDistance: 20});
var P1 = board.create('point', [-4,-2],{attractors: [linep1], attractorDistance:0.2, snatchDistance: 20, name:'P_1'});
var P2 = board.create('point', [-4,4],{attractors: [linep2], attractorDistance:0.2, snatchDistance: 20,name:'P_2'});
var linep =board.create('line', [P1,P2]); 
var o = board.create('point', [-4,-4],{attractors: [linep], size:0, attractorDistance:0.2, snatchDistance: 20,name:'o'});
</script>

