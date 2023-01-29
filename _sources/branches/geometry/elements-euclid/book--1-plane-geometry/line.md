layout: definition
categories: branches,geometry,euclidean-geometry,elements-euclid,book--1-plane-geometry
nodeid: bookofproofs$636
orderid: 100
parentid: bookofproofs$685
title: 1.02: Line, Curve
description: 1.02: LINE, CURVE &#9733; bring your math skills to the graduate level &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$626,bookofproofs$628,bookofproofs$6419
keywords: curve,curved line,line
contributors: bookofproofs,@calahan,@casey,@fitzpatrick

---


---



> And a **line** is a length without breadth.

### Modern Definition

A **curve** (or a **curved line**) `\(g\)` is a connected [subset][bookofproofs$552] of a [Euclidean metric space][bookofproofs$1206] `\(A\in\mathbb R^n\)` such that taking away a [point][bookofproofs$631] `\(A\in g\)` disconnects `\(g\)`.


Example of two curves in a plane:

<div id="boxE16484" class="jxgbox centered"  style="max-width:100%; width:500px; height:500px;"></div>
<div style ='clear:both'></div> 

§§§1

---

§§§1

<script type="text/javascript">
 var b = JXG.JSXGraph.initBoard('boxE16484', {boundingbox: [-5, 5, 5, -5]});
 var li3 = b.create('line',[[-1,1],[2,-1]], {straightFirst:false, straightLast:false, strokeWidth:2});
var graph = b.create('curve',
                       [function(t){ return t-Math.sin(t)-3;},
                        function(t){ return -1+Math.cos(t);},
                        0, 2*Math.PI], {straightFirst:false, straightLast:false, strokeWidth:2}
                    );
</script>

