layout: definition
categories: branches,number-theory
nodeid: bookofproofs$280
orderid: 600
parentid: bookofproofs$8104
title: Floor and Ceiling Functions
description: FLOOR AND CEILING FUNCTIONS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$1112
keywords: ceiling,floor,functions,floor and ceiling functions
contributors: bookofproofs

---
The [existence of integers exceeding real numbers][bookofproofs$1342] motivates the following definitions:
* The greatest [integer][bookofproofs$844] `\(n\)` [less than or equal to][bookofproofs$1107] `\(x\)` denoted by `\(\lfloor x \rfloor\)`.
* The least [integer][bookofproofs$844] `\(n\)` [greater than or equal to][bookofproofs$1107] `\(x\)` denoted by `\(\lceil x \rceil\)`.

---

The **floor** `$\lfloor \cdot \rfloor:\mathbb R\to\mathbb Z$` and the **ceiling** function `$\lceil \cdot \rceil:\mathbb R\to\mathbb Z$` are [functions][bookofproofs$592] from the set `$\mathbb R$` of [real numbers][bookofproofs$1105] to the set `$\mathbb Z$` of [integers][bookofproofs$844], defined by:

`\[\begin{array}{rcl}
\lfloor x \rfloor=n&\Longleftrightarrow& n\le x < n+1,\\
\lfloor x \rfloor=n&\Longleftrightarrow& x-1 < n \le x,\\
\lceil x \rceil=n&\Longleftrightarrow& x\le n < x+1,\\
\lceil x \rceil=n&\Longleftrightarrow& n-1 < x \le n.\\
\end{array}\]`


§§§1

---

§§§1

<div id="boxE16870" class="jxgbox centered" style="max-width:500px; height:500px;"></div>

<script type="text/javascript">
var brd = JXG.JSXGraph.initBoard('boxE16870', {boundingbox: [-5, 5, 5, -5], axis:true});

var ffloor = function(x) {
	return Math.floor(x);
}
	
var fceil = function(x) {
	return Math.ceil(x);
}

var f = function(x) {
	return x;
}

brd.create('functiongraph',[ffloor], {strokeColor:"#0000ff", strokeWidth:3}); 
brd.create('functiongraph',[fceil], {strokeColor:"#ff0000", strokeWidth:3}); 
brd.create('functiongraph',[f], {strokeColor:"#00ff00", strokeWidth:1}); 

brd.create('text',[1,-2,function() { return '\`\(f(x) = \\lfloor x \\rfloor\\)`';}],{strokeColor:"#0000ff"});
brd.create('text',[1,-2.7,function() { return '\`\(g(x) = \\lceil x \\rceil\\)`';}],{strokeColor:"#ff0000"});
brd.create('text',[1,-3.4,function() { return '\`\(h(x) = x \\)`';}],{strokeColor:"#00ff00"});

</script>

