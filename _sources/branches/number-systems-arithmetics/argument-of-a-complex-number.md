layout: definition
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$8547
orderid: 600
parentid: bookofproofs$8601
title: Argument of a Complex Number
description: ARGUMENT OF A COMPLEX NUMBER ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$8311
keywords: argument,complex argument,argument of a complex number,argument of the complex number,arguments,complex arguments,arguments of complex numbers,arguments of the complex numbers
contributors: bookofproofs

---
The _argument_ of a complex number is the angle of its [vector][bookofproofs$1698] with the real axis of the [complex plane][bookofproofs$216].
---

Let `$z=(a,b)=a+bi$` be a [complex number][bookofproofs$216]. The **argument** of `$z$` is defined by
`$$\phi=\arg(z):=\begin{cases}
\arctan\left(\frac ba\right)&\text{ for }a > 0\\
\arctan\left(\frac ba\right)+\pi&\text{ for }a < 0,\;b\ge 0\\
\arctan\left(\frac ba\right)-\pi&\text{ for }a < 0,\;b < 0\\
\pi/2&\text{ for }a = 0,\;b > 0\\
-\pi/2&\text{ for }a = 0,\;b < 0\\
\text{undefined}&\text{ for }a = 0,\;b = 0
\end{cases}$$`

where `$\pi$` denotes the [number pi][bookofproofs$6738] and `$\arctan$` denotes the [inverse tangent][bookofproofs$6749] function.

Geometrically, the argument of `$z$` measures the angle between the vector `$z$` and the `$x$` axis.

<div id="box-E21625" class="jxgbox centered" style="max-width:500px; height:500px;"></div>
 
§§§1

---

§§§1

<script type="text/javascript">
board = JXG.JSXGraph.initBoard('box-E21625', {boundingbox: [-6, 6, 6, -6], axis: true});
 
var z = board.create('point', [2,2], {style:5,color:'blue',name:'z'});
var rez = board.create('point', ["X(z)",0], {style:5,color:'blue',name:'a'});
var rez2 = board.create('point', [z.X(),0], {visible:false});
var imz = board.create('point', [0,"Y(z)"], {style:5,color:'blue',name:'b'});
var ax2 =board.create('segment', [z,rez], {strokeColor:'blue',strokeWidth:1,dash:1});
var r =board.create('segment', [[0,0],z], {strokeColor:'blue',strokeWidth:2});
r.setLabel('r');
var ay2 =board.create('segment', [z,imz], {strokeColor:'blue',strokeWidth:1,dash:1});
alpha = board.create('angle', [rez2,[0,0],z], {type:'sector',  name:'ϕ', orthoType:'sector', radius:function() {return Math.sqrt(z.X()*z.X()+z.Y()*z.Y());}});

</script>

