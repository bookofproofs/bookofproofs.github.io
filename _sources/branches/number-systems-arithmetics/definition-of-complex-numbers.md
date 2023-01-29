layout: definition
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$216
orderid: 50
parentid: bookofproofs$6788
title: Definition of Complex Numbers
description: DEFINITION OF COMPLEX NUMBERS ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: 
keywords: complex number,complex plane,set of complex numbers,complex numbers,real part,imaginary part,real parts,imaginary parts,complex-valued,real and imaginary parts,definition of complex numbers
contributors: bookofproofs

---


---

A **complex number** `\(x\)` is an [ordered pair][bookofproofs$747] of [real numbers][bookofproofs$1105] `\(a\)` and `\(b\)`: 

`\[x:=(a,b),\quad\quad  a,b\in\mathbb R\]`

`\(\Re(x):=a\)` is called the **real part** and `\(\Im(x):=b\)` is called the **imaginary part** of the complex number `\(z\)`. 

This means that two complex numbers `$z$` and `$z'$` are equal, if and only if `$\Re(z)=\Re(z')$` and `$\Im(z)=\Im(z').$`
 
The **set of complex numbers** is denoted by `\(\mathbb C\)`. 
 
The set of complex numbers can be interpreted as a **complex plane**, in which every complex number `\(z\)` is a single point. In the following figure, you can drag the point `\(z\)` to see, how it moves through the complex plane and how the real and imaginary parts of the complex number change:

<div id="box216" class="jxgbox centered" style="max-width:500px; height:500px;"></div>
 
§§§1

---

§§§1

<script type="text/javascript">
board = JXG.JSXGraph.initBoard('box216', {boundingbox: [-6, 6, 6, -6], axis: true});
 
var z = board.create('point', [2,2], {style:5,color:'blue',name:'z'});
var rez = board.create('point', ["X(z)",0], {style:5,color:'blue',name:'\Re(z)'});
var imz = board.create('point', [0,"Y(z)"], {style:5,color:'blue',name:'\Im(z)'});
var ax2 =board.create('segment', [z,rez], {strokeColor:'blue',strokeWidth:1,dash:1});
var ay2 =board.create('segment', [z,imz], {strokeColor:'blue',strokeWidth:1,dash:1});
</script>

