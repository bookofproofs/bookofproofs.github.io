layout: definition
categories: branches,analysis
nodeid: bookofproofs$199
orderid: 1100
parentid: bookofproofs$166
title: Polynomials
description: POLYNOMIALS &#9733; bring your math skills to the graduate level &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: 
keywords: degree,polynomial,polynomials,real polynomial,x + a3.value(),x + a4.value()
contributors: bookofproofs

---


---

Let `\(a_0,a_1,\ldots,a_n\)` be [real numbers][bookofproofs$1105] with `\(a_n\neq 0\)`. A **real polynomial** (or just a **polynomial**) is a [function][bookofproofs$592].
`\[p:=\begin{cases}
\mathbb R&\to\mathbb R\\
x&\to p(x):=a_nx^n + \ldots + a_1x + a_0\\
\end{cases}\]`

The numbers `\(a_0,a_1,\ldots,a_n\)` are called the **coefficients** of the polynomial. The highest number `\(n\)`, for which the coefficient `\(a_n\neq 0\)`, is called the **degree** of the polynomial.

In the following interactive figure, you can drag the sliders to manipulate the values of the coefficients `\(a_0,a_1,\ldots,a_5\)` and see the behavior of resulting polynomials of the degree up to `\(5\)`. The initial polynomial (when the Reset button is pressed) is of degree `\(0\)`. 

§§§1

---

§§§1


<div id="box199_1" class="jxgbox centered" style="max-width:400px; height:250px;"></div>
<div id="box199" class="jxgbox centered" style="max-width:500px; height:500px;"></div>
 
<script type="text/javascript">
var brd1 = JXG.JSXGraph.initBoard('box199_1', {boundingbox: [2, 0, 20, -20], showNavigation:false, showCopyright: false, axis:false});
var a5 = brd1.create('slider',[[3,-2],[11,-2],[-5,0,5]], {name:'a_5'});
var a4 = brd1.create('slider',[[3,-4],[11,-4],[-5,0,5]], {name:'a_4'});
var a3 = brd1.create('slider',[[3,-6],[11,-6],[-5,0,5]], {name:'a_3'});
var a2 = brd1.create('slider',[[3,-8],[11,-8],[-5,0,5]], {name:'a_2'});
var a1 = brd1.create('slider',[[3,-10],[11,-10],[-5,0,5]], {name:'a_1'});
var a0 = brd1.create('slider',[[3,-12],[11,-12],[-5,0,5]], {name:'a_0'});
var button1 = brd1.create('button', [3, -15, 'Reset', function() {
	a5.moveTo([7,-2]); 
	a4.moveTo([7,-4]);
	a3.moveTo([7,-6]);
	a2.moveTo([7,-8]);
	a1.moveTo([7,-10]);
	a0.moveTo([7,-12]);
	brd.update();
}], {});

var brd = JXG.JSXGraph.initBoard('box199', {boundingbox: [-10, 20, 10, -20], axis:true});

var f = brd.create('functiongraph',[function(x){ 
	return a5.Value()*x*x*x*x*x + a4.Value()*x*x*x*x + a3.Value()*x*x*x + a2.Value()*x*x + a1.Value()*x + a0.Value(); 
}]);
    
a5.on('drag',function(){ brd.update();});
a4.on('drag',function(){ brd.update();});
a3.on('drag',function(){ brd.update();});
a2.on('drag',function(){ brd.update();});
a1.on('drag',function(){ brd.update();});
a0.on('drag',function(){ brd.update();});
</script>

