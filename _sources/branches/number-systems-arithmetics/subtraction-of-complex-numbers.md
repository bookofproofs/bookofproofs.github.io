layout: definition
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1701
orderid: 300
parentid: bookofproofs$216
title: Subtraction of Complex Numbers
description: SUBTRACTION OF COMPLEX NUMBERS ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: 
keywords: complex difference,subtraction of complex numbers,subtraction
contributors: bookofproofs

---


---

Let `\(x\)` and `\(y\)` be [complex numbers][bookofproofs$1698] represented by `\[\begin{array}{rcl}x&:=&(a,b),\\
y&:=&(c,d).\end{array}\]`

The  **subtraction of complex numbers**, written `\(x-y\)`, is defined as the [addition][bookofproofs$1657] of the first complex number `\(x\)` with the [inverse of the second complex number with respect to addition][bookofproofs$1664] `\((-y)\)`, formally
`\[x-y:=(a,b)+(-c,-d)=(a-c,b-d).\]`

The result of the subtraction is called **difference**. Geometrically, the difference of two complex numbers can be interpreted as the vector pointing from `\(y\)` to `\(x\)`, which has been shifted to start at the origin:

<div id="boxE20486" class="jxgbox centered" style="max-width:500px; height:500px;"></div>

<div style ='clear:both'></div> 
 
§§§1

---

§§§1

<script type="text/javascript">
board = JXG.JSXGraph.initBoard('boxE20486', {boundingbox: [-6, 6, 6, -6], axis: true});
 
var org = board.create('point', [0,0], {style:10,visible:true,fixed:true,name:' '});
var x = board.create('point', [2,2], {style:5,color:'blue',name:'x'});
var y = board.create('point', [-1,-3], {style:5,color:'blue',name:'y'});
var xy = board.create('point', 
    ["X(x)-X(y)","Y(x)-Y(y)"], {style:7,color:'green',name:'x-y'});
var ax =board.create('arrow', [org,x], {strokeColor:'blue'});
var ay =board.create('arrow', [org,y], {strokeColor:'blue'});
var axy =board.create('arrow', [org,xy], {strokeColor:'red'});
var ax2 =board.create('segment', [x,xy], {strokeColor:'blue',strokeWidth:1,dash:1});
var ay2 =board.create('segment', [y,x], {strokeColor:'red',strokeWidth:1,dash:1})
</script>

