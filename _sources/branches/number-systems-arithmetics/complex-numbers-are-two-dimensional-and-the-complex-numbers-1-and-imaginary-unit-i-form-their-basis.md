layout: lemma
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1698
orderid: 100
parentid: bookofproofs$8601
title: Complex Numbers are Two-Dimensional and the Complex Numbers `\(1\)` and Imaginary Unit `\(i\)` Form Their Basis
description: COMPLEX NUMBERS ARE TWO-DIMENSIONAL AND THE COMPLEX NUMBERS 1 AND IMAGINARY UNIT I FORM THEIR BASIS ★ master maths ✔ visit BookOfProofs!
references: bookofproofs$696,bookofproofs$1038,bookofproofs$1692
keywords: basis of complex numbers,two-dimensional complex numbers,complex numbers as vectors
contributors: bookofproofs

---


---

In the [complex vector space of complex numbers over the field or real numbers][bookofproofs$1694], the set of vectors `\(B:=\{1,i\}\)` forms a [basis][bookofproofs$299], i.e. any complex number `\(x\in\mathbb C\)` can be represented by a linear combination of the vectors:

* [complex number one][bookofproofs$1673] `\(1\)` and the 
* [imaginary unit][bookofproofs$1160] `\(i\)` 

`\[x=a \cdot 1+b \cdot i\]`

for some real numbers `\(a,b\in\mathbb R\)`. In particular, every complex number `\(x\)` can be written as `\(a+bi\)`, where `\(a\)` is the **real part** of `\(x\)`, also denoted by `\(\Re (x)\)`, and `\(b\)` is the **imaginary part** of `\(x\)`, also denoted by `\(\Im (x)\)`.
 
In the following interactive figure, a complex number `\(x=a+bi\)` is visually represented as a pair of numbers `\(a\)` and `\(b\)` forming a vector (green) `\(x\)` in the complex plane.


<div id="boxE21061" class="centered jxgbox" style="max-width:500px; height:500px;"></div>

 
§§§1

---

§§§1

<script type="text/javascript">
board = JXG.JSXGraph.initBoard('boxE21061', {boundingbox: [-6, 6, 6, -6], axis: true});
 
var x = board.create('point', [2,2], {style:5,color:'blue',name:'x'});
var i = board.create('point', [0,1], {style:5,color:'red',name:'i',fixed:true});
var ein = board.create('point', [1,0], {style:5,color:'red',name:'1',fixed:true});
var org = board.create('point', [0,0], {style:5,color:'blue',name:''});
var rez = board.create('point', ["X(x)",0], {style:5,color:'blue',name:'a'});
var imz = board.create('point', [0,"Y(x)"], {style:5,color:'blue',name:'b'});
var ax =board.create('arrow', [org,x ], {strokeColor:'green'});
var ax2 =board.create('segment', [x,rez], {strokeColor:'blue',strokeWidth:1,dash:1});
var ay2 =board.create('segment', [x,imz], {strokeColor:'blue',strokeWidth:1,dash:1});
</script>

