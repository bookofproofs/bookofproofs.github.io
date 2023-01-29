layout: proposition
categories: branches,analysis
nodeid: bookofproofs$46
orderid: 700
parentid: bookofproofs$166
title: Nth Roots of Positive Numbers
description: NTH ROOTS OF POSITIVE NUMBERS ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: 
keywords: nth roots,nth root
contributors: bookofproofs

---


---

Let `\(\mathbb R_{+}:=\{x\in\mathbb R, x\ge 0\}\)` be the [subset][bookofproofs$552] of real numbers consisting of [positive real numbers][bookofproofs$1107], including `\(0\)`. For an [integer][bookofproofs$844] `\(n\ge 2\)` or `\(n\le -2\)`, the function `\(f:\mathbb R_{ + }\to\mathbb R\)`,  denoted by `\(x\to \sqrt[n]{x}\)`, is continuous and strictly monotonically increasing, and called the *`\(n\)`-th root* of the positive number `\(x\)`.

The  `\(n\)`-th root is the [inverse function][bookofproofs$407] to the [`\(n\)`-th power][bookofproofs$1618], i.e. for  `\(n\ge 2\)` or `\(n\le -2\)`, we have

`\[(\sqrt[n]{x})^{n}=x\]`

and `\[(\sqrt[-n]{x})^{-n}=\left(\frac {1}{\sqrt[n]{x}}\right)^{-n}=\left(\frac {\sqrt[n]{x}}{1}\right)^n=x\]`

### Notes

* For `\(n=2\)`, we call `\(\sqrt x \)` the **square root** of `\(x\ge 0\)`. 
* `$\sqrt[n]x$` can also be written as the [generalized power of `$x$`][bookofproofs$1626], i.e. as `$$\sqrt[n]x:=x^{\frac 1n}=\exp_x\left(\frac 1n\right).$$`
* The nth root is defined for `$x > 0$` and is itself always positive, since the exponential function is always positive.




The following interactive figure shows the `\(n\)`-th root (red) and the `\(-n\)`-nt root (blue) for `\(2\le|n|\le20\)`: 

<div><div id="box461" class="jxgbox centered" style="max-width:400px; height:100px;"></div></div>
<div><div id="box46" class="jxgbox centered" style="max-width:500px; height:500px;"></div></div>
 
§§§1

---

§§§1

<script type="text/javascript">
var brd1 = JXG.JSXGraph.initBoard('box461', {boundingbox: [0, 0, 12, -10], showNavigation:false, showCopyright: false, axis:false});

var a0 = brd1.create('slider',[[1,-3],[9,-3],[2,0,20]], {name:'n', snapWidth:1});
var a1 = brd1.create('slider',[[1,-7],[9,-7],[-20,0,-2]], {name:'-n', snapWidth:1});


var brd = JXG.JSXGraph.initBoard('box46', {boundingbox: [0, 5, 5, -1], axis:true}); 

var f = brd.create('functiongraph',[function(x){ 
	return Math.pow(x, 1/a1.Value());
}], {strokeColor:'blue'});

var g = brd.create('functiongraph',[function(x){ 
	return Math.pow(x, 1/a0.Value());
}], {strokeColor:'red'});
a0.on('drag',function(){ brd.update();});
a1.on('drag',function(){ brd.update();});
</script>

