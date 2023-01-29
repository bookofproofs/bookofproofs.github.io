layout: definition
categories: branches,geometry,analytic-geometry
nodeid: bookofproofs$7959
orderid: 50
parentid: bookofproofs$139
title: Points in a Coordinate System - Number Spaces
description: POINTS IN A COORDINATE SYSTEM - NUMBER SPACES &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: 
keywords: a-5,10,coordinate,coordinates,number,number line,number space,number spaces,points,spaces,system
contributors: bookofproofs

---


---

The analytic geometry is based on the modern definition of a [point][bookofproofs$631] in the Euclidean geometry. Recall that a point `$P$` in an `$n$`-dimensional [Euclidean vector space][bookofproofs$1206] `$\mathbb R^n$` is represented by `$n$` [real-numbered][bookofproofs$1105] **coordinates**:

`$$P=(x_1,\ldots,x_n).$$`

### A note on terminology

In analytic geometry deals with the most common, real-valued vector spaces, i.e. the vector spaces over the field of real numbers `$\mathbb R^n$`. In general, vector spaces can be defined on other types of fields (e.g. rational numbers `$Q^n$`). In order to learn more about general vector spaces and their properties, please refer to its [formal definition][bookofproofs$560] and theory established in the linear algebra branch of <strong><span style='color:orange'>Bookof</span><span style='color:lightblue'>Proofs</span></strong>. 

In the following, we will use the term **number spaces** as a synonym to the vector space over the field of real numbers `$\mathbb R^n$`, and we will be using the terms **number line**, **number plane** and **number space** depending on the dimension `$n=1,2,3,\ldots$`.



### Case `$n=1:$` Number line

In the following example, we see the **number line** `$\mathbb R^1$` with some points on it. Each point on the number line can be represented by exactly one coordinate. Actually, the points can be identified by the real numbers being their coordinates, e.g. `$P_0=(-1),$` `$P_1=(0),$` `$P_2=(\sqrt 2),$`, `$P_3=(\Pi),$` etc.


<div id='box-E15102' class='jxgbox centered' style='max-width:500px; height:500px;'></div>

§§§1

### Case `$n=2:$` Number plane

In the two-dimensional case, `$\mathbb R^2$` consists of all points, which can be represented by exactly two coordinates. This space is called the **number plane**. In the below example, the same points as in example 1 have now two coordinates: `$P_0=(-1,0),$` `$P_1=(0,0),$` `$P_2=(\sqrt 2,0)$`, `$P_3=(\Pi,0)$`, in which the first coordinate is the same as in example 1, and the second coordinate is zero. Of course, we can designate also any points having a non-zero second coordinate:

<div id='box-E15102a' class='jxgbox centered' style='max-width:500px; height:500px;'></div>

§§§2

### Case `$n=3:$` Number space

In the three-dimensional **number space** `$\mathbb R^3$` each point is represented by three coordinates. Thus, the above four example points would be `$P_0=(-1,0,0),$` `$P_1=(0,0,0),$` `$P_2=(\sqrt 2,0,0)$`, `$P_3=(\Pi,0,0).$` This demonstrates the following diagram:

<div id='box-E15102b' class='jxgbox centered' style='max-width:500px; height:500px;'></div>

§§§3

In order to get a sense of the three-dimensional number space, you can click on the following "Evaluate" button and animate 10 randomly generated points with your mouse:

§§§4

### Case `$n > 3:$` More-dimensional Number space

In an analogous manner, a point `$P$` in an `$n$`-dimensional number space `$\mathbb R^n$`, `$n > 3$` is represented by exactly `$n$` coordinates. While it is perfectly possible to write down all `$n$` coordinates of a given point and calculate with them, it is unfortunately not possible to visualize a space with more than `$3$` dimensions.

---

§§§1

