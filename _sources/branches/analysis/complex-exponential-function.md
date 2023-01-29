layout: proposition
categories: branches,analysis
nodeid: bookofproofs$312
orderid: 50
parentid: bookofproofs$201
title: Complex Exponential Function
description: COMPLEX EXPONENTIAL FUNCTION &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: 
keywords: (p4.x()-p3.x()),p3.y()+t,complex,complex exponential series,exponential,function
contributors: bookofproofs

---


---

The **complex exponential series** 

`\[\sum_{n=0}^\infty\frac{z^n}{n!}\]`

is an [absolutely convergent complex series][bookofproofs$1725] for every [complex number][bookofproofs$1698] `\(z\in\mathbb C\)`. It defines a [function][bookofproofs$592] `\(\exp:\mathbb C\mapsto \mathbb C\)`, called the **complex exponential function** for all `\(z\in\mathbb C\)`.

`\[\exp(x):=\sum_{n=0}^\infty\frac{z^n}{n!},\quad\quad z\in\mathbb R.\]`

In the following interactive figure, in the "`\(z\)`-plane", you can drag the circle's midpoint, drag the segment's endpoints or change the radius of the circle and get a feeling of how the complex exponential function deforms their images    in the "`\(w\)`-plane".

`\(z\)`-Plane

<div><div id="boxZ312" class="jxgbox centered" style="max-width:400px; height:400px;"></div></div>

`\(w\)`-Plane

<div><div id="boxW312" class="jxgbox centered" style="max-width:400px; height:400px;"></div></div>

§§§1

---

§§§1

<script type="text/javascript">
 var boardZ = JXG.JSXGraph.initBoard('boxZ312', {boundingbox: [-10, 10, 10, -10], showCopyright: false, axis:true, grid:false});
 var p1 = boardZ.create('point',[-1,0], {name:'A',size: 2, face: 'o'});
 var p2 = boardZ.create('point',[1.5,-1], {name:'B',size: 2, face: 'o'});
 var ci = boardZ.create('circle',["A","B"], {strokeColor:'#0000ff', strokeWidth:1, fillColor:'#00ff00', fillOpacity:0.5});
 ci.on('drag', function(){ transform();});
 p1.on('drag', function(){ transform();});
 p2.on('drag', function(){ transform();});
 var p3 = boardZ.create('point',[1.5,-6.3], {name:'C',size: 2, face: 'o'});
 var p4 = boardZ.create('point',[0.5,2], {name:'D',size: 2, face: 'o'});
 var li2 = boardZ.create('line',[p3,p4], {straightFirst:false, straightLast:false, strokeWidth:2, strokeColor:"#ff00ff"});
 p3.on('drag', function(){ transform();});
 p4.on('drag', function(){ transform();});
 li2.on('drag', function(){ transform();});
 


 
var boardW = JXG.JSXGraph.initBoard('boxW312', {boundingbox: [-10, 10, 10, -10], showCopyright: false, axis:true, grid:false});

 // image of circle's mid point
 var compc=complexFunction (p1.X(),p1.Y());
 var p1w=boardW.create('point',[compc.real,compc.imaginary], {size:2, name:'exp(A)', fixed:true});
 
// image of segment's ends
 var compc=complexFunction (p3.X(),p3.Y());
 var p3w=boardW.create('point',[compc.real,compc.imaginary], {size:2, name:'exp(C)', fixed:true});
 var compc=complexFunction (p4.X(),p4.Y());
 var p4w=boardW.create('point',[compc.real,compc.imaginary], {size:2, name:'exp(D)', fixed:true});

 
 // image of circle
 var pArrW = [];

 var N=160;
 var indexOfPointB=0;
 var rad=ci.Radius();
 for (var i=0; lt(i,N); i++) {
	 var t=i/N;
	 if (lt(Math.abs(ci.X(t)-p2.X())+Math.abs(ci.Y(t)-p2.Y()),0.05) ) {
		 indexOfPointB=i; // calculate, which one is the image point of point B and remember it for transform()
		 var compc=complexFunction (ci.X(t),ci.Y(t));
		 pArrW[i] = boardW.create('point',[compc.real,compc.imaginary], {size:2, name:'exp(B)', fixed:true});
	 } else {
		 var compc=complexFunction (ci.X(t),ci.Y(t));
		 pArrW[i] = boardW.create('point',[compc.real,compc.imaginary], {size:1, name:'', fixed:true,visible:false});
	 }
 }
 var polW = boardW.create('polygon',pArrW, {fillOpacity:0.5});
 
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

 function complexFunction(x,y) {
         var w=new JXG.Complex(Math.exp(x),0); // exp(x)
         var w1=new JXG.Complex(Math.cos(y),0); // cos(y)
         var w2=new JXG.Complex(0,Math.sin(y)); // i*sin(y)
         w1.add(w2); // exp(iy) Euler's Formula
         w.mult(w1); // exp(z)
	 return w;

 }

</script>


