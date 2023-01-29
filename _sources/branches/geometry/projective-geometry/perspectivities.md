layout: definition
categories: branches,geometry,projective-geometry
nodeid: bookofproofs$7974
orderid: 500
parentid: bookofproofs$7967
title: Perspectivities
description: PERSPECTIVITIES &#9733; bring your math skills to the graduate level &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: 
keywords: perspectivities,perspectivity,projective axis,projective center
contributors: bookofproofs


---


---

In projective geometry, a **perspectivity** [$\overline{\overline\wedge}$" is a "composition][bookofproofs$1314] of two [projectivities][bookofproofs$7973]. A perspectivity establishes a [bijection][bookofproofs$771] (one-to-one-relationship) between two [ranges][bookofproofs$7973] of two distinct [straight lines][bookofproofs$645] `$p_1$` and `$p_2$` in relation to a [pencil][bookofproofs$7973] of a [point][bookofproofs$631] `$O,$` called the **projective center** of the projectivity. We write in this case
`$$p_1\overline{\overline\wedge}p_2.$$`

In its dual formulation, a perspectivity establishes a bijection between two [pencils][bookofproofs$7973] of two distinct [points][bookofproofs$631] `$P_1$` and `$P_2$` in relation to a [range][bookofproofs$7973] of a [straight line][bookofproofs$645] `$o,$` called the **projective axis**. We write in this case
`$$P_1\overline{\overline\wedge}P_2.$$`

### Example
 
The following interactive figure demonstrates a perspectivity of the ranges `$P_1P_2\overline{\overline\wedge}Q_1Q_2$` and the corresponding dual perspectivity of the pencils `$p_1\cdot p_2\overline{\overline\wedge}q_1\cdot q_2.$`


Perspectivity | Dual Definition 
:------------- |:-------------
<div id='box-E15176a' class='jxgbox centered' style='max-width:300px; height:300px;'></div>|<div id='box-E15176b' class='jxgbox centered' style='max-width:300px; height:300px;'></div>

§§§1

§§§2

---

§§§1

<script>
board = JXG.JSXGraph.initBoard('box-E15176a', {boundingbox: [-6, 6, 6, -6], axis:false, showCopyright:false});

var A1 = board.create('point', [0,0],{name:'O'});
var D2 = board.create('point', [-2,-1],{size:0, name:'p_1'}); 
var linep1 =board.create('line', [D2,A1], {attractors: [A1], attractorDistance:0.2, snatchDistance: 20});
var D4 = board.create('point', [-2,2],{size:0, name:'p_2'});
var linep2 =board.create('line', [D4,A1], {attractors: [A1], attractorDistance:0.2, snatchDistance: 20});
var P1 = board.create('point', [-4,-2],{attractors: [linep1], attractorDistance:0.2, snatchDistance: 20, name:'P_1'});
var P2 = board.create('point', [-4,4],{attractors: [linep2], attractorDistance:0.2, snatchDistance: 20,name:'P_2'});
var linep =board.create('line', [P1,P2]); 
var p = board.create('point', [-4,-4],{attractors: [linep], size:0, attractorDistance:0.2, snatchDistance: 20,name:'p'});

var Q1 = board.create('point', [-3,-1.5],{attractors: [linep1], attractorDistance:0.2, snatchDistance: 20, name:'Q_1'});
var Q2 = board.create('point', [-2.5,2.5],{attractors: [linep2], attractorDistance:0.2, snatchDistance: 20,name:'Q_2'});
var lineq =board.create('line', [Q1,Q2]); 

var q = board.create('point', [-3.5,-5],{attractors: [lineq], size:0, attractorDistance:0.2, snatchDistance: 20,name:'q'});
 
</script>


§§§2

<script>
board1 = JXG.JSXGraph.initBoard('box-E15176b', {boundingbox: [-6, 6, 6, -6], axis:false, showCopyright:false});

var Q = board1.create('point', [-2,-2],{name:'Q'});
var P = board1.create('point', [2,-2],{name:'P'});
var lineo =board1.create('line', [Q,P]); 
var O = board1.create('point', [4.5,-2],{attractors: [lineo], size:0, attractorDistance:0.2, snatchDistance: 20, name:'o'});

var P1 = board1.create('point', [-4,4],{name:'P_1'});
var P2 = board1.create('point', [4,4],{name:'P_2'}); 

var linep1 =board1.create('line', [P1,P]); 
var lineq1 =board1.create('line', [P1,Q]); 
var linep2 =board1.create('line', [P2,P]); 
var lineq2 =board1.create('line', [P2,Q]); 

var p1 = board1.create('point', [-2.05,2.05],{attractors: [linep1], size:0, attractorDistance:0.2, snatchDistance: 20, name:'p_1'});
var q1 = board1.create('point', [-3,1],{attractors: [lineq1], size:0, attractorDistance:0.2, snatchDistance: 20, name:'q_1'});
var q2 = board1.create('point', [2.05,2.05],{attractors: [lineq2], size:0, attractorDistance:0.2, snatchDistance: 20, name:'q_2'});
var p2 = board1.create('point', [3,1],{attractors: [linep2], size:0, attractorDistance:0.2, snatchDistance: 20, name:'p_2'}); 
 
</script> 

