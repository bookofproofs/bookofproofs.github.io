layout: proposition
categories: branches,analysis
nodeid: bookofproofs$1618
orderid: 900
parentid: bookofproofs$166
title: Nth Powers
description: NTH POWERS ★ bring your math skills to the graduate level ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: 
keywords: nth powers,nth power,powers
contributors: bookofproofs

---


---

Let `\(n\ge 0\)` be an [integer][bookofproofs$844]. The [exponentiation][bookofproofs$673] of a [real number][bookofproofs$1105] `\(x\in\mathbb R\)` defines a [function][bookofproofs$592] `\(x^n:\mathbb R\to\mathbb R\)`, 
`\[x^n:=\cases{1&\text{if }n=0\\
\underbrace{x\cdot\ldots\cdot x}_{n\text{ times}}&\text{if }n > 0,\\
\underbrace{x^{-1}\cdot\ldots\cdot x^{-1}}_{-n\text{ times}}&\text{if }n < 0,
}\]`
called the *`\(n\)`-th power* of the number `\(x\)`. 


### Note
 `$x^n$` can also be written as the [generalized power of `$x$`][bookofproofs$1626], i.e. as `$$x^n=\exp_x\left(n\right).$$`



The following interactive picture demonstrates the exponentiation for different values of the exponent `\(n\)`:


<div id="boxE20839" class="centered jxgbox" style="max-width:500px; height:500px;"></div>
<div id="boxE208391" class="centered jxgbox" style="max-width:400px; height:100px;"></div>
 
§§§1

---

§§§1

<script type="text/javascript">
var brd1 = JXG.JSXGraph.initBoard('boxE208391', {boundingbox: [0, 0, 12, -10], showNavigation:false, showCopyright: false, axis:false});
var a0 = brd1.create('slider',[[1,-5],[9,-5],[-10,0,10]], {name:'n', snapWidth:1});

var brd = JXG.JSXGraph.initBoard('boxE20839', {boundingbox: [-7, 50, 7, -50], axis:true});

var f = brd.create('functiongraph',[function(x){ 
	return Math.pow(x,a0.Value()); 
}]);
    
a0.on('drag',function(){ brd.update();});
</script>

