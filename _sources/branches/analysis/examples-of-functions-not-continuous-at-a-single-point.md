layout: example
categories: branches,analysis
nodeid: bookofproofs$6879
orderid: 100
parentid: bookofproofs$219
title: Examples of Functions Not Continuous at a Single Point
description: EXAMPLES OF FUNCTIONS NOT CONTINUOUS AT A SINGLE POINT &#9733; graduate maths &#10004; step by step &#10010; visit BookOfProofs now!
references: bookofproofs$6823
keywords: continuous,examples,functions,not,point,proof,single
contributors: bookofproofs

---


---

The following are examples of real functions, which are [not continuous at single points][bookofproofs$219].
### Example 1:

The function `$f:\mathbb R\to \mathbb R$`, 
`$$f(x):= \begin{cases}
-1&\text{if }x < 0\\
1&\text{if }x \ge 0
\end{cases}$$` is not continuous at the point `$x=0$`.

<div id="box68791a" class="jxgbox centered" style="width:500px; max-width:100%; height:500px;"></div>
 
§§§1

*Proof*: 
* Let `$f(x):=-1$`, if `$x < 0$` and `$f(x)=1$` else. 
* Assume `$f$` is continuous at `$0$` and its limit equals `$L\in\mathbb R$`, i.e. `$\lim_{x\to 0}f(x)=L.$`
* This means by definition that for all `$\epsilon > 0$` there is a `$\delta > 0$` such that for all `$x$` satisfying `$0 < |x| < \delta$` we have `$|f(x)-L| < \epsilon.$` 
* Now, we will find an `$\epsilon > 0$`, for which this condition does not hold. We will show that `$\epsilon = 1$` will do. Let `$\delta > 0$` be given.
* Let `$x_1:=\frac\delta2$` and `$x_2:=-\frac\delta2.$` 
* Note that `$0 < |x_1|,|x_2| = \frac\delta2 < \delta.$`
* Also note that `$f(x_1)=1$` and `$f(x_2)=-1.$` 
* Now, if `$|f(x_1) - L| < \epsilon=1$` and `$|f(x_2) - L| < \epsilon=1$`, it would follow that `$2=\epsilon + \epsilon  > |f(x_1) - L| + |f(x_2) - L| = |f(x_1) - L| + |L - f(x_2)| \ge |f(x_1) - L + L - f(x_2)|=|f(x_1) - f(x_2)|=2$`, i.e. that `$2 > 2.$`
* Since `$2 > 2$` is a contradition, the assumption must be wrong and `$f$` has no limit at `$x=0$`.


### Example 2:

The function `$f:\mathbb R\to \mathbb R$`, `$f(x):=\sin\left(\frac 1x\right)$` is not continuous at the point `$x=0$`.

<div id="box6879a" class="jxgbox centered" style="width:500px; max-width:100%; height:500px;"></div>

§§§2

*Proof*: 
* Let `$f(x)=\sin\left(\frac 1x\right).$`
* Assume `$f$` is continuous at `$0$` and its limit equals `$L\in\mathbb R$`, i.e. `$\lim_{x\to 0}f(x)=L.$`
* This means by definition that for all `$\epsilon > 0$` there is a `$\delta > 0$` such that for all `$x$` satisfying `$0 < |x| < \delta$` we have `$|f(x)-L| < \epsilon.$` 
* Now, we will find an `$\epsilon > 0$`, for which this condition does not hold. We will show that `$\epsilon = 1$` will do. Let `$\delta > 0$` be given.
* Select an integer `$k > \frac{1}{2\pi\delta}.$` Let `$x_1:=\frac{2}{(4k+1)\pi}$` and `$x_2:=\frac{2}{(4k+3)\pi}.$` 
* Note that `$0 < |x_1|,|x_2| < \frac{2}{4k\pi} < \delta.$`
* Also note that `$f(x_1)=\sin\left(\left(2k+\frac 12\right)\pi\right)=1$` and `$f(x_2)=\sin\left(\left(2k+\frac 32\right)\pi\right)=-1.$` 
* Now, if `$|f(x_1) - L| < \epsilon=1$` and `$|f(x_2) - L| < \epsilon=1$`, it would follow that `$2=\epsilon + \epsilon  > |f(x_1) - L| + |f(x_2) - L| = |f(x_1) - L| + |L - f(x_2)| \ge |f(x_1) - L + L - f(x_2)|=|f(x_1) - f(x_2)|=2$`, i.e. that `$2 > 2.$`
* Since `$2 > 2$` is a contradition, the assumption must be wrong and `$f$` has no limit at `$x=0$`.

---

§§§1

<script type="text/javascript">
var brd1 = JXG.JSXGraph.initBoard('box68791a', {boundingbox: [-1, 1.5, 1, -1.5], axis:true});
var f = brd1.create('functiongraph',[function(x){ 
	if (lt(x,0)) {
		return -1;
	} else {
		return 1;
	}
}]);

</script>


§§§2

<script type="text/javascript">

var brd = JXG.JSXGraph.initBoard('box6879a', {boundingbox: [-1, 1.5, 1, -1.5], axis:true});

var f = brd.create('functiongraph',[function(x){ 
	return Math.sin(1/x); 
}]);
</script>

