layout: definition
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1245
orderid: 300
parentid: bookofproofs$8601
title: Complex Conjugate
description: COMPLEX CONJUGATE ★ bring your math skills to the graduate level ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: 
keywords: complex conjugate,complex conjugates,complex conjugate definition,complex conjugation,conjugate of a complex number
contributors: bookofproofs

---
The _complex conjugate_ of a complex number is its reflection on the real axis in the [complex plane][bookofproofs$216].
---

Let  `\(z=x + yi\in\mathbb C\)` be a [complex number][bookofproofs$1698]. The **complex conjugate** of `\(z\)`, denoted by `\(z^* \)`, is the complex number with the same real part and the negative imaginary part, i.e.

`\[z^* :=\Re(z) - \Im (z) i=x - y i.\]`

In the complex plane, complex conjugates can be interpreted as the reflections of complex numbers across the real axis, as shown in the below figure


![Complex_conjugate_picture](https://github.com/bookofproofs/bookofproofs.github.io/blob/main/_sources/_assets/images/examples/Complex_conjugate_picture.png?raw=true)

(from Wikipedia, uploaded by Aflafla1)

Below, you can experiment with complex conjugation of a polygon in the complex plane. Just move around (e.g. using your mouse, mouse-pad or touchscreen) the points in the `\(z\)`-Plane and see the result in the `\(w\)`-Plane:

`\(z\)`-Plane:
<div id="boxZ" class="jxgbox centered" style="max-width:500px; height:500px;"></div>

`\(w\)`-Plane with `\(w:= z^\ast \)`:
<div id="boxW" class="jxgbox centered" style="max-width:500px; height:500px;"></div>

§§§1

---

§§§1

<script type="text/javascript">
 var boardZ = JXG.JSXGraph.initBoard('boxZ', {boundingbox: [-10, 10, 10, -10], showCopyright: false, axis:true, grid:true});
 var pArrZ = [];
 pArrZ[^0] = boardZ.create('point',[0,0], {size:3});
 pArrZ[^1] = boardZ.create('point',[2,1], {size:3});
 pArrZ[^2] = boardZ.create('point',[2,2], {size:3});
 pArrZ[^3] = boardZ.create('point',[0,1], {size:3});
 var polyZ = boardZ.create('polygon',pArrZ);
 
 
 var boardW = JXG.JSXGraph.initBoard('boxW', {boundingbox: [-10, 10, 10, -10], showCopyright: false, axis:true, grid:true});
 var pArrW = [];
 pArrW[^0] = boardW.create('point',[complexFunction(pArrZ[^0],0).real,complexFunction(pArrZ[^0],0).imaginary], {size:3, fixed:true});
 pArrW[^1] = boardW.create('point',[complexFunction(pArrZ[^1],1).real,complexFunction(pArrZ[^1],1).imaginary], {size:3, fixed:true});
 pArrW[^2] = boardW.create('point',[complexFunction(pArrZ[^2],2).real,complexFunction(pArrZ[^2],2).imaginary], {size:3, fixed:true});
 pArrW[^3] = boardW.create('point',[complexFunction(pArrZ[^3],3).real,complexFunction(pArrZ[^3],3).imaginary], {size:3, fixed:true});
 
 var polyW = boardW.create('polygon',pArrW);

 pArrZ[^0].on('drag', function(){ transform(this,0);});
 pArrZ[^1].on('drag', function(){ transform(this,1);});
 pArrZ[^2].on('drag', function(){ transform(this,2);});
 pArrZ[^3].on('drag', function(){ transform(this,3);});
 

 
 function complexFunction(point,id) {
	 var compl=new JXG.Complex(point.X(), point.Y());
	 
	 // insert the complex function here
	 // begin of function 
	 var compc=compl.conj();
	 // end of runction  

	 return compc;
 }
 

 
 function transform(point,id) {
	 var compc=complexFunction (point,id);
	 pArrW[id].setPosition(JXG.COORDS_BY_USER,[compc.real,compc.imaginary]);
	 boardW.update();
 }
</script>

