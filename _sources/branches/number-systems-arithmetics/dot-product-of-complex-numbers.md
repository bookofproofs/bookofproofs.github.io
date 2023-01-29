layout: definition
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1246
orderid: 400
parentid: bookofproofs$8601
title: Dot Product of Complex Numbers
description: DOT PRODUCT OF COMPLEX NUMBERS ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$696
keywords: dot product of two complex numbers,dot product of complex numbers,complex number dot product,dot product complex numbers,complex dot product,dot product of two complex vectors,dot product of complex vectors,dot product complex vectors,dot product with complex numbers,dot product in complex numbers,dot product complex,complex numbers dot product,inn
contributors: bookofproofs

---


---

Let `\[\begin{array}{rcl}
x & := & a + b i\\
y & := & c + d i
\end{array}\]`
be two complex numbers, i.e. [vectors represented by linear combinations][bookofproofs$1698] of the basis `\(\{1,i\}\)`. We define the [dot product][bookofproofs$1049] of these two complex numbers as follows

`\[\begin{array}{rcl}
\langle x,y\rangle &:=&\Re(x\cdot y^*)\\
&=&\Re((a+bi)\cdot (c-di))\\
&=&\Re(ac-adi+bci-bdi^2)\\
&=&\Re(ac-bd\cdot(-1)+(bc-ad)i)\\
&=&\Re((ac+bd)+(bc-ad)i)\\
&=&ac+bd
\end{array}\]`

where  `\(y^*\)` is the [complex conjugate][bookofproofs$1245] of `\(y\)` and `\(\Re(x\cdot y^*)\)` denotes the [real part][bookofproofs$216] of the the complex number `\(x\cdot y^*\)`. Please note that the dot product of complex numbers is always a [real number][bookofproofs$1105].
The following interactive figure shows two complex numbers (blue), which you can drag to see how their position influences the dot product (red).


<div id="boxE21059" class="centered jxgbox" style="max-width:500px; height:500px;"></div>

*Fun questions:* 
* When is the dot product negative?
* When is the dot product positive?
* When does the dot product equal zero?


 
§§§1

---

§§§1

<script type="text/javascript">
board = JXG.JSXGraph.initBoard('boxE21059', {boundingbox: [-6, 6, 6, -6], axis: true});
 
var x = board.create('point', [1,2], {style:5,color:'blue',name:'x'});
var y = board.create('point', [2,1], {style:5,color:'blue',name:'y'});
var dotpr = board.create('point', ["X(x)*X(y)+Y(x)*Y(y)",0], {style:5,color:'red',name:'dot product',fixed:true});
var org = board.create('point', [0,0], {style:5,color:'blue',name:''});
var ax =board.create('arrow', [org,x ], {strokeColor:'green'});
var ax =board.create('arrow', [org,y ], {strokeColor:'green'});
</script>

