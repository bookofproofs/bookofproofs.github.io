layout: definition
categories: branches,geometry,analytic-geometry
nodeid: bookofproofs$7961
orderid: 200
parentid: bookofproofs$139
title: Describing a Straight Line Using Two Vectors
description: DESCRIBING A STRAIGHT LINE USING TWO VECTORS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: 
keywords: (r.x()-q.x())+(p1.y()-q.y()),describing,line,math.sqrt((p1.x()-q.x()),straight,two,using,vectors
contributors: bookofproofs

---
We have seen in the [definition of a straight line][bookofproofs$645] that in the `$n$`-dimensional [number space][bookofproofs$7959], a **straight line** can be defined given two points `$A$` and `$B,$` `$A\neq B$` with the Cartesian coordinates
`$$\begin{array}{rcl}A&=&(x_1,\ldots,x_n)\\B&=&(y_1,\ldots,y_n)\end{array}$$`

as a [map][bookofproofs$592] `$AB:\mathbb R\to \mathbb R^n$` with the formula `$$AB(t):=(x_1+t(y_1-x_1),x_2+t(y_2-x_2)\ldots,x_1+t(y_n-x_n)).$$` We want to explain this seemingly complicated formula. First of all, note that the above formula is very similar to what we have seen in our discussion about [points vs. vectors in a number space][bookofproofs$7960]. Using the argumentation given there, the above formula can be written much more concisely as follows:

---

Let `$A,B$` be points of an `$n$`-dimensional [number space][bookofproofs$7959] `$\mathbb R^n$` with `$A\neq B$` and the origin `$O\in\mathbb R^n.$` The [subset][bookofproofs$552] `$L\subset \mathbb R^n$` of points defined 

`$$L:=\{P\in\mathbb R^n:\;\overrightarrow{OP}=\overrightarrow{OA}+t\cdot \overrightarrow{AB}\},$$`
where `$\overrightarrow{OA}$` and `$\overrightarrow{AB}$` are [vectors][bookofproofs$560] and `$t\cdot \overrightarrow{AB}$` is a [scalar multiplication][bookofproofs$560] with `$t\in\mathbb R$` is called a **straight line** in `$\mathbb R^n.$` 

### Example

You can study the behavior of this formula in the following figure for `$n=2$` (i.e. in the [number plane][bookofproofs$7959]). Of course, the situation is the same for all dimensions `$n.$`

<div id='box-E15106s' class='jxgbox centered' style='max-width:500px; height:500px;'></div>

§§§1

In the above figure, you can move the points `$A$` and `$B$` as well as the point `$AB(t)$` depending on the parameter `$t$` (try it!). The figure demonstrates that as the parameter `$t$` changes, taking all possible real values, the point `$AB(t)$` will move along the points of a straight line. In this sense, the [set][bookofproofs$550] of all points `$P$` whose vectors `$\overrightarrow{OP}$` are given by `$\overrightarrow{OA}+t\cdot \overrightarrow{AB}$` for all `$t\in\mathbb R$` is a [subset][bookofproofs$552] of the number plane which actually __is__ the straight line `$AB.$`

---

§§§1

<script>
JXG.Options.axis.ticks.insertTicks = true;
board = JXG.JSXGraph.initBoard('box-E15106s', {boundingbox: [-5, 5, 5, -5], showCopyright:false, axis:true, grid: true, keepaspectratio: true});


var grid = board.create('grid', []);
var q = board.create('point', [0,2], {name:'A'});
var r = board.create('point', [-1, 2], {name:'B'});
var o = board.create('point', [0,0], {name:'O'});
var l1 = board.create('arrow', [o, q] ,{dash:1, opacity:0.6, strokeWidth:3, }); 

var l3 = board.create('line', [q, r], {color:'green'});

var l21 = board.create('arrow', [q, r], {strokeWidth:3, });
var p1 = board.create('point', [1,2], {name:'OP', attractors: [l3], attractorDistance:0.2, snatchDistance: 20});
var l2 = board.create('arrow', [o, p1] ,{dash:1, opacity:0.6, strokeWidth:3, });

var graph = board.create('text', [-4, 3, function(){var dotproduct=(p1.X()-q.X())*(r.X()-q.X())+(p1.Y()-q.Y())*(r.Y()-q.Y()); var length=Math.sign(dotproduct)*Math.sqrt((p1.X()-q.X())*(p1.X()-q.X())+(p1.Y()-q.Y())*(p1.Y()-q.Y())); return "t ="+length;}]);
</script>

