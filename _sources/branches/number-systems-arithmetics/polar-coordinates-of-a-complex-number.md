layout: proposition
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$6750
orderid: 700
parentid: bookofproofs$8601
title: Polar Coordinates of a Complex Number
description: POLAR COORDINATES OF A COMPLEX NUMBER ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$8311
keywords: polar coordinates,polar coordinate,polar coordinate of complex number,polar coordinates of complex numbers,polar,polar coordinates uniquely represent the complex numbers
contributors: bookofproofs

---
The [argument of a complex number][bookofproofs$8547] and its [absolute value][bookofproofs$1247] allow for another unique representation of a complex number, which is different from its vector representation `$z=(a,b)=a+bi$` but particularly useful in some applications.

---

Every complex number `$z\in\mathbb C$` can be written as `$z=r\exp(i\phi),$` for some [real numbers][bookofproofs$1105] `$\phi\in\mathbb R$` and `$r=|z|\in\mathbb R_+,$` where `$\exp$` denotes the [complex exponential function][bookofproofs$312] and `$|z|$` denotes the [absolute value][bookofproofs$1247] of `$z$`. For `$z\neq 0,$` the number `$\phi$` is uniquely determined apart of a multiple of `$2\pi,$` i.e. for all `$k\in Z$`:

`$$z=r\exp(i\phi)=r\exp(i\phi+2\pi k).$$`

The number `$r$` can be interpreted as the radius of the circle drawn at the origin of the complex plane which equals the distance of `$z$` to the origin. The number `$\phi$` can be interpreted as the angle between the positive `$x-$`axis and the ray from the origin to the point `$z.$`

<div id="boxE20050" class="jxgbox centered" style="max-width:500px; height:500px;"></div>
 
§§§1

---

§§§1

<script type="text/javascript">
board = JXG.JSXGraph.initBoard('boxE20050', {boundingbox: [-6, 6, 6, -6], axis: true});
 
var z = board.create('point', [2,2], {style:5,color:'blue',name:'z'});
var rez = board.create('point', ["X(z)",0], {style:5,color:'blue',name:'\Re(z)'});
var rez2 = board.create('point', [z.X(),0], {visible:false});
var imz = board.create('point', [0,"Y(z)"], {style:5,color:'blue',name:'\Im(z)'});
var ax2 =board.create('segment', [z,rez], {strokeColor:'blue',strokeWidth:1,dash:1});
var r =board.create('segment', [[0,0],z], {strokeColor:'blue',strokeWidth:2});
r.setLabel('r');
var ay2 =board.create('segment', [z,imz], {strokeColor:'blue',strokeWidth:1,dash:1});
alpha = board.create('angle', [rez2,[0,0],z], {type:'sector',  name:'ϕ', orthoType:'sector', radius:function() {return Math.sqrt(z.X()*z.X()+z.Y()*z.Y());}});

</script>

