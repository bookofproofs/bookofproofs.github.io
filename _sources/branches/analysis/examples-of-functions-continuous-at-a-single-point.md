layout: example
categories: branches,analysis
nodeid: bookofproofs$6868
orderid: 50
parentid: bookofproofs$219
title: Examples of Functions Continuous at a Single Point
description: EXAMPLES OF FUNCTIONS CONTINUOUS AT A SINGLE POINT &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: 
keywords: continuous,examples,functions,point,proof,single,x+3
contributors: bookofproofs

---


---

The following are examples of real functions, which are continuous at single points. They exhibit the [main ideas of the definition of continuity of a function at a single point][bookofproofs$219]:

### Example 1:

The function `$f:\mathbb R\to \mathbb R$`, `$f(x):=2x- 3$` is continuous at a point `$x=5$`.
<div id="box68681" class="jxgbox centered" style="max-width:30%; height:500px;"></div>
 
§§§1

*Proof*: 
* Let `$f(x)=2x- 3.$`
* Take any `$\epsilon > 0$` and set `$\delta:=\epsilon/2.$`
* Select `$x$` such that `$0 < |x- 5| < \delta = \epsilon/2.$`
* Then `$\delta > |x- 5|$` implies `$\epsilon > 2|x- 5| = |2x-10| = |(2x- 3)- 7| = |f(x)- 7|.$`
* Because `$\epsilon$` might have been chosen arbitrarily small, it follows that the limit `$$\lim_{x\to 5}f(x)=\lim_{x\to 5}2x- 3=7$$` exists (and equals `$7$`). 
* Thus, `$f$` is continuous at the point `$x=5.$`

### Example 2

The function `$f:\mathbb R\to \mathbb R$`, `$f(x):=\frac{x+2}{x^2+3x+2}$` is continuous at a point `$x=-2$`. Please note that the function is not defined for this value of `$x$` (division by zero!), even though its limit, as `$x$` approaches `$-2$`, exists. 

<div id="box68682" class="jxgbox centered" style="max-width:30%; height:500px;"></div>
 
§§§2


*Proof*:

* Let `$f(x)=\frac{x+2}{x^2+3x+2}.$`
* Take any `$\epsilon > 0$` and set `$\delta:=\min(\epsilon/2,1/2).$`
* Select `$x$` such that `$\delta > |x- (-2)| > 0.$`
* `$1/2 \ge \delta > |x+2|$` implies `$-1/2 < x + 2 < 1/2$`, so `$-3/2 < x + 1 < -1/2$`. Thus `$2 > \frac 1{|x+1|}$` and `$\epsilon/2 < \epsilon |x+1|.$`
* `$\epsilon /2 \ge \delta > |x+2|$` implies together with the above result `$|x+2| < \epsilon / 2 < \epsilon |x+1|.$`
* Thus, for `$x$` with `$\delta > |x-(-2)| > 0$` we have `$$\begin{array}{rcl}\epsilon &>& 2|x+2|\\
&>& \frac 1{|x+1|}|x+2|\\
&=&\frac 1{|x+1|}|1+(x+1)|\\
&=&\left|\frac1{x+1}+1\right|\\
&=&\left|\frac{(x+2)}{(x+2)(x+1)}+1\right|\\
&=&\left|\frac{x+2}{x^2 + 3 x + 2}-(-1)\right|\\
&=&|f(x) - (-1)|
\end{array}$$`
* Because `$\epsilon$` might have been chosen arbitrarily small, it follows that the limit `$$\lim_{x\to -2}f(x)=\lim_{x\to -2}\frac{x+2}{x^2 + 3x + 2}=-1$$` exists (and equals `$-1$`). 
* Thus, `$f$` is continuous at the point `$x=-2.$`

---

§§§1

<script type="text/javascript">


var brd = JXG.JSXGraph.initBoard('box68681', {boundingbox: [0, 10, 6, -1], axis:true});

var f = brd.create('functiongraph',[function(x){ 
	return 2*x-3;
}]);

</script>


§§§2

<script type="text/javascript">


var brd = JXG.JSXGraph.initBoard('box68682', {boundingbox: [-3, 1, 0.5, -5], axis:true});

var f = brd.create('functiongraph',[function(x){ 
	return (x+2)/(x*x+3*x+2);
}]);

</script>

