layout: proposition
categories: branches,analysis
nodeid: bookofproofs$1626
orderid: 1000
parentid: bookofproofs$166
title: General Powers of Positive Numbers
description: GENERAL POWERS OF POSITIVE NUMBERS ★ graduate maths ✔ step by step ✚ by the axiomatic method ➜ visit BookOfProofs now!
references: bookofproofs$581
keywords: general powers of positive numbers,general powers,general power
contributors: bookofproofs

---


---

Let `\(x\)` be any [real number][bookofproofs$1105] and let `\(a > 0 \)` be a [positive real number][bookofproofs$1107]. Then the **general power function** `\(a\to a^x\)` is well-defined and equals the [exponential function of general base][bookofproofs$1603] `\(a\)`, formally:

`\[a^x=\exp_a(x).\]`

The following interactive figure demonstrates the general power in relation to different values of exponents `\(x\in[-20,20]\)`.

<div id="boxE20450" class="jxgbox centered" style="max-width:500px; height:500px;"></div>
<div id="box1E20450" class="jxgbox centered" style="max-width:400px; height:100px;"></div>
<div style ='clear:both'></div> 
 
§§§1

---

§§§1

<script type="text/javascript">
var brd1 = JXG.JSXGraph.initBoard('box1E20450', {boundingbox: [0, 0, 12, -10], showNavigation:false, showCopyright: false, axis:false});
var x = brd1.create('slider',[[1,-5],[9,-5],[-20,0,20]], {name:'x'});


var brd = JXG.JSXGraph.initBoard('boxE20450', {boundingbox: [-2, 20, 20, -2], axis:true});

var f = brd.create('functiongraph',[function(a){ 
	return Math.pow(a,x.Value()); 
}]);
    
x.on('drag',function(){ brd.update();});

</script>

