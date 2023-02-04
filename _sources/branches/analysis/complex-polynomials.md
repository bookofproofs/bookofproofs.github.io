layout: definition
categories: branches,analysis
nodeid: bookofproofs$252
orderid: 700
parentid: bookofproofs$201
title: Complex Polynomials
description: COMPLEX POLYNOMIALS ★ bring your math skills to the graduate level ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: 
keywords: complex polynomial,polynomials
contributors: bookofproofs

---


---

Let `\(a_0,a_1,\ldots,a_n\)` be [complex numbers][bookofproofs$1243] with `\(a_n\neq 0\)`. A **complex polynomial** (or just a **polynomial**) is a [function][bookofproofs$592].
`\[p:=\cases{
\mathbb C\to\mathbb C\\
z\to p(z):=a_nz^n + \ldots + a_1z + a_0\\ 
}\]`

The numbers `\(a_0,a_1,\ldots,a_n\)` are called the **coefficients** of the polynomial. The highest number `\(n\)`, for which the coefficient `\(a_n\neq 0\)`, is called the **degree** of the polynomial.

In the following interactive figure, you can drag the sliders to manipulate the values of the (complex) coefficients `\(a_j=x_j+iy_j\)`, `\(j=0,1,2,3\)`, by manipulating their real (respectively imaginary) parts `\(x_j\)` (respectively `\(y_j\)`). You can then study the behavior of the resulting polynomials of a degree up to `\(3\)`. The images of a circle and a segment in the complex plane are shown. The initial polynomial (when the Reset button is pressed) is of degree `\(0\)` ("constant polynomial").

`$w:=a_3z^3+a_2z^2+a_1z+a_0$`

<div id="box2-252a" class="jxgbox centered" style="max-width:400px; width:100%; height:150px;"></div>

`$z$`-plane 

<div id="boxZ-252a" class="jxgbox centered" style="max-width:400px; width:100%; height:400px;"></div>

`$w$`-plane 
<div id="boxW-252a" class="jxgbox centered" style="max-width:400px;width:100%;  height:400px;"></div>

§§§1

---

§§§1

