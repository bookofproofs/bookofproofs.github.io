layout: definition
categories: branches,number-theory
nodeid: bookofproofs$1283
orderid: 700
parentid: bookofproofs$8153
title: Modulo Operation for Real Numbers
description: MODULO OPERATION FOR REAL NUMBERS &#9733; graduate maths &#10004; step by step &#10010; by the axiomatic method &#10140; visit BookOfProofs now!
references: bookofproofs$1112
keywords: modulo,modulus,numbers,operation,real,modulo real numbers
contributors: bookofproofs

---
The [connection between quotient, remainder, modulo and floor functions][bookofproofs$1284] motivates the following generalization of congruences:

---

Using the [definition of the floor function][bookofproofs$280], we define for any two [real numbers][bookofproofs$1105] `\(x,y\)` with `\(y\neq 0\)` the **modulo** operation "`\(\operatorname{mod}\)`" as follows:

`\[x\mod y:=x-y\cdot \left\lfloor \frac xy \right\rfloor.\]`

This definition leaves the case `\(y=0\)` undefined, in order to avoid division by zero. For `\(y=0\)`, we set[^1]

`\[x\mod 0:=x.\]`

The number `\(y\)` after "`\(\operatorname{mod}\)`" is called the **modulus**.

### Example

In the following interactive figure you can study the graph of `\(x\mod y\)` by manipulating the value of `\(y\)`:

 
<div><div id="boxE16872" class="jxgbox centered" style="max-width:500px; height:500px;"></div></div>
<div><div id="boxE168721" class="jxgbox centered" style="max-width:400px; height:100px;"></div></div>

§§§1

[^1]: This convention preserves the property that `\(x\operatorname{mod}y\)` always differs from `\(x\)` by a multiple of `\(y\)`.

---

§§§1

<script type="text/javascript">
var brd1 = JXG.JSXGraph.initBoard('boxE168721', {boundingbox: [0, 0, 12, -5], showNavigation:false, showCopyright: false, axis:false});
var a0 = brd1.create('slider',[[1,-1],[9,-1],[-4,0,4]], {name:'y'});
var button1 = brd1.create('button', [1, -3, 'Reset', function() {
	a0.moveTo([5,-1]);
	brd.update();
}], {});

var brd = JXG.JSXGraph.initBoard('boxE16872', {boundingbox: [-5, 5, 5, -5], axis:true});

var f = brd.create('functiongraph',[function(x){ 
	var y=a0.Value();
	if (lt(Math.abs(y),0.005)) {
		return x;
	} else {
		return x-y*Math.floor(x/y);
	}
}]);
    
a0.on('drag',function(){ brd.update();});
</script>