<script>
JXG.Options.axis.ticks.majorHeight = 60;
JXG.Options.axis.ticks.insertTicks = false;
JXG.Options.axis.ticks.ticksDistance = 100;
board = JXG.JSXGraph.initBoard('box-E15102', {boundingbox: [-3, 3, 4, -3], axis:false, showCopyright:false, grid:false, showCopyright:false, showNavigation:false});
xaxis = board.create('axis', [[0, 0], [1,0]]);


var org = board.create('point', [0,0], {style:5,visible:true,fixed:true,name:'(0)'});
var pi = board.create('point', [Math.PI,0], {style:5,visible:true,fixed:true,name:'(π)'});
var sqrt2= Math.sqrt(2);
var sqrt2p = board.create('point', [sqrt2,0], {style:5,visible:true,fixed:true,name:'(√2)'});
var minus1 = board.create('point', [-1,0], {style:5,visible:true,fixed:true,name:'(-1)'});
</script>


§§§2

<script>
JXG.Options.axis.ticks.insertTicks = false;
board = JXG.JSXGraph.initBoard('box-E15102a', {boundingbox: [-3, 3, 4, -3], showCopyright:false, axis:true});

var org = board.create('point', [0,0], {style:5,visible:true,fixed:true,name:'(0,0)'});
var pi = board.create('point', [Math.PI,0], {style:5,visible:true,fixed:true,name:'(π,0)'});
var sqrt2= Math.sqrt(2);
var sqrt2p = board.create('point', [sqrt2,0], {style:5,visible:true,fixed:true,name:'(√2,0)'});


var pa = board.create('point', [-1,-1], {style:5,visible:true,fixed:true,name:'(-1,-1)'});
var pb = board.create('point', [-1,0], {style:5,visible:true,fixed:true,name:'(-1,0)'});
var pc = board.create('point', [-1,1], {style:5,visible:true,fixed:true,name:'(-1,1)'});
var pd = board.create('point', [0,1], {style:5,visible:true,fixed:true,name:'(0,1)'});
var pf = board.create('point', [0,-1], {style:5,visible:true,fixed:true,name:'(0,-1)'});
var pe = board.create('point', [1,1], {style:5,visible:true,fixed:true,name:'(1,1)'});
var pg = board.create('point', [1,-1], {style:5,visible:true,fixed:true,name:'(1,-1)'});


</script>


§§§3

<script>
JXG.Options.axis.ticks.insertTicks = false;
board = JXG.JSXGraph.initBoard('box-E15102b', {boundingbox: [-3, 3, 4, -3], showCopyright:false, axis:true});

var l1 = board.create('axis', [[-2, -1.0], [0.0, 0.0]]);

var org = board.create('point', [0,0], {style:5,visible:true,fixed:true,name:'(0,0,0)'});
var pi = board.create('point', [Math.PI,0], {style:5,visible:true,fixed:true,name:'(π,0,0)'});
var sqrt2= Math.sqrt(2);
var sqrt2p = board.create('point', [sqrt2,0], {style:5,visible:true,fixed:true,name:'(√2,0,0)'});
var minus1 = board.create('point', [-1,0], {style:5,visible:true,fixed:true,name:'(-1,0,0)'});

var pa = board.create('point', [-1,-0.5], {style:5,visible:true,fixed:true,name:'(0,-1,0)'});
var pb = board.create('point', [1,0.5], {style:5,visible:true,fixed:true,name:'(0,1,0)'});
var pc = board.create('point', [-2,-0.5], {style:5,visible:true,fixed:true,name:'(-1,-1,0)'});
var pd = board.create('point', [2,0.5], {style:5,visible:true,fixed:true,name:'(1,1,0)'});

var pe = board.create('point', [0,1], {style:5,visible:true,fixed:true,name:'(0,0,1)'});
var pf = board.create('point', [2,0.5], {style:5,visible:true,fixed:true,name:'(1,1,0)'});

</script>


§§§4
<div class='sage'>

v = [(random(), random(), random()) for _ in [1..10]]
sum([cube((10*a-5,10*b-5,10*c-5), size=1/3, color=(a,b,c)) for a,b,c in v])
</div>