<script type="text/javascript">
 var boardZ = JXG.JSXGraph.initBoard('boxZ-252a', {boundingbox: [-10, 10, 10, -10], showCopyright: false, axis:true, grid:false});
 var p1 = boardZ.create('point',[0,0], {name:'A',size: 2, face: 'o'});
 var p2 = boardZ.create('point',[3,0], {name:'B',size: 2, face: 'o'});
 var ci = boardZ.create('circle',["A","B"], {strokeColor:'#0000ff', strokeWidth:1, fillColor:'#00ff00', fillOpacity:0.5});
 ci.on('drag', function(){ transform();});
 p1.on('drag', function(){ transform();});
 p2.on('drag', function(){ transform();});
 var p3 = boardZ.create('point',[-3,-4], {name:'C',size: 2, face: 'o'});
 var p4 = boardZ.create('point',[4,2], {name:'D',size: 2, face: 'o'});
 var li2 = boardZ.create('line',[p3,p4], {straightFirst:false, straightLast:false, strokeWidth:2, strokeColor:"#ff00ff"});
 p3.on('drag', function(){ transform();});
 p4.on('drag', function(){ transform();});
 li2.on('drag', function(){ transform();});
 
 var brdS = JXG.JSXGraph.initBoard('box2-252a', {boundingbox: [2, 0, 30, -20], showNavigation:false, showCopyright: false, axis:false});
 var ca3 = brdS.create('slider',[[3,-3],[11,-3],[-5,0,5]], {name:'x_3'});
 var ca2 = brdS.create('slider',[[3,-5.5],[11,-5.5],[-5,0,5]], {name:'x_2'});
 var ca1 = brdS.create('slider',[[3,-8],[11,-8],[-5,2,5]], {name:'x_1'});
 var ca0 = brdS.create('slider',[[3,-10.5],[11,-10.5],[-5,0,5]], {name:'x_0'});
 var t3 = brdS.create('text',[15.2,-3,"+ i *"]);
 var cb3 = brdS.create('slider',[[17,-3],[25,-3],[-5,0,5]], {name:'y_3'});
 var t2 = brdS.create('text',[15.2,-5.5,"+ i *"]);
 var cb2 = brdS.create('slider',[[17,-5.5],[25,-5.5],[-5,0,5]], {name:'y_2'});
 var t1 = brdS.create('text',[15.2,-8,"+ i *"]);
 var cb1 = brdS.create('slider',[[17,-8],[25,-8],[-5,2,5]], {name:'y_1'}); 
 var t0 = brdS.create('text',[15.2,-10.5,"+ i *"]);
 var cb0 = brdS.create('slider',[[17,-10.5],[25,-10.5],[-5,0,5]], {name:'y_0'});

 ca3.on('drag',function(){ transform();});
 ca2.on('drag',function(){ transform();});
 ca1.on('drag',function(){ transform();});
 ca0.on('drag',function(){ transform();});
 cb3.on('drag',function(){ transform();});
 cb2.on('drag',function(){ transform();});
 cb1.on('drag',function(){ transform();});
 cb0.on('drag',function(){ transform();});
 
 var button1 = brdS.create('button', [3, -15, 'Reset', function() {
 	ca3.moveTo([7,-3]);
 	ca2.moveTo([7,-5.5]);
 	ca1.moveTo([7.8,-8]);
 	ca0.moveTo([7,-10.5]);
 	cb3.moveTo([21,-3]);
 	cb2.moveTo([21,-5.5]);
 	cb1.moveTo([21,-8]);
 	cb0.moveTo([21,-10.5]);
 	transform();
 }], {});

 var boardW = JXG.JSXGraph.initBoard('boxW-252a', {boundingbox: [-10, 10, 10, -10], showCopyright: false, axis:true, grid:false});

 // image of circle's mid point
 var compc=complexFunction (p1.X(),p1.Y());
 var p1w=boardW.create('point',[compc.real,compc.imaginary], {size:2, name:'p(A)', fixed:true});
 
 // image of segment's ends
 var compc=complexFunction (p3.X(),p3.Y());
 var p3w=boardW.create('point',[compc.real,compc.imaginary], {size:2, name:'p(C)', fixed:true});
 var compc=complexFunction (p4.X(),p4.Y());
 var p4w=boardW.create('point',[compc.real,compc.imaginary], {size:2, name:'p(D)', fixed:true});

 
 // image of circle
 var pArrW = [];

 var N=160;
 var indexOfPointB=0;
 var rad=ci.Radius();
 for (var i=0; lt(i,N); i++) {
	 var t=i/N;
	 if (lt(Math.abs(ci.X(t)-p2.X())+Math.abs(ci.Y(t)-p2.Y()),0.1) ) {
		 indexOfPointB=i; // calculate, which one is the image point of point B and remember it for tranform()
		 var compc=complexFunction (ci.X(t),ci.Y(t));
		 pArrW[i] = boardW.create('point',[compc.real,compc.imaginary], {size:2, name:'p(B)', fixed:true});
	 } else {
		 var compc=complexFunction (ci.X(t),ci.Y(t));
		 pArrW[i] = boardW.create('point',[compc.real,compc.imaginary], {size:0, name:'', fixed:true});
	 }
 }
 var polW = boardW.create('polygon',pArrW, {fillOpacity:0.5, fixed:true});  
 
 // image of segment
 var x=[];
 var y=[];
 for (var i=0; le(i,N); i++) {
	 var t=i/N;
	 var compc=complexFunction (p3.X()+t*(p4.X()-p3.X()),p3.Y()+t*(p4.Y()-p3.Y()));
	 x[i]=compc.real;
	 y[i]=compc.imaginary;
 }
 var segment = boardW.create('curve', [x,y], {strokeWidth:2, strokeColor:"#ff00ff", fixed:true});
 
 function complexFunction(x,y) {
	 var complcoeff=[];
	 complcoeff[0]=new JXG.Complex(ca0.Value(), cb0.Value());
	 complcoeff[1]=new JXG.Complex(ca1.Value(), cb1.Value());
	 complcoeff[2]=new JXG.Complex(ca2.Value(), cb2.Value());
	 complcoeff[3]=new JXG.Complex(ca3.Value(), cb3.Value()); 
	 
	 var z=new JXG.Complex(x, y);
	 
	 // insert the complex function here
	 // begin of function 
	 var w=new JXG.Complex(0, 0);
	 w.add(complcoeff[0]);
	 w.add(complcoeff[1].mult(z));
	 z=z.mult(z); w.add(complcoeff[2].mult(z));
	 z=z.mult(z); w.add(complcoeff[3].mult(z));
	 // end of function  

	 return w;
 }

 var offset=0;
 
 function transform() {

	// update circle
	 for (var i=0; lt(i,N); i++) {
		 var t=i/N;
		 if (lt(Math.abs(ci.X(t)-p2.X())+Math.abs(ci.Y(t)-p2.Y()),0.1) ) {
			 offset=i; break; // calculate, which point is the image of point B this time.
		 }
	 }
	 var j=0; 
	 do {
		 var t=(offset+j)/N;
		 var compc=complexFunction (ci.X(t),ci.Y(t)); // when j==0, the image of point B is computed
		 pArrW[(indexOfPointB+j) % N].setPosition(JXG.COORDS_BY_USER,[compc.real,compc.imaginary]);
		 j=j+1
	 } while (lt(j,N));

	 
	 // update circle's mid point
	 var compc=complexFunction (p1.X(),p1.Y()); 
	 p1w.setPosition(JXG.COORDS_BY_USER,[compc.real,compc.imaginary]);

	 // update segment's ends
	 compc=complexFunction (p3.X(),p3.Y()); 
	 p3w.setPosition(JXG.COORDS_BY_USER,[compc.real,compc.imaginary]);
	 compc=complexFunction (p4.X(),p4.Y()); 
	 p4w.setPosition(JXG.COORDS_BY_USER,[compc.real,compc.imaginary]);

	 // update segment
	 var x=[];
	 var y=[];
	 for (var i=0; lt(i,N); i++) {
		 var t=i/N;
		 compc=complexFunction (p3.X()+t*(p4.X()-p3.X()),p3.Y()+t*(p4.Y()-p3.Y()));
		 x[i]=compc.real;
		 y[i]=compc.imaginary;
	 }
	 segment.dataX=x;
	 segment.dataY=y;
	 boardW.update();
 }
</script>


