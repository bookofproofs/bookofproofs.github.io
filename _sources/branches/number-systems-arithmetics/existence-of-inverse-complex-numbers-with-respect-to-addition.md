layout: proposition
categories: branches,number-systems-arithmetics
nodeid: bookofproofs$1664
orderid: 300
parentid: bookofproofs$1657
title: Existence of Inverse Complex Numbers With Respect to Addition
description: EXISTENCE OF INVERSE COMPLEX NUMBERS WITH RESPECT TO ADDITION ★ graduate maths ✔ step by step ✚ visit BookOfProofs now!
references: bookofproofs$581
keywords: addition of complex numbers inverse
contributors: bookofproofs

---


---

For every [complex number][bookofproofs$1105] `\(x\in\mathbb C\)`, there exists an **inverse complex number** `\(-x\in\mathbb C\)` such that the [sum of both numbers][bookofproofs$1657] equals the [complex zero][bookofproofs$1662]:

`\[x+(-x)=0.\]`

In the following interactive figure, you can experiment with the value of `\(x\)` (i.e. its position in the complex plane) and see, how it influences the value of `\(-x\)`, the inverse complex number with respect to addition:


<div id="boxE22642" class="jxgbox centered" style="max-width:500px; height:500px;"></div>
 
§§§1

---

§§§1

<script type="text/javascript">
board = JXG.JSXGraph.initBoard('boxE22642', {boundingbox: [-6, 6, 6, -6], axis: true});
 
var org = board.create('point', [0,0], {style:10,visible:true,fixed:true,name:' '});
var x = board.create('point', [2,1], {style:5,color:'blue',name:'x'});
var mx = board.create('point', ["-X(x)","-Y(x)"], {style:5,color:'green',name:'-x'});
var ax =board.create('arrow', [org,x], {strokeColor:'blue',strokeWidth:1,dash:1});
var amx =board.create('arrow', [org,mx], {strokeColor:'blue',strokeWidth:1,dash:1});
</script>

