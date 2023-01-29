layout: proposition
categories: branches,analysis
nodeid: bookofproofs$1622
orderid: 800
parentid: bookofproofs$166
title: Rational Powers of Positive Numbers
description: RATIONAL POWERS OF POSITIVE NUMBERS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$581
keywords: numbers,positive,powers,rational
contributors: bookofproofs

---


---

Let `\(a > 0\)` be a [positive real number][bookofproofs$1107]. The [exponential function of general base][bookofproofs$1603] `\(a\)` with the [rational][bookofproofs$1033] exponent `\(\frac pq\in\mathbb Q\)`, (`\(q\neq 0\)`), is well-defined and justifies the definition of the **rational power function of positive real numbers** `\(a\to a^{\frac pq}\)`:

`\[a^{\frac pq}=\sqrt[q]{a^p}:=\exp_a\left(\frac pq \right).\]`

### Notes

* `$a^{\frac pq}$` can also be written as the [generalized power of `$a$`][bookofproofs$1626], i.e. as `$$a^{\frac pq}=\exp_a\left(\frac pq\right).$$`
* If `\(\frac pq\)` is a rational number `\(\ge 0\)`, then the function is defined for all `\(a \in\mathbb R\)`. 
* If `\(\frac pq\)` is a rational number `\(< 0\)`, then the function is defined for positive bases `\(a > 0\)` only.

The following interactive figure demonstrates the rational power of different real bases `\(a \in\mathbb R\)` for different rational exponents `\(\frac pq\in\mathbb Q\)`. 


<div style ='float:left'>
	<div id="box" class="jxgbox" style="width:500px; height:500px;"></div>
</div>
<div>
	<div id="box1" class="jxgbox" style="width:400px; height:100px;"></div>
</div>
<div style ='clear:both'></div> 
 
§§§1

---

§§§1

<script type="text/javascript">
var brd1 = JXG.JSXGraph.initBoard('box1', {boundingbox: [0, 0, 12, -10], showNavigation:false, showCopyright: false, axis:false});
var a0 = brd1.create('slider',[[1,-3],[9,-3],[-20,0,20]], {name:'p', snapWidth:1});
var a1 = brd1.create('slider',[[1,-7],[9,-7],[1,0,20]], {name:'q', snapWidth:1});

var brd = JXG.JSXGraph.initBoard('box', {boundingbox: [-7, 50, 7, -50], axis:true});

var f = brd.create('functiongraph',[function(x){ 
	return Math.pow(x,a0.Value()/a1.Value()); 
}]);
    
a0.on('drag',function(){ brd.update();});
a1.on('drag',function(){ brd.update();});
</script>

