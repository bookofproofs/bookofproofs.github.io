layout: definition
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1247
orderid: 500
parentid: bookofproofs$8601
title: Absolute Value of Complex Numbers
description: ABSOLUTE VALUE OF COMPLEX NUMBERS ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$696
keywords: complex absolute value,absolute value of a complex number,absolute value of complex numbers
contributors: bookofproofs

---
When a [complex number][bookofproofs$1247] `$z=(a,b)=a+bi$` is interpreted as a [vector][bookofproofs$1698], the _absolute value_ of it is simply the length of the vector. Its definition is chosen in such a way that it is "compatible" with the [Euclidean distance][bookofproofs$1206] of two points in the [complex plane][bookofproofs$216].
---

The **absolute value** `\(|z|\)` of a [complex number][bookofproofs$216] `\(z=a+bi\in\mathbb C\)` is the (positive) [square root][bookofproofs$1161] of the [dot product][bookofproofs$1246] of `\(z\)` with itself, i.e. the [non-negative real number][bookofproofs$1107].
`\[|z|:=\sqrt{\langle z, z\rangle}=\sqrt{\Re(z\cdot z^*)}=\sqrt{a^2+b^2}.\]`

Geometrically, it is the real number, which equals the distance of the complex number from the origin:


<div id="box" class="jxgbox centered" style="max-width:500px; height:500px;"></div>
 
§§§1

---

§§§1

<script type="text/javascript">
board = JXG.JSXGraph.initBoard('box', {boundingbox: [-6, 6, 6, -6], axis: true});
 
var z = board.create('point', [2,2], {style:5,color:'blue',name:'z'});
var p1 = board.create('point', [0,0], {style:-1,color:'blue',name:''});
var p2 = board.create('point', [function xx(){ return Math.sqrt(z.X()*z.X()+z.Y()*z.Y());},0], {style:5,color:'blue',name:'|z|'});
var a = board.create('arc', [p1, p2 , z]);
</script>

